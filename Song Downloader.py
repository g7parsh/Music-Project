from __future__ import unicode_literals
import youtube_dl
import json
import os
import datetime
import shutil
from pprint import pprint
musicFile = ""
def remove_non_ascii_1(text):

	return ''.join([i if ord(i) < 128 else ' ' for i in text])





if __name__ == '__main__':
	songURLs = open("Song URLs.txt",'w')
	songList = []
	
	saveDir = "Songs"
	if not os.path.exists(saveDir):
		os.makedirs(saveDir)
	musicFile = raw_input("Enter Songs JSON ")
	
	with open(musicFile) as data_file:    
		data = json.load(data_file)
		#print(data)
	
	#print len(data)
	for x in data:
		print >>songURLs, [x['url'],remove_non_ascii_1(x['title'])] 
		songList.append(x['url'])
	
	
	options = {
		'format': 'bestaudio/best', # choice of quality
		'extractaudio' : True,      # only keep the audio
		#'quiet':True,
		#'audioformat' : "mp3",      # convert to mp3 
		#'outtmpl': saveDir +'/%(title)s.mp3',        # name the file the ID of the video
		#'outtmpl': saveDir +'/%(ext)s/%(title)s.mp3',        # name the file the ID of the video
		'outtmpl':saveDir +'/%(ext)s/%(title)s.%(ext)s',        # name the file the ID of the video
		
		'noplaylist' : True,        # only download single song, not playlist
		'prefer_ffmpeg':True,
	   # 'simulate': True,
	}
	
	with youtube_dl.YoutubeDL(options) as ydl:
		#with songURLs.open()
		#print "hi"
		#for item in songList:
		ydl.download(songList)
		#test =  ydl.extract_info(songList[0])
		#newString = remove_non_ascii_1(test["title"])
		#shutil.move(newString, saveDir+'/'+ newString+'.mp3') 		