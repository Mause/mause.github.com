---
layout: page
title: Podcasts
---

### Podcasts

Some podcasts that I've listened to I forgot in a moment, but, some, *some*, change me. Here's a list of them!

{% for podcast_pair in site.data.podcasts %}
{% assign podcast = podcast_pair[1] %}
##### {{ podcast.name }}

{{ podcast }}

{% endfor %}
