import re
import requests

schedule = requests.get(
    # 'https://2017.pycon-au.org/schedule/conference.json'
    'https://2019.pycon-au.org/schedule/avdata.json'
).json()

schedule = {item['name']: item.get('conf_url') for item in schedule['schedule']}

TEMPLATE = ' * Talk: '


def replace(match):
    name = match.groups()[0]
    return TEMPLATE + (
        name if name[0] == '[' else '[%s](%s)' % (name, schedule[name])
    )


def add_links(contents):
    return re.sub(
        r'^' + re.escape(TEMPLATE) + r'(.*)$',
        replace,
        contents,
        flags=re.MULTILINE,
    )


def main():
    filename = '2019-07-29-pyconau-2019.md'

    with open(filename) as fh:
        contents = add_links(fh.read())

    with open(filename, 'w') as fh:
        fh.write(contents)


if __name__ == '__main__':
    main()
