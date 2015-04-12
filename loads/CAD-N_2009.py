from p4a.loadout import Crate
from base import Base

class CAD_pilot(Base):
	headgear = 'H_mas_uk_PilotHelmetHeli_B'
	items = Base.items + ['tf_fadak'] + ['ItemGPS'] + ['A3_GPNVG18b_BLK_F']

	class Primary:
		weapon = 'arifle_mas_mp5'
		optic = 'optic_Holosight'
		mags = [['30Rnd_mas_9x21_Stanag', 30],]

	class HandGun:
		weapon = 'RH_g18'
		mags = [['RH_33Rnd_9x19_g18', 33]]

	class Uniform:
		type = 'U_mas_uk_B_IndUniform1_d'
		items = Base.Uniform.items + [
			['30Rnd_mas_9x21_Stanag', 2],
			['RH_33Rnd_9x19_g18', 2],
		]
	class Vest:
		type = 'V_mas_uk_TacVest_p'
		items = [
			['tf_fadak', 1],
		]

class CAD_crew(soar_pilot):
	headgear = 'H_CrewHelmetHeli_O'


class CAD_vehicle(Crate):
	weapons = [
		['VTN_SP81', 1],
		['VTN_RSP30_RED', 5],
		['VTN_RSP30_GREEN', 5],
		['VTN_RSP30_WHITE', 5],
	]
	magazines = [
		['VTN_OP_1k_WHITE', 20],
		['VTN_SP_1k_GREEN', 2],
		['VTN_SP_1k_RED', 2],
		['VTN_AK74_30b_SC', 15],
		['VTN_AKM_30b_SC', 15],
		['VTN_PK_100s_SC', 5],
		['VTN_NSPD', 5],
		['VTN_NSP_RED', 2],
		['VTN_NSP_GREEN', 2],
		['VTN_NSP_YELLOW', 2],
		['VTN_RGO', 10],
		['cse_bandage_basic', 25],
		['cse_bandageElastic', 15],
		['cse_tourniquet', 5],
		['SatchelCharge_Remote_Mag', 1],
	]
	backpacks = [
		['rhs_sidor', 2]
	]

