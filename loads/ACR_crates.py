from p4a.loadout import Crate

class ACR_gear(Crate):
	title = 'ACR Gear'
 	base = 'VTN_WPNE_LMG_BOX'
	headgear = [
		['H_mas_uk_headset_b', 20]
	]
	backpacks = [
		['B_mas_Kitbag_des', 10],
		['tf_rt1523g_big', 10],
	]


class ACR_weapons(Crate):
	title = '3ACR Rifles, rockets and Ammo'
 	base = 'VTN_WPNE_LMG_BOX'
	weapons = [
		['kio_l85a2', 10],
		['RH_g17', 10],
		['mas_launch_LAW_F', 40],
	]
	items = [
		['HandGrenade', 50],
		['SmokeShellGreen', 50],
		['SmokeShellRed', 50],
		['SmokeShell', 100],
	optics = [
	    ['optic_Hamr', 5],
	]	
	magazines = [
		['30rnd_556_magazine', 300],
		['RH_17Rnd_9x19_g17', 100],
	]
