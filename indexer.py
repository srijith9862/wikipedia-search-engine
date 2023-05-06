import sys
import time
from nltk.corpus import stopwords
import xml.sax
from nltk.stem import PorterStemmer
from collections import OrderedDict
import re
import json

from numpy import number

ps = PorterStemmer()
sw = stopwords.words('english')

global num_pages
num_pages = 0

global pageCount
pageCount = 0

global wordCount
wordCount = 0

global numb
numb=1

stop_words_url = set(["http", "https", "www", "ftp", "com", "net",
                      "org", "archives", "pdf", "html", "png", "txt", "redirect"])
global main_dic
main_dic = {}
# tf = defaultdict(dict)

global titl 
titl = []
stems = {}

def processTitle(title):
	return tokenize(title.lower)

def tokenize(text):
	text = str(text)
	temp = []
	wordCount = 0
	text = re.sub(r"`|~|!|@|#|\$|%|\^|&|\*|\(|\)|-|_|=|\+|\||\\|\[|\]|\{|\}|;|:|'|\"|,|<|>|\.|/|\?|\n|\t", " ", text) 
	for item in text:
		wordCount += 1
		item = ps.stem(item)
		if(sw.count(item) or len(item) > 50 or len(item)<1):
			continue
		temp.append(item)

	return temp





def createdic(t,b,i,c,l,r):
	temp = {}
	x=t.lower()
	x= re.split(r'\W+', x)
	for j in x:
		if j not in stop_words_url and j != '':
			if j in temp.keys():
				temp[j][0] += 1
			else:
				temp[j] = [0,0,0,0,0,0]
				temp[j][0] += 1;
	x=b.lower()
	x= re.split(r'\W+', x)
	for j in x:
		if j not in stop_words_url and j != '':
			if j in temp.keys():
				temp[j][1] += 1
			else:
				temp[j] = [0,0,0,0,0,0]
				temp[j][1] += 1;
	x=i.lower()
	x= re.split(r'\W+', x)
	for j in x:
		if j not in stop_words_url and j != '':
			if j in temp.keys():
				temp[j][2] += 1
			else:
				temp[j] = [0,0,0,0,0,0]
				temp[j][2] += 1;
	x=c.lower()
	x= re.split(r'\W+', x)
	for j in x:
		if j not in stop_words_url and j != '':
			if j in temp.keys():
				temp[j][3] += 1
			else:
				temp[j] = [0,0,0,0,0,0]
				temp[j][3] += 1;
	x=l.lower()
	x= re.split(r'\W+', x)
	for j in x:
		if j not in stop_words_url and j != '':
			if j in temp.keys():
				temp[j][4] += 1
			else:
				temp[j] = [0,0,0,0,0,0]
				temp[j][4] += 1;
	x=r.lower()
	x= re.split(r'\W+', x)
	for j in x:
		if j not in stop_words_url and j != '':
			if j in temp.keys():
				temp[j][5] += 1
			else:
				temp[j] = [0,0,0,0,0,0]
				temp[j][5] += 1;
	return temp;

def createfile(n):
	str2 = str(n) + '.txt'
	dic = OrderedDict(sorted(main_dic.items()))
	with open(str2, 'w') as f: 
		for key, value in dic.items(): 
			f.write('%s:%s\n' % (key, value))
	# with open(str2, "w") as outfile:
	# 	json.dump(dic,outfile)
def createtitles(numb):
	global titl
	str3 = 't' + str(numb) + '.txt'
	with open(str3, 'w') as fp:
		for item in titl:
			fp.write("%s\n" % item)

def createTF(text, title):
	global pageCount
	t=title.lower()
	if 'wikipedia:' in t:
		t=t[10:]
	titl.append(t)
	b = ''
	i = ''
	r = ''
	l = ''
	c = ''
	ref_flag = 0
	info_flag = 0
	lines  = text.split('\n')
	for line in lines:
		if not line:
			continue
		line = line.lower()

		if ref_flag == 0:
			if re.search(r"==\s*references\s*==", line):
				ref_flag = 1
				continue
			b += line
			b += ' '
			if re.search(r'\{\{\s*infobox', line):
				i = re.sub(r'\{\{\s*infobox(.*)', r'\1', line)
				i += ' '
				info_flag = 1
			elif info_flag == 1:
				if re.search(r'\s*\}\}\s*', line):
					info_flag = 0
					continue
				else:
					i += line
					i += ' '
		elif ref_flag == 1:
			if ("[[category" in line) or ("==" in line) or ("defaultsort" in line):
				ref_flag = 2
				continue
			r += line
			r += ' '
		elif ref_flag == 2:
			# print(line[0])
			if line[0] == '*':
				l += line
				l += ''
			else:
				x = re.findall(r'.*category\s*:\s*(.*)\]\]', line)
				c += ''.join(x)
				c += ''	
	# return createdic(title,b,i,c,l,r)
	temp_dic = createdic(title,b,i,c,l,r)
	# return temp_dic
	for i in temp_dic:
		str1 = str(pageCount) + ':'
		str1 = str1 + 't' + str(temp_dic[i][0]) + 'b' + str(temp_dic[i][1]) + 'i' + str(temp_dic[i][2]) + 'c' + str(temp_dic[i][3]) + 'l' + str(temp_dic[i][4]) + 'r' + str(temp_dic[i][5])
		# str1 = str1 + 'b' + str(temp_dic[i][1])
		# str1 = str1 + 'i' + str(temp_dic[i][2])
		# str1 = str1 + 'c' + str(temp_dic[i][3])
		# str1 = str1 + 'l' + str(temp_dic[i][4])
		# str1 = str1 + 'r' + str(temp_dic[i][5])
		if i in main_dic.keys():
			main_dic[i] = main_dic[i] + "*" + str1
		else:
			main_dic[i] = str1




	# fillTable(t, 1)
	# fillTable(b, 2)
	# fillTable(i, 3)
	# fillTable(l, 4)
	# fillTable(r, 5)
	# fillTable(c, 6)



class XMLParser(xml.sax.ContentHandler):
	def __init__(self):

		self.tag = ''
		self.title = ''
		self.text = ''


	def startElement(self,name,attrs):
		self.tag=name
		if(name == "page"):
			self.title = []
			self.text = []	

	def endElement(self,name):
		global pageCount
		global main_dic
		global numb
		if(pageCount >= 50000*numb):
			createfile(numb)
			createtitles(numb)
			numb = numb+1
			# print(main_dic)
			main_dic={}
			titl = []
			# exit()
		if name=="page":
			self.title = "".join(self.title).strip()
			self.text = "".join(self.text)
			# print(self.title)
			# print(self.text)
			# print(self.tag)
			title = processTitle(self.title)
			# body, infobox, categories, links, references = processText(self.text)
			text = self.text
			pageCount += 1
			print(pageCount)
			createTF(self.text, self.title)
			# print('\n')



	def characters(self, content):

		if self.tag == 'title':
			self.title.append(content)

		if self.tag == 'text':
			self.text.append(content)

		# if self.tag == 'id' and self.idDoc == 0:
		# 	self.id.append(content)
		# 	self.idDoc = 1



if __name__ == '__main__':
	start = time.time()

	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	handler = XMLParser()
	parser.setContentHandler(handler)

	parser.parse("data.xml")
	# print(main_dic)
	if((pageCount-50000*(numb-1))>0): createfile(numb)
	print(numb)
	end = time.time()
	print("Total Time Taken: ", end-start)