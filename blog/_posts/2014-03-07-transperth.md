---
layout: post
title: Transperth
published: true
---

Those people who live, or have lived in <a href="http://en.wikipedia.org/wiki/Perth">Perth</a> are likely familiar with the government organisation that provides the public transportation facilities, <a href="http://www.transperth.wa.gov.au">Transperth</a>.

Put simply, I wished to create a more or less simply to use API library in Python. This would involve some scraping, as I had trouble figuring out the location of the API the mobile app used.

I think I have now figure it out, in part;

 * Train times API: <http://livetimes.transperth.wa.gov.au/LiveTimes.asmx/GetSercoTimesForStation?stationname=Perth%20Underground%20Stn>
 * Journey Planner API: <https://api.transperth.info/DesktopModules/JJPApiService/api/jjpapi/>


For the livetimes API, i found a JSON string in `com.jeppesen.transperth.vm.TrainTimesVm` that gave a [list of the lines and station names](https://gist.github.com/Mause/3a01216b8611bb2fb6ea) that the API would accept. You can see an example in the list above.

I will continue updating; what would be ideal would be to be able to access the settings file for the App.
