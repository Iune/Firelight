a = open('Files/c1.txt')
c1 = [line.strip() for line in open('Files/c1.txt')]
a.close()

a = open('Files/c2.txt')
c2 = [line.strip() for line in open('Files/c2.txt')]
a.close()

a = open('Files/c3.txt')
c3 = [line.strip() for line in open('Files/c3.txt')]
a.close()

a = open('Files/c4.txt')
c4 = [line.strip() for line in open('Files/c4.txt')]
a.close()

a = open('Files/c5.txt')
c5 = [line.strip() for line in open('Files/c5.txt')]
a.close()

a = open('Files/c6.txt')
c6 = [line.strip() for line in open('Files/c6.txt')]
a.close()

a = open('Files/c7.txt')
c7 = [line.strip() for line in open('Files/c7.txt')]
a.close()

a = open('Files/c8.txt')
c8 = [line.strip() for line in open('Files/c8.txt')]
a.close()

a = open('Files/c9.txt')
c9 = [line.strip() for line in open('Files/c9.txt')]
a.close()

a = open('Files/c10.txt')
c10 = [line.strip() for line in open('Files/c10.txt')]
a.close()

print "Please enter the points given to Song 1: " + c1[0]
s1p = int(raw_input())
c1[1] = s1p
c1[2] = int(c1[2]) + int(c1[1])

k = open('Files/c1.txt', 'w')
k.write(str(c1[0]) + '\n')
k.write(str(c1[1]) + '\n')
k.write(str(c1[2]) + '\n')
k.close()

print "Please enter the points given to Song 2: " + c2[0]
s2p = int(raw_input())
c2[1] = s2p
c2[2] = int(c2[2]) + int(c2[1])

k = open('Files/c2.txt', 'w')
k.write(str(c2[0]) + '\n')
k.write(str(c2[1]) + '\n')
k.write(str(c2[2]) + '\n')
k.close()

print "Please enter the points given to Song 3: " + c3[0]
s3p = int(raw_input())
c3[1] = s3p
c3[2] = int(c3[2]) + int(c3[1])

k = open('Files/c3.txt', 'w')
k.write(str(c3[0]) + '\n')
k.write(str(c3[1]) + '\n')
k.write(str(c3[2]) + '\n')
k.close()

print "Please enter the points given to Song 4: " + c4[0]
s4p = int(raw_input())
c4[1] = s4p
c4[2] = int(c4[2]) + int(c4[1])

k = open('Files/c4.txt', 'w')
k.write(str(c4[0]) + '\n')
k.write(str(c4[1]) + '\n')
k.write(str(c4[2]) + '\n')
k.close()

print "Please enter the points given to Song 5: " + c5[0]
s5p = int(raw_input())
c5[1] = s5p
c5[2] = int(c5[2]) + int(c5[1])

k = open('Files/c5.txt', 'w')
k.write(str(c5[0]) + '\n')
k.write(str(c5[1]) + '\n')
k.write(str(c5[2]) + '\n')
k.close()

print "Please enter the points given to Song 6: " + c6[0]
s6p = int(raw_input())
c6[1] = s6p
c6[2] = int(c6[2]) + int(c6[1])

k = open('Files/c6.txt', 'w')
k.write(str(c6[0]) + '\n')
k.write(str(c6[1]) + '\n')
k.write(str(c6[2]) + '\n')
k.close()

print "Please enter the points given to Song 7: " + c7[0]
s7p = int(raw_input())
c7[1] = s7p
c7[2] = int(c7[2]) + int(c7[1])

k = open('Files/c7.txt', 'w')
k.write(str(c7[0]) + '\n')
k.write(str(c7[1]) + '\n')
k.write(str(c7[2]) + '\n')
k.close()

print "Please enter the points given to Song 8: " + c8[0]
s8p = int(raw_input())
c8[1] = s8p
c8[2] = int(c8[2]) + int(c8[1])

k = open('Files/c1.txt', 'w')
k.write(str(c1[0]) + '\n')
k.write(str(c1[1]) + '\n')
k.write(str(c1[2]) + '\n')
k.close()

print "Please enter the points given to Song 9: " + c9[0]
s9p = int(raw_input())
c9[1] = s9p
c9[2] = int(c9[2]) + int(c9[1])

k = open('Files/c9.txt', 'w')
k.write(str(c9[0]) + '\n')
k.write(str(c9[1]) + '\n')
k.write(str(c9[2]) + '\n')
k.close()

print "Please enter the points given to Song 10: " + c10[0]
s10p = int(raw_input())
c10[1] = s10p
c10[2] = int(c10[2]) + int(c10[1])

k = open('Files/c10.txt', 'w')
k.write(str(c10[0]) + '\n')
k.write(str(c10[1]) + '\n')
k.write(str(c10[2]) + '\n')
k.close()
