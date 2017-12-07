from vidpy import Clip, Composition


video1 = 'sunset/sunset1_small.mp4'

clips = []

clip1 = Clip(video1)

# attempt to automatically remove background color
# you can also specify a color with color='#00ff00'
clip1.chroma(amount=0.001)
clip1.chroma(color="#9187ff")

clips = [clip1]


comp = Composition(clips, bgcolor='#FF87DC')
comp.save('sunsetlayer1.mp4')
comp.preview()
