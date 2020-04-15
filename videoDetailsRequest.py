import urllib.request
import json 

def getViews(VID_ID, API_KEY):

        url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id='  + VID_ID + '&key=' + API_KEY
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        res = json.loads(respData.decode('utf-8'))
        print(res)
        statistics = res["items"][0]["statistics"]
        viewCount = statistics["viewCount"]

        return viewCount

