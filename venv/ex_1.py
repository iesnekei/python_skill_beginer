out_f = open('my_file.txt','w')

a = (input('Please write what you want to add in file:.. '))
b = (input('Please write what you want to add in file:.. '))
c = (input('Please write what you want to add in file:.. '))
d = (input('Please write what you want to add in file:.. '))

out_f.write(a+'\n')
out_f.write(b+'\n')
out_f.write(c+'\n')
out_f.write(d+'\n')

out_f.close()

