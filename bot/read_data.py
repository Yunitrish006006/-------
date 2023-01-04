def add_userdata(add):
    out = []
    lst = [line.strip('\n').split(" ") for line in open('database/jobs.txt').readlines()]
    for i in lst:
        cnt = 0
        #把檔案重複名字更新只留最後一個
        for j in out:
            if i[0]==j[0]:
                j[1]=i[1]
            else:
                cnt+=1
        if cnt == len(out):
            out.append(i)
    #如果新加入的user名字存在在檔案中 -> 更新檔案
    cnt = 0
    for i in out:
        if add[0]==i[0]:
            i[1]=add[1]
        else:
            cnt += 1
    if cnt == len(out):
        out.append(add)
    print(out)
    with open('database/jobs.txt', 'w') as f:
        for i in out:
            f.write(str(i[0])+" "+str(i[1])+"\n")
add_userdata(['jimmy', 'minerX'])