---
layout: page
title: Blog
extra_css: css/blog_index.css
---

{% feed_meta %}

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
