# Ragnarok Online Randomizer

A randomizer for [rAthena](https://github.com/rathena/rathena) servers.

---

Currently, the randomization covers only monster spawns, which means any monster can spawn in any field or dungeon (e.g. an Ice Titan spawning in Prontera fields). It is done by modifying the monster spawn tables and swapping a monster for another. For example, the prt\_fild08 map spawns 70 Porings. By swapping the Poring entry with another monster's, like a Dokebi, prt\_fild08 now spawns 70 Dokebis instead.

An option to keep the randomized monsters to a certain level range is also available, to avoid situations like having those Porings being swapped for a much stronger monster such as Baphomets. By setting this argument to an integer, only monsters with levels within this integer will be randomized (by setting the range to 10, a level 50 monster will only be replaced by monsters with levels between 40 and 60).

Monster drops randomization is also planned. Other forms of randomization may be coming too.
