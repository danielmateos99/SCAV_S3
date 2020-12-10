import os

print("Name of the file you want to stream:")
video = input()

if os.path.isfile(video):
    line = "ffmpeg -i {} -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000".format(video)
    os.system(line)
else:
    print("The file does not exist")
