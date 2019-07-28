---
layout: post
title: Post files with requests
published: true
---

AKA `requests.post(files=?)`

Today I was attempting to <code>POST</code> some data to [Docverter's API](http://docverter.com)  with the python [requests](http://docs.python-requests.org/en/latest/) library, and ran into a problem. Although [`requests.post`](http://docs.python-requests.org/en/latest/api/#requests.post) supports a <code>files</code> keyword argument, it does not seem to support custom, per file, <code>Content-Type</code> headers.

However, trawling through the source code, it would seem that yes, yes, it does. It's just not documented. It was initially added in a [commit](https://github.com/abarnert/requests/commit/20b10aed1bbe277745a74953b6dc73290bfa82fa) over <span title="relatively speaking">a year ago</span>, but alas, the commit did not include documentation.

It seems the following are possible, where ellipses indicate the inclusion of every argument of the above example;

{% gist 9688766 %}

Albeit good that these different forms are supported, ideally all forms should be documented, not just the first.

N.B; now that I know what to look for, the <code>Content-Type</code> form is also mentioned in a [Stackoverflow answer](http://stackoverflow.com/questions/20244757/content-type-in-for-individual-files-in-python-requests), and in the [<code>urllib3</code> documentation](http://urllib3.readthedocs.org/en/latest/helpers.html#urllib3.request.RequestMethods.request_encode_body) (though it fails to mention the custom headers)
