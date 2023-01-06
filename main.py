f = open("032-huge.in", "r")
fl = f.readline().split()
n = int(fl[0])
knoten_liste = [i for i in range(n)]
size_liste = [1 for i in range(n)]
kinder_liste = [[] for i in range(n)]


def find(s):
    while s != knoten_liste[s]:
        s = knoten_liste[s]
    return s


def query(s, t):
    if find(s) == find(t):
        return 1
    else:
        return 0


def union(s, t):
    rs = find(s)
    rt = find(t)
    if rs != rt:
        if size_liste[rs] < size_liste[rt]:
            size_liste[rt] = size_liste[rs] + size_liste[rt]
            kinder_liste[rt].append(rs)
            knoten_liste[rs] = rt
        else:
            size_liste[rs] = size_liste[rt] + size_liste[rs]
            kinder_liste[rs].append(rt)
            knoten_liste[rt] = rs


def search_remove(s, slist):
    end = slist[-1]
    counter = 0
    for i in slist:
        if i == s:
            slist[-1] = s
            slist[counter] = end
        counter += 1
    slist.pop()


def move(s, t):
    rs = find(s)
    rt = find(t)
    if rs != rt:
        if s != rs:
            # wenn s nicht Wurzel ist
            search_remove(s, kinder_liste[knoten_liste[s]])
            while kinder_liste[s]:
                knoten_liste[kinder_liste[s][0]] = rs
                kinder_liste[rs].append(kinder_liste[s][0])
                kinder_liste[s].pop(0)
        else:
            # wenn s Wurzel ist
            if kinder_liste[s]:
                rs = kinder_liste[s][0]
                knoten_liste[rs] = rs
                kinder_liste[s].pop(0)
                while kinder_liste[s]:
                    knoten_liste[kinder_liste[s][0]] = rs
                    kinder_liste[rs].append(kinder_liste[s][0])
                    kinder_liste[s].pop(0)
        if size_liste[rt] == 1:
            size_liste[rt] += 1
        knoten_liste[s] = rt
        kinder_liste[rt].append(s)


def BFS(start_node, max_counter, counter=1):
    if kinder_liste[start_node]:
        for kind in kinder_liste[start_node]:
            BFS(kind, max_counter, counter + 1)
            # if not kinder_liste[start_node]:
            #     if counter > max_counter:
            #         max_counter = counter
    else:
        if counter > max_counter[0]:
            max_counter[0] = counter
    if counter == 1:
        return max_counter[0]


def auswertung(r, s, t):
    if r == 0:
        g = open("union_ans.txt", "a")
        g.write(str(query(s, t)) + "\n")
    elif r == 1:
        union(s, t)
    else:
        move(s, t)


array = []
for line in f:
    array.append([int(x) for x in line.split()])
for i in array:
    auswertung(i[0], i[1], i[2])

# print(len(array))
counter_o = 0
for i in array:
    if i[0] == 0:
        counter_o += 1

# print(counter_o)
print(knoten_liste)
print(kinder_liste)
print(BFS(4, [1]))