'''from kec_rn import *
def rectify(a):
	if(a[2:4]=='cs'):
		x='cse'
	elif(a[2:4]=='ec'):
		x='ece'
	elif(a[2:4]=='ee'):
		x='eee'
	for i,j in zip(kec_stud.keys(),kec_stud.values()):
		if a==i.lower():
			return (j.replace("_","")+"."+a[:2]+x+'@kongu.edu').lower()'''
from kec_rn import *
def rectify(a):
	if(a[2:4]=='cs'):
		x='cse'
	elif(a[2:4]=='ec'):
		x='ece'
	elif(a[2:4]=='ee'):
		x='eee'
	elif(a[2:4]=='ei'):
		x='eie'
	elif(a[2:4]=='it'):
		x='it'
	elif(a[2:4]=='me'):
		x='mech'
	elif(a[2:4]=='mt'):
		x='mts'
	elif(a[2:4]=='ce'):
		x='civil'
	elif(a[2:4]=='au'):
		x='auto'
	elif(a[2:4]=='ft'):
		x='food'
	elif(a[2:4]=='ch'):
		x='chem'
	for i,j in zip(kec_stud.keys(),kec_stud.values()):
		if a==i.lower():
			return (j.replace("_","")+"."+a[:2]+x+'@kongu.edu').lower()

