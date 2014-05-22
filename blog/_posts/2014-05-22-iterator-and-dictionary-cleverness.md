---
layout: post
title: Iterator and dictionary cleverness
published: true
---

Something I seem to come across moderately often in my travels in the land of python is having a sequence of key value pairs that need to be converted into a dictionary. It seems to be the case that such patterns are found during scraping of websites and the like.

The usual pattern used is something this;
{% gist Mause/db3c2a3e2bb09a600895 %}
this method, although it works, is not very helpful if you have an iterator and want to keep the code clean; this method only works with things that can be sliced, and iterators cannot.

This version is both useful and a little clever;
{% gist Mause/1abe1941c20818b37423 %}
it may not be immediately obvious how it works unless you are familiar with iterators.

Iterators in Python are consumable once; this means that once a value has been consumed from an iterator, you must obtain a new copy of the iterator if you wish to access said value again. This also means that you can repeatedly consume and get each value in the sequence.  

The `zip` function works here because for each of its arguments, it iterates from the first to last, getting one value from each, and bundling them into a `tuple`, so you end up with something like this; `[('key1', 'value1'), ('key2', 'value2')]`. This is then passed to the `dict` function where it deconstructs this (iterable, mind you, from `zip`) and builds a dictionary using the given values.