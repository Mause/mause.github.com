---
layout: page
title: Projects
sitemap:
    priority: 1
    lastmod: 2014-02-08T17:40:00-08:00
extra_css: css/projects_index.css
---

## Projects

Much of the code I have written is in Python, as is it both my language of choice, and the language with which I possess the most experience, having learnt Python through the [NCSS Challenge](https://groklearning.com/challenge/) of 2009, at age 13.
Some years later, I learnt Javascript, and used it to add functionality to some websites.
I dabbled in C and C++ during the course of the DCPU fever.
I started university in 2014, at Curtin's Bentley campus in Perth, Western Australia. During the Object Oriented Program Design course I learnt some basic Java.

For much of these projects, more information is available on the linked GitHub pages, where appropriate.

---

{% comment %} projects are defined in _data/projects.yml {% endcomment %}

{% for project in site.data.projects %}
#### [{{project.name}}:]({{project.link}}) <small>{{project.languages}}</small>
{{project.description}}
{% endfor %}
