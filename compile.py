from vidpy import Clip, Composition

video1 = "files/rainTest.mp4"
video2 = "files/N2.mov"

clips = []

clip1 = Clip(video1)

# attempt to automatically remove background color
# you can also specify a color with color='#00ff00'
clip1.chroma(amount=5.8)
clip1.chroma(color="#00FFFF")

clip2 = Clip(video2)

clips = [clip2, clip1]


comp = Composition(clips, bgcolor='#ffffff')
comp.save('output/test.mp4')
comp.preview()
