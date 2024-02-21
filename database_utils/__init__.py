import yaml

with open('db_config.yml', 'r') as file:
    config = yaml.safe_load(file)
db = config['database']