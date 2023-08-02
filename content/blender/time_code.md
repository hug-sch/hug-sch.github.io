+++
title = "How many time codes do you need?"
date = 2021-01-26
lastmod = 2021-05-26
categories = ["Blender", "VSE"]
+++
Every video editor has some kind of timeline. When a clip starts or ends is stored in a so called time code. Blender keeps track of several time codes. You can find some (but not all) of them, in the sidebar under the Time panel (see figure 1).

As the name implies, the timeline represents time (seconds). But, because the unit of a video clip (or strip in Blender talk) is one frame, the timeline is sometimes labeled in frames or a combination of time and frames. For example, in Blender you can choose to show the timeline in seconds or in frames. But, even the "seconds"-view is in fact a combination. The time code 01:21+11 indicates "1 minute and 21 seconds and 11 frames". Because each project has a frame-per-seconds `fps` parameter, you can always derive one code from the other. In a 30 fps project:

* frame 155 is at time 115/30 = 3.8333 seconds or in Blender notation: 00:03+25.
* time 2.5s falls within frame  2.5 * 30 = 75.

But what about all those time codes? Why do you need them? And what do they mean?

## 1. Simple strip with no cutting or trimming

When you add a strip to the timeline, the UI field `Start` is set to the frame number of the play head at the position you have chosen. The `Duration` is filled with the number of frames of the strip. That's all! You, as a user has to point where the strip should be placed and the duration is set automatically by the number of frames that the video clip contains (see figure 1).

{{< carousel
    "/blender/assets/time_code/time_code_1a.png"
    "/blender/assets/time_code_1b.png"
    "/blender/assets/time_code_1c.png"
>}}
Figure 1: Simple strip with no cutting or trimming.

So far, so good. But, let's take a closer look at the info in the side panel. For a starter, it feels a little awkward that the UI field `Current Frame` indicates 0 (zero) while the play head is at frame 5. But, OK. No big deal! `Current Frame` means the position of the play head relative to the start of the active strip. So, the frame counting within the strip starts at 0.

What about the field `End` (= frame 105) and the number appearing when you select the right handle (= 104). Frame 104 is definitely the last frame, not frame 35 (= Start + Duration). If the duration = 2 then the last frame is 6 (frame 5 & frame 6), not 7. Only with starting frame = 0, the equation End = Start + Duration is true.

It's also a little bit disturbing that you can change the UI field `Duration`; for example you can make the strip 50 frames long by entering that number in the `Duration` field. You'll get a visual indication that there is something wrong; there aren't 50 frames available. But nothing seems to be changed in the UI Time panel. When you shorten the duration, you will notice that the UI field `Strip Offset End` shows exactly how many frames you have shortened the clip (this is essentially trimming; see next section). To change the duration, you can also drag the left or right handle. So, it's possible to let the strip start before the original frame 5. But, what will you see in these non-existent frames. It turns out that you see the first and last fame as a "still" image. And this is exactly what the non-exposed Python fields `frame_still_start` and `frame_still_end` are used for.

With the following code, you can print the different time codes that Blender uses internally (see [Script Editor](script_editor.md) for an introduction to scripting). For this example, I have dragged the left handle of figure 1 to frame 0 and the right handle to frame 39; extending the original clip with 5 + 5 frames.

    strip = bpy.context.scene.sequence_editor.active_strip
    print("frame_start: ", strip.frame_start)
    print("frame_duration: ", strip.frame_duration)
    print("frame_final_duration: ", strip.frame_final_duration)
    print("frame_final_start: ", strip.frame_final_start)
    print("frame_final_end: ", strip.frame_final_end)
    print("frame_offset_start: ", strip.frame_offset_start)
    print("frame_offset_end: ", strip.frame_offset_end)
    print("frame_still_start: ", strip.frame_still_start)
    print("frame_still_end: ", strip.frame_still_end)

The result is:

    frame_start:  5
    frame_duration:  30
    frame_final_duration:  40
    frame_final_start:  0
    frame_final_end:  40
    frame_offset_start:  0
    frame_offset_end:  0
    frame_still_start:  5
    frame_still_end:  5

Please note, the value of  `frame_still_start` and `frame_still_end`. You should interpret these as offsets to the original start and end. Have you ever wondered why you can add a duration to a still image? When you import a still image in the timeline, the default duration is set to 26. But of course, there is only one frame (it should be a very big waste of storage to copy the same image for 24 more frames). The solution is the field `frame_still_end`. Below you'll find the result of the above code run on a fresh imported still image.

    frame_start:  0
    frame_duration:  1
    frame_final_duration:  26
    frame_final_start:  0
    frame_final_end:  26
    frame_offset_start:  0
    frame_offset_end:  0
    frame_still_start:  0
    frame_still_end:  25

