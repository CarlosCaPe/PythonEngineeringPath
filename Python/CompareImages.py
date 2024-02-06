
# pp 34 - 35 

l = [
	 {
	  "name": "photo1.jpg",
	  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food', 'meal'}
	 },
	 {
	  "name": "photo2.jpg",
	  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
	 },
	 {
	  "name": "photo3.jpg",
	  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
	 },
	 {
	  "name": "photo4.jpg",
	  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
	 }
	]
  
#def intersection(lst1, lst2):
  #return "_".join([value for value in lst1 if value in lst2]) 

def intersection(lst1, lst2):
    return "_".join(set(lst1) & set(lst2))  # Use set intersection for efficiency

  
#photo_groups = {}
#for i in range(1, len(l)):
#  for j in range(i+1,len(l)+1):
#    print(f"Intersecting photo {i} with photo {j}")
#    lst = intersection(l[i-1]["tags"],l[j-1]["tags"])
#    if lst: 
#      k = photo_groups.setdefault(lst, list((l[i-1]["name"], l[j-1]["name"])))  
#print(photo_groups)


photo_groups = {}
for i in range(len(l)):
    for j in range(i+1, len(l)):
        common_tags = intersection(l[i]["tags"], l[j]["tags"])
        if common_tags:
            photo_groups.setdefault(common_tags, []).extend([l[i]["name"], l[j]["name"]])


# Removing duplicates in each group
for tags, photos in photo_groups.items():
    photo_groups[tags] = list(set(photos))

print(photo_groups)