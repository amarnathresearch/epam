#a = {'id':1}
#print(a)
#print(a['id'])

#b = {'id':1, 'name':'amar', 'designation':'trainer', 'time':[(9,12),(2,5)]}
#print(b)

trainer1 = {'id':1, 'name':'amar', 'designation':'trainer', 'time':[('9AM','12PM'),('2PM','5PM')]}
#print(trainer1)
#print(trainer1['time'][0][0])

trainer2 = {'id':2, 'name':'sivaram', 'designation':'trainer', 'time': [('10AM','12:30PM'),('2:30PM','5:30PM')]}

#print(trainer2)

trainers = [trainer1, trainer2]
print(trainers)


ex = {'id':1, 'id':2}
print(ex)

a = {'id':1, 'subjects':{'name':'python'}}
print(a)

print(a['subjects']['name'])

b = {'id':1, 'next':{'id':1, 'next':{'id':2, 'next':'none'}}}

print(b)
print(b['next']['next']['next'])






