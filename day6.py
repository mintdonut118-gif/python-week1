routes=[{"from":"Hyderbad","to":"Bangalore","fare":"1000"},
        {"from":"Visakapatnam","to":"Hyderbad","fare":"600"},
        ]
f = open("routes.txt", "w")
for r in routes:
     f.write(f"{r['from']}|{r['to']}|{r['fare']}\n")
f.close()
f2 = open("routes.txt", "r")
total = 0
for line in f2:
    parts = line.strip().split("|")
    total = total + int(parts[2])
f2.close()
print(total)
