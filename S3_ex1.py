import os

exit = True
while exit == True:

    print("Select a resolution: ")
    print("[1]: 720p")
    print("[2]: 480p")
    print("[3]: 360x240")
    print("[4]: 160x120")
    print("[5]: Exit")

    x = int(input())


    if x == 1:
        videores = "cut1280x720.avi"
        exit = False
    elif x == 2:
        videores = "cut720x480.avi"
        exit = False
    elif x == 3:
        videores = "cut360x240.avi"
        exit = False
    elif x == 4:
        videores = "cut160x120.avi"
        exit = False
    elif x == 5:
        break
    else:
        print('Error: Select another value.')
        print(" ")

if os.path.isfile(videores):
    line1 = "ffmpeg -i {} -c:v libvpx -b:v 1M -c:a libvorbis vp8.webm".format(videores)
    line2 = "ffmpeg -i {} -c:v libvpx-vp9 -b:v 2M vp9.webm".format(videores)
    line3 = "ffmpeg -i {} -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265.mp4".format(videores)
    line4 = "ffmpeg -i {} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental av1.mkv".format(videores)
    os.system(line1)
    os.system(line2)
    os.system(line3)
    os.system(line4)
else:
    print("The file can't be found.")
    print(" ")
