import os
import hashlib

filelist = list()

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)
		if os.path.isfile(path):
			#print(path)
			filelist.append(path)
		else:
			walk(path)

def get_key(dict, value):
	return [k for k,v in dict.items() if v==value]
def checksum(filelist):
	#md5 = hashlib.md5()
	filedict = dict()
	for filename in filelist:
		md5 = hashlib.md5()
		print(filename)
		fr = open(filename,'rb')
		for line in fr:
			md5.update(line)
		filedict[filename] = md5.hexdigest()
		print("close file")
		fr.close()
	#print(filedict)
	result = list()
	for i in filedict.values():
		keys = get_key(filedict,i)
		if len(keys)>1:
			result.append(keys)
	print(result)

walk("/home/student/final")#here should be a directory
checksum(filelist)

