import moviepy.editor as mp
from moviepy.editor import VideoFileClip, clips_array, vfx

video = mp.VideoFileClip("files/N3.mov")


clips = []
finalHold2 = []
arrayHolder = []
arrayHolder2 = []
arrayHolder3 = []
#
#
first1 = video.set_pos((0, 0)).resize((720, 360))
first2 = first1.fx( vfx.mirror_x)
first3 = first1.fx( vfx.mirror_y)
first4 = first2.fx( vfx.mirror_y)
finalHold2 = clips_array([[first1, first2],
                         [first3, first4]])



# composition = mp.concatenate(clips)
finalHold2.write_videofile("files/neurontest.mp4")
