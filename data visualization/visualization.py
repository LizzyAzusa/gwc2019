'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarityList=[]

for i in range(len(tweetData)):
    textblob = TextBlob(tweetData[i]["text"])
    polarityList.append(textblob.polarity)

print (polarityList)

#Create the Graph
plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()



# Textblob sample:
# tb = TextBlob("I hate school")
# print(tb.polarity)
