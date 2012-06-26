import os

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

k = open('Files/c8.txt', 'w')
k.write(str(c8[0]) + '\n')
k.write(str(c8[1]) + '\n')
k.write(str(c8[2]) + '\n')
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

def schose(snum):
    print "Please enter the number of the song that placed: " + str(snum)
    sval = int(raw_input())
    if sval == 1:
        l = open('Files/c1.txt')
        stemp = [line.strip() for line in open('Files/c1.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c1.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 2:
        l = open('Files/c2.txt')
        stemp = [line.strip() for line in open('Files/c2.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c2.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 3:
        l = open('Files/c3.txt')
        stemp = [line.strip() for line in open('Files/c3.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c3.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 4:
        l = open('Files/c4.txt')
        stemp = [line.strip() for line in open('Files/c4.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c4.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 5:
        l = open('Files/c5.txt')
        stemp = [line.strip() for line in open('Files/c5.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c5.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 6:
        l = open('Files/c6.txt')
        stemp = [line.strip() for line in open('Files/c6.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c6.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 7:
        l = open('Files/c7.txt')
        stemp = [line.strip() for line in open('Files/c7.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c7.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 8:
        l = open('Files/c8.txt')
        stemp = [line.strip() for line in open('Files/c8.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c8.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 9:
        l = open('Files/c9.txt')
        stemp = [line.strip() for line in open('Files/c9.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c9.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
    if sval == 10:
        l = open('Files/c10.txt')
        stemp = [line.strip() for line in open('Files/c10.txt')]
        l.close()
        sloc = 'Files/s' + str(snum) + '.txt'
        m = open(sloc, 'w')
        m.write(str(stemp[0]) + '\n')
        m.write(str(stemp[1]) + '\n')
        m.write(str(stemp[2]) + '\n')
        m.close()
        cpcmd = 'cp Scoreboard/Images/Songs/c10.png Scoreboard/Images/Songs/s' + str(snum) + '.png'
        os.system(cpcmd)
        
schose(1)
schose(2)
schose(3)
schose(4)
schose(5)
schose(6)
schose(7)
schose(8)
schose(9)
schose(10)

a = open('Files/s1.txt')
s1 = [line.strip() for line in open('Files/s1.txt')]
a.close()

a = open('Files/s2.txt')
s2 = [line.strip() for line in open('Files/s2.txt')]
a.close()

a = open('Files/s3.txt')
s3 = [line.strip() for line in open('Files/s3.txt')]
a.close()

a = open('Files/s4.txt')
s4 = [line.strip() for line in open('Files/s4.txt')]
a.close()

a = open('Files/s5.txt')
s5 = [line.strip() for line in open('Files/s5.txt')]
a.close()

a = open('Files/s6.txt')
s6 = [line.strip() for line in open('Files/s6.txt')]
a.close()

a = open('Files/s7.txt')
s7 = [line.strip() for line in open('Files/s7.txt')]
a.close()

a = open('Files/s8.txt')
s8 = [line.strip() for line in open('Files/s8.txt')]
a.close()

a = open('Files/s9.txt')
s9 = [line.strip() for line in open('Files/s9.txt')]
a.close()

a = open('Files/s10.txt')
s10 = [line.strip() for line in open('Files/s10.txt')]
a.close()



print "Please enter the current region/jury number"
regnum = raw_input()
print "Please enter the total number of juries"
regtotal = raw_input()

regamt = float(regnum) / float(regtotal)
linewdth = float(regamt) * 946

n = open('Scoreboard/Scoreboard.svg', 'w')
n.write("""
<svg xmlns=\"http://www.w3.org/2000/svg\"
    xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"1502\" height=\"1127\">
 
<image x=\"0\" y=\"0\" width=\"1502\" height=\"1127\"
     xlink:href=\"Images/background.jpg\" /> 

 <rect id=\"background\" x=\"30\" y=\"50\" width=\"1455\" height=\"1027\"
  style=\"fill: black; fill-opacity: 0.75;\"/>
  
<!-- Region Setup -->
<text x=\"1090\" y=\"225\" style=\"font-family:Ubuntu Light; font-size: 42pt; font-style:bold;fill:white;\">Now Voting:</text>
 
<image x=\"1012\" y=\"257\" width=\"452\" height=\"452\"
     xlink:href=\"Images/Regions/R""" + str(regnum) + """.png\" /> 

<image x=\"1170\" y=\"750\" width=\"139\" height=\"85\"
     xlink:href=\"Images/Flags/R""" + str(regnum) + """.png\" /> 
     
<image x=\"1020\" y=\"850\" width=\"420\" height=\"70\"
     xlink:href=\"Images/Names/R""" + str(regnum) + """.png\" /> 

<!-- Voting Box -->
<line x1=\"50\"  y1=\"125\" x2=\"50\"   y2=\"940\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"50\"  y1=\"125\" x2=\"1000\"   y2=\"125\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"50\"  y1=\"940\" x2=\"1000\"   y2=\"940\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"1000\"  y1=\"125\" x2=\"1000\"   y2=\"940\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<!-- Voting Dividers -->
<line x1=\"50\"  y1=\"206.5\" x2=\"1000\"   y2=\"206.5\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"288\" x2=\"1000\"   y2=\"288\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"369.5\" x2=\"1000\"   y2=\"369.5\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"451\" x2=\"1000\"   y2=\"451\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"532.5\" x2=\"1000\"   y2=\"532.5\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"614\" x2=\"1000\"   y2=\"614\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"695.5\" x2=\"1000\"   y2=\"695.5\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"777\" x2=\"1000\"   y2=\"777\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>
<line x1=\"50\"  y1=\"858.5\" x2=\"1000\"   y2=\"858.5\" style=\"stroke:#FFFFFF; stroke-width: 2.0\"/>

<!-- Region Box -->
<line x1=\"1015\"  y1=\"125\" x2=\"1015\"   y2=\"940\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"1465\"  y1=\"125\" x2=\"1465\"   y2=\"940\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"1015\"  y1=\"940\" x2=\"1465\"   y2=\"940\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"1015\"  y1=\"125\" x2=\"1465\"   y2=\"125\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>


<!-- # Voters Box -->
<line x1=\"50\"  y1=\"965\" x2=\"50\"   y2=\"1025\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"1000\"  y1=\"965\" x2=\"1000\"   y2=\"1025\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"50\"  y1=\"965\" x2=\"1000\"   y2=\"965\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
<line x1=\"50\"  y1=\"1025\" x2=\"1000\"   y2=\"1025\" style=\"stroke:#FFFFFF; stroke-width: 4.0\"/>
     
<!-- Maximum Width is 946 -->
<rect id=\"background\" x=\"52\" y=\"967\" width=\"""" + str(linewdth) + """\" height=\"56\"
  style=\"fill: #FF9900; fill-opacity:1.0; stroke: white; stroke-width: 4.0\"/>
  
<text x=\"1030\" y=\"1005\" style=\"font-family:Ubuntu Light; font-size: 30pt; font-style:bold;fill:white;\">""" + str(regnum) + " of " + str(regtotal) + """ regions voting</text>

<!-- Placings -->
<text x=\"60\" y=\"185\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">01</text>
<text x=\"60\" y=\"266.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">02</text>
<text x=\"60\" y=\"348\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">03</text>
<text x=\"60\" y=\"429.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">04</text>
<text x=\"60\" y=\"511\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">05</text>
<text x=\"60\" y=\"592.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">06</text>
<text x=\"60\" y=\"674\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">07</text>
<text x=\"60\" y=\"755.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">08</text>
<text x=\"60\" y=\"837\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">09</text>
<text x=\"60\" y=\"918.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">10</text>

<!-- Points -->
<text x=\"900\" y=\"185\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s1[2]) + """</text>
<text x=\"900\" y=\"266.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s2[2]) + """</text>
<text x=\"900\" y=\"348\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s3[2]) + """</text>
<text x=\"900\" y=\"429.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s4[2]) + """</text>
<text x=\"900\" y=\"511\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s5[2]) + """</text>
<text x=\"900\" y=\"592.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s6[2]) + """</text>
<text x=\"900\" y=\"674\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s7[2]) + """</text>
<text x=\"900\" y=\"755.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s8[2]) + """</text>
<text x=\"900\" y=\"837\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s9[2]) + """</text>
<text x=\"900\" y=\"918.5\" style=\"font-family:Ubuntu Light; font-size: 40pt; font-style:bold;fill:white;\">""" + str(s10[2]) + """</text>

<!-- Given Points -->
<image x=\"820\" y=\"145\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s1[1]) + """.png\" /> 
<image x=\"820\" y=\"227.5\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s2[1]) + """.png\" /> 
<image x=\"820\" y=\"309\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s3[1]) + """.png\" /> 
<image x=\"820\" y=\"390.5\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s4[1]) + """.png\" /> 
<image x=\"820\" y=\"472\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s5[1]) + """.png\" /> 
<image x=\"820\" y=\"553.5\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s6[1]) + """.png\" /> 
<image x=\"820\" y=\"635\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s7[1]) + """.png\" /> 
<image x=\"820\" y=\"716.5\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s8[1]) + """.png\" /> 
<image x=\"820\" y=\"798\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s9[1]) + """.png\" /> 
<image x=\"820\" y=\"879.5\" width=\"60\" height=\"60\"
     xlink:href=\"Images/Points/point""" + str(s10[1]) + """.png\" /> 

<!-- Songs -->
<image x=\"125\" y=\"130\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s1.png\" /> 
<image x=\"125\" y=\"211.5\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s2.png\" />
<image x=\"125\" y=\"293\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s3.png\" />
<image x=\"125\" y=\"374.5\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s4.png\" />
<image x=\"125\" y=\"456\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s5.png\" />
<image x=\"125\" y=\"537.5\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s6.png\" />
<image x=\"125\" y=\"619\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s7.png\" />
<image x=\"125\" y=\"700.5\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s8.png\" />
<image x=\"125\" y=\"782\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s9.png\" />
<image x=\"125\" y=\"863.5\" width=\"675\" height=\"70\"
     xlink:href=\"Images/Songs/s10.png\" />
 </svg>""")
n.close()

svgconvert = "for i in Scoreboard/Scoreboard.svg; do rsvg-convert -a $i -o `echo $i | sed -e 's/svg$/png/'`; done"
os.system(svgconvert)
oscpcmd = "mv Scoreboard/Scoreboard.png Scoreboard/Output/Scoreboard" + str(regnum) + ".png"
os.system(oscpcmd)

