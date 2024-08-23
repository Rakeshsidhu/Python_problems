#patterns
#for i in range(1,6):
 #   print('*' * i)

#print ABCDE
for i in range(1,7):
    print(' '.join(chr(96 + j)for j in range(1,i)))