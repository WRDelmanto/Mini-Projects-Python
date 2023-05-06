import speedtest


def getInternetInfo():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Find the best server based on latency and assign it to a variable
    servernames = []
    st.get_servers(servernames)
    st.get_best_server()

    # Print the ping time
    print("---------------------------------")
    ping = int(st.results.ping)
    print("Ping", ping)

    # Print the download speed
    print("-")
    download = round(st.download()/1000000, 2)
    print("Download", download)

    # Print the upload speed
    print("-")
    upload = round(st.upload()/1000000, 2)
    print("Upload", upload)
    print("---------------------------------")


getInternetInfo()
