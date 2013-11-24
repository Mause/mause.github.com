---
layout: page
title: Blog
---

<link rel="alternate" type="application/rss+xml" title="RSS"
      href="http://mause.me/blog/atom.xml">

## Blog

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