The original frame duration is 1. The final duration is 26 frames; from frame 0 (`frame_start`) until `frame_start` + offset `frame_still_end` = frame 25. The amount of 26 frames seems to be hard-coded into Blender. The number of 26 seems a bit awkward and probably meant to be 25; which is more of a standard frame rate.

And there are more questions. What about audio? An audio file has no frames; only sampled data (see post [Audio Volume](audio_volume.md) for an introduction). I' ll cover this in a later post. Let's first tackle the problem of trimming and cutting. 

## 2. Strip with left and right trimming

Figure 2 shows a typical timeline with one strip of 30 frames (or seconds if you like). The original strip started at frame 5 and ended at frame 35. But, there has been some trimming, so that the actual strip - the one that you see in the timeline - starts at frame 12 and ends at frame 32. You can trim a strip by dragging the left and/or right handle or by changing the `Strip Offset Start` or `Strip Offset End` field in the Time panel. Or by cutting the strip, but this brings us into a new unknown territory (see section 3).

![fig 1](/blender/assets/time_code/time_code.svg)Figure 2: Time codes for a trimmed strip in Blenders's VSE.

You can find the same time codes with different names or interpretation in the Properties panel of the strip (see figure 2) and the Python interface. And here comes the confusion! The UI `Start` field is the same as the `frame_start` Python field and refers to the Start location of the original, untrimmed or uncut strip. From the UI perspective this is confusing because you "see" the strip starting at a different location than indicated in the `Start` field. The UI `Start` field states that the strip starts at frame 5; which is the start position of the original strip and which you can also derive from the Offset Overlay line. But the actual strip (the one that you see) starts at frame 1. This is also visible as a number if you select the left handle. This is the Python `frame_final_start` field but that field isn't exposed in the panel (as mentioned, you could see it if you select the left handle).

The UI `Duration` and `End` field then resembles the actual situation. The original strip had a duration of 30 frames (= the Python `frame_duration`  field), but the actual (trimmed) strip is only 15 frames long (= Python `frame_final_duration` field). So, the UI `Duration` is not the same as the Python `frame_duration` field. The same holds for the `End` field. This is asking for trouble.

![fig 3](/blender/assets/time_code/time_code_2.png)Figure 3: time_code.mp4 (bottom) is the strip from fig 1. time_code.001 is a different strip with different start and offsets.

Let's try a little exercise. You want to move strip time_code.001 from fig 3 to start at the same position as time_code.mp4, which is frame 12. How should you do it? I know: you could place the play head at frame 12, select the top strip and press Shift - S to snap the strip to the current frame. Or you can eye-ball it by dragging. But neither of these methods is very accurate on a large timeline. Also, to make our case: let's do the exercise with the Time panel of the UI.

The most obvious but wrong way is to change the strip's `Start` field to frame 12. This will actually move the strip further away. You have to set the actual start field. Doing it in code will also result in an error.

    strip_bottom = bpy.context.scene.sequence_editor.sequences_all['time_code.mp4']
    strip_top = bpy.context.scene.sequence_editor.sequences_all['time_code.001']
    strip_top.frame_final_start = strip_bottom.frame_final_start    #wrong!

The code above will align the top strip with the bottom one, but unfortunately by decreasing the `Strip Offset Start`. This is not what you want. The `Start` field should be reduced by 3 frames (the difference between the actual start of both strips). And that brings us to the last confusion in this section? How can you calculate the difference between the actual starts. One technique is the following. Place the play head at the actual start of the top strip (the frame indicated when you select the left handle). Select then the bottom strip. The difference is shown in the UI field `Current Frame`. This field does not mirror the current frame in the timeline (this is shown above the play head) but the (current) frame in the actual strip where the play head is positioned.

# Negative offsets 
To recapitulate: 
 You can increase the duration; either by dragging the right handle or by increasing the Duration time code in the side panel. But of course, then your strip in the timeline will reference non-existing frames in the file, so the last frame is extended (you'll get a still image). Strangely enough, you can also drag the left handle to the left. This will increase the duration but apparently not the start position.The newly created frames will also reference non-existing counterparts in the file, so the first image is extended. 


From the [documentation](https://docs.blender.org/manual/en/dev/video_editing/sequencer/sidebar/strip.html#time):

1. Start: Changes the starting frame number of the strip, which is the same as selecting and moving the strip.
2. Duration: Changes the length, in frames of the strip. This works by changing the end frame, which is the same as selecting and moving the strip’s right handle.
3. End: Specifies the ending time and ending frame number for the strip.
4. Strip Offset Start/End: Can be used to either extend the strip beyond the end frame by repeating the last frame. Or it can be used to shorten the strip, as if you were cropping the end frame. This is the same as adjusting the strip handles.
5. Hold Offset Start/End: Offset of the uncut strip content.
6. Current Frame: Position of the Playhead relative to the start of the active strip.


nine time codes: frame_start, frame_duration, frame_final_duration, frame_final_start, frame_final_end, frame_offset_start, frame_offset_end, frame_still_start, frame_still_end.