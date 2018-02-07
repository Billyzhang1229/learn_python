rivers = {'nile':'egypt', 
          'amazon': 'brail',
          'yangzi':'china',
          }

for river, nation in rivers.items():
	print("The " + river.title() + ' runs through ' + nation.title())

for river_name in rivers.keys():
    print(river_name)
    
for nation_name in rivers.values():
    print(nation_name)