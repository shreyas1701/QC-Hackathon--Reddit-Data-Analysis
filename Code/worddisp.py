from os import path
from wordcloud import WordCloud

#d = path.dirname('C:\Users\shrey\Downloads\HackQueenCIty')

# Read the whole text.
text = open("C:\\Users\\shrey\\Downloads\\HackQueenCIty\\wordscom.txt", "r")


# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()