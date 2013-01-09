import jlib 

#Video settings

#default window size
WINDOW_WIDTH = 800
WINDOW_HEIHGT = 600

#Colour, race distinction
COLOURS = {
	'WHITE' = (128, 128, 128), #Knights
	'BLUE' = (0, 255, 0), #Gnomes
	'BLACK' = (0, 0, 0), #Undead
	'RED' = (255, 0, 0), #Goblins
	'GREEN' = (0, 255, 0) #Fae
}

#Mechanical distinctions
RACES = Enum('KNIGHT', 'GNOME', 'UNDEAD', 'GOBLIN', 'FAE')

#Spell distinction 

#Spell type, enumerated as INSTANT, SORCERY, ENCHANTMENT
SPELL_TYPE = Enum('INSTANT', 'SORCERY', 'ENCHANTMENT')

#Spell target type(s), enumerated 
#
TARGET_TYPE = Enum('UNIT', 'SPELL', 'SPACE', 'WORLD', 'PLAYER', 'COLOUR')

#
TARGET_NUM = Enum('SINGLE', 'X', 'ALL')

EFFECT_TYPE = Enum('CHANGE', 'SET', 'REMOVE', 'SPAWN')

#Attributes of objects
UNIT_ATTRIBUTES = Enum('HEALTH', 'MANA', 'STRENGTH', 'DEFENSE'. 'AFFINITY')
