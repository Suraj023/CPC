string = "I am what I am and you are what you eat"
s = string.split()
u = []
for i in s:
    u.append(s.count(i))
print(str(list(set((zip(s,u))))))
