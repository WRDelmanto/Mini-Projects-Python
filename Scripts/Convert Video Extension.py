from moviepy.editor import VideoFileClip

path = "temp"
oldExtension = ".ts"
newExtension = ".avi"

videoClip = VideoFileClip(path)
videoClip.write_gif(path.replace(oldExtension, newExtension))
