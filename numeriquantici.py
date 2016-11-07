def irange(start, end):
	return range(start, end+1)

def quantic(n):
    out = []
    for l in irange(0, n-1):
        for m in irange(-l,l):
            for s in [1, -1]:
                out.append([n, l, m, s])
    return out            

print('Inserisci il numero quantico principale')
n = int(input('>'))
if n==0:
	for n in irange(1, 7):
		for row in quantic(n):
			print('n:{: >2} l:{: >2} m:{: >2} s:{: >2}'.format(*row))
		if n<7:	print('-------------------')
else:
	for row in quantic(n):
	    print('n:{: >2} l:{: >2} m:{: >2} s:{: >2}'.format(*row))