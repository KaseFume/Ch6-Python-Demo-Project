with open('./Gibberish Generator/Gibberish Generator.txt', 'r') as file:
    paragraph = file.read()
    ParaCount = int(input('How many Paragraphs do you want? \n'))
    with open('./Gibberish Generator/Paste.txt', 'a') as writefile:
        for count in range(ParaCount):
                writefile.write(paragraph + '\n')
