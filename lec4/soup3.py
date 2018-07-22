from bs4 import BeautifulSoup
from urllib import request
def hook(index=0,frame_size=0,total=0):
    download = index * frame_size
    per = download/total * 100
    print(per)
res=request.urlretrieve("https://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4","fds1.mp4",hook)