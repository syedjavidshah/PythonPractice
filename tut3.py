# dictionary is key value pairs
d1= {}
print(type(d1))
d2 = {"javid":"meat","abc" : "chicken","ali":"roti"}
print(d2)
print(d2["javid"])
print(d2["ali"])
d2["syed"]="junk food"
d2["aliyas"]="cold drink"
del d2["aliyas"]
print(d2)
print(d2.copy())
print(d2.get("abc"))
print(d2.update({"syed":"ice cream"}))
print(d2)
print(d2.keys())
print(d2.items())



















































