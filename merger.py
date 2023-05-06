import linecache
import heapq
from indexer import numb
import time

global arr
arr = []
def get_iv(line):
    return line[:line.index(":")] , line[line.index(":"):]

def get_l(filepath,line_num):
    line = linecache.getline(filepath, line_num)
    return line
def fp(ind):
    return str(ind+1) + ".txt"

def out_fp(ind):
    return "f" + str(ind) + ".txt"

def write_to_file(out,ind):
    with open(out_fp(ind), 'w') as f:
        for item in out:
        # write each item on a new line
            f.write("%s\n" % item)


start = time.time()
numb = 10
print(numb)
h=[]
li = [1 for i in range(numb)]
lc = []
for i in range(numb):
    with open(fp(i), 'r') as f:
        lc.append(sum(1 for line in f))
heapq.heapify(h)
for i in range(numb):
    heapq.heappush(h,(get_iv(get_l(fp(i),li[i]))[0],i))

final = []
size = 0
last_ind = ""
out_ind = 1
while(True):
    if(len(h) == 0):
        break
    ind,f_num = heapq.heappop(h)
    #print("File number : " + str(f_num))
    if li[f_num] <= lc[f_num]:
        heapq.heappush(h,(get_iv(get_l(fp(f_num),li[f_num]))[0],f_num))
        li[f_num]+=1
    
    if(ind == last_ind):
        final[size-1] = final[size-1] + get_iv(get_l(fp(f_num),li[f_num]-1))[0]

    else:
        if(size == 50000):
            #write final to text file
            arr.append(get_iv(final[0])[0])
            write_to_file(final,out_ind)
            print("Output Index : " + str(out_ind))
            out_ind+=1
            final = []
            size = 0
        final.append(get_l(fp(f_num),li[f_num]-1))
        size+=1
        last_ind = ind

if(size>0):
    print("Last file")
    arr.append(get_iv(final[0])[0])
    write_to_file(final,out_ind)
print(arr)
        
end = time.time()
print("Total Time Taken: ", end-start)













