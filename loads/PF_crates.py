from p4a.loadout import Crate

class cdf_explosives(Crate):
	title = 'CDF Explosives and CSW'
 	base = 'VTN_WPNE_LMG_BOX'
	weapons = [
		['VTN_SP81', 50],
		['VTN_RSP30_RED', 200],
		['VTN_RSP30_GREEN', 200],
		['VTN_RSP30_WHITE', 200],
	]
	magazines = [
		['VTN_OP_1k_WHITE', 500],
		['VTN_SP_1k_WHITE', 100],
		['VTN_SP_1k_RED', 100],
		['VTN_SP_1k_GREEN', 100],
		['VTN_SP_1k_YELLOW', 100],
		
		['rhs_mag_rgd5', 200],
		['VTN_RDG2B', 500],
		['VTN_RDG2CH', 500],

		['VTN_NSPD', 500],
		['VTN_NSP_RED', 50],
		['VTN_NSP_YELLOW', 50],
		['VTN_NSP_GREEN', 50],
		['rhs_mine_tm62m_mag', 100],

		['VTN_VOG25', 100],
		['VTN_VOG25P', 100],
		['VTN_VG40MD', 100],
		['VTN_VG40OP', 100],
		['VTN_VGS401', 100],
		['VTN_VGS402', 100],
	]

	backpacks = [
		['RHS_NSV_Gun_Bag', 10],
		['RHS_NSV_Gun_Bag', 10],
		
		['RDS_DShkM_Gun_Bag', 10],
		['RDS_DShkM_TripodLow_Bag', 10],

		['RDS_AGS30_Gun_Bag', 10],
		['RDS_AGS30_Tripod_Bag', 10],
	]

class 40_launchers(Crate):
	title = '40 Commando Launchers and Warheads'
 	base = 'VTN_WPNE_SN_BOX'
	weapons = [
		['rhs_weap_rpg7', 10],
		['rhs_weap_rpg26', 500],
		['rhs_weap_rshg2', 100],
	]
	magazines = [
		['rhs_rpg7_PG7VL_mag', 400],
		['rhs_rpg7_PG7VR_mag', 200],
		['rhs_rpg26_mag', 500],
		['rhs_rshg2_mag', 100],
	]

class 40_weapons(Crate):
	title = '40 Commando Rifles and Ammo'
 	base = 'VTN_WPNE_LMG_BOX'
	weapons = [
		['kio_l85a2', 10],
		['kio_l85a2_ugl', 5],
		['Trixie_L7A2', 5],
		['RH_g17', 20],
	]
	optics = [
	    ['optic_Hamr', 20],
	]	
	magazines = [
		['30rnd_556_magazine', 500],
		['Trixie_100Rnd', 200],
		['RH_17Rnd_9x19_g17', 200],
	]

class 40_Radios(Crate):
	title = '40 Commando Radios and Misc'
 	base = 'VTN_WPNE_LMG_BOX'