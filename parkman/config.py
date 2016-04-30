import yaml
import os

if os.environ['CONFIG']:
    config_file_path = os.environ['CONFIG']
else:
    config_file_path = 'config/base.yaml'

with open(config_file_path, 'r') as stream:
    config = yaml.load(stream)