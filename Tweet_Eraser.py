import os
import time
import twitter

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open(r'..\settings\Tweet_Eraser.ini') as f:
    lines = f.readlines()

api = twitter.Api(
    consumer_key = lines[0].rstrip('\n'),
    consumer_secret = lines[1].rstrip('\n'),
    access_token_key = lines[2].rstrip('\n'),
    access_token_secret = lines[3].rstrip('\n')
)

dt1 = time.time()
screen_name = lines[4].rstrip('\n')
leaving_word = 'ㅤ'

while True:
    statuses = api.GetUserTimeline(screen_name = screen_name) 
    for s in statuses:
        if not leaving_word in s.text :
            api.DestroyStatus(s.id)
    dt2 = time.time()
    if dt2-dt1>=120:
        break