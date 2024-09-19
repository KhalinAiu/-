st = input().split()
sch = 0
for i in st:
    sch = max(sch, st.count(i))
    if st.count(i) == sch:
         ma = i
print(ma)