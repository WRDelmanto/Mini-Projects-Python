from moviepy.editor import VideoFileClip

path = "test.mp4"

videoClip = VideoFileClip(path)
videoClip.write_gif(path.replace(".mp4", ".gif"))
