#Difference Between Shallow and Deep copy
import copy
list1 = [[1,2], [3,4]]
shallow = copy.copy(list1)  
 # shallow copy
print(list1 is shallow) #False
#outer list new (Address are different)
print(list1[0][0] is shallow[0][0]) #True
#inner elements address are shared (Addresses are same)
#if element change in list1 also change in shallow because of address
deep=copy.deepcopy(list1)
#deep copy
print(list1 is deep) #False
#outer list new (Addresses are different)
print(list1[0][0] is deep[0][0]) #False
#inner list also new (Addresses are different)
print(shallow)
print(deep)