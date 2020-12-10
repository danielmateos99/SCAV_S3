import os

os.system('ffmpeg -i vp8.webm -i vp9.webm -i h265.mp4 -i av1.mkv \
    -filter_complex "nullsrc=size=640x480 [base]; \
    [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] \
    setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] \
    setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] \
    setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] \
    overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 \
    [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; \
    [tmp3][lowerright] overlay=shortest=1:x=320:y=240"\
     -c:v libx264 mandanga.mkv')
