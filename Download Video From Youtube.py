from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=rYEDA3JcQqw")

print("----------------------------------------------")
print("----- Downloading -----")
print("")
print("- Title")
print(yt.title)
print("")
print("- Author")
print(yt.author)
print("")
print("- Duration (Seconds)")
print(yt.length)
print("")
print("- Description")
print(yt.description)
print("----------------------------------------------")

stream = yt.streams.get_by_itag(22)
stream.download()
