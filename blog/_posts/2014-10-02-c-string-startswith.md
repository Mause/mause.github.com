---
layout: post
title: C string startswith
published: false
---

Just a nice snippet of code I found useful;

{% gist b59e2fc914e4bfa7f2dc %} 

It gets the position of the needle in the haystack using `strstr` (who came up
with that name, seriously), then, as `strstr` returns a pointer to the
needle`s occurance in the string, we simply make sure that if it ain`t null,
and that it`s equal to the original string.

Day to day C stuff, I guess.

