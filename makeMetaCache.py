f = open('metaCache.in','w')

for i in range(0,1000000,1000):
  f.write(str(i+1)+' '+str(i+1000)+'\n')

f.close()
