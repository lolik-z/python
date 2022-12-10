# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import sys
sys.path.append('../')
import Functions5 as F

while True:
   try:
      fileName = input('Введите имя файла для сжатия данных: ') #text.txt
      f = open(fileName, 'r')
      my_data = f.read()
      f.close()
      break
   except:
      print(f'Ошибка! Ошибка чтения файла {fileName}!')
fileName = fileName.split('.')
fileName_encode = fileName[0] + '_encode.txt'
f = open(fileName_encode, 'w')
f.write(F.rle_encode(my_data))
f.close()

f = open(fileName_encode, 'r')
encode_data = f.read()
f.close()
new_data = F.rle_decode(encode_data)

fileName_encode = fileName_encode.split('_')
fileName_decode = fileName_encode[0] + '_decode.txt'
f = open(fileName_decode, 'w')
f.write(new_data)
f.close()

# print(my_data)
# print(F.rle_encode(my_data))
# print(new_data)




