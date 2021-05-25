print("Delete Duplicate For Huge Database ...")
###############################################
seen = set()
ii = input(" || Enter Name Text File : ")
ss = input(" || Save To : ")
with open(ii, 'r') as infile:
    with open(ss, 'w') as outfile:
        for line in infile:
            h = (line)
            if h in seen:
                continue
            seen.add(h)
            outfile.write(line)
