import pickle
# name = ['prabhu','sudheer','thiru','renu','madhu']
# outfile = open(file='c:/d1/seriexm',mode='wb')
# pickle.dump(name,outfile)

readfile = open('c:/d1/seriexm',mode='rb')
print(pickle.load(readfile))