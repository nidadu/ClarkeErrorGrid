#%%
import matplotlib.pyplot as plt
import numpy as np
from ClarkeErrorGrid import clarke_error_grid

# accuchek
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\accuchek_50.txt'
my_file = open(path, "r") 
content5 = my_file.read().splitlines() 
content5 = [float(i) for i in content5]
my_file.close()
print (content5)
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\accuchek_70.txt'
my_file = open(path, "r") 
content7 = my_file.read().splitlines() 
content7 = [float(i) for i in content7]
my_file.close()
print (content7)
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\accuchek_90.txt'
my_file = open(path, "r") 
content9 = my_file.read().splitlines() 
content9 = [float(i) for i in content9]
my_file.close()
print (content9)
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\accuchek_120.txt'
my_file = open(path, "r") 
content12 = my_file.read().splitlines() 
content12 = [float(i) for i in content12]
my_file.close()
print (content12)

ref_values_ac = [50]*len(content5) + [70]*len(content7) + [90]*len(content9) + [120]*len(content12)
pred_values_ac = content5 + content7 + content9 + content12
pred_values_ac = [x * 18.018 for x in pred_values_ac] 

# truemetrix
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\tru_50.txt'
my_file = open(path, "r") 
content5 = my_file.read().splitlines() 
content5 = [float(i) for i in content5]
my_file.close()
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\tru_70.txt'
my_file = open(path, "r") 
content7tr = my_file.read().splitlines() 
content7 = [float(i) for i in content7]
my_file.close()
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\tru_90.txt'
my_file = open(path, "r") 
content9 = my_file.read().splitlines() 
content9 = [float(i) for i in content9]
my_file.close()
path = r'C:\Users\nidad\Documents\Ukai\Unis\IIB\IIB Modules\4I14 Biosensors and bioelectronics\Coursework 1\error grid\ClarkeErrorGrid\tru_120.txt'
my_file = open(path, "r") 
content12 = my_file.read().splitlines() 
content12 = [float(i) for i in content12]
my_file.close()

ref_values_tr = [50]*len(content5) + [70]*len(content7) + [90]*len(content9) + [120]*len(content12)
pred_values_tr = content5 + content7 + content9 + content12
pred_values_tr = [x * 18.018 for x in pred_values_tr] 

plot, zone = clarke_error_grid(ref_values, pred_values, 'title') 
plot.show()

# %%
