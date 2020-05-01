import json
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


def changeVideoTitle(viewCount, id, c):

    title = "This Video Has " + str(viewCount) + " Views (How It Works)"
    desc = "This video is about how awesome APIs are. At the time that this script is updating the video has "  +str(viewCount)  + " views.\n\nSOCIAL\n--------------------------------------------------------------------------\nPatreon: https://patreon.com/eriktoor\nInstagram: https://instagram.com/erik_toor\nYoutube (Subscribe): https://www.youtube.com/user/TEDBET622?sub_confirmation=1 \n\nGithub Repo: https://github.com/eriktoor/youtube-api-video"


    scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]


    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = c.flow if c.flow else google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    c.flow = flow 

    credentials = c.credentials if c.credentials else flow.run_console()
    c.credentials = credentials 

    youtube = c.youtube if c.youtube else googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    c.youtube = youtube 

    request = youtube.videos().update(
        part="snippet", #,status
        body={
          "id": id,
          "snippet": {
            "categoryId": 22,
            # "defaultLanguage": "en",
            "description": desc,
            # "tags": [
            #   "tom scott","tomscott","api","coding","application programming interface","data api"
            # ],
            "title": title
          },
        }
    )
    response = request.execute()
    # print(response)
