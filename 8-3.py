import collections

data = 'すもももももももものうち'
count_dic = {}
for v in data:
    if v in count_dic:
        count_dic[v] += 1
    else:
        count_dic[v] = 1
print(count_dic)

count_dic = collections.defaultdict(int)
for v in data:
    count_dic[v] += 1
print(count_dic)

count_dic = collections.defaultdict(list)
for v in data:
    count_dic[v].append(v)
print(count_dic)

counter = collections.Counter(data)
print(counter)

