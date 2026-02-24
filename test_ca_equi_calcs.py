import unittest
import ca_equi_calcs as calc

class TestCalcs(unittest.TestCase): 

	def test_num_supp(self):
		self.assertEqual(calc.num_supp(0), 2)
		self.assertEqual(calc.num_supp(1), 2)
		self.assertEqual(calc.num_supp(2), 10)
		self.assertEqual(calc.num_supp(3), 218)
		self.assertEqual(calc.num_supp(4), 64594)
		self.assertEqual(calc.num_supp(5), 4294642034)

	def test_num_orbits(self):
		self.assertEqual(calc.num_orbits(calc.Type.T_c_r, 0), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_cr, 0), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_c, 0), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_r, 0), 1)
		self.assertEqual(calc.num_orbits(calc.Type.T_1, 0), 0)

		self.assertEqual(calc.num_orbits(calc.Type.T_c_r, 1), 2)
		self.assertEqual(calc.num_orbits(calc.Type.T_cr, 1), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_c, 1), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_r, 1), 1)
		self.assertEqual(calc.num_orbits(calc.Type.T_1, 1), 0)

		self.assertEqual(calc.num_orbits(calc.Type.T_c_r, 2), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_cr, 2), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_c, 2), 2)
		self.assertEqual(calc.num_orbits(calc.Type.T_r, 2), 4)
		self.assertEqual(calc.num_orbits(calc.Type.T_1, 2), 1)
	
		self.assertEqual(calc.num_orbits(calc.Type.T_c_r, 3), 8)
		self.assertEqual(calc.num_orbits(calc.Type.T_cr, 3), 4)
		self.assertEqual(calc.num_orbits(calc.Type.T_c, 3), 4)
		self.assertEqual(calc.num_orbits(calc.Type.T_r, 3), 28)
		self.assertEqual(calc.num_orbits(calc.Type.T_1, 3), 44)

		self.assertEqual(calc.num_orbits(calc.Type.T_c_r, 4), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_cr, 4), 0)
		self.assertEqual(calc.num_orbits(calc.Type.T_c, 4), 128)
		self.assertEqual(calc.num_orbits(calc.Type.T_r, 4), 512)
		self.assertEqual(calc.num_orbits(calc.Type.T_1, 4), 16064)

	def test_num_all_orbits(self):
		self.assertEqual(calc.num_all_orbits(1), 3)
		self.assertEqual(calc.num_all_orbits(2), 7)
		self.assertEqual(calc.num_all_orbits(3), 88)
		self.assertEqual(calc.num_all_orbits(4), 16704)


	def test_num_irreducible(self):
		self.assertEqual(calc.num_irreducible(0), 2)
		self.assertEqual(calc.num_irreducible(1), 2)
		self.assertEqual(calc.num_irreducible(2), 10)
		self.assertEqual(calc.num_irreducible(3), 218)
		self.assertEqual(calc.num_irreducible(4), 64594)

	def test_num_orbits_irr(self):
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c_r, 0), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_cr, 0), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c, 0), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_r, 0), 1)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_1, 0), 0)

		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c_r, 1), 2)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_cr, 1), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c, 1), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_r, 1), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_1, 1), 0)

		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c_r, 2), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_cr, 2), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c, 2), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_r, 2), 3)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_1, 2), 1)

		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c_r, 3), 6)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_cr, 3), 4)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c, 3), 2)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_r, 3), 24)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_1, 3), 38)

		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c_r, 4), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_cr, 4), 0)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c, 4), 104)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_r, 4), 505)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_1, 4), 15844)

		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c_r, 5), 1010)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_cr, 5), 32248)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c, 5), 31688)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_r, 5), 523216)
		self.assertEqual(calc.num_orbits_irr(calc.Type.T_1, 5), 1073366680)


		self.assertEqual(calc.num_orbits_irr(calc.Type.T_c_r, 4) + calc.num_orbits_irr(calc.Type.T_cr, 4) + 
			calc.num_orbits_irr(calc.Type.T_c, 4) + calc.num_orbits_irr(calc.Type.T_r, 4) +
			calc.num_orbits_irr(calc.Type.T_1, 4), 16453)

	def test_num_all_orbits_irr(self):
		self.assertEqual(calc.num_all_orbits_irr(0), 1)
		self.assertEqual(calc.num_all_orbits_irr(1), 2)
		self.assertEqual(calc.num_all_orbits_irr(2), 4)
		self.assertEqual(calc.num_all_orbits_irr(3), 74)
		self.assertEqual(calc.num_all_orbits_irr(4), 16453)
		self.assertEqual(calc.num_all_orbits_irr(5), 1073954842)


	def test_num_all_orbits_with_shift(self): 
		orb_irr = [calc.num_all_orbits_irr(n) for n in range(6)]
		self.assertEqual(orb_irr[0], 1)
		self.assertEqual(orb_irr[0] + orb_irr[1] , 3)
		self.assertEqual(orb_irr[0] + orb_irr[1] + orb_irr[2], 7)
		self.assertEqual(orb_irr[0] + orb_irr[1] + 2 * orb_irr[2] + orb_irr[3], 85)
		orb_all_shift_4 = orb_irr[0] + orb_irr[1] + 3 * orb_irr[2] + 2 * orb_irr[3] + calc.num_orbits_irr(calc.Type.T_1, 3) + \
			calc.num_orbits_irr(calc.Type.T_c, 3) + orb_irr[4]
		self.assertEqual(orb_all_shift_4, 16656)
		orb_all_shift_5 = orb_irr[0] + orb_irr[1] + 4 * orb_irr[2] + 4 * orb_irr[3] + 2 * calc.num_orbits_irr(calc.Type.T_1, 3) + \
			2 * calc.num_orbits_irr(calc.Type.T_c, 3) + 3 * orb_irr[4] + calc.num_orbits_irr(calc.Type.T_1, 4) + \
			calc.num_orbits_irr(calc.Type.T_c, 4) + orb_irr[5]
		self.assertEqual(orb_all_shift_5, 1074020544)


if __name__ == '__main__':
    unittest.main()

		 

