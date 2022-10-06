import pandas as pd

wordList = pd.read_csv("words.csv", header=None, names=["word"])

print(wordList[0:10])