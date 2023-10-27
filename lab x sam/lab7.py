lines = ['one', 'two', 'three']
with open('lab1.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run' + line)
        print('Done!')