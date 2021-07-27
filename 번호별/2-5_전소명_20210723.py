string = "".join(map(lambda x : x.upper(),input()))
sset = set(string)
cnt = dict()
for i in sset: cnt[str(i)] = string.count(i)
rst = list()
m = max(cnt.values())
for k,v in cnt.items():
    if v == m:
        rst.append(k)
if len(rst)==1: print(rst[0])
else: print("?")