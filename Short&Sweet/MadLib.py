import pyinputplus as pyip
text = open('MadLib.txt', 'w')

text.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was \
unaffected by these events.')

text.close()

adj = pyip.inputStr(prompt="Enter an adjective: ")
noun = pyip.inputStr(prompt="Enter a noun: ")
verb = pyip.inputStr(prompt="Enter a verb: ")
nounV2 = pyip.inputStr(prompt="Enter a noun: ")

with open('MadLib.txt', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('ADJECTIVE', adj)
filedata = filedata.replace('NOUN', noun, 1)
filedata = filedata.replace('VERB', verb)
filedata = filedata.replace('NOUN', nounV2)

with open('MadLib.txt', 'w') as file:
    content = file.write(filedata)

file.close()
