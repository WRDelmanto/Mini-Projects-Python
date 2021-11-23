from moviepy.editor import AudioFileClip

videoSource = 'test.mp4'
audioDestination = 'test.mp3'

def extract_audio(video, audio):
    audio = AudioFileClip(video)
    audio.write_audiofile(audio, 44100)  # fps

if __name__ == '__main__':
    extract_audio(videoSource, audioDestination)