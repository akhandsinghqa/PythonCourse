a_dict = {"name": "akhand"}
b_dict = {"tech": "python"}
c_dict = a_dict | b_dict  # Merge
print(c_dict.items())
c_dict |= {"tech": "Java"}  # Update
print(c_dict.items())
