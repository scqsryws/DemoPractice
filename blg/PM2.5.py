# PM2.5空气质量
def pmwarm(pm):
    pmi = {"0,35": '优', "36,75": "良", "76,115": "轻度污染", "116,150": "中度污染", "151,250": "重度污染", "251,500": "严重污染"}
    for i in pmi:
        warning = pmi[i]
        i = i.split(",")
        l = [x for x in i]
        if int(l[0]) <= pm <= int(l[1]):
            print(l[0], l[1])
            print(warning)


pmwarm()



