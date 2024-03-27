intersphinx = ['python', 'pytest', 'salt', 'dummy', 'saltext-prometheus', 'saltext-moosefs', 'saltext-azurerm', 'saltext-proxmox', 'saltext-zabbix', 'saltext-apache', 'saltext-vault', 'extension_migration', 'saltext-mysql', 'saltext-namecheap', 'saltext-restconf', 'saltext-elasticsearch', 'saltext-kubernetes', 'salt-extension-copier', 'saltext-pushover', 'saltext-servicenow', 'saltext-mongodb', 'central-artifacts', 'saltext-mattermost', 'saltext-helm', 'saltext-consul', 'saltext-grafana', 'saltext-github', 'saltext-freezer', 'saltext-haproxy', 'saltext-redis', 'saltext-pagerduty', '.github', 'saltext-dell', 'saltext-splunk', 'saltext-zookeeper', 'community-extensions-holding', 'community', 'salt-describe', 'saltext-vector']

repos = ["saltext-prometheus","saltext-moosefs","saltext-azurerm","saltext-proxmox","saltext-zabbix","saltext-apache","saltext-vault","extension_migration","saltext-mysql","saltext-namecheap","saltext-restconf","saltext-elasticsearch","saltext-kubernetes","salt-extension-copier","saltext-pushover","saltext-servicenow","saltext-mongodb","central-artifacts","saltext-mattermost","saltext-helm","saltext-consul","saltext-grafana","saltext-github","saltext-freezer","saltext-haproxy","saltext-redis","saltext-pagerduty",".github","saltext-dell","saltext-splunk","saltext-zookeeper","community-extensions-holding","community","salt-describe","saltext-vector","saltext-tsl"]

with open('source/conf.py', 'r') as f:
    conf_content = f.read()
          
# Find the start and end of the intersphinx_mapping block
start_idx = conf_content.find('intersphinx_mapping = {')
end_idx = conf_content.find('}', start_idx)
    
# Extract the block
mapping_block = conf_content[start_idx:end_idx+1]
# print(mapping_block)

# Find the start and end of the dictionary
start_idx = mapping_block.find('{')
end_idx = mapping_block.rfind('}')

# Extract the dictionary part
dictionary_string = mapping_block[start_idx:end_idx + 1]

# Parse the dictionary string
mapping_dict = eval(dictionary_string)

# Extract keys from the dictionary
keys = list(mapping_dict.keys())

# print(keys)
    
for item in repos:
    if item not in intersphinx:
        print("new repo: ", item)