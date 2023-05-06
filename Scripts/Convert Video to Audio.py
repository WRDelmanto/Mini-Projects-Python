from moviepy.editor import VideoFileClip


def videoToAudio(input_video, output_audio):
    # Open the video file
    video = VideoFileClip(input_video)

    # Get the audio from the video
    audio = video.audio

    # Save the audio
    audio.write_audiofile(output_audio)

    # Close the video file
    video.close()


videoToAudio("temp.mp4", "temp.mp3")
