import inspect

r0 = 0
r1 = 1
r2 = 2
r3 = 3
r4 = 4
r5 = 5
r6 = 6
r7 = 7
r8 = 8
r9 = 9
r10 = 10
r11 = 11
r12 = 12
r13 = 13
r14 = 14
r15 = 15
r16 = 16
r17 = 17
r18 = 18
r19 = 19
r20 = 20
r21 = 21
r22 = 22
r23 = 23
r24 = 24
r25 = 25
r26 = 26
r27 = 27
r28 = 28
r29 = 29
r30 = 30
r31 = 31

ops = {
	'add':		(0x20, False),
	'addc':		(0x30, True),
	'and':		(0x28, False),
	'andc':		(0x38, True),
	'beq':		(0x1C, True),
	'bne':		(0x1D, True),
	'cmpeq':	(0x24, False),
	'cmpeqc':	(0x34, True),
	'cmple':	(0x26, False),
	'cmplec':	(0x36, True),
	'cmplt':	(0x25, False),
	'cmpltc':	(0x35, True),
	'div':		(0x23, False),
	'divc':		(0x33, True),
	'jmp':		(0x1B, False),
	'ld':		(0x18, True),
	'ldr':		(0x1F, True),
	'mul':		(0x22, False),
	'mulc':		(0x32, True),
	'or':		(0x29, False),
	'orc':		(0x39, True),
	'shl':		(0x2C, False),
	'shlc':		(0x3C, True),
	'shr':		(0x2D, False),
	'shrc':		(0x3D, True),
	'sra':		(0x2E, False),
	'srac':		(0x3E, True),
	'sub':		(0x21, False),
	'subc':		(0x31, True),
	'st':		(0x19, True),
	'xor':		(0x2A, False),
	'xorc':		(0x3A, True),
	'xnor':		(0x2B, False),
	'xnorc':	(0x3B, True)
}

def hex32(value):
	return "{0:#0{1}x}".format(value, 8)

def w_reg(op, a, b, c):
	op &= 0x3F
	a &= 0x1F
	b &= 0x1F
	c &= 0x1F

	return hex32(op << (32-6) | c << (32-6-5) | a << (32-6-5-5) | b << (32-6-5-5-5))

def w_literal(op, a, literal, c):
	op &= 0x3F
	a &= 0x1F
	literal &= 0xFFFF
	c &= 0x1F

	return hex32(op << (32-6) | c << (32-6-5) | a << (32-6-5-5) | b)

address = 0
while True:
	instruction = raw_input(hex32(address)+': ')
	
	parts = instruction.split();

	op_name = parts[0].lower()

	a	= int(parts[1].lower())
	b	= int(parts[2].lower())
	c	= int(parts[3].lower())
	lit	= int(parts[2].lower())

	if ops[op_name][1]:
		print '\t', w_literal(ops[op_name][0], a, lit, c)
	else:
		print '\t', w_reg(ops[op_name][0], a, b, c)

	address += 1
