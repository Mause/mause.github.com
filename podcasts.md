---
layout: page
title: Podcasts
---

### Podcasts

{% for podcast_pair in site.data.podcasts %}
  {% assign podcast = podcast_pair[1] %}
  {{ podcast.name }}
{% endfor %}
