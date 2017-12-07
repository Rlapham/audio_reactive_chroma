import moviepy.editor as mp

video1 = mp.VideoFileClip("files/trees.mp4").resize((1280, 640))

video1.write_videofile("files/trees_pro.mp4", fps=20)
