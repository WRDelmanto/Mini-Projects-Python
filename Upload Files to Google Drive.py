from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

path = "D:\Programming\Mini-Projects-Python"

gauth = GoogleAuth()

gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

for i in os.listdir(path):
    f = drive.CreateFile({"title": i})
    f.SetContentFile(os.path.join(path, i))
    # f.Upload()

f = None  # Prevent Bug
