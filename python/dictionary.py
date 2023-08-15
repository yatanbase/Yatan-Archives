dict= {
    "name":"rak",
    "name":"yatan", #overwrite
    "stream":"cs",
    "course":"btech"
}

print(dict)

dict["name"]="yoda"

print(dict)

dict.pop("stream")
print(dict)

dict["id"]="21cs05x"
print(dict)

print(dict.get("id"))