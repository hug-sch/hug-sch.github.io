+++
title = "Color picker in Blender"
date = 2022-10-01
lastmod = 2022-10-15
categories = ["Blender", "VSE"]
+++
Color is my daylong obsession, joy, and torment. Claude Monet (1840 – 1926)

Color is a perceptual phenomenon, created by our brain. It is the result of the stimulation of three specific types of cells within the retina. Normally with light of a certain frequency. But, it doesn't need to be light. It can also easily be triggered by other stimuli; e.g. pressure on the eyeball. As such, color does not exist in reality and is not an inherent property of light but the result of the interaction between our brain and light. Many of the technical implementation details of color in our computers and their associated problems cannot be fully understood without this link to the human eye and brain.

For example, [Blender](https://docs.blender.org/manual/en/dev/interface/controls/templates/color_picker.html) has 5 alternative color pickers. You can choose one of them with Edit > Preferences > Interface. They all look very similar, yet also a bit different. Why? And why do we need 5 of them? Does it matter if you choose one or the other to pick a color? And if not, why is there a little warning ('Gamma corrected') only underneath the Hex selection? What is the meaning of those abbreviations like RGB, HSV, HSL, Hex? The sliders (H, S, ...) suggest that you can enter a value between 0 and 1. This is true for most of them but with a few you can enter values > 1. What do those values mean? ...

![Color Picker](/blender/assets/color-picker.png)
The blueish color with the name "Iceberg" is selected in each example. The little white dot in the circle or square shows the location of this particular color in color space. There are two circle and three square variants of the color picker. For each variant, you can choose between a RGB, HSV or Hex notation of the values; except for type 2 (only RGB, HSL or hex). So, the Hex panel (top right) is only shown for illustration of this notation. Note however, that Hex #71A6D2 &#8800; RGB (0.165, 0.381, 0.644). You can check it with the [hex color calculator](https://www.w3schools.com/colors/colors_hexadecimal.asp) of W3Schools. For the solution, please read-on. With the horizontal bar (type 3 - 5) you can pin the Hue (3), the Saturation (4) or the Value (5). With the horizontal bar, you can set the value (1) or Lightness (2) of the color.

## Color model

RGB, HSV and HSL are color models: mathematical descriptions of color. These models define a color according to three attributes. Red, green and blue for the RGB model. Hue, Saturation, and Value or Lightness for the HSV or HSL model.

The RGB color model is based on an analogy with the inner workings of the human eye. The color-sensitive cells in the retina belong to three types, that were once thought to be sensitive for red, green or blue color. The so-called primary colors.

A computer display mimics this organization by providing each pixel with red-, green-, and blue-light emitting led's. So, for a red color, turn on the red LED's. But, what if you want another color, say yellow. In humans, yellow is seen when the so-called red- and green-sensitive cells are responding. The output of these two cells is integrated in our brain to create the yellow perception. So, if you want yellow on the computer display, you have to turn on both the red and green LED's. The light rays of these led's hit our color-sensitive cells at the back of the retina and initiate the color perception.

The RGB color model is thus an additive model. New colors are created by adding the three primary colors in various quantities. Adding red and green gives us yellow, red and blue forms magenta and green and blue results in cyan. Undoubtedly, you have seen the additive diagrams as in figure 3.

So, let's try to test our understanding of the additive model by recreating those diagrams in Blender. That shouldn't be to hard, is it?