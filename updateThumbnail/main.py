import urllib.request
import json 

def get_views(VIDEO_ID, API_KEY):
    url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=' + VIDEO_ID +'&key=' + API_KEY
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    res = json.loads(respData.decode('utf-8'))
    stats = res["items"][0]["statistics"]
    views = stats["viewCount"]

    return views 



def views_to_string(views): 
    ret = []

    curr = 0 
    v = str(views)[::-1]
    for idx, i in enumerate(v):
        if idx % 3 == 0 and idx > 0: 
            ret.append(",") 
        ret.append(i)
    
    return "".join(ret[::-1])

from PIL import Image
from PIL import ImageFont 
from PIL import ImageDraw

def create_thumbnail(views): 
    view_string = views_to_string(views)

    img = Image.open("sample-in.JPG")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Corp-Bold.otf", 90)
    draw.text((590,200), view_string + " VIEWS", (50, 205, 50), font=font)
    draw.text((590,300), "SO FAR", (255, 255, 255), font=font)

    img.save("thumbnail.jpg")


import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload


def update_video_thumbnail(ID, CREDENTIALS): 
    scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client.json"

    # Get credentials and create an API client
    flow = CREDENTIALS.flow if CREDENTIALS.flow else google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    CREDENTIALS.flow = flow 

    credentials = CREDENTIALS.credentials if CREDENTIALS.credentials else flow.run_console()
    CREDENTIALS.credentials = credentials 

    youtube = CREDENTIALS.youtube if CREDENTIALS.youtube else googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    CREDENTIALS.youtube = youtube 

    request = youtube.thumbnails().set(
        videoId=ID,
        media_body=MediaFileUpload("thumbnail.jpg")
    )
    response = request.execute()



class credentials: 
    def __init__(self):
        self.credentials = False 
        self.flow = False 
        self.youtube = False 
        self.viewCount = 0 
        self.num = 0


import time

def main():

    ID = "YDyrTlJ7YBo"
    API_KEY = "YOUR-API-KEY"  

    CREDENTIALS = credentials()

    while True: 
        timeout = 120 
        # STEP 1: Get Video Views
        current_views = get_views(ID, API_KEY)

        if int(current_views) > int(CREDENTIALS.viewCount): 
            # STEP 2: Create New Thumbnail 
            create_thumbnail(current_views)
            # STEP 3: Update Video Thumbnail
            update_video_thumbnail(ID, CREDENTIALS)
            print("UPDATING THUMBANIL, go to https://youtube.com/" + ID + " to check it out")
            timeout = 300
        else: 
            print("DID NOT UPDATE THUMBNAIL, will check again in 120" + str(timeout) + " seconds")
            timeout = 120 
        CREDENTIALS.viewCount = current_views 
        time.sleep(timeout)

            
if __name__ == "__main__":
    main()





