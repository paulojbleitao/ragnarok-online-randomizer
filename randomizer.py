import argparse
import yaml # pyyaml dependency
from mobs import randomize_mobs

parser = argparse.ArgumentParser(prog='Ragnarok Online Randomizer')
parser.add_argument('-p', '--path')
parser.add_argument('--level-range', default=-1, type=int) # a negative level range means randomizing completely
args = parser.parse_args()

rathena_path = args.path # pass rAthena path through the command line
mob_dp_path = f'{rathena_path}/db/pre-re/mob_db.yml'
mob_db_file = open(mob_dp_path)
mob_db = yaml.load(mob_db_file, Loader=yaml.CLoader)
mob_db_file.close()

randomize_mobs(rathena_path, mob_db, args.level_range)
