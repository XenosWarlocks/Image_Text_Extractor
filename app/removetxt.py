# unwantedtxt.py
# File path
file_path = r"C:\Users\mannu\Pictures\Screenshots\work\Aramark\extracted_names.txt"

# Terms to remove
remove_terms = [
    "show details v", "innovation", "[3", "business" , "digital", "and", "tech", "ficer", "member", 
    "show phones", " ff)", "procurement", "crm", "data", "center", "show", "details", "v", "show", "phones",
    "usa with more", "[i", "chief", "executive", "ficer",
    "middle", "east" , "africa" , "turkey", "engagement", "europe",
    "[}chief financial officer","emea", "president", "group", "operations",
    "complex commercial director", "[)", " (3)", "executive",  "cyber", "security", "world",
    "[5", "luxury" , "leisure" , "lifestyle", "sitel" , "mgallery",
    "[}", "global", "director", "of", "sales", "information", "technology", "[f)",
    "senior", "vice", "president", "contact", "center", "human", "resources", "sustainability", "development", "south", "europe",
    "[]", "director", "of", "marketing", "brand", "management","[j",
]

# Open the file and process the content
with open(file_path, 'r') as file:
    content = file.read()

# Replace periods with spaces
content = content.replace('.', ' ')

# Remove the specified terms
for term in remove_terms:
    content = content.replace(term, '')

# Save the filtered content back to a file
output_path = 'filtered_file.txt'
with open(output_path, 'w') as file:
    file.write(content)

print("File processed and saved as filtered_file.txt")


# python removetxt.py
