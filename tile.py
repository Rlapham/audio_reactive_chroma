import moviepy.editor as mp
from moviepy.editor import VideoFileClip, clips_array, vfx

video = mp.VideoFileClip("files/N5.mov")

clips = []
finalHold = []
arrayHolder = []
arrayHolder2 = []
arrayHolder3 = []
#
first1 = video.set_pos((0, 0)).resize((640, 320))
first2 = first1.fx( vfx.mirror_x)
first3 = first1.fx( vfx.mirror_y)
first4 = first2.fx( vfx.mirror_y)
finalHold = clips_array([[first1, first2],
                         [first3, first4]])

finalHold.write_videofile("files/N5_K.mp4", fps=20)
