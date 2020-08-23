fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "email_data.txt"
fopen = open(fname)
count = dict()

for line in fopen:
    if line.startswith("From "):
        schedule = line.split()
        time = schedule[5]
        hour = time[:2]
        #print(hour)
        count[hour] = count.get(hour, 0) + 1

for k, v in sorted(count.items()):
    print(k,v)
