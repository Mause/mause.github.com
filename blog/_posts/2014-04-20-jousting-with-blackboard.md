---
layout: post
title: Jousting with blackboard
published: false
---

I figured it might be useful to hook up a notification service for when materials were updated on blackboard, the learning management system used by Curtin, the university which i attend. This is a summary of my findings.

I have reverse engineered the android app, though I have noticed that it is against Blackboard's EULA.
I am not sure what to do from here.


Firstly 

 * [SAM Spec](https://service.blackboardconnect.com/SAM/V2/SAMService.asmx)
 * [Contact Spec](https://service.blackboardconnect.com/SAM/V2/SAMService.asmx)
 * [suds docs](https://fedorahosted.org/suds/wiki/Documentation)
 * [how to use api](http://blog.mosheldon.com/2012/05/blackboard-connect-5-api-with-php.html)
 * [blackboard mobile app trello board](https://trello.com/b/GlsTPNN6/blackboard-mobile-learn-development-board) (suggests that blackboard app is provided with api via a blackboard plugin (refered to as a "brick"?), rather than being part of blackboard)
 * [managing api evolution slideshow](http://www.edugarage.com/download/attachments/72811512/Managing+API+Evolution+for+the+Blackboard+Mobile+Solution.pdf?version=1&modificationDate=1311710766503) (states internal api usage)