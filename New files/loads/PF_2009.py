import base

class PF_base(base.Base):
	headgear = 'H_HelmetWood'
	items = [
		'ItemWatch',
		'ItemMap',
		'ItemCompass',
		'tf_rf7800str_1',
	]	
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]

	class Uniform:
		type = 'U_ANA_CombatUniform_Forest'
		items = base.Base.Uniform.items + [
			['RH_15Rnd_9x19_M9', 2],
		]
	class Vest:
		type = 'V_ANA_TacVest_Wdl'
		items = [
			['Chemlight_red', 2],
			['Chemlight_blue', 2],
			['HandGrenade', 2],
			['SmokeShell', 2],
		]
	class Backpack:
		type = 'ANA_Carryall_AR_oli'
		items = [
			['rhs_weap_rsp30_white', 2],
		]
################  Rifleman

class PF_rifleman(PF_base):
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(PF_base.Vest):
		items = PF_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		]
	class Backpack(PF_base.Backpack):
		items = PF_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		]
################  Rifleman AT/AA

class PF_riflemanAT(PF_base):
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 30],
		]
	class Secondry:
		weapon = 'rhs_weap_rpg7'
		mags = [
			['rhs_rpg7_PG7VR_mag', 1],
		]
	class Vest(PF_base.Vest):
		items = PF_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		]
	class Backpack(PF_base.Backpack):
		items = PF_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
			['rhs_rpg7_PG7VR_mag', 2],
			['rhs_rpg7_OG7V_mag', 2],
		]
################  Grenadier 

class PF_grenadier(PF_base):
	class Primary:
		weapon = 'rhs_weap_ak74m_gp25'
		mags = [
			['rhs_30Rnd_545x39_AK', 30],
			['rhs_VOG25', 1],
		]
	class Vest(PF_base.Vest):
		type = 'V_ANA_TacVest_Wdl'
		items = PF_rifleman_light.Vest.items + [
			['rhs_VOG25', 5],
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		]

	class Backpack(PF_base.Backpack):
		type = 'ANA_Carryall_AR_oli'
		items = PF_rifleman_light.Backpack.items + [
			['rhs_VOG25', 5],
			['rhs_VG40OP_white', 4],
			['rhs_GRD40_White', 4],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		]

################  Fire Team Leader

class PF_ftl(PF_rifleman):
	binoc = 'Binocular'
	headgear = 'H_HelmetWood'
	items = PF_rifleman.items + ['tf_fadak_1']

	class Primary:
		weapon = 'arifle_mas_mk17'
		mags = [
			['20Rnd_mas_762x51_Stanag', 20],
		]
	class Vest(PF_rifleman.Vest):
		type = 'V_ANA_TacVest_Wdl'
		items = PF_base.Vest.items + [
			['20Rnd_mas_762x51_Stanag', 5],
		]
	class Backpack(PF_rifleman.Backpack):
		items = PF_base.Backpack.items + [
			['20Rnd_mas_762x51_T_Stanag', 5],
		]
	
################  Heavy Machine Gunner
class PF_hmg(PF_base):
	binoc = 'Binocular'
	class Primary:
		weapon = 'rhs_weap_pkp'
		mags = [
			['rhs_100Rnd_762x54mmR', 100],
		]
	class Vest(PF_base.Vest):
		type = 'V_ANA_TacVest_Wdl'
		items = PF_base.Vest.items + [
			['rhs_100Rnd_762x54mmR', 1],
		]
	class Backpack(PF_base.Backpack):
		items = PF_base.Backpack.items + [
			['rhs_100Rnd_762x54mmR_green', 2],
		]

################  Medic
class PF_medic(PF_rifleman_light):
	items = PF_crew.items 
	
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(PF_rifleman_light.Vest):
		items = PF_rifleman_light.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		] 
		
	class Backpack(PF_rifleman_light.Backpack):
		items = PF_base.Backpack.items + base.MedicSupplies + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		] 
		
		


################  Platoon Leader

class PF_pl(PF_rifleman):
	items = PF_rifleman.items + ['tf_anprc152']
	binoc = 'Binocular'
	headgear = 'H_HelmetWood'
	class Primary:
		weapon = 'arifle_mas_mk17'
		mags = [
			['20Rnd_mas_762x51_Stanag', 20],
		]
	class HandGun:
		weapon = 'RH_m9'
		mags = [
			['RH_15Rnd_9x19_M9', 15],
		]
	class Uniform(PF_rifleman.Uniform):
		type = 'U_ANA_OfficerUniform_Forest'
		items = PF_rifleman.Uniform.items + [
			['tf_anprc152', 1],
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Vest(PF_rifleman.Vest):
		type = 'V_ANA_TacVest_Wdl'
		items = PF_base.Vest.items + [
			['20Rnd_mas_762x51_Stanag', 5],
		]
	class Backpack(PF_base.Backpack):
		type = 'tf_rt1523g_big_rhs'
		items = PF_base.Backpack.items + [
			['alive_tablet', 1],
			['20Rnd_mas_762x51_T_Stanag', 5],
		]