from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from os import path
import numpy as np
from PIL import Image
import random

def blue_color(word,font_size,position,orientation,random_state=None, **kwargs):
	#Recoloring function to generate shades of blue
	return "rgb(0,%d,%d)" % (random.randint(0,100), random.randint(100,254))

def custom_wordcloud(tempFileName, emphDictionary, maskFile, inputFile="", color_function="blue_color"):
	
	randomWords = []
	for word in emphDictionary:
		for x in range(emphDictionary[word]):
			randomWords.append(word)

	#Shuffle to fix the problem of repeated words being interpreted as being together
	random.shuffle(randomWords)

	#Generate text file wor wordcloud to use
	with open(tempFileName,"w") as f:
		for word in randomWords:
			f.write(word + ", ")
		with open(inputFile) as f2:
			words = f2.read()
			f.write(words)

	dir = path.dirname(__file__)

	text = open(path.join(dir,tempFileName)).read()

	mask = np.array(Image.open(path.join(dir,maskFile)))

	wordcloud = WordCloud(max_words=100, mask=mask, margin=10, random_state=3).generate(text)
	plt.imshow(wordcloud.recolor(color_func=blue_color),interpolation="bilinear")
	plt.axis("off")
	plt.show()
 
#wordList = {"Python" : 50, "Physics" : 6, "Data-analysis" : 25, "Creative" : 20, "Research" : 15, "Programming" : 8}
#custom_wordcloud("test.txt", wordList, maskFile="star.png", inputFile="qualitywords.txt")
