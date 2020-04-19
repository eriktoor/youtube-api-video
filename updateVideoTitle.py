import json
# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.update
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


def changeVideoTitle(viewCount, id, c):
    
    title = "This video has " + str(viewCount) + " views."
    desc = "At the time that this script is updating the video I have "  +str(viewCount)  + " views on it. \n\nIt runs once every x min so it might miss a view here or there."
    
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
        part="snippet,status,localizations",
        body={
          "id": id,
          # "localizations": {
          #   "es": {
          #     "title": "no hay nada a ver aqui",
          #     "description": "Esta descripcion es en español."
          #   }
          # },
          "snippet": {
            "categoryId": 22,
            "defaultLanguage": "en",
            "description": desc,
            "tags": [
              "new tags"
            ],
            "title": title
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
 
