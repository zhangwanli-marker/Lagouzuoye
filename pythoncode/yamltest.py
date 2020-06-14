import yaml

with open("mydatasyaml.yml", 'rb') as f:
    print(yaml.safe_load(f))

