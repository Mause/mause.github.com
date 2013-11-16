---
layout: post
title: 0x10^C, or, DCPUToolchain
published: false
---

Cross posted at over at [my techy blog](http://mause.me/blog/2013/11/20/dcputoolchain.html)

Back in 2009, Notch aka Markus Persson, announced a game entitled 0x10^C, essentially a space adventure game with a twist. That twist was that you built your own ships, but more importantly, you could then program computers to control your ships. The only known computer from the game was called the DCPU16. It was, as the name suggests, a sixteen bit computer, which the lore stated was from the nineteen eighties.

Having, relative to todays computers minute power and memory, was to be part of the fun/challenge of the game.

Many computer minded people were injured by the idea, and as soon as draft specifications were released, set about writing assemblers, emulators, and in some cases, compilers, linkers and debuggers.

One of these people was HachQue, who decided to, rather than create a few disparate tools, create a toolchain.
He decided to entitled his project DCPUToolchain, after the DCPU16.

As best as I can tell, as this was before I was involved with the project, work began on the toolchain on <date datetime="2012-04-05T03:20:49-07:00">fifth of April 2012</date>, with my first contact with the project shortly before they migrated from his own version control system[^2] to GitHub.

Said first contact, was via an issue[^3] they had filed on the repository on GitHub about setting up a Buildbot[^1] for the project.
This issue is still live, though appears to be missing some context that I may have to track down in some IRC logs.

Though there are a few definitions

For those unfamiliar with the concepts, high performance software must be compiled to take full advantage of the hardware upon which it is running.

---


 * [^1]: Buildbot: An automated system that whenever an updated version of code is
 * [^2]: Version Control System/VCS: A system that allows developers to
 * [^3]: https://github.com/DCPUTeam/DCPUToolchain/issues/69
