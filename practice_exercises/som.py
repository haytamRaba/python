fname = input("Enter file name: ")
x=0
count =0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x += float(line[line.find('0'):len(line)]) 
    count+=1 
print("Average spam confidence:", x/count)