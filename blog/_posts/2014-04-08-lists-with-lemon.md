---
layout: post
title: Parsing lists with Lemon
published: true
---

I was parsing some lists of, erm, labels today in [Lemon](http://www.hwaci.com/sw/lemon/) (with [Ragel](http://www.complang.org/ragel/) as the lexer), and couldn't quickly (read lazily) find a grammar for parsing lists, so voila;

```lemon
list(A) ::= LIST_ITEM(B). { A=B; }
list(A) ::= LIST_ITEM(B) list_clause(C). {
    A=B;
    append_contents of C to B
}
list_clause(A) ::= COMMA list(B). { A=B; }
```

with the pseudocode replaced with code appropriate for your host language, and with `list` being the uppermost rule, and with `COMMA` being whatever delimiter you desire :)

Enjoy!
