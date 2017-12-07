import moviepy.editor as mp

video1 = mp.VideoFileClip("files/clouds.mp4").resize((1280, 640))

video1.write_videofile("files/clouds_pro.mp4", fps=20)
