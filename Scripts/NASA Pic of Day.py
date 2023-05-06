import requests


def downloadNasaPicOfTheDay(shouldDownloadHd=True):
    # Set the URL for NASA's Astronomy Picture of the Day API and a filename for the image
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

    # Send a GET request to the API
    request = requests.get(url)

    # Check the response status code to make sure the request was successful
    if request.status_code != 200:
        print('Error: Status code = 200')
    else:
        if shouldDownloadHd:
            # HD image
            picture_url = request.json()['hdurl']
        else:
            # Low resolution image
            picture_url = request.json()['url']

        # Get the image title
        filename = request.json()['title']

        # If the image URL does not contain "jpg", it's likely a video instead of an image
        if "jpg" in picture_url or "png" in picture_url:
            # Send a GET request to the image URL
            pic = requests.get(picture_url, allow_redirects=True)

            # Save the image with the filename
            open(filename + ".jpg", 'wb').write(pic.content)

            # Print a success message
            print("Image saved")
        else:
            print("No image for today, it must be a video")


downloadNasaPicOfTheDay(True)
