# Configuration file fintersphinx_mapping = {'python': ('https://docs.python.org/3', None), 'pytest': ('https://docs.pytest.org/en/stable', None), 'salt': ('https://docs.saltproject.io/en/latest/', None), 'dummy': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-prometheus': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-moosefs': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-azurerm': ('https://saltext-azurerm.readthedocs.io/en/latest/', None), 'saltext-proxmox': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-zabbix': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-apache': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-vault': ('https://m3gh4nn.github.io/dummy-repo/', None), 'extension_migration': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-mysql': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-namecheap': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-restconf': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-elasticsearch': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-kubernetes': ('https://m3gh4nn.github.io/dummy-repo/', None), 'salt-extension-copier': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-pushover': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-servicenow': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-mongodb': ('https://m3gh4nn.github.io/dummy-repo/', None), 'central-artifacts': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-mattermost': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-helm': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-consul': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-grafana': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-github': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-freezer': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-haproxy': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-redis': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-pagerduty': ('https://m3gh4nn.github.io/dummy-repo/', None), '.github': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-dell': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-splunk': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-zookeeper': ('https://m3gh4nn.github.io/dummy-repo/', None), 'community-extensions-holding': ('https://m3gh4nn.github.io/dummy-repo/', None), 'community': ('https://m3gh4nn.github.io/dummy-repo/', None), 'salt-describe': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-vector': ('https://m3gh4nn.github.io/dummy-repo/', None), 'saltext-tsl': ('https://m3gh4nn.github.io/dummy-repo/', None)}ce at the top
# of the sidebar.
html_logo = ""

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large. Favicons can be up to at least 228x228. PNG
# format is supported as well, not just .ico'
html_favicon = ""

# Sphinx Napoleon Config
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# ----- Intersphinx Config ---------------------------------------------------------------------------------------->
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
}

# ----- Autodoc Config ---------------------------------------------------------------------------------------------->
autodoc_default_options = {"member-order": "bysource"}
autodoc_mock_imports = ["salt"]
# <---- Autodoc Config -----------------------------------------------------------------------------------------------




def setup(app):
    app.add_crossref_type(
        directivename="fixture",
        rolename="fixture",
        indextemplate="pair: %s; fixture",
    )
    # Allow linking to pytest's confvals.
    app.add_object_type(
        "confval",
        "pytest-confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )