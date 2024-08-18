data = list(map(int, input().split()))
def quick_sort(data):
   if len(data) <= 1:
       return data
   else:
       q = data[len(data) // 2]
       data1 = []
       data2 = []
       data3 = []
       for i in data:
           if i < q:
               data1.append(i)
           elif i > q:
                data3.append(i)
           else:
               data2.append(i)
       return quick_sort(data1) + data2 + quick_sort(data3)

print(quick_sort(data))