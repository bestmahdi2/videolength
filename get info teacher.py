from datetime import timedelta
from os import walk, path
from sys import stdout
from moviepy.editor import VideoFileClip


source = "."
duration = 0
types = ".mp4"
files_count = 0

def with_moviepy(filename):
	clip = VideoFileClip(filename)
	duration = clip.duration

	return duration #, fps, (width, height)


for dirpath, dirnames, filenames in walk(source):
	for file in filenames:
		if file.endswith(types):
			files_count += 1

count = 0
for dirpath, dirnames, filenames in walk(source):
	for file in filenames:
		if file.endswith(types):
			path_ = path.join(dirpath, file)
			duration += with_moviepy(path_)
			count += 1
	
		stdout.write('\r' + str("Files processed : {0}/{1}".format(count, files_count)))


# print(duration)


print("\nFull time: {}".format(str(timedelta(seconds=duration))))
input()