#17
y = 0
job = [
    {
        'name' : 'Huy',
        'role' : 'waiter',
        'hours' : 12,
        'salary per hour' : 0.8
    },
    {
        'name' : 'Tung',
        'role' : 'cook',
        'hours' : 24,
        'salary per hour' : 1.5
    },
    {
        'name' : 'M.Duc',
        'role' : 'manager',
        'hours' : 20,
        'salary per hour' : 2,
    }
]
#18
b = {
    'name' : 'Don',
    'role' : 'waiter',
    'hours' : 12,
    'salary per hour' : 0.9
}
a = {
    'name' : 'H.Duc',
    'role' : 'waiter',
    'hours' : 14,
    'salary per hour' : 0.7
}

job.append(a)
job.append(b)
# print(job)
#19,20
print(job[2])
job[0] ={
    'name' : 'Huyen',
    'job' : 'waitress',
    'hours' : 14,
    'salary per hour' : 1
}
print(job)
#21
job.pop(-1)
print(job)
#22,23
for i in job:
    print(i)
    print(i['hours']*i['salary per hour'])
    y = y + i['hours']*i['salary per hour']
#24

print(y)