while True:
    check = False
    date = input("Date: ")
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    date = date.strip()
    if "," in date:
        if date.index(",") == (len(date)) - 6:
            date = date.replace(",", "")
            date = date.replace(" ", "-")
            check = True
    date = date.replace("/", "-")
    list = date.split(sep="-")
    month = list[0]
    if month.isdigit():
        month = int(month)
    elif month in months and check:
        month = (months.index(month)) + 1
    else:
        break
    day = list[1]
    year = int(list[2])
    if month > 12:
        continue
    if day.isdigit():
        day = int(day)
        if day > 31:
            continue
    else:
        break

    month = str(month).zfill(2)
    day = str(day).zfill(2)
    print("%d-%s-%s" % (year, month, day))
    break
