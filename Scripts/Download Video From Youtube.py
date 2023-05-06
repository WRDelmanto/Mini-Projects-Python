from pytube import YouTube


def downloadVideoFromYoutube(link):
    # Set the YouTube URL of the video you want to download
    video = YouTube(link)

    # Download the video with the highest resolution
    video.streams.get_highest_resolution().download()  # Highest

    # Print when downloaded
    print("Video downloaded")


# This pytube version has an error, link for correction:
# https://github.com/pytube/pytube/issues/1558#issuecomment-1528377258
downloadVideoFromYoutube("https://www.youtube.com/watch?v=wYs_Y4OI4Ho")
