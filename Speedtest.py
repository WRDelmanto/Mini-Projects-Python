# Python program to test
# internet speed

import speedtest

st = speedtest.Speedtest()

print("---------------------------------")
print("Ping")
# servernames = []
# st.get_servers(servernames)
st.get_best_server()

print(int(st.results.ping))

print("-")
print("Download")
print(round(st.download()/1000000, 2))

print("-")
print("Upload")
print(round(st.upload()/1000000, 2))
print("---------------------------------")
