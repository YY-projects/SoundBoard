import codecs
import math
import csv

with open('work.hex', 'r') as f:
    datain = f.read()
    f.close()


fullrange = len(datain)
datain = datain[16:(fullrange-16)]

print(fullrange)

def findend():
    for x in range(len(datain)):
        if (datain[x] == 'F') and (datain[(x + 44)] == 'F') and (datain[(x + 88)] == 'F') and (datain[(x + 660)] == 'F') and (datain[(x + 880)] == 'F'):
            if (datain[(x - 1)] == '0') and (datain[(x - 9)] == ':'):
                if (datain[(x + 1)] == 'F') and (datain[(x + 3)] == 'F') and (datain[(x + 5)] == 'F') and (datain[(x + 7)] == 'F') and (datain[(x + 9)] == 'F'):
                    return x

end = findend()
datain = datain[0:(end-10)]
print(end)
print(len(datain))
#print(datain)

lines = []
n = 0
for z in range(len(datain)):
    if datain[z] == ':':
        newline = ""
        newline = datain[(z+9):(z+41)]
        lines.append(newline)

print(len(lines))

bytes = []
for a in range(len(lines)):
    line = lines[a]
    for b in range(len(line)):
        if b%2 == 0:
            byte = line[b] + line[b+1]
            bytes.append(byte)


bins = []
for c in range(len(bytes)):
    hbyte = bytes[c]
    dec_form = int(hbyte, 16)
    hex_form = hex(dec_form)
    res = "{0:08b}".format(int(hex_form, 16))
    bins.append(res)


splits = []
for d in range(len(bins)):
    current = bins[d]
    tophalf = current[0:4]
    plusinst = "0011" + tophalf
    splits.append(plusinst)
    leasthalf = current[4:8]
    plusdata = leasthalf + "0000"
    splits.append(plusdata)


hexdump = []
intdump = []
bindump = []
for e in range(len(splits)):
    decvar = int(splits[e], 2)
    intdump.append(int(decvar))
    binvar = bin(int(splits[e]))
    bindump.append(binvar)
    hexvar = hex(decvar)
    hexdump.append(hexvar)
    #print(hexvar, end = "   ")


rownum = int(len(hexdump)/16)
print(rownum)
rows = []
for i in range(len(hexdump)):
    if i%16 == 0:
        fullrow = ''
        for j in range(16):
            formhex = hexdump[i + j]
            if len(formhex) != 4:
                formhex = '0x0' + formhex[2]
            justhex = formhex[2:4]
            fullrow = fullrow + justhex
        rows.append(fullrow)

print(len(rows))

finstr = []
address = '0000'
check = 0

for k in range(len(rows)):
    string = ":10" + address + "00" + rows[k] + '00'
    finstr.append(string)
    addy = int(address, 16)
    addy = addy + 16
    address = hex(addy)
    if len(address) == 4:
        address = '00' + address[2:4]
    elif len(address) == 5:
        address = '0' + address[2:5]
    elif len(address) == 6:
        address = address[2:6]

print(len(finstr))


with open('final.hex', 'w') as g:
    for w in range(len(finstr)):
        g.write(finstr[w])
        g.write('\n')
        #number = intdump[op]
        #finval = chr(intdump[row])
        #numb = bin(number)
        #g.write()
        #finalint = int(hexdump[row], 16)
        #finalhex = hex(finalint)
        #g.write(finalhex)
        #g.write("%s\n" % row)

    g.close()