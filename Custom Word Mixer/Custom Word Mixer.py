Custom=['Blue','Indigo','Violet'] #different test data from video
from random import randint
def randomG(word):
    randomindex=randint(0,len(Custom)-1)
    return f'{Custom[randomindex]} {word}'
     
with open('./Custom Word Mixer/Custom Word Mixer.txt', 'r') as file:
    paragraph = file.read()
    wordList=paragraph.split()
    SentenceList=list(map(randomG,wordList))
    ParaCount = int(input('How many Paragraphs do you want? \n'))
    with open('./Custom Word Mixer/Paste.txt', 'a') as writefile:
        for count in range(ParaCount):
                writefile.write(''.join(SentenceList) + '\n\n')
