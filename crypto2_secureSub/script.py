import io
import uu
import collections

ciphertext = open("ciphertext", "rb").read()

def uuencode(data):
    data = data + b'\0' * (-len(data) % 3)
    inp = io.BytesIO(data)
    out = io.BytesIO()
    uu.encode(inp, out)
    return out.getvalue()

def uudecode(data):
    inp = io.BytesIO(data)
    dec = io.BytesIO()
    uu.decode(inp, dec)
    dec = dec.getvalue()
    dec = dec[:-2] + dec[-2:].rstrip(b'\0')
    return dec

encoded = uuencode(ciphertext)
encoded = encoded.split(b'\n')
head, data, tail = encoded[:1], encoded[1: -3], encoded[-3:]

# a = []
# b = []
# for line in data:
# 	for i in range(1, len(line), 4):
# 		a.append(line[i:i+4])
# 	b.append(line[-1])

# a = collections.Counter(a)
# b = collections.Counter(b)

# for i, j in a.items():
# 	if i[-2] == ord('H') and j == 1 and b"A" not in i and b'5' not in i and b"'" not in i and b'P' not in i:
# 		print(i, j)

# print(a)

before = b"A5'HPCJ*"
after = b"=&AE 043"
mapping = [0] * 64
for i in range(len(before)):
	mapping[before[i] - 32] = after[i]

temps = []
for line in data:
	temp = chr(line[0])
	for c in line[1:]:
		if mapping[c - 32] == 0: temp += chr(c)
		else: temp += chr(mapping[c - 32])
	temp = bytes(temp, 'utf-8')
	temps.append(temp)

encrypted = b'\n'.join(head + temps + tail)
encrypted = uudecode(encrypted)
print(encrypted)