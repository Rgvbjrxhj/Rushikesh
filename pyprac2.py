# dic={
#     "name":"wagnor",
#     "brand":"maruti",
#     "year":2012
# }
# print(dic)
# print(dic["brand"])
# print(len(dic))

# lee = dict(name="rushi", room = "TE", college = "zeal")
# print(lee)

#TO ACCESS DICTIONARY:
# xyz = dict(name="rst", bike="mt15",year=2024)
# print(xyz.get("bike"))
# print(xyz.keys())
# print(xyz.values())
# print(xyz.items())
# xyz["month"]="augest"
# print(xyz)
# xyz["bike"]="H2"
# xyz.update({"name":"uvw"})
# print(xyz)

#TO REMOVE DICTIONARY:
xyz = dict(name="rst", bike="mt15",year=2024)
xyz.pop("year")
print(xyz)
xyz.popitem()
print(xyz)
del(xyz["name"])
print(xyz)

dic={
    "name":"wagnor",
    "brand":"maruti",
    "year":2012
}
print(dic)
print(dic.clear())
