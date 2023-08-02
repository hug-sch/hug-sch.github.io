+++
title = "Creating a traveling map"
date = 2022-12-05
lastmod = 2022-12-08
categories = ["QGIS","Blender"]
+++
Using QGIS to create a big map with an inset.

# Creating  your travel map with an inset

- see figure for end result.
- the global map could be produced with the QGIS world map, Natural Earth (110m). You need the latter to add the graticules to the map anyway.
- Because Zanzibar is a small island (xxxkm²) you cannot use the global maps because they are not high enough resolution. You have to search for shp-files of the specific country (Tanzania) or region. For the island itself there doesn't seem to be dataset available. For he country, you can search the site https://www.diva-gis.org/gdata
Another possibility is to use openstreet map; both for the global and specific region. Because zanzibar is small enough, you can export this region separately from the global map. This will not work for a large region. Even Zanzibar is too big; you can of course , export the map in two parts. Then you need services as geofabrik.de. 
- goto https://www.openstreetmap.org/. Zoom in on Zanzibar. Click Export in the menu and choose "Manually select a different area". Drag a rectangle around Zanzibar.
   - You can choose between different layers: standard, Cycle Map, Transport map, ... Choose the latter.
   - If the map isn't too big, you can download it with the Export button
- Mexico: goto http://download.geofabrik.de/ Choose North America and Mexico as sub region. Download the shp-file (971 MB). The PBF-file is much smaller but can't be processed easily with QGIS. There are lots of layers available: osm_buildings, osm_landuse, osm_roads, ... But apparently no country borders. You could use the borders from the global map, but probably they are detailled enough. 
- How to get the country-borders? --> Geofabrik.de seems to be a dead end. The roads-table contains almost 4.5 mio entries. So, you have to filter it before processing.
Apparently, you can get land, water and coasline polygons from OSM via https://osmdata.openstreetmap.de/ The lands polygon is 769 MB (there are two projections: WGS84 and Mercator).
Perhaps better, how to download OSM within GQIS? Search on Google There is a tutorial from OSM: https://learnosm.org/en/osm-data/osm-in-qgis/ and QIS itself (https://www.qgistutorials.com/en/docs/downloading_osm_data.html). The last tutorial is for London for a map of pubs; works with OSM Place Search and OpenLayers plugins . The first tutorial works with the QuickOSM plugin. But, you have to know what to extract or else most of the time you get a timeout. The site https://osm-boundaries.com/ (still in alpha) promises to show boundaries for countries and regions. It kinda work but also too mauch data.

- searching for specific websites for downloading regions/countries: eg. Mexico Cancun. A very good website is : http://www.diva-gis.org/gdata for downloading per country (not region of werelddeel). For mexico, the follwing data sources were available: administrative areas (level 1 -3), Inland water (polygons (lakes) and lines (rivers)), roads & railroads, elevation (with mask???), land cover (with maks???), population (with mask), gazetter (?)
There is too much detail: filter the roads (RTT_DESCRI = 'Primary route") and MEX_water_lines (NAM != 'UNK'); name <> unknown.
- you could position the world map behind it to see the neighbouring countries but there is a problem with the boundaries which are that detailed in the world map. Therefore, you have to filter. But how? You can filter in the World map on country and switch off the fill and stroke for Mexico, but you should do it also for the neighbours, otherwise, you see the border by them. Switching off all borders is probably sufficient. But later on, with the map view; that's also not OK. You need a separate world map intact and one as overlay for Mexico.
- how to make background of inset transparent?












Figure 3 shows a flat map of the world with all of the countries and one specific is colored. This country is then enlarged in the inset. For this kind of map, you need a better resolution; e.g. the Large Scale data 1:10m (1 cm = 100 km). Because you need the countries, you also need the Cultural data sets (ne-10m-admin_0_countries). 

- add a rule-based layer styling --> "SOV_A3" = 'BEL' + color and TZA
- add a group global & TZA
- add countries, rivers and lakes center line to group TZA; label regions?
- Select project > New Print layout. Create the global map first. see https://www.youtube.com/watch?v=2c4axNtuDwI&t=2s


