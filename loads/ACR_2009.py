import base

class ACR_base(base.Base):
	headgear = 'BAF_Soldier_Crewman_Headgear_D_DG1'
	items = [
		'ItemWatch',
		'ItemMap',
		'ItemCompass',
		'tf_rf7800str_1',
		'STKR_HMNVS',
	]	
	class HandGun:
		weapon = 'RH_g17'
		mags = [['RH_17Rnd_9x19_g17', 17]]

	class Uniform:
		type = 'U_mas_uk_B_IndUniform1_d'
		items = base.Base.Uniform.items + [
			['RH_17Rnd_9x19_g17', 2],
		]
	class Vest:
		type = 'BAF_Soldier_Crewman_Vest_D_DG1'
		items = [
			['Chemlight_red', 2],
			['Chemlight_blue', 2],
			['HandGrenade', 2],
			['SmokeShell', 2],
			]
	class Backpack:
		type = 'B_mas_Kitbag_des'
		
################  Crewman

class ACR_crewman(ACR_base):
	class Primary:
		weapon = 'kio_l85a2'
		optic = 'optic_Hamr'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(ACR_base.Vest):
		items = ACR_base.Vest.items + [
			['30rnd_556_magazine', 5],
		]
	class Backpack(ACR_base.Backpack):
		items = ACR_base.Backpack.items + [
			['30rnd_556_magazine', 5],
		]
		

		
################  Commander

class ACR_commander(ACR_base):
	items = + ['ItemGps']
	class Primary:
		weapon = 'kio_l85a2'
		optic = 'optic_Hamr'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(ACR_base.Vest):
		items = ACR_base.Vest.items + [
			['30rnd_556_magazine', 5],
		]
	class Backpack(ACR_base.Backpack):
		items = ACR_base.Backpack.items + [
			['30rnd_556_magazine', 5],
		]