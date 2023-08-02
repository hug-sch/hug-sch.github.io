+++
title = "Creating a locator globe map"
date = 2022-11-28
lastmod = 2022-12-01
categories = ["QGIS", "Blender"]
+++

Did you ever need a locator globe map to illustrate your magnificent trip of the last holidays? There are, of course, plenty of globe maps on the internet; e.g. [Wikimedia SVG's](https://commons.wikimedia.org/w/index.php?search=world+globe&title=Special:MediaSearch&go=Go&type=image&filemime=svg). But to find just that one you have in mind; from the right perspective? It *should* be rather easy to create your own locator globe with exactly that look and feel that you wish with those two great open-source tools: [QGIS](https://www.qgis.org/) and [Blender](https://www.blender.org).

My first attempt -with Blender and QGIS- was successful and rather uncomplicated. Another (supposedly simpler) technique -only within QGIS- resulted in a pile of problems and work-arounds.

# Creating a locator globe with Blender and QGIS

Start Blender and create a new project. Replace the default cube with a UV Sphere. Switch to the Material or Rendered Preview with Viewport Shading buttons (top right). Now, you need a texture map to cover the sphere. You could try to download an image from internet; there are plenty available. Search for "texture world map". Or, you could generate one to your liking with QGIS.

The easiest way is to use the built-in world map from QGIS. Just enter the word "World" in the coordinate box in the middle of the status bar at the bottom (see figure 1). This world map is flat, grey-styled map with all the countries of the world outlined. Of course, you can customize it to your liking; see [Improvements]({{< ref "#improvements" >}})

{{< figure src="/QGIS/assets/_qgis-worldmap.svg" caption="Figure 1: QGIS with the QIS World Map layer" width="100%" >}}

Then, you need to export this image as a PNG. Choose the menu Project > Import/Export > Export Map to Image and select Calculate from Layer (World Map) to define the size of the image.

Switch to Blender and assign this image as a texture for the sphere. Select the Material Properties tab in the Properties panel and add a new material. Replace the Base Color with the image: click on the yellow button next to Base Color to add an Image Texture and assign the exported image from QGIS with the Open button. If you need this image, you have to render it out.

{{< figure src="/QGIS/assets/blender-screenshot.svg" caption="Figure 2: Blender with textured sphere." width="100%" >}}

## Improvements

First of all, there is in fact a slight problem with the UV Unwrapping (but you probably won't see it on this small scale). If you switch to the UV Editing workspace and select the sphere in Edit mode, you will notice two rows of triangles in the UV map. This is because the sphere is closed at the top and bottom. The result however is that a square area of the flat world map will be squeezed into a smaller triangle. This is not optimal and will result in distortion. But again, at the polar regions, you probably won't notice it. There are a few work-arounds; see for example [Mastering Blender](https://www.youtube.com/watch?v=72hgMoyTbXE&t=116s).

The surface of the sphere is by default made of 16 x 32 flat faces. They are very noticeable in figure 2. You can smoothen the surface by applying a Subdivision Surface Modifier (see for example [5 minutes Blender](https://www.youtube.com/watch?v=Y99L5YC-Uw0from)).

And, of course, you can animate the globe, for example simulating the earth rotation and create some day-and-night animation.

Improvements of the map (e.g. coloring) should be done in QGIS. A small enhancement is the coloring of a specific country of interest. If you select the World map layer and press F6 (Open attribute Table); you will notice that each country has a full name and three-letter abbreviation (ISO-A3). You can use this field to apply a rule-based styling to this layer. In the Layer Styling panel, select the World Map and change the "Single Symbol" styling to "Rule Based". Create a new rule and insert the text ```"ISO_A3"  =  'ESP'``` into the Filter text box to style the country Spain (ESP). ISO_A3 has to be surrounded by double quotes and ESP by single quotes. You can build the formula with the Ɛ button next to it.

If you need more sophisticated maps, you also need more sophisticated data sets.  A very good starting point for global data are the free vector and raster map data from [Natural Earth](https://www.naturalearthdata.com/). For a locator globe, you don't need very detailled data; a scale of 1:110m is sufficient (1 to 110 million or 1 cm = 1,100 km). So, you can start with the following files 

- Land: ne_110m_land.zip [link](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/physical/ne_110m_land.zip)
- Ocean: ne_110m_ocean.zip [link](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/physical/ne_110m_ocean.zip)
- Graticules at 15° interval: ne_110m_graticules_15.zip [link](http//www.naturalearthdata.com/download/110m/physical/ne_110m_graticules_15.zip)

You need the last file to create the graticules (parallels & meridians). You don't have to unzip the files. QGIS can work right away with the zip files. Start QGIS and drag the zip-files to the Layers panel (see figure 1). Note that only the shp-file is added to the Layers panel. QGIS is a layered application such as GIMP or Inkscape. This means that if the graticule layer is below the land and/or ocean layer, it will not be visible. You can change the Layer Style in the Properties panel at the right hand side.

One downside of the current technique is that you need two programs and/or a bunch of intermediate files.

# Creating a locator globe with QGIS ONLY!

*Isn't it possible to create a locator globe map within QGIS alone?* Of course! A quick search on the internet ("how to create a globe in QGIS") produced several solutions; e.g [cartographyclass.com](https://cartographyclass.com/a-world-locator-map-in-5-minutes/) and the excellent tutorial (in Dutch) from [Geojuffie](https://www.youtube.com/watch?v=BXtZlTPlMj8). They all have in common that you need to create a specific Coordinate Reference System (CRS). A CRS defines how the two-dimensional, projected map in your GIS relates to real places on the earth. In this case, the two-dimensional map however resembles a globe (but still is a two-dimensional map). This is a two step technique.

- Create the custom CRS with the menu Settings > Custom Projections. In the Name field, you can enter the name of your CRS e.g. myGlobe. In the Format > Project String, you need to enter the commands to create a so-called azimuth orthographic projection, e.g.

  ```(1) +proj=ortho +lat_0=42.53 +lon_0=-72.53 +ellps=sphere +units=m +no_defs```

  or alternative version

  ```(2) +proj=ortho +lat_0=21 +lon_0=6 +a=6371000 +b=6371000 +units=m +no_defs```

With this command, you will create an orthogonal projection, where the focus of the map will be placed at coordinate (42.53; -72.53) of the real earth. The projection itself is an a sphere or alternatively, you specify that the globe has a radius of 6371000 m.

- Switch the project to the just created CRS with the menu Project > Properties or the CRS box in the statusbar below (right hand corner).

And like so many tutorials, they all produce very nice results as long as you follow them precisely. Of course, you want a map, tailored to your needs. And then it started to go wrong.

My first map was based on the Natural Earth land and ocean maps. I used the following projection command.

```+proj=ortho +lat_0=21 +lon_0=6 +x_0=0 +y_0=0 +a=6371000 +b=6371000 +units=m +no_defs```

Figure 4 shows the result; which is not at all perfect.

{{< figure src="/QGIS/assets/QGIS-test-1-custom-crs.svg" caption="Figure 3: My first attempt to produce a globe." width="100%" >}}

Notice that parts of America and Asia are gone, as was the color of the ocean! What did I do wrong? My first reaction (googling), opened once again the box of Pandora and let me drown in the endless ocean of the internet. Some impressions of my voyage.

1. A reasonable explanation (at that time in the exploration) came from [Avenza.com](https://www.avenza.com/resources/blog/2019/01/14/orthographic-projections/). With the globe projection, you always see only half of the flat map. The other half is hidden behind the horizon. So, the QGIS projection command should hide those lines.

2. But how? I first tried to erase the points in the flat map that weren't visible in the globe view in a rather sketchy way. Of, course, you have to do this on the rectangular map; not the globe. With the Vertex Editor, you can delete points from the polygons. Very soon, there appeared straight lines. If you delete points, QGIS will connect the remaining ones automatically on a closed polygon. And there, it should have become clear to me what the fundamental problem was. But unfortunately that wasn't the case. My map improved a bit; so I decided to delete more precisely the points that were on the hidden half.

3. How can you know which points will be visible after the reprojection. A very big work-around was to introduce blender once again. Create the [globe in Blender]({{ref #Creating a locator globe with Blender and QGIS}}). Rotate the globe to your liking. Switch to the UV Editing workspace. Select the globe in Edit mode and select all visible points. They will light up them in the UV map. You can add a Bezier circle around the globe to make it more precise. Make a screenshot of the UV map and import that UV map in QIS. Et voila, there you have a precise collection of all the points you have to delete.

4. A minor problem was that the size of the QGIS and Blender map aren't the same. So, you have to move & scale the UV bitmap so that it aligns with the shp-layer. Hm, how? After googling "qgis scale move a bitmap", it turns out that you need a plugin for that (Freehand Georeferencer).

5. Edit the shp-layer and remove the points that are not visible from your perspective. Once again: some obstacles. The land and ocean layer came from a downloaded ZIP-file. Apparently, that kind of layer could not be edited but there is not much info about that. Ultimately, I succeeded to export the layer (Layer > Save AS). This exported layer then could be edited with the Vertex tool.

6. Perhaps -I thought- the detour with Blender isn't necessary. May be, I can draw a circle within QGIS itself. After one more Google search (try "QGIS add circle"), I needed a memory layer (nowadays called Scratch layer) and the "Digitizing toolbar". But, this toolbar was greyed out (inactive). You can't draw a circle on a globe projection. By then, I  realized that I didn't know where to draw the circle on the flat map. So, that's a dead end, once again.

7. At last, I thought having found THE solution: a post that exactly describes the problem at [StackExchange](https://gis.stackexchange.com/questions/78346/ortho-projection-produces-artifacts). I need a plugin called [Clip to Hemisphere](https://github.com/jdugge/ClipToHemisphere). But, again. A death end. An error pops up: ne_110m_land.shp has an invalid geometry. This is the point where it started dawning on me. There were less problems with other data sources and center points; for example the built-in world map of QGIS (also a tip from [Geojuffie](https://www.youtube.com/watch?v=BXtZlTPlMj8)) gives most of the time acceptable results. The ocean layer was in fact not necessary; it's the complement of the land layer. At that moment, I also discovered the Globe Builder plug-in and observed that this plugin uses the country layer of Natural Earth as base.

As far as I understand it now (but this is a seedling post in my digital garden!), the land layer contains very large polygons; spreading over multiple continents. The chance that one or more polygons extend in the hidden part of the orthographic projection is significant. QGIS can not draw these closed polygons. Some of the vertices are on the backside of the globe. They shouldn't be visible. Drawing this closed polygon is not possible. So, QGIS deletes it from view; e.g. parts of America and Asia in figure 4.

OK. But, how to solve it? By then, I have discovered the Globe Builder plugin.


## The easy and better way!

Install the plug-in "Globe Builder": menu Plugins > Manage and Install Plugins ... Select All and search for Globe Builder. The plugin creates a separate panel that you can make visible with menu View > Panels > Globe Builder. If you want the globe right away, click on Add the Globe to a Map at the bottom! But perhaps, it's better to take the following steps to get a better understanding.
 
{{< figure src="/QGIS/assets/QGIS-plugin-globe-builder.png" caption="Figure 3: Worldmap with graticules created with plugin Globe Builder" width="100%" >}}

If you haven't already a map downloaded, the plugin can "Load Data to a Map" from the Natural Earth website. But, remember, not all maps are suitable for orthographic projection. If you should try it with the same Land layer and center coordinates as in figure 3, you will get the same -distorted- result.

With the plugin, you can choose between the 50m or 110m scale and some graticules. It will download the Countries layer from Natural Earth. The checkbox "Sentinel-2 cloudless adds a more colorful and photographic appearance of the earth surface. A group "Globe" is created with the layers Countries (from Natural Earth), and/or Graticules and S2 Cloudless (depending on the selected options). The assigned CRS is EPSG:4326 - WGS 84 (flat map).

Then, you can choose the Projection method. Under the hood, the coordinate transformation within QGIS is done with the [open-source software PROJ](https://proj.org/index.html). A complete list of the about 150 projections is found [here](https://proj.org/operations/projections/index.html). With the Globe Builder plugin, you can choose between 5 options.

{{< row >}}
{{< column >}}
## Projection
{{< /column >}}

{{< column >}}
## Example
{{< /column >}}
{{< /row >}}

{{< row >}}
{{< column >}}
[Azimuthal Orthographic](https://proj.org/operations/projections/ortho.html) (default): the earth is projected on a flat plane, positioned tangentially at a given center position from a light source at infinite distance. This projection gives you the wanted globe view.
{{< /column >}}

{{< column >}}
{{< figure
  src = "/QGIS/assets/azimuthal-projection.png"
  class = "img-fluid float-end" 
>}}

{{< /column >}}
{{< /row >}}

{{< row >}}
{{< column >}}
[Equal Earth ](https://proj.org/operations/projections/eqearth.html) Like the name implies, this projection retains the relative size of areas. It is [invented](https://en.wikipedia.org/wiki/Equal_Earth_projection) in 2018.
{{< /column >}}

{{< column >}}
{{< figure
  src = "/QGIS/assets/equal-earth-projection.png"
  class = "img-fluid float-end" 
>}}

{{< /column >}}
{{< /row >}}

{{< row >}}
{{< column >}}
[Hammer & Eckert-Greifendorff](https://proj.org/operations/projections/hammer.html). Is also an [equal-area map projection](https://en.wikipedia.org/wiki/Eckert-Greifendorff_projection) described by Max Eckert-Greifendorff in 1935.
{{< /column >}}

{{< column >}}
{{< figure
  src = "/QGIS/assets/Hammer & Eckert-projection.png"
  class = "img-fluid float-end" 
>}}

{{< /column >}}
{{< /row >}}

{{< row >}}
{{< column >}}
[Aitoff](https://proj.org/operations/projections/aitoff.html). is a modified azimuthal map projection proposed by [David A. Aitoff](https://en.wikipedia.org/wiki/Aitoff_projection) in 1889.
{{< /column >}}

{{< column >}}
{{< figure
  src = "/QGIS/assets/aitoff-projection.png"
  class = "img-fluid float-end" 
>}}

{{< /column >}}
{{< /row >}}

{{< row >}}
{{< column >}}
[Eckerty I](https://proj.org/operations/projections/eck1.html). According to [ArcGIS](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/eckert-i.htm), the Eckert I projection is a compromise pseudocylindrical map projection with rectilinear meridians and an odd appearance. The projection is simple, but it has no practical use other than making a world map with an unusual shape.
{{< /column >}}

{{< column >}}
{{< figure
  src = "/QGIS/assets/eckert-projection.png"
  class = "img-fluid float-end" 
>}}

{{< /column >}}
{{< /row >}}


After setting the projection method, create the globe view with the Center button from "Center the globe based on:" panel. But, what exactly is meant by "center the globe"? The Globe Builder plugin uses by default the Azimuthal Orthographic projection to create the globe. A flat plane (in contrast to a cylinder or cone) is used to project the earth surface to. It's called Orthographic because the light source is set at infinity, resulting in orthogonal parallel projection lines from the earth globe to the flat surface. The flat plane is positioned tangentially at a give position (for example the North pole). This point is the center point and will appear in the middle of the projected circle. Because this center point is only useful in a orthographic projection, the option is only available for the first (Azimuthal Orthographic) projection method and greyed out for the others. The four options are: 

- Geocoding: perhaps the easiest way. Enter the name of a place (e.g. New York), click search, select the correct place if there are multiple locations and click center to change the globe view. You can display up to max 5 addresses to choose from.
- Coordinates, you can set the midpoint of the orthogonal projection (=circle) to the specified lon + lat combination. For example, to have the country Spain at the center of the globe map, enter the coordinates of Madrid (lon=-3.70, lat=40.41). Please, note that due to the perspective view, this doesn't look correct. However, the chosen coordinate is indeed the midpoint of the *circle* of the globe map. You can always alter the center point by entering new coordinates and clicking Center.
- Center of the current view. For example, you can zoom in on Iceland to make that country the center of the globe.
- Layer: each layer map has a center; for example the Natural Earth maps have a center point somewhere in the Atlantic Ocean (coordinates 0,0).

With the the visualization panel, you can change colors and add a Halo effect (= colored ring around the sun or a planet). This Halo effect greatly enhances the optical illusion of perspective from outer space. With the [layout panel](https://docs.qgis.org/3.22/en/docs/user_manual/print_composer/index.html), you can create the globe map into a new Layout; which can be handy when you want to create inset maps.

The last two buttons (Add the Globe to a Map and Add the Globe to a Layout) are shortcuts to create the globe in one step.

This plugin makes it really easy to create high-quality globe maps. I found it through the enlightening post of [Alasdair Rae](http://www.statsmapsnpix.com/2019/09/globe-projections-and-insets-in-qgis.html) (2019). The code is at [Github](https://github.com/GispoCoding/GlobeBuilder). One last warning, the created Halo and graticule layers are Scratch layers, meaning that they only exist in memory and will not be preserved upon saving the project. If you want these layers for latter use, you have to save them manually. The Countries layer was downloaded upon installing the plugin and is located in your user folder as a geojson file (that's why it goes so fast).

