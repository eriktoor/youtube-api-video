from videoDetails import getVideoViews
from updateVideoTitle import changeVideoTitle
import time
 


class creds: 
    def __init__(self):
        self.credentials = False 
        self.flow = False 
        self.youtube = False 
        self.num = 0
        
def main():
    c = creds() 
    timeout = 12000
    while (c.num < 5): 
        id = [YOUR-VIDEO-ID]
        viewCount = getVideoViews(id, c)
        print(viewCount)

        changeVideoTitle(viewCount, id, c)
        print("Go to https://www.youtube.com/watch?v=" + str(id) + " and check out the name.")

        for i in range(timeout):
            time.sleep(1)
            print(timeout-i)
        c.num += 1 
        timeout += 10

if __name__ == "__main__": 
    main()
