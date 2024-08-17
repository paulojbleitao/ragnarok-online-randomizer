import yaml # pyyaml dependency
import json
import random
from mobs import randomize_mobs
from drops import randomize_drops

config_file = open('./config.json')
config = json.load(config_file)
config_file.close()

random.seed(config['seed'])

rathena_path = config['rathenaPath']
version = 'pre-re' if config['preRe'] else 're'
mob_dp_path = f'{rathena_path}/db/{version}/mob_db.yml'
mob_db_file = open(mob_dp_path)
mob_db = yaml.load(mob_db_file, Loader=yaml.CLoader)
item_db_equip_file = open(f'{rathena_path}/db/{version}/item_db_equip.yml')
item_db_etc_file = open(f'{rathena_path}/db/{version}/item_db_etc.yml')
item_db_usable_file = open(f'{rathena_path}/db/{version}/item_db_usable.yml')
item_db_equip = yaml.load(item_db_equip_file, Loader=yaml.CLoader)['Body']
item_db_etc = yaml.load(item_db_etc_file, Loader=yaml.CLoader)['Body']
item_db_usable = yaml.load(item_db_usable_file, Loader=yaml.CLoader)['Body']
item_db = { 'equip': item_db_equip, 'etc': item_db_etc, 'usable': item_db_usable }
mob_db_file.close()
item_db_equip_file.close()
item_db_etc_file.close()
item_db_usable_file.close()

randomize_mobs(rathena_path, mob_db, config)
randomize_drops(rathena_path, mob_db, item_db, config)
