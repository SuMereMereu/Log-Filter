'''
Author : Riccardo Mereu
Mini-library
'''



import json

def simple_search (dictionary, keywords): 
	
	temp_dict = {}
	
	if isinstance(dictionary, dict) and keywords:  #THE FIRST ONE IN THE BRACKETS IS THE VARIABLE NAME
		
		for element in dictionary:
			if isinstance(dictionary[element], dict):
				temp_dict[element] = simple_search(dictionary[element], keywords)	
				
				if temp_dict[element] == {}:
					temp_dict.pop(element)
			
			else:
				for key in keywords:
					if key in dictionary.keys():
						temp_dict[key] = dictionary[key]
	
	return temp_dict
	
				
def json_search (keywords, j_string):
	
	diz = json.loads(j_string)

	final_dict = simple_search(diz, keywords)
				
	print final_dict
	return
