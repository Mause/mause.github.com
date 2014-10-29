---
layout: page
title: Blog
extra_css: css/blog_index.css
---

<link rel="alternate" type="application/rss+xml" title="RSS"
      href="http://mause.me/blog/atom.xml">

## Blog

<ul>
  {% for post in site.posts %}
    <li>
        <div class="title"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></div>
        <div class="date">{{ post.date | date: "%-d %B %Y" }}</div>
        <br/>
    </li>
  {% endfor %}
</ul>
