import webbrowser
import time
import random

while True:
    sites = random.choice(['www.youtube.com/watch?v=dQw4w9WgXcQ', 'www.youtube.com/watch?v=7PCkvCPvDXk', 'www.youtube.com/watch?v=2H5uWRjFsGc', 'www.youtube.com/watch?time_continue=5&v=qr-IdHU3A5M'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)