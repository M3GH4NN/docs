import ast
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pytest": ("https://docs.pytest.org/en/stable", None),
    "salt": ("https://docs.saltproject.io/en/latest/", None),
    "dummy": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-prometheus": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-moosefs": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-azurerm": ("https://saltext-azurerm.readthedocs.io/en/latest/", None),
    "saltext-proxmox": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-zabbix": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-apache": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-vault": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "extension_migration": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-mysql": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-namecheap": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-restconf": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-elasticsearch": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-kubernetes": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "salt-extension-copier": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-pushover": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-servicenow": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-mongodb": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "central-artifacts": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-mattermost": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-helm": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-consul": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-grafana": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-github": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-freezer": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-haproxy": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-redis": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-pagerduty": ("https://m3gh4nn.github.io/dummy-repo/", None),
    ".github": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-dell": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-splunk": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-zookeeper": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "community-extensions-holding": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "community": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "salt-describe": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-vector": ("https://m3gh4nn.github.io/dummy-repo/", None),
    "saltext-tsl": ("https://m3gh4nn.github.io/dummy-repo/", None),
}

# print(intersphinx_mapping.keys())


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