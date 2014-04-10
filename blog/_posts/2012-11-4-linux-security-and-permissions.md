---
layout: post
title: Linux Security and Permissions
sitemap:
    priority: 0.25
    lastmod: 2014-02-08T17:40:00-08:00
---

#### Updated 4/11/2013

Whilst revisiting this post during a move back to the Jekyll blogging engine,
I realized I had probably overcomplicated this solution; a simple shell script would have sufficed.

Said shell script;

{% highlight sh %}
    #!/bin/bash

    chown www-data:www-data /var/www/docs;
    chmod go+rx -R /var/www/docs;
    chmod go+rw -R /var/www/builds;
{% endhighlight %}

#### Original

I suppose geek's are supposed to find ways of doing things in different ways, but I don't really classify myself as a geek.

The problem was that, due to security concerns, the buildbot I run/manage for the DCPUToolchain was running as a user with normal privileges  A problem then arose that, for some reason, apache could not access the files that the buildbot was creating. A quick `chmod`/`chown` command fixed it; but these commands can only be run under root. One solution was simply to run the server under root, but, again, security concerns.

The solution, as put forward by IRC user eXeC64 was to create a small executable that executed the commands itself, and to run that with sudo. But another problem then arose; the buildbot could not enter the password requested from sudo.
This was solved with a quick edit of `/etc/sudoers` to allow users in the `www-data` group to run the aforementioned executable without having to enter a password.
The code for said small executable was ridiculously simple;


{% highlight c %}
    int main() {
        system("chown www-data:www-data /var/www/docs;");
        system("chmod go+rx -R /var/www/docs");
        system("chmod go+rw -R /var/www/builds");
        return 0;
    }
{% endhighlight %}
