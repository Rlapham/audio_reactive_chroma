from vidpy import Clip, Composition
import cv2
from numpy import interp
import moviepy.editor as mp
from pydub import AudioSegment


sound = AudioSegment.from_file("files/rain.mp4")
vidcap = cv2.VideoCapture('/Users/richardlapham/desktop/fade/files/rain.mp4')

valArray = []
count = 0
audioCount = 0
audioMax = sound.max
print audioMax


###map
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


# each frames
ret, image = vidcap.read()
## max RGB: 765

while ret is True:
    success, img = vidcap.read()
    tempAudio = translate(sound[audioCount].rms, 0, audioMax, 0, 765)
    # print tempAudio

    for i in range (0, 640):
        for a in range (0, 1280):
            tempVal = img[i][a]
            tempTot = tempVal[0] + tempVal[1] + tempVal[2]
            if tempTot < tempAudio:
                img[i][a] = (255, 255, 0)

    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite("files/rain/frame%d.jpg" % count, img)     # save frame as JPEG file

    count += 1
    audioCount += 20
