programmingLang_1 = {"Java","C#","Javascript","Python"}
programmingLang_2= {"Java","Python","C","C++","PHP"}

print(f"Programming languages set 1: {programmingLang_1}")
print(f"Programming languages set 2: {programmingLang_2}")
print(f"Programming set 1 union set 2 :{programmingLang_1.union(programmingLang_2)}")          
print(f"Programming set 1 intersection set 2 :{programmingLang_1.intersection(programmingLang_2)}")   
print(f"Programming set 1 difference set 2 : {programmingLang_1.difference(programmingLang_2)}") 