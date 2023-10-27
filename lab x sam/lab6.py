with open('lab1.txt', 'a+') as f:
    f.write('\nIm additional line')
with open('lab1.txt' , 'r') as f:
    result = f.readlines()
    print(result)