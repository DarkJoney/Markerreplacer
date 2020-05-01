import os
import codecs
import re

newspage = codecs.open("newsout.html", "r", "utf-8")
count = 0
newsdata = []
newsdata2 = []
marker = '<!-- REPLACE ME -->\n'
markefound = False

postSkeleton = codecs.open("bps.data", "r", "utf-8")
postSkeletonData = []

while True:
    count += 1
    # Get next line from file
    line = newspage.readline()
    line = re.sub(r'\t', '', line)
    result = line.find(marker)

    if result != -1:
        markefound = True
        print("marker found")
    if result == -1:
        if markefound is True:
            newsdata2.append(line)
            print("add to news2")
        else:
            newsdata.append(line)
        # if line is empty
        # end of file is reached
    if not line:
        break

while True:
    count += 1
        # Get next line from file
    line = postSkeleton.readline()
    line = re.sub(r'\t', '', line)
    postSkeletonData.append(line)
        # if line is empty
        # end of file is reached
    if not line:
        break

    # print(newsdata)
    # print(markefound)

    # for i in range(len(newsdata)):
    #     print(newsdata[i])
    #

for i in range(len(newsdata2)):
    print(newsdata2[i])

f = codecs.open("newsout.html", "w", "utf-8")
for i in range(len(newsdata)):
    f.write(newsdata[i])
f.close()
f = codecs.open("newsout.html", "a+", "utf-8")

for i in range(len(postSkeletonData)):
    f.write(postSkeletonData[i])
f.close()
f = codecs.open("newsout.html", "a+", "utf-8")
for i in range(len(newsdata2)):
    f.write(newsdata2[i])
f.close()



