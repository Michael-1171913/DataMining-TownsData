import pandas as pd
import numpy as np

fileinput = open('university_towns.txt', 'r')
fileoutput = open('university_towns_clean.csv', 'w')
lines = fileinput.readlines()

fileoutput.write('State,RegionName\r\n')

state = ''
for line in lines:
    lastpiece = line[line.find('[') + 1 : line.find(']')]
    firstpiece = ''
    if '(' in line[0:line.find('[')]:
        firstpiece = line[line.find('(') + 1 : line.find(')')]
    else:
        firstpiece = line[0:line.find('[')]
    if lastpiece == 'edit':
        state = firstpiece
    else:
        fileoutput.write('{},{}\r\n'.format(state, firstpiece))
        print(state, '|', firstpiece)
        

fileinput.close()
fileoutput.close()
