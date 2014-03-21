## `requests.post(files=?)`

Today I was attempting to `POST` some data to [Docverter's API](http://docverter.com)  with Python's `requests` library, and ran into a problem. Although `requests.post` supports a `files` keyword argument, it does not seem to support custom, per file,  `Content-Type` headers.

However, trawling through the source code, it would seem that yes, yes, it does. It's just not documented. It was initially added in a [commit](https://github.com/abarnert/requests/commit/20b10aed1bbe277745a74953b6dc73290bfa82fa) over a year ago, but alas, the commit did not include documentation.

It seems the following are possible, where elipses indicate the inclusion of every argument of the above example;
```py
files = {
  'unique_filename': 'file_data',
  'unique_filename': ('filename', 'file_data'),
  'unique_filename': ('filename', 'file_data', 'custom file content type'),
  'unique_filename': (
    'filename',
    'file_data',
    'custom file content type',
    <custom headers in tuple or dict>
  )
}

...

request.post(<url>, files=files)
```

Albeit good that these different forms are supported, ideally all forms should be documented, not just the first.

N.B; now that I know what to look for, the `Content-Type` form is also mentioned in a [Stackoverflow answer](http://stackoverflow.com/questions/20244757/content-type-in-for-individual-files-in-python-requests)
