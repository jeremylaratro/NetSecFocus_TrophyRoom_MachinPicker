# NetSecFocus_TrophyRoom_MachineSelector

Python script that automatically chooses your next OSCP prep machine from TJNull's NetSecFocus Trophy Room excel sheet.

Features:
 - Text files containing the machines within the PG Practice, PG Play, and HTB (updated 2022) sheets
 - Weighted selection of oscp-like boxes (90% chance of oscp-level box, 10% chance of harder-than-oscp level box)
 
 Usage:
 ```
 python trophychoice.py {num}
 
 python trophychoice.py 1
 ```
Options:
  - 1 = PG Practice
  - 2 = PG Play
  - 3 = HTB (updated 2022 only)
  
  
  
