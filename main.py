from updateVideoTitle import changeVideoTitle
from videoDetailsRequest import getViews
import time
 


class creds: 
    def __init__(self):
        self.credentials = False 
        self.flow = False 
        self.youtube = False 
        self.viewCount = 0 
        self.num = 0

        
def main(): 
    c = creds()
    timeout = 720 
    while(c.num < 20,000): 
        id = "7-74A-FKWxo"
        API_KEY = "YOUR-API-KEY"
        viewCount = int(getViews(id, API_KEY))
        if viewCount != c.viewCount: 
            changeVideoTitle(viewCount, id, c)
            print("Changing viewCount...")
            print("Go to https://www.youtube.com/watch?v=" + str(id) + " and check out the name.")
            timeout = 720
        else: 
            print("The view count is the same as it was so we are not changing")
            timeout = 240 

        c.viewCount = viewCount 

        for i in range(timeout):
            time.sleep(1)
            if (timeout - i) % 60 == 0: 
                print(timeout-i)
        print("Completed running time number " + str(c.num) + ".")
        c.num += 1 


if __name__ == "__main__": 
    main()

