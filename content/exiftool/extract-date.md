+++
title =  "Extract date & time from videos & photos"
date =  2022-12-05
lastMod =  2022-12-01
categories =  ["exiftool"]
+++

Sometimes you need to know the date and time a photo is taken or a video is recorded. Nowadays, digital cameras store these metadata within the file itself, next to the actual image, or in an external file (sidecar). Typical metadata elements are: date and time the photo was taken, location, camera brand, camera setup (aperture, shutter speed), ... There are a few standard types of metadata: Exif, XMP, IPTC, and Dublin Core; see [PhotoMetadata.org](https://photometadata.org/META-101-metadata-types) for an in-depth review. Sometimes, the metadata is absent or deleted or incorrect.
- You have scanned the photo from paper or the video from film. Maybe the development date is printed at the back of the photo or is reflected in the filename e.g. 20230431_135520.jpg. But, how can you transfer these dates into the metadata?
- You have imported the digital images from a source that has deleted the metadata. For example, Whatsapp & Facebook will remove the date & time (and other info) at the time you upload the material. The name of the file gives you no clue what-so-ever; see figure 1. Other services will keep the metadata but make other changes. For example, uploading photos & videos to OneDrive will give you filenames like YYYYMMDD_HHMMSS, based on the available metadata or upload date. GooglePhotos will not change the original filename (e.g. img_1314.jpg) but will add a so-called side car file next to your photo or video with the same name (e.g. img_1314.jpg.xmp ). This sidecar contains either the date/time info from the original image and/or the date/time of uploading the file to the Google services. It will also convert your "live" (iPhone) photo to a small mp4-video.
- The settings of your camera weren't correct at the time of recording. The metadata then, of course, will also no be correct. For dates, if you know the time of a particular recording however, you can always recalculate the other info by adding or subtracting time.

On top of that, there is no universal agreement on the naming and interpretation of the possible metadata fields, in particular the date/time fields: are we talking about the date/time the photo is taken, is processed, is stored, ...? Certainly for videos, you are in nowhere land. So, it's up to the software you are using (Digikam, XnView, Faststone, ...) how to manage these metadata. And also here is the quality of service very also very uneven.

# How discover all dates in your photo or video

You need the open source software [Exiftool](https://exiftool.org/). For video files, the [MediaInfo](https://mediaarea.net/en/MediaInfo) app is also widely used.

To install ExifTool, you can follow the nice tutorial of [Q-tips](https://youtu.be/j9osB_eRuCU?t=93); start at 1:33. Suppose you have two files in a test-folder: IMG_4397.JPG and IMG_4392.MOV (both shot with an iPhone).

In Windows, you can right-click on a file and select Properties. For a JPG, this will reveal a Date Taken field. For the MOV, you can get (sometimes) a Media Created field under the Details tab. There are however much more date fields and these are also not the standard names. The following exif-command shows all date/time related info from a photo or video.

```exiftool -time:all -groupNames -short IMG_4397.JPG```

-time:all is a shortcut for all time-related fields. -groupNames will print the name of the group in front of the fields. -short will print the tag names in stead of the longer tag descriptions. The output for a typical jpg file is as follows.

{{< figure
  src = "/exiftool/assets/exif-jpg-time-all.png"
  caption = "Figure 1: Output of exif command for a jpg-file."
  class = "img-fluid float-end" 
>}}


# Rename the Google TakeOut files in a YYYYMMDD_HHMMSS format

If you store your photos and videos on Google Photos, there is a less known feature, called [Google TakeOut](https://takeout.google.com/). Besides downloading your photos and videos (without any size limit as in the regular download), it provides you with some additional benefits such as save-guarding your face recognition data and the upload date. The latter could useful in case the source service (e.g. WhatsApp, Facebook) has deleted the metadata).

You probably don't want to download all of your photos, so, it's better to create beforehand some albums e.g. one album per year or per month. Then, head to the Google TakeOut website, select the option Google Photos and your album. Wait for a ready-mail and download the zip-file. A typical TakeOut of iPhone material is:

{{< figure
  src = "/exiftool/assets/google-take-out.png"
  caption = "Figure 2: Typical output from Google Take Out."
  class = "img-fluid float-end" 
>}}

For each image or video, there is an accompanying sidecar JSON-file. The files with the weird names (0100E3....) are from WhatsApp. The sidecar JSON contains the following data.

``` JSON
{
  "title": "0100E30E-AA4F-4D02-A1E8-727A4107063D.mov",
  "description": "",
  "imageViews": "2",
  "creationTime": {
    "timestamp": "1670266930",
    "formatted": "Dec 5, 2022, 7:02:10 PM UTC"
  },
  "photoTakenTime": {
    "timestamp": "1667502010",
    "formatted": "Nov 3, 2022, 7:00:10 PM UTC"
  },
  "geoData": {
    "latitude": 0.0,
    "longitude": 0.0,
    "altitude": 0.0,
    "latitudeSpan": 0.0,
    "longitudeSpan": 0.0
  },
  "geoDataExif": {
    "latitude": 0.0,
    "longitude": 0.0,
    "altitude": 0.0,
    "latitudeSpan": 0.0,
    "longitudeSpan": 0.0
  },
  "people": [{
    "name": "Marietta"
  }],
  "url": "",
  "googlePhotosOrigin": {
    "fromPartnerSharing": {
    }
  },
  "photoLastModifiedTime": {
    "timestamp": "1670267176",
    "formatted": "Dec 5, 2022, 7:06:16 PM UTC"
  }
}
```
The geoDataExif are the original location but these data has been erased by WhatsApp.  As know, it is also possible to add a location within the Google Photos. This location is stored within the key geoData. It is also possible to use face recognition. The recognized faces are stored within the key people. Note that there are also three dates available: creationTime, photoTakenTime, and photoLastModifiedTime. The first and last one are the date and time the photo is downloaded. The photoTakenTime is more interesting. It contains either the date/time from the metadata of the photo OR -if absent as is the case for WhatsApp photos- the date/time that the photo is uploaded to the Google storage. If you are in the habitude to save a photo immediately upon receiving it from WhatsApp, then this Date/time field is an approximation of the original date/time the photo was taken.

With the following ExifTool command you can update the date/time fields of the exif metadata with the PhotoTakenTime field. The dot at the end of the command is necessary. It means that all files from the current directory (= .) should be processed.

```exiftool --ext json -r -overwrite_original -tagsfromfile "%d/%F.json" -d %s "-Alldates<PhotoTakenTimeTimestamp" .```

If you want to change the filename to a format as YYYYMMDD_HHMMSS.xxx then you should run the following command.

```exiftool --ext json -d %Y%m%d_%H%M%S%%-c.%%e "-filename<CreateDate" -overwrite_original .```

In case you don't want loose the connection between the JSON file and the corresponding photo or video, you need also change the name of the JSON file. This is done with the following command.

```exiftool -ext json -d %s "-filename<${PhotoTakenTimeTimestamp;$_=$self->InverseDateTime($_);DateFmt('%Y%m%d_%H%M%S%%-c.%%e')}" -overwrite_original .```
