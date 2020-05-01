import os
import codecs
import re

newspage = codecs.open("newsout.html", "r", "utf-8")
count = 0
newsdata = []
newsdata2 = []
marker = '<!-- REPLACE ME -->\n'
marker2 = 'REPLACE'
markefound = False

postSkeleton = codecs.open("bps.data", "r", "utf-8")
postSkeletonData = []

while True:
    count += 1
    line = newspage.readline()
    line = re.sub(r'\t', '', line)
    result = line.find(marker)
    if marker in line or marker2 in line:
        markefound = True
        print("marker found")
    else:
        if markefound is True:
            newsdata2.append(line)
            print("add to news2")
        else:
            newsdata.append(line)
    if not line:
        break
newspage.close()
for i in range(len(newsdata2)):
    print(newsdata2[i])

while True:
    count += 1
    line = postSkeleton.readline()
    line = re.sub(r'\t', '', line)
    postSkeletonData.append(line)
    if not line:
        break



f = codecs.open("newsout.html", "w", "utf-8")
for i in range(len(newsdata)):
    f.write(newsdata[i])
f.close()

f = codecs.open("newsout.html", "a", "utf-8")
for i in range(len(postSkeletonData)):
    f.write(postSkeletonData[i])
f.close()

f = codecs.open("newsout.html", "a", "utf-8")
for i in range(len(newsdata2)-1):
    f.write(newsdata2[i])
f.close()
