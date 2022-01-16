from datetime import datetime
import instaloader

login = ""
password = ""
instagram = ""

L = instaloader.Instaloader()
L.login(login, password)

posts = instaloader.Profile.from_username(L.context, instagram).get_posts()

since = datetime(2021, 1, 16)
until = datetime(2021, 1, 18)

for post in posts:
    if (post.date >= since) and (post.date <= until):
        print(post.date)
        L.download_post(post, "insta-posts-downloads")
