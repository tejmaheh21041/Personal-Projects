import pickle

f=open('details.dat','rb')
a=pickle.load(f)
print(a)
f.close()


f=open('details.dat','wb')
pickle.dump('Hi',f)
f.flush()
f.close()


f=open('details.dat','rb')
a=pickle.load(f)
print(a)
f.close()
