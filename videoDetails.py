# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import json




API_KEY = [YOUR-API-KEY]





def getVideoViews(id, c):

    scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"


    # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials)

    flow = c.flow if c.num else google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    c.flow = flow 

    credentials = c.credentials if c.num else flow.run_console(prompt='consent')
    #flow.run_console() pulls everything up 
    c.credentials = credentials 
    print(flow)

    youtube = c.youtube if c.num else googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    c.youtube = youtube 

    request = youtube.videos().list(
        key=API_KEY, 
        # part="snippet,contentDetails,statistics",
        part="statistics",
        id=id
    )


    response = request.execute()
    print(response)
    statistics = response["items"][0]["statistics"]
    viewCount = statistics["viewCount"]

    return viewCount
