

data = [0,1,0,0,0]
for i in range(len(data)-2):
    data[i+1]+=data[i]
print(data)
