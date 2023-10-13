# Internet speed test using the OOKLA speed test API
import speedtest as test

# Set best server
server = test.Speedtest()
server.get_best_server()

# Test ping
ping = server.results.ping
print(f"Ping: {round(ping,2)}")

# Test the download speed
down = server.download()
down = down / 1000000
print(f"Download Speed: {round(down,2)} Mb/s")

# Test the upload speed
up = server.upload()
up = up / 1000000
print(f"Upload Speed: {round(up,2)} Mb/s")