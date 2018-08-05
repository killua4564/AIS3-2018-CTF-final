import hashlib

v19 = [0] * 28
B = [0x59, 0x59, 0x59, 0x45, 0x45, 0x45, 0x45, 0x41, 0x59, 0x59, 0x59, 0x45, 0x45, 0x45, 0x45, 0x49, 0x59, 0x59, 0x59, 0x45, 0x45, 0x45, 0x45, 0x53, 0x59, 0x59, 0x59, 0x45, 0x45, 0x45, 0x45, 0x33, 0x59, 0x59, 0x59, 0x59, 0x45, 0x45, 0x45, 0x7B, 0x59, 0x59, 0x59, 0x59, 0x45, 0x45, 0x45, 0x5F, 0x59, 0x59, 0x59, 0x59, 0x45, 0x45, 0x45, 0x5F, 0x59, 0x59, 0x59, 0x59, 0x45, 0x45, 0x45]
C = [0xD4, 0xCF, 0x20, 0x44, 0x81, 0x13, 0xCF, 0x54, 0x6E, 0xD3, 0x50, 0xEF, 0x53, 0xD9, 0xD9, 0x18, 0xD3, 0xD1, 0x11, 0x64, 0xDA, 0xB8, 0x6C, 0x25, 0xFB, 0x08, 0x60, 0x52, 0xE9, 0x59, 0x5C, 0x52, 0x6B, 0xEA, 0x8F, 0x14, 0x44, 0xD9, 0xC8, 0xAE, 0x10, 0xC8, 0x9D, 0x7F, 0xCF, 0xC6, 0x3E, 0x3E, 0x91, 0xAA, 0xA3, 0x21, 0xD6, 0x7B, 0x40, 0xE6, 0x13, 0x4A, 0xBA, 0x0A, 0x10, 0x23, 0x50, 0x28]
E = [0x20, 0x1, 0x2, 0x3, 0x4, 0x5, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x8, 0x9, 0x0A, 0x0B, 0x0C, 0x0D, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x1, 0x10]
P = [0x10, 0x7, 0x14, 0x15, 0x1D, 0x0C, 0x1C, 0x11, 0x1, 0x0F, 0x17, 0x1A, 0x5, 0x12, 0x1F, 0x0A, 0x2, 0x8, 0x18, 0x0E, 0x20, 0x1B, 0x3, 0x9, 0x13, 0x0D, 0x1E, 0x6, 0x16, 0x0B, 0x4, 0x19]
FP = [0x28, 0x8, 0x30, 0x10, 0x38, 0x18, 0x40, 0x20, 0x27, 0x7, 0x2F, 0x0F, 0x37, 0x17, 0x3F, 0x1F, 0x26, 0x6, 0x2E, 0x0E, 0x36, 0x16, 0x3E, 0x1E, 0x25, 0x5, 0x2D, 0x0D, 0x35, 0x15, 0x3D, 0x1D, 0x24, 0x4, 0x2C, 0x0C, 0x34, 0x14, 0x3C, 0x1C, 0x23, 0x3, 0x2B, 0x0B, 0x33, 0x13, 0x3B, 0x1B, 0x22, 0x2, 0x2A, 0x0A, 0x32, 0x12, 0x3A, 0x1A, 0x21, 0x1, 0x29, 0x9, 0x31, 0x11, 0x39, 0x19]
PL = [0x39, 0x31, 0x29, 0x21, 0x19, 0x11, 0x9, 0x1, 0x3A, 0x32, 0x2A, 0x22, 0x1A, 0x12, 0x0A, 0x2, 0x3B, 0x33, 0x2B, 0x23, 0x1B, 0x13, 0x0B, 0x3, 0x3C, 0x34, 0x2C, 0x24, 0x4]
PR = [0x3F, 0x37, 0x2F, 0x27, 0x1F, 0x17, 0x0F, 0x7, 0x3E, 0x36, 0x2E, 0x26, 0x1E, 0x16, 0x0E, 0x6, 0x3D, 0x35, 0x2D, 0x25, 0x1D, 0x15, 0x0D, 0x5, 0x1C, 0x14, 0x0C, 0x4, 0x4]
P2 = [0x0E, 0x11, 0x0B, 0x18, 0x1, 0x5, 0x3, 0x1C, 0x0F, 0x6, 0x15, 0x0A, 0x17, 0x13, 0x0C, 0x4, 0x1A, 0x8, 0x10, 0x7, 0x1B, 0x14, 0x0D, 0x2, 0x29, 0x34, 0x1F, 0x25, 0x2F, 0x37, 0x1E, 0x28, 0x33, 0x2D, 0x21, 0x30, 0x2C, 0x31, 0x27, 0x38, 0x22, 0x35, 0x2E, 0x2A, 0x32, 0x24, 0x1D, 0x20, 0x10]
byte_1900 = [0x3A, 0x32, 0x2A, 0x22, 0x1A, 0x12, 0x0A, 0x2, 0x3C, 0x34, 0x2C, 0x24, 0x1C, 0x14, 0x0C, 0x4, 0x3E, 0x36, 0x2E, 0x26, 0x1E, 0x16, 0x0E, 0x6, 0x40, 0x38, 0x30, 0x28, 0x20, 0x18, 0x10, 0x8, 0x39, 0x31, 0x29, 0x21, 0x19, 0x11, 0x9, 0x1, 0x3B, 0x33, 0x2B, 0x23, 0x1B, 0x13, 0x0B, 0x3, 0x3D, 0x35, 0x2D, 0x25, 0x1D, 0x15, 0x0D, 0x5, 0x3F, 0x37, 0x2F, 0x27, 0x1F, 0x17, 0x0F, 0x7]

def xor(a1, a2):
	return ''.join([chr(i ^ j) for i, j in zip(a1, a2)])

A = bytes(input(), 'utf-8')
assert len(A) == 64

v23 = [letter + byte_1900[index] - 1 for index, letter in enumerate(A)]

for j in range(28):  # pre process
	v19[j] = B[PL[j] - 1]
	v19[j + 28] = B[PR[j] - 1]

for k in range(16):  # main loop
	for l in range(48):
		v31 = [letter + E[index] + 31 for index, letter in enumerate(A)]
	v4 = v19[0]
	v5 = 0
	for m in range(28):
		v19[m] = v19[m + 1]
		v19[m + 28] = v19[m + 29]
	v20 = v4
	v22 = v5
	v31 = [v ^ v19[P2[index] - 1] for index, v in enumerate(v31)]
	v17 = hashlib.sha256(''.join(v31))
	v18 = [v17[P[ii] - 1] for ii in range(32)]
	A = xor(A, v18)
	if k != 15:
		A = xor(A, v27)
		v27 = xor(v27, A)

A = [A[FP[jj] - 1] for jj in range(64)]

assert A == C


