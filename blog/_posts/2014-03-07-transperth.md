---
layout: post
title: Transperth
published: true
---

### This project is sorta in limbo, thanks to the new transperth website being significantly more difficult to scrape.

Those people who live, or have lived in <a href="http://en.wikipedia.org/wiki/Perth">Perth</a> are likely familiar with the government organisation that provides the public transportation facilities, <a href="http://www.transperth.wa.gov.au">Transperth</a>.

Put simply, I wished to create a more or less simply to use API library in Python to pull data out of their system. I originally thought that this would primarily involve scraping their website, as I had trouble figuring out the location of the API the mobile app used.

I think I have now figured it out, in part;

## Train times API

Example; <http://livetimes.transperth.wa.gov.au/LiveTimes.asmx/GetSercoTimesForStation?stationname=Perth%20Underground%20Stn>
Python interface; <https://github.com/Mause/pytransperth/blob/master/transperth/livetimes.py>

I found a JSON string in `com.jeppesen.transperth.vm.TrainTimesVm` that gave a [list of the lines and station names](https://gist.github.com/Mause/3a01216b8611bb2fb6ea) that the API would accept. The example above shows the corresponding URL for the `Perth Underground Stn`.

## Journey Planner API
Root URL; <https://api.transperth.info/DesktopModules/JJPApiService/api/jjpapi>

## Silver Rails Journey Planner API:

The SaaS service provides endpoints for [reference data](http://journeyplanner.silverrailtech.com/JourneyPlannerService/V2/rest/Datasets/:dataset/AvailableReferenceData) (stops, routes, timetable, etc.), [a journey planner](http://journeyplanner.silverrailtech.com/JourneyPlannerService/V2/rest/Datasets/PerthRestricted/JourneyPlan?from=:from&to=:to&date=:date), [a localities index](http://journeyplanner.silverrailtech.com/JourneyPlannerService/V2/rest/Datasets/PerthRestricted/Localities?searchTerm=:searchTerm), [a nearby stops service](http://journeyplanner.silverrailtech.com/JourneyPlannerService/V2/rest/Datasets/PerthRestricted/NearbyTransitStops?geoCoordinate=:geoCoordinate), [a timetable lookup](http://journeyplanner.silverrailtech.com/JourneyPlannerService/V2/rest/Datasets/PerthRestricted/StopTimetable?stop=:stop&time=:time), and a [trip lookup](http://journeyplanner.silverrailtech.com/JourneyPlannerService/V2/rest/Datasets/PerthRestricted/Trip?tripUid=:tripUid&tripDate=:tripDate), presumably for trips already determined via the API.

Having rooted my phone, and installing [Root Browser](https://play.google.com/store/apps/details?id=com.jrummy.root.browserfree) to access the android Transperth App's assets, I was able to retrieve the `ApiKey` for the Silver Rails API, as well as many other settings.

Because I would probably get the shit sued out of me, I don't feel comfortable sharing the key here.

Anyway, using the ApiKey, I was able to download all the reference data that the app uses which is a rather large amount, and it seems to be downloaded everytime the app is started, at least partially. I shall investigate this further.

The reference data contains info about;

 * ServiceProviderReferenceData - TransPerth, TransBunbury, etc.
 * TransitStopReferenceData - All the train, bus, and presumably ferry stops
 * RouteTimetableGroupReferenceData - Timetables for the routes, routes themselves
 * LandmarkReferenceData - Landmark info - `Curtin University of Technology` for example
 * TransportModeReferenceData - Lists the transport modes; School Bus, Rail, Bus, and Ferry
 * RouteReferenceData - Metadata for routes

Using `apktool`, I managed to extract an XML file from the `.apk` that contains a large number of strings not present in the code I extracted. This is where I retrieved the list of datasets for the [Silver Rail Technology](http://silverrailtech.com) API from;

 * PerthDataset
 * BrisbaneDataset
 * BostonDataset

You can insert these into some of the above URLs, along with a an `ApiKey` query parameter, to make use of the endpoint.

I also found some documentation; <http://journeyplanner.silverrailtech.com/JourneyPlanner/Help/html/R_Project_Journey_Planner_Interface_Specification.htm>

## Misc

#### 7:02PM 8/3/2014 ####

Browsing through the action list on the transperth website, I noticed that it generated a synthetic TAG ON event to account for my incorrect TAG ON at the wrong scanner.


