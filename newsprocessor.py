import os
import codecs
newspage = codecs.open("blog-home.html", "r", "utf-8")
newsdata = newspage.readlines()
replacement = 'NEY\n'

postSkeleton = codecs.open("bps.data", "r", "utf-8")
postSkeletonData = postSkeleton.readlines()
print(newsdata)
marker = '<!-- REPLACE ME -->\n'
markefound = False

fileLength = 0
for x in newsdata:
    fileLength = fileLength + 1
    result = newsdata[fileLength].find(marker)
    if result != -1:
        markefound = True
        newsdata[x] = str(postSkeletonData).strip('[]')

postLength = 0
for x in postSkeletonData:
    postLength = postLength + 1
#print(postSkeletonData)

for x in range(0, fileLength):
    #print(newsdata[x])
    result = newsdata[x].find(marker)
    if result != -1:
        markefound = True
        newsdata[x] = str(postSkeletonData).strip('[]')

if markefound is True:
    print("MARKER FOUND")

fileLength = fileLength + postLength

f = codecs.open("guru99.txt","w+", "utf-8")
for i in range(0, fileLength):
    f.write(newsdata[i])