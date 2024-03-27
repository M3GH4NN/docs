
with open('source/conf.py', 'r') as f:
    conf_content = f.read()
          
# Find the start and end of the intersphinx_mapping block
start_idx = conf_content.find('intersphinx_mapping = {')
end_idx = conf_content.find('}', start_idx)
    
# Extract the block
mapping_block = conf_content[start_idx:end_idx+1]
print(mapping_block)

# Find the start and end of the dictionary
start_idx = mapping_block.find('{')
end_idx = mapping_block.rfind('}')

# Extract the dictionary part
dictionary_string = mapping_block[start_idx:end_idx + 1]

# Parse the dictionary string
mapping_dict = eval(dictionary_string)

# Extract keys from the dictionary
keys = list(mapping_dict.keys())

print(keys)
    
# Split the block into lines and remove the line containing intersphinx_mapping
lines = mapping_block.split('\n')
filtered_lines = [line.strip() for line in lines if 'intersphinx_mapping' not in line]
# print(filtered_lines)
# Join the lines back together and print
filtered_mapping = '\n'.join(filtered_lines)

# print(filtered_mapping)