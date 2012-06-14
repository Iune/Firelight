a = open('Files/c1.txt')
c1 = [line.strip() for line in open('Files/c1.txt')]
a.close()

b = open('Files/c2.txt')
c2 = [line.strip() for line in open('Files/c2.txt')]
b.close()

c = open('Files/c3.txt')
c3 = [line.strip() for line in open('Files/c3.txt')]
c.close()

d = open('Files/c4.txt')
c4 = [line.strip() for line in open('Files/c4.txt')]
d.close()

e = open('Files/c5.txt')
c5 = [line.strip() for line in open('Files/c5.txt')]
e.close()

f = open('Files/c6.txt')
c6 = [line.strip() for line in open('Files/c6.txt')]
f.close()

g = open('Files/c7.txt')
c7 = [line.strip() for line in open('Files/c7.txt')]
g.close()

h = open('Files/c8.txt')
c8 = [line.strip() for line in open('Files/c8.txt')]
h.close()

i = open('Files/c9.txt')
c9 = [line.strip() for line in open('Files/c9.txt')]
i.close()

j = open('Files/c10.txt')
c10 = [line.strip() for line in open('Files/c10.txt')]
j.close()

print "Hi, add a number" 
num1 = int(raw_input())
print "Hi, add another number"
num2 = int(raw_input())
num3 = num1 + num2
print num1 + num2
