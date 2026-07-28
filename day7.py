try:
    f = open("routes.txt", "r")
    total = 0
    for line in f:
        parts = line.strip().split("|")
        total = total + int(parts[2])
    f.close()
    print(total)
except FileNotFoundError:
    print("No routes file found — starting fresh")
except ValueError:
    print("Bad fare data in file — skipping")
