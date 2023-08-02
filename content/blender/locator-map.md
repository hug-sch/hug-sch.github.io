+++
title =  "Creating a locator globe map"
date = 2022-11-28
lastmod = 2022-12-01

categories =  ["Blender", "QGIS"]
+++

Did you ever need a locator globe map to illustrate your magnificent trip of the last holidays? There are, of course, plenty of globe maps on the internet; e.g. [Wikimedia SVG's](https://commons.wikimedia.org/w/index.php?search=world+globe&title=Special:MediaSearch&go=Go&type=image&filemime=svg). But to find just that one you have in mind; from the right perspective? It *should* be rather easy to create your own locator globe with exactly that look and feel that you wish with those two great open-source tools: [QGIS](https://www.qgis.org/) and [Blender](https://www.blender.org).

My first attempt -with Blender and QGIS- was successful and rather uncomplicated. Another (supposedly simpler) technique -only within QGIS- resulted in a pile of problems and work-arounds.

# Creating a locator globe with Blender and QGIS

Start Blender and create a new project. Replace the default cube with a UV Sphere. Switch to the Material or Rendered Preview with Viewport Shading buttons (top right). Now, you need a texture map to cover the sphere. You could try to download an image from internet; there are plenty available. Search for "texture world map". Or, you could generate one to your liking with QGIS.

The easiest way is to use the built-in world map from QGIS. Just enter the word "World" in the coordinate box in the middle of the status bar at the bottom (see figure 1). This world map is flat, grey-styled map with all the countries of the world outlined. Of course, you can customize it to your liking; see [Improvements]({{< ref "#improvements" >}})

{{< figure src="_qgis-worldmap.svg" caption="Figure 1: QGIS with the QIS World Map layer" width="100%" >}}

Then, you need to export this image as a PNG. Choose the menu Project > Import/Export > Export Map to Image and select Calculate from Layer (World Map) to define the size of the image.

Switch to Blender and assign this image as a texture for the sphere. Select the Material Properties tab in the Properties panel and add a new material. Replace the Base Color with the image: click on the yellow button next to Base Color to add an Image Texture and assign the exported image from QGIS with the Open button. If you need this image, you have to render it out.

{{< figure src="blender-screenshot.svg" caption="Figure 2: Blender with textured sphere." width="100%" >}}

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

