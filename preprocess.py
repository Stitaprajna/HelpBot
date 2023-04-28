file1 = open('','r')
text = file1.readlines()

import re
for i in range(len(text)):
  text[i] = text[i].lower()
  text[i] = re.sub('^[*\ufeff]',' ',text[i])
  text[i] = text[i].split()
  text[i] = ' '.join(text[i])
  
Text = [i for i in text if i!='']
txt = ' '
for i in Text:
  txt = txt + i + ' '

file2 = open('train_phase_1.txt','a+')
file2.write(txt)
file2.close()