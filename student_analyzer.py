nos = input('How many students?')
new_num = int(nos)
main_list = []
x = 0
total = 0
avg = 0
grade = ''

try:
    for i in range(new_num):
        name = input('What is name of student?')

        dic = {}
        new_list = []

        eng = int(input('Score in english? '))
        new_list.append(eng) 

        math = int(input('Score in math? '))
        new_list.append(math) 

        sci = int(input('Score in Science? '))
        new_list.append(sci) 
    #print('before',new_list)
    #print('before',dic)
    #print('before',main_list)
        dic[name] = new_list
        main_list.append(dic)
#print('after',new_list)
except:
    print('Enter correct score in digits')
for x in main_list:
    for k,v in x.items():
        total = sum(v)
        avg = total / len(v)
        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 60:
            grade = 'C'
        else:
            grade = 'F'
        print('Student:',k)
        print('Marks:',v)
        print('Total:',total)
        print('Average:',avg)
        print('Grade:',grade)

#print('after',dic)
#print('after',main_list)



