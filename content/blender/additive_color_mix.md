+++
title = "Additive color mix diagram"
date = 2021-01-25
lastmod = 2021-01-25
categories = ["Blender", "VSE"]
+++

In this journey, I will try to recreate the additive color mix diagram in Blender. As usual, there are several possibilities.

## 1. Three colored spotlights
The easiest solution is to create three spot lights. So, start Blender, delete the default cube and the light. Switch to top view; add three lights of type spotlight and a plane.

{{< figure src="/blender/assets/additive_color_mix_3_spots_setup.jpg" title="Figure 1: Blender setup for the three colored spot-lights solution" >}}

1. Switch to top view. This is not really essential but it makes your life much easier to get a spot light projection as a perfect circle.
2. Add three lights of type spot. Position them at location: Red (0, -0.25, 1), Green (-0.5, 0.5,1) and blue (0.5, 0.5, 1). Select the appropriate color and eventually Power (1000 W) and Spot Shape Size (75°).
3. Switch to render preview. Are the colored circles visible? NO, because there is no surface to 'shine' on.
4. Add a plane at location (0,0,0) with the appropriate size. The colored circles become visible. 
5. You need also to position the camera at location (0,0, 10) and change the view to camera view (Alt+Ctrl+0). Then you can render the image.

{{< figure src="/blender/assets/additive_color_mix_3_spots_render.png" title="Figure 2: Evee render of setup from figure 1" >}}

Figure 2 shows a nice additive color mix diagram. Note, however the status bar with extra info concerning the red color (obtained by Right-clicking on the red circle in the render preview).

## 2. Grease Pencil layers
Another solution is to use the 2D animation object Grease PenciL. You can create three 2D layers and draw a colored circle on it.
1. Delete cube and light from the default scene, switch to top view and add a blank Grease Pencil object to the workspace.
2. Switch to the object data properties panel and add a layer to the grease pencil object. Remember you have created a blank grease pencil object.
3. Draw a circle on that layer and name the layer appropriately; e.g. circle-red.
4. Switch to edit mode, select all the points of the stroke (with the shortcut key L) and copy those points.
5. Create a new layer, give it a name and paste the copied points. Move the selection with the Grab tool.
6. Repeat step 5 for the third color.
7. Create three fill materials, select all the points from the first circle and assign a fill color to them. Repeat for the other two circles.
8. Note that (1) the last drawn circle will occlude the other two and (2) the colors look terrible.
9. Change the blend mode of the last two drawn circles from regular to Add to fix the occlusion problem. Add a sun light to the scene to get brighter colors. But once again, check the color intensities in render view and note that the intensities go way well over 1 (depending on the strength of your sun light).



