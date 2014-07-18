---
layout: post
title: OpenFL, Android and Sqlite3
published: true
---

I've been working on a little toy app for Android written in a language entitled Haxe.
The app relies on a 10MB cache of transit data that must be either loaded into memory or accessible at runtime. Of course, on a device with only 200MB of RAM to begin with.

My original attempt was to simply load the 10MB JSON file into memory. This did not work.
My second attempt was to write a custom file format to store the data. This was too slow to load.
As I finalised my second attempt, I realized I was being stupid. I should just be querying a database, that way I need not load the entire cache into memory to query it.

This seemed all good in practice; a simple python script to load the JSON file into an appropriate database, which I could then add as an asset to the app. I would then connect to the database from the Android app. For performance reasons I kept an in memory cache.

It didn't take me long to realise that Sqlite3 support on the android target was a tad broken. Or at least, without help or documentation.

The first problem was that the Sqlite3 library couldn't seem to load the database. A quick Google pointed out that the database needed to be on a writable filesystem; this was easy enough, just copy it over on app startup to the devices SD card.

The second was non-obvious; it involved the Sqlite3 library itself. For whatever reason, the supporting haxe side couldn't extract the required functions from the Sqlite3. I tried a number of solutions, but the one that worked was to tell Haxe to statically link the Sqlite3 library to the app library;

`import hxcpp.StaticSqlite;`
