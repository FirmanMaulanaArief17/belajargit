listfibo = [1,2]
c = 1
while(listfibo[c]<=4000000):
    c+=1
    dummy=listfibo[c-1] + listfibo[c-2]
    listfibo.append(dummy)
listfibo.pop()
print(sum(listfibo))