# OBSHitPointOverlay
Python script that takes the health information from D&amp;D beyond and changes the opacity of a specified layer in OBS

The below variables need to be changed in order for the script to change OBS settings
![Required variables changes](/Images/Variables.png)

**Sources** is the name of the source layer in OBS 
![OBS source name example](images/OBSSourceName.png)

**Filter** is the name of the filter of the source above in OBS 
![OBS filter name example](/Images/Filters.png)

**CharacterID** is the D&D beyond ID of the character that wanted to be track. This can be found at the end of the URL on the character sheet on D&D beyond.

Example: https://www.dndbeyond.com/characters/67835216
CharacterID would be **67835216**