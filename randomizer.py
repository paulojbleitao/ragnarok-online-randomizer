import argparse
import yaml # pyyaml dependency
import random

parser = argparse.ArgumentParser(prog='Ragnarok Online Randomizer')
parser.add_argument('-p', '--path')
parser.add_argument('--same-level', action='store_true')
args = parser.parse_args()

rathena_path = args.path # pass rAthena path through the command line
mob_dp_path = f'{rathena_path}/db/pre-re/mob_db.yml'
prt_fild_path = f'{rathena_path}/npc/pre-re/mobs/fields/prontera.txt'
mob_db = open(mob_dp_path)
prt_fild = open(prt_fild_path)

mob_list = yaml.load(mob_db, Loader=yaml.CLoader)['Body']

new_file = []
for line in prt_fild:
    if line.startswith('//') or line == '\n': continue
    new_line = line.split('\t')

    if args.same_level:
        mob_level = next(filter(lambda mob: mob['Name'] == new_line[2], mob_list))['Level']
        mobs_with_same_level = list(filter(lambda mob: mob['Level'] == mob_level, mob_list))
        random_mob = random.choice(mobs_with_same_level)
    else:
        random_mob = random.choice(mob_list)

    new_line[2] = random_mob['Name']
    id_part = new_line[3].split(',')
    id_part[0] = str(random_mob['Id'])
    new_line[3] = ','.join(id_part)
    new_file.append('\t'.join(new_line))

prt_fild.close()

prt_fild_new = open(prt_fild_path, 'w')
for line in new_file:
    print(line, end='', file=prt_fild_new)
prt_fild_new.close()