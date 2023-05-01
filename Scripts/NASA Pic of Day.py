import requests

# Set the URL for NASA's Astronomy Picture of the Day API and a filename for the image
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Send a GET request to the API
request = requests.get(url)

# Check the response status code to make sure the request was successful
if request.status_code != 200:
    print('Error: Status code = 200')
else:
    # picture_url = request.json()['url']  # Low resolution image
    picture_url = request.json()['hdurl']  # HD image

    filename = request.json()['title']

    if "jpg" not in picture_url:
        print("No image for today, it must be a video")
    else:
        pic = requests.get(picture_url, allow_redirects=True)

        open(filename + ".jpg", 'wb').write(pic.content)

        print("Image saved")
