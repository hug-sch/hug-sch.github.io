+++
title = "FFMPEG useful commands"
date = 2021-01-05
lastmod = 2021-01-05
categories = ["ffmpeg"]
+++
FFMPEG is a command line tool for handling (decode, encode, convert, ...) video and audio files. It is used by many commercial and free software products, including Blender.  The core is the FFMPEG program, together with a video & audio player (FFPLAY) and a stream analyzer (FFPROBE). 

## 1. Generate testfiles

Sometimes you need a test video or test image with a specific resolution, duration or framerate. You can first try with ffplay to view the test video. Replace afterwards the ffplay command with ffmpeg and add the outputfile parameter.

<code>
ffplay -f lavfi -i testsrc=duration=10:size=1280x720:rate=30

ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 test.mp4
</code>

This command will show/create a count-up video with a resolution of 1280 x 720 pixels, a framerate of 30 frames per second with a duration of 10 seconds in MP4-format
More commands and test formats can be found at [bogotobogo](https://www.bogotobogo.com/FFMpeg/ffmpeg_video_test_patterns_src.php).

The following command will show/create a red color background with opacity set to 0.2, with a duration of 10 seconds and a resolution of 640x480 in MP4-format.

<code>
ffplay -f lavfi -i color=c=red@0.2:duration=5:s=640x480:r=10


ffmpeg -f lavfi -i color=c=red@0.2:duration=5:s=640x480:r=10 test.mp4
</code>

## 2. Combine several video fragments into one file

I used to create my videos in separate scenes; e.g. one scene for each month of a yearly review montage. During the year I could render the separate scenes into a video fragment. At the end of the year I need then to combine them into one piece.

<code>
concatenate: ffmpeg -safe 0 -f concat -i list.txt -c copy output.mp4
</code>

The output file is called "output.mp4". The monthly fragments are named in a separate file "list.txt" which contains 12 lines with the name of the fragments, eg. "01-jan.mp4 02-feb.mp4 ... 12-dec.mp4". You have to run the command in the folder where the fragments are located.
