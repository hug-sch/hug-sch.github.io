+++
title = "Creating a photo or video collage in Blender"
date = 2022-11-01
lastmod = 2022-12-15
categories = ["Blender", "VSE"]
+++

# Creating a video or photo collage within Blender

A video or photo collage is a grouping of two or more smaller images and/or videos into 1 frame. Figure 1, for example has 6 smaller areas, each filled with and image and/or video. Creating such a collage isn't very difficult. Yet, there are quite a few steps to take. Automating this process could definitely help here a lot.


{{< figure
  src = "/blender/assets/photo-collage.png"
  title = "Figure 1: collage with 6 areas for video and/or images."
>}}

You can download the [blend-file](collage.blend) to recreate the collage of figure 1. To use the Strip Masks in your project, you need to append (File > Append) the appropriate scene (collage) to your project. Then, you also need to copy/paste them in the scene of your timeline (see Disadvantage 2 below).

A mask is in essence a black-and-white image; where the white area represents the look-through or transparent area. It is based on the multiplication rule. Multiplying something by zero will always result in zero. Multiplying by one will left everything untouched. So, every pixel from an image is multiplied with a pixel from the mask. If the mask pixel is 1 (or white), it leaves the image untouched. If the mask pixel is zero (or black), the result will also be zero or black; effectively removing the image from view.

## How-to create this collage within Blender Video Sequence Editor (VSE)

There are essentially two ways to achieve this result. You can use strip masks which is the most intuitive and straight-forward method but also the least flexible. Or, you can use regular masks; created in the Image Editor.

There is also a wrong method. You could crop (Strip Properties > Crop > Left, Right, Top, Bottom) and change the position X and Y appropriately. The problem here is that it's not easy to move or scale the aera content, nor is it possible to add some animation (e.g. Ken Burns effect) to it. Masks is the way to go.


### Method 1: strip masks

1. Create 6 Color strips (white color) with the correct size (here, you have to use crop) and location. Place them on top of each other starting at top left and working clockwise. Give each color strip a name, e.g. msk-A1, msk-A2, ...  Do not group the Color or Movie strips. Masks don't work across metastrips.
2. Add 6 movie or image strips. Follow the same clockwise path as for the Color strips.
3. Apply the appropriate mask modifier to each Movie or image strip. Select a strip and press N to show the Properties panel, if it is not visible. Select the tab Modifiers and click on Add Strip Modifier. Choose Mask as modifier. Because the masks are strips in this method,click the Strip button from the Mask Input Type. Start typing the name of the mask strip, e.g. msk-... Select the appropriate one from the preview. In Figure 2, the top-left strip is selected and the mask msk-A1 will be applied.

{{< figure
  src = "/blender/assets/Mask-modifier.png"
  title = "Figure 2: Properties of the top-left strip; Modifiers panel."
>}}

4. Use the Transform tools to scale and reposition the strips until you have a nice picture within the area.
5. Put a full-size Color strip as background (e.g. white) underneath all other strips.

Advantages
* Creating the layout of the collage is straight-forward. You can see your collage growing. It's easy to change the dimensions of the different areas.
* Mask strips can be re-used in the same scene and don't have to be close to the strips where they are applied. So, you could collect all your mask strips at the front (e.g. negative frames) or end of your timeline.

Disadvantages
* You cannot group the masks nor the other strips. Strip masks that are contained in a metastrip are not visible outside it and vice versa.
* Strip masks are also not visible in other scenes. For example, if you have downloaded the blend-file from figure 1, you'll notice that the mask strips are contained in a scene "collage". If you need them in your scene, you'll have to copy/paste them.
* Non-rectangular masks are difficult to create. For example, you'll need 1 white and 3 black Color strips to create a triangular mask. 

### Method 2: regular masks

Masks are also used in other parts of Blender, e.g. Compositor. Regular masks are created with the Image Editor or the Movie Clip Editor; see [docs](https://docs.blender.org/manual/en/latest/movie_clip/masking/introduction.html). A nice YouTube tutorial is done by [Blender Frenzy](https://www.youtube.com/watch?v=ix8tmIdLRZg).

1. Create the masks in the Image Editor. You can search for "photo collage template" in Google Images for [some examples](https://img.freepik.com/free-vector/black-photo-frame-collage-template_23-2147871137.jpg). Use this image as background in the Image Editor. Name the masks as in the previous method; starting at top left and working clockwise. You can reuse these masks; so make sure that the names are meaningful to you.
3. Continue with step 2 from method 2. Choose Mask type in the Mask modifier and select the appropriate mask.

Advantages
* You can group your image or movie strips into metastrips. Regular masks are independent of metastrips and scenes. You can use them wherever you like.
* The mask shapes are very flexible. You can create masks within masks.

Disadvantages
* The creation of the masks is not as intuitive and straight-forward. You need a separate editor.
* The background of the masks is not immediately available as in the Sequencer. You' have to add a background image.
* Finetuning a mask with the real background movie is rather difficult because you see the result in the sequencer and you have to make the changes in the Image Editor.



