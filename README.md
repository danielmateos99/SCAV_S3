### SCAV S3 ###
Daniel Mateos Manjón
NIA: 205514

## Excersise 1 ##
You can see it in the script "S3_ex1.py".
We change the codecs from the videos of seminar 2 to VP8, VP9, h265 and AV1.
In this case the names of the files are:
cut1280x720.avi, cut720x480.avi, cut360x240.avi and cut160x120.avi
The names of the generated videos are:
vp8.webm, vp9.webm, h265.mp4 and av1.mkv

Links:
VP8---> https://trac.ffmpeg.org/wiki/Encode/VP8
VP9---> https://trac.ffmpeg.org/wiki/Encode/VP9
h265--> https://trac.ffmpeg.org/wiki/Encode/H.265
AV1---> https://trac.ffmpeg.org/wiki/Encode/AV1

## Excersise 2 ##
You can see it in the script "S3_ex2.py".
Puts the four videos generated in the last excersise side by side and generates a new video, "mandanga.mkv".
Link: https://trac.ffmpeg.org/wiki/Create%20a%20mosaic%20out%20of%20several%20input%20videos

**Analysis and coment:**
For the 720p resolution I have noticed that the video with the VP8 codec played smoother than the VP9, ​​the h265 and the AV1; where I could see some clipping.
For a smaller resolution, such as 360x240, all the video looked similar to me because of the quality, but I saw the one with the AV1 codec as the worse, because i coud see some clipping in the movements.



## Excersise 3 ##
Using the command **"ffmpeg -re -i FILE -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000"** you stream the FILE in the local udp server.
You can watch the stream in another terminal using: **"ffplay udp://127.0.0.1:23000"**
Link: https://stackoverflow.com/questions/43826675/how-to-live-stream-a-local-video-using-ffmpeg

## Excersise 4 ##
You can see it in the script "S3_ex4.py".
We implement the excersise 3 into python where you can select the file you want to stream.
