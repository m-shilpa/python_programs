##string = input()
##letters = []
##i=0
##for i in string:
##    if i.isalpha():
##        print(i)
##
####print(letters)


name = str
names = []
result = []

while name != '':
	name = input()
	names.append(name)
#print(name)
#print(names)

def corrector():
	#your code
    k = ''
    i=0
    for i in names:
        if i != '':
            for j in i:
                if j.isalpha() or j.isspace():
                    k += j
            
            result.append(k)
            k = ''

#    print(result)
    for i in result:
        print(i)
        


corrector()
