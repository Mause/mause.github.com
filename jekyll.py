import sys
import base64
from os.path import expanduser, normpath, join, splitext

# sep,
# from six.moves.urllib_parse import quote

normexpanduser = lambda path: normpath(expanduser(path))

BLOG_DIR = normexpanduser('~/Dropbox/mause.github.com')
# os.environ['BLOG_DIR']


def get_notebook():
    for arg in sys.argv:
        if arg.endswith('.ipynb'):
            return arg.split('.ipynb')[0]


def extend_config():
    conf = get_config()
    conf.NbConvertApp.export_format = 'markdown'
    conf.MarkdownExporter.template_path = [
        join(BLOG_DIR, '_layouts')
    ]
    conf.MarkdownExporter.template_file = 'jekyll'

    conf.MarkdownExporter.filters = {'inline_image': inline_image}

    filename = get_notebook()
    if filename:
        conf.NbConvertApp.output_base = filename.lower().replace(' ', '_')
        conf.FilesWriter.build_directory = BLOG_DIR

    return conf


def mimetype_from_output(output):
    for key in output:
        if key.endswith('_filename'):
            return key.rstrip('_filename')


def inline_image(output):
    mimetype = mimetype_from_output(output)

    contents = output[mimetype].strip()
    contents = ''.join(contents.splitlines())

    return 'data:{};base64,{}'.format(
        'image/{}'.format(mimetype),
        contents
    )

extend_config()
