from datetime import datetime 
from math import sqrt 
def main(**kwargs): 
for key in kwargs.items():
result = sqrt(key[1][0] **2 + key[1][1] **2) 
print(result) 
if __name__ == '__main__': 
    main()
start_time= datetime.now() main(one=[10, 3], two=[5, 4], three=[15, 13], four=[93, 53], five=[133, 15])
time_costs= datetime.now() -start_time
print(f"Время выполнения программы -{time_costs}")