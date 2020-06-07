import yaml

with open('yaml.yml') as f:
    content = yaml.load(f)
    print(type(content))
