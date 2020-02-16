# Subtitle Matcher

Often, videos and its subtitles don't match.
It can be fixed with regex command like `rename`, but it's quite cumbersome.
So, I created a simple program that automatically match subtitles and videos.

The algorithm is simple.
1. Read each video file list and subtitle list.
2. Sort both of them.
3. For each zipped item, overwrite video file's name into subtitle file, except its extension.

This program requies the number of videos and subtitles are equal and the relative order of video files and subtitle files must be same.

Belows are valid examples.

video file list | subtitle list
----------------|-------------
videoS01E01.mp4 | videoE1.srt
videoS01E02.mp4 | videoE2.srt
videoS01E03.mp4 | videoE3.srt
videoS01E04.mp4 | videoE4.srt
videoS01E05.mp4 | videoE5.srt
videoS01E06.mp4 | videoE6.srt
videoS01E07.mp4 | videoE7.srt
videoS01E08.mp4 | videoE8.srt
videoS01E09.mp4 | videoE9.srt
videoS01E10.mp4 | videoE10.srt
videoS01E11.mp4 | videoE11.srt
videoS01E12.mp4 | videoE12.srt

Even though video file's number doesn't correspond to its subtitle, it's relative order fits and the program can automatically rename them.

video file list | subtitle list
----------------|-------------
another_video_1.mp4 | sub101.srt
another_video_2.mp4 | sub202.srt
another_video_3.mp4 | sub303.srt

## How to build an executable
```
npm install
npm run build
```