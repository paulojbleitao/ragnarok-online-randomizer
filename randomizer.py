import argparse
import yaml # pyyaml dependency
import random
from pathlib import Path

def navigate_directories(directory, files):
    for path in directory.iterdir():
        if path.is_dir():
            navigate_directories(path, files)
        else:
            files.append(path)
    return files

def randomize_mobs(filepath, mob_list, filtered_mob_list, level_range):
    file = open(filepath)
    new_file = []
    for line in file:
        new_line = line.split('\t')
        # ignore comment lines, blank lines
        if line.startswith('//') or line == '\n': continue
        # make sure to keep script lines
        if not 'monster' in line or len(new_line) != 4: new_file.append(line); continue

        if level_range >= 0:
            mob_id = int(new_line[3].split(',')[0])
            mob_level = next(filter(lambda mob: mob['Id'] == mob_id, mob_list))['Level']
            mobs_in_level_range = list(filter(lambda mob: mob_level - level_range <= mob['Level'] <= mob_level + level_range, filtered_mob_list))
            random_mob = random.choice(mobs_in_level_range)
        else:
            random_mob = random.choice(filtered_mob_list)

        new_line[2] = random_mob['Name']
        id_part = new_line[3].split(',')
        id_part[0] = str(random_mob['Id'])
        new_line[3] = ','.join(id_part)
        new_file.append('\t'.join(new_line))
    file.close()

    file = open(filepath, 'w')
    for line in new_file:
        print(line, end='', file=file)
    file.close()

parser = argparse.ArgumentParser(prog='Ragnarok Online Randomizer')
parser.add_argument('-p', '--path')
parser.add_argument('--level-range', default=-1, type=int) # a negative level range means randomizing completely
args = parser.parse_args()

rathena_path = args.path # pass rAthena path through the command line
mob_dp_path = f'{rathena_path}/db/pre-re/mob_db.yml'
mob_db = open(mob_dp_path)
mob_list = yaml.load(mob_db, Loader=yaml.CLoader)['Body']
filtered_mob_list = list(filter(lambda mob: 'BaseExp' in mob and 'Drops' in mob, mob_list))

mob_files = navigate_directories(Path(f'{rathena_path}/npc/pre-re/mobs/'), [])
for file in mob_files:
    randomize_mobs(file, mob_list, filtered_mob_list, args.level_range)
