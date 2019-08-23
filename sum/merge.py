import csv
for fname in ['test','train','validation']:
    f1 = open(fname+'.src','r', encoding='utf-8')
    f2 = open(fname+'.dst', 'r', encoding='utf-8')
    f3 = open(fname+'.csv', 'w', newline ='', encoding='utf-8')
    src = f1.readlines()
    dst = f2.readlines()
    wr = csv.writer(f3)
    for i in range(len(src)):
        if len(src[i])<4 or len(dst[i]) < 4: continue
        if i % 500 == 0 and fname=='test':
            print(src[i].encode('utf-8'),dst[i].encode('utf-8'))
        wr.writerow([src[i].strip('\n'),
                     dst[i].strip('\n')])
