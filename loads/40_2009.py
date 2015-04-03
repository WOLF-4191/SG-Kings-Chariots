import base

class 40_base(base.Base):
	headgear = 'H_VTN_6B26'
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
		type = 'BAF_Soldier_1_Vest_D_DG1'
		items = [
			['Chemlight_red', 2],
			['Chemlight_blue', 2],
			['HandGrenade', 2],
			['SmokeShell', 2],
			['AGM_M84', 2],
		]
	class Backpack:
		type = 'B_mas_Kitbag_des'
		items = [
			['', 2],
		]
################  Rifleman

class 40_rifleman(40_base):
	class Primary:
		weapon = 'kio_l85a2'
		optic = 'optic_Hamr'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(40_base.Vest):
		items = 40_base.Vest.items + [
			['30rnd_556_magazine', 5],
		]
	class Backpack(40_base.Backpack):
		items = 40_base.Backpack.items + [
			['30rnd_556_magazine', 5],
		]

class 40_rifleman_light(40_base):
	class Primary:
		weapon = 'kio_l85a2'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(40_base.Vest):
	        items = 40_base.Vest.items + [
			['30rnd_556_magazine', 5],
		]
	class Backpack(40_base.Backpack):
		items = 40_base.Backpack.items + [
			['30rnd_556_magazine', 5],
		]

		
################  Grenadier 

class 40_grenadier(40_rifleman_light):
	class Primary:
		weapon = 'kio_l85a2_ugl'
		mags = [
			['VTN_AK74_30b_TRC', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class Vest(40_rifleman_light.Vest):
		type = 'BAF_Soldier_gl_Vest_D_DG1'
		items = 40_rifleman_light.Vest.items + [
			['1Rnd_HE_Grenade_shell', 5],
		]

	class Backpack(40_rifleman_light.Backpack):
		type = 'B_mas_Kitbag_des'
		items = 40_rifleman_light.Backpack.items + [
			['1Rnd_HE_Grenade_shell', 5],
			['UGL_FlareWhite_F', 4],
			['1Rnd_Smoke_Grenade_shell', 4],
		]

################  Fire Team Leader

class 40_ftl(40_rifleman):
	headgear = 'BAF_Soldier_1_Headgear_D_DG1'
	items = 40_rifleman.items + ['tf_anprc152']

	class Primary:
		weapon = 'kio_l85a2'
		optic = 'optic_Hamr'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(40_rifleman.Vest):
		type = 'BAF_Soldier_2_Vest_D_DG1'
		items = 40_rifleman.Vest.items 
		]
    class Uniform(40_rifleman.Uniform):
		type = 'U_mas_uk_B_IndUniform1_d'
		items = 40_rifleman.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Backpack(40_rifleman.Backpack):
		items = 40_rifleman.Backpack.items 
		]
		
		
class 40_tl(40_sl):
	headgear = 'BAF_Soldier_1_Headgear_D_DG1'

################  Heavy Machine Gunner
class 40_hmg(40_base):
	binoc = 'Binocular'
	class Primary:
		weapon = 'Trixie_L7A2'
		optic = 'optic_Hamr'
		mags = [
			['Trixie_100Rnd', 100],
		]
	class Vest(40_base.Vest):
		type = 'BAF_Soldier_Engineer_Vest_D_DG1'
		items = 40_base.Vest.items + [
			['Trixie_100Rnd', 1],
		]
	class Backpack(40_base.Backpack):
		items = 40_base.Backpack.items + [
			['Trixie_100Rnd', 2],
		]

################  Medic
class 40_medic(40_rifleman_light):
	items = 40_crew.items 
	
	class Primary:
		weapon = 'kio_l85a2'
		optic = 'optic_Hamr'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class Vest(40_rifleman_light.Vest):
		items = 40_rifleman_light.Vest.items 
		
	class Backpack(40_rifleman_light.Backpack):
		items = 40_base.Backpack.items + base.MedicSupplies
		


################  Platoon Leader

class 40_pl(40_rifleman):
	items = 40_rifleman.items + ['tf_anprc152']
	binoc = 'tf_rf7800str_5'
	headgear = 'BAF_Soldier_1_Headgear_D_DG1'
	class Primary:
		weapon = 'kio_l85a2'
		optic = 'optic_Hamr'
		mags = [
			['30rnd_556_magazine', 30],
		]
	class HandGun:
		weapon = 'RH_g19t'
		mags = [
			['RH_17Rnd_9x19_g17', 17],
		]
	class Uniform(40_rifleman.Uniform):
		type = 'U_mas_uk_B_IndUniform1_d'
		items = 40_rifleman.Uniform.items + [
			['tf_anprc152', 1],
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Vest(40_rifleman.Vest):
		type = 'BAF_Soldier_Officer_Vest_D_DG1'
		items = 40_base.Vest.items + [
			['30rnd_556_magazine', 5],
		]
	class Backpack(40_base.Backpack):
		type = 'tf_rt1523g_big_rhs'
		items = 40_base.Backpack.items + [
			['alive_tablet', 1],
		]

################  Platoon RTO

class 40_rto(40_rifleman_light):
	binoc = 'tf_rf7800str_5'
	items = 40_rifleman_light.items + ['tf_anprc152']
	class Backpack(40_rifleman_light):
		type = 'tf_rt1523g_big_rhs'
		items = 40_rifleman_light.Backpack.items + [
			['tf_anprc152', 1],
		]