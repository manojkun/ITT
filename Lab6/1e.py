import re
st = "my reg no is 160911164"
reg = re.sub(r'\D',"",st)
print("reg no is: ",reg)
