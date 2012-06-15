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



print "Please enter the points given to Song 1: " + c1[0]
s1p = int(raw_input())
c1[1] = int(c1[1]) + s1p

print "Please enter the points given to Song 2: " + c2[0]
s2p = int(raw_input())
c2[1] = int(c2[1]) + s2p

print "Please enter the points given to Song 3: " + c3[0]
s3p = int(raw_input())
c3[1] = int(c3[1]) + s3p

print "Please enter the points given to Song 4: " + c4[0]
s4p = int(raw_input())
c4[1] = int(c4[1]) + s4p

print "Please enter the points given to Song 5: " + c5[0]
s5p = int(raw_input())
c5[1] = int(c5[1]) + s5p

print "Please enter the points given to Song 6: " + c6[0]
s6p = int(raw_input())
c6[1] = int(c6[1]) + s6p

print "Please enter the points given to Song 7: " + c7[0]
s7p = int(raw_input())
c7[1] = int(c7[1]) + s7p

print "Please enter the points given to Song 8: " + c8[0]
s8p = int(raw_input())
c8[1] = int(c8[1]) + s8p

print "Please enter the points given to Song 9: " + c9[0]
s9p = int(raw_input())
c9[1] = int(c9[1]) + s9p

print "Please enter the points given to Song 10: " + c10[0]
s10p = int(raw_input())
c10[1] = int(c10[1]) + s10p

