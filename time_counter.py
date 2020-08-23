fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "email_data.txt"
fopen = open(fname)
score = []
count = 0
for line in fopen:
    #print(line)
    if line.startswith("From"):
        #print(line)
        if line.startswith("From:"):
            continue
        p_data = line.split()
        #print(p_data)
        data = p_data[5]
        #print(data)
        new_data = data.split(":")

        for hour in new_data:
            if hour == new_data[0] :

                print(hour)
                if hour in score:
                    count = count + 1
                else :
                    add_data = score.append(hour)

        print(hour, count)


        #hours = new_data[0]
        #print(hours)
        #if hours not in score:
        #    add_data = score.append(hours)
        #    count = 0
        #else:
        #    count = count + 1
        #print(hours, count)