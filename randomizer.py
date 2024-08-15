import argparse
import yaml # pyyaml dependency
from mobs import randomize_mobs
from drops import randomize_drops

parser = argparse.ArgumentParser(prog='Ragnarok Online Randomizer')
parser.add_argument('-p', '--path')
parser.add_argument('--level-range', default=-1, type=int) # a negative level range means randomizing completely
args = parser.parse_args()

rathena_path = args.path # pass rAthena path through the command line
mob_dp_path = f'{rathena_path}/db/pre-re/mob_db.yml'
mob_db_file = open(mob_dp_path)
mob_db = yaml.load(mob_db_file, Loader=yaml.CLoader)
item_db_equip_file = open(f'{rathena_path}/db/pre-re/item_db_equip.yml')
item_db_etc_file = open(f'{rathena_path}/db/pre-re/item_db_etc.yml')
item_db_usable_file = open(f'{rathena_path}/db/pre-re/item_db_usable.yml')
item_db_equip = yaml.load(item_db_equip_file, Loader=yaml.CLoader)['Body']
item_db_etc = yaml.load(item_db_etc_file, Loader=yaml.CLoader)['Body']
item_db_usable = yaml.load(item_db_usable_file, Loader=yaml.CLoader)['Body']
item_db = { 'equip': item_db_equip, 'etc': item_db_etc, 'usable': item_db_usable }
mob_db_file.close()
item_db_equip_file.close()
item_db_etc_file.close()
item_db_usable_file.close()

# randomize_mobs(rathena_path, mob_db, args.level_range)
randomize_drops(rathena_path, mob_db, item_db)
