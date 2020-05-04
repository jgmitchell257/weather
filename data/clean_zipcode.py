loc_data = {}
with open("zipcode.csv","r") as f:
    for line in f:
        ugly = line.split()
        clean_data = []
        for (a,b) in enumerate(ugly):
            columns = b.split(",")
            for (a,b) in enumerate(columns):
                clean = b.strip()
                clean_data.append(clean)
            if len(clean_data[0]) == 3:
                ZIPCODE = "00" + clean_data[0]
            if len(clean_data[0]) == 4:
                ZIPCODE = "00" + clean_data[0]
            else:
                ZIPCODE = clean_data[0]
            LATITUDE = clean_data[1]
            LONGITUDE = clean_data[2]
            loc_data[ZIPCODE] = [LATITUDE,LONGITUDE]
print(loc_data)