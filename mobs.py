import random
from util import navigate_directories
from pathlib import Path

def randomize_mob_file(filepath, mob_list, filtered_mob_list, level_range):
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

def randomize_mobs(rathena_path, mob_db, level_range):
    mob_list = mob_db['Body']
    filtered_mob_list = list(filter(lambda mob: 'BaseExp' in mob and 'Drops' in mob, mob_list))
    mob_files = navigate_directories(Path(f'{rathena_path}/npc/pre-re/mobs/'), [])
    for file in mob_files:
        randomize_mob_file(file, mob_list, filtered_mob_list, level_range)
