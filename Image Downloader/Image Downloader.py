from urllib.request import urlretrieve
link=input('Image Downloader Link: ') #test data: https://preview.redd.it/version-4-2-livestream-megathread-masquerade-of-the-guilty-v0-y98dzjsrk4yb1.png?width=1920&format=png&auto=webp&s=f276f05d2268f851b7e408fbf5e011c48f896375
filename=input('File Name: ')
urlretrieve(link,filename+'.jpg')