d = {"elem1": 1, "elem2": 2}
print(d)

d["elem1"], d.get("elem1") = d.get("elem1"), d["elem1"]
print(d)


