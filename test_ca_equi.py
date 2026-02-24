import unittest
from ca_equi import CAEquivalence 

class TestCAEquivalence(unittest.TestCase):

	def test_rfl_pairs(self):
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.rfl_pairs, [(1, 4), (3, 6), (4, 1), (6, 3)])

	def test_enc(self):
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.enc([]), 0)
		self.assertEqual(ca_equi.enc([0,0,0,1]), 1)
		self.assertEqual(ca_equi.enc([1,0,0,0]), 8)

	def test_encRule(self):
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.encRule([1,0,0,0,0,0,0,0,]), 1)
		self.assertEqual(ca_equi.encRule([0,0,0,0,0,0,0,1]), 128)

	def test_decRule(self):
		ca_equi = CAEquivalence(2,3)
		f = ca_equi.decRule(12)
		self.assertEqual(f, [0, 0, 1, 1, 0, 0, 0, 0])
		f = ca_equi.decRule(110)
		self.assertEqual(ca_equi.encRule(f), 110)

	def test_dec(self):
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.enc(ca_equi.dec(255, 8)), 255)
		ca_equi = CAEquivalence(3,2)
		self.assertEqual(ca_equi.dec(3,2), [1,0])

	def test_reflect_rule(self):
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.decRule(110)
		ref_rule = ca_equi.reflectRule(rule)
		self.assertEqual(ca_equi.encRule(ref_rule), 124)

	def test_permutateRule(self):
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.dec(110,8)
		perm_rule = ca_equi.permutateRule(rule, (1,0))
		self.assertEqual(ca_equi.enc(perm_rule), 137)

	def test_is_dependent(self):
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.decRule(12)
		self.assertEqual(ca_equi.is_dependent(rule, 0), True)
		self.assertEqual(ca_equi.is_dependent(rule, 1), True)
		self.assertEqual(ca_equi.is_dependent(rule, 2), False)


	def test_support(self):
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.dec(110,8)
		self.assertEqual(ca_equi.support(rule), [0,1,2])
		rule = ca_equi.dec(0,8)
		self.assertEqual(ca_equi.support(rule), [])
		rule = ca_equi.dec(12,8)
		self.assertEqual(ca_equi.support(rule), [0,1])

	def test_cycle(self):
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.cycle([1,2,3,4,5],1), [5,1,2,3,4])
		self.assertEqual(ca_equi.cycle([1,2,3,4,5],5), [1,2,3,4,5])


	def test_shiftRule(self):
		"""
		\\sigma_{-1} = f_{240}, id = f_{204}, \\sigma =  f_{170}
		"""
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.dec(240,8)
		shifted = ca_equi.shiftRule(rule, 1)
		self.assertEqual(ca_equi.enc(shifted), 204)
		shifted = ca_equi.shiftRule(rule, 2)
		self.assertEqual(ca_equi.enc(shifted), 170)
		rule = ca_equi.dec(170,8)
		shifted = ca_equi.shiftRule(rule, -2)
		self.assertEqual(ca_equi.enc(shifted), 240)

	def test_symClass(self):
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.decRule(110)
		equi_class = ca_equi.symClass(rule)
		self.assertEqual(equi_class, (110, 124, 137, 193))
		ca_equi = CAEquivalence(2,4)
		rule = ca_equi.decRule(110)
		equi_class = ca_equi.symClass(rule)
		self.assertEqual(equi_class, (110, 5456, 35327, 62807))

	def test_shiftClass(self):
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.dec(240,8)
		equi_class = ca_equi.shiftClass(rule)
		self.assertEqual(equi_class, {170, 204, 240})
		rule = ca_equi.dec(12,8)
		equi_class = ca_equi.shiftClass(rule)
		self.assertEqual(equi_class, {12, 34})

	def test_shiftSymClass(self): 
		ca_equi = CAEquivalence(2,3)
		rule = ca_equi.decRule(240)
		equi_class = ca_equi.shiftSymClass(rule)
		self.assertEqual(equi_class, {170, 204, 240})
		# from Ruivo et al., Shift-equivalence of k-ary, one-dimensional cellular automata rules 
		rule = ca_equi.decRule(12)
		equi_class = ca_equi.shiftSymClass(rule)
		self.assertEqual(equi_class, {12, 34, 48, 68, 187, 207, 221, 243})

	def test_countSymClasses(self):
		# permutation and reflection
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.countSymClasses(), 88)
		ca_equi = CAEquivalence(2,4)
		self.assertEqual(ca_equi.countSymClasses(), 16704)

	def test_getCountSymClasses(self):
		# permutation and reflection
		ca_equi = CAEquivalence(2,3)
		clazzes = ca_equi.getSymClasses()
		self.assertEqual(len(clazzes), 88)

	def test_countShiftSymClasses(self):
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.countShiftSymClasses(), 85)
		ca_equi = CAEquivalence(2,4)
		# Ruivo et al. give 16032 for the (2,4) classes, error in the article?
		self.assertEqual(ca_equi.countShiftSymClasses(), 16656)

	def test_getShiftSymClasses(self):
		ca_equi = CAEquivalence(2,3)
		eq_classes = ca_equi.getShiftSymClasses()
		self.assertEqual(len(eq_classes), 85)

		ca_equi = CAEquivalence(2,4)
		# Ruivo et al. give 16032 for the (2,4) classes, error in the article?
		eq_classes = ca_equi.getShiftSymClasses()
		self.assertEqual(len(eq_classes), 16656)

		# test the total number of rules = 2**(2**4)
		counter_all_rules = 0
		for c in eq_classes:
			counter_all_rules += len(c)  
		self.assertEqual(counter_all_rules, 2**(2**4))

		# count classses by support
		count_by_supp = dict()
		for c in eq_classes:
			f = ca_equi.decRule(list(c)[0])
			num_supp = len(ca_equi.support(f))
			count_by_supp[num_supp] = count_by_supp.get(num_supp, 0) + 1
		# print(count_by_supp)

	
	def test_minRule(self):
		ca_equi = CAEquivalence(2,3)
		f = ca_equi.decRule(12)		# ECA 12 and 34 are shift-equivalent
		self.assertEqual(ca_equi.minRule(f), [0,1,0,0])
		f = ca_equi.decRule(34)
		self.assertEqual(ca_equi.minRule(f), [0,1,0,0])
		f = ca_equi.decRule(240)	# \\sigma^{-1}, left-shift
		self.assertEqual(ca_equi.minRule(f), [0,1])
		f = ca_equi.decRule(204)	# id
		self.assertEqual(ca_equi.minRule(f), [0,1])
		f = ca_equi.decRule(170)	# \\sigma, right-shift
		self.assertEqual(ca_equi.minRule(f), [0,1])
		f = ca_equi.decRule(110)	# minRule=f
		self.assertEqual(ca_equi.minRule(f), f)

	def test_moveRule(self):
		ca_equi = CAEquivalence(2,3)
		f= ca_equi.decRule(12)
		f_min = ca_equi.minRule(f)
		g = ca_equi.moveRule(f_min, [1,2])
		self.assertEqual(ca_equi.encRule(g), 34)	
		f = ca_equi.decRule(240)	# \\sigma^{-1}, left-shift
		f_min = ca_equi.minRule(f)
		g = ca_equi.moveRule(f_min, [2])
		self.assertEqual(ca_equi.encRule(g), 170)	
		f = ca_equi.decRule(170)	# \\sigma, right-shift
		f_min = ca_equi.minRule(f)
		g = ca_equi.moveRule(f_min, [0])
		self.assertEqual(ca_equi.encRule(g), 240)	

	def test_scaleClass(self):
		ca_equi = CAEquivalence(2,3)
		f = ca_equi.decRule(12)
		c = ca_equi.encRuleSeq(ca_equi.scaleClass(f))
		self.assertEqual(c, {10, 12, 34})
		f = ca_equi.decRule(110)
		c = ca_equi.encRuleSeq(ca_equi.scaleClass(f))
		self.assertEqual(c, {110})

	def test_allRelEquiClass(self):
		# permutation, reflection, shift, and scaling
		ca_equi = CAEquivalence(2,3)
		f = ca_equi.decRule(12)
		self.assertEqual(ca_equi.allRelEquiClass(f), {68, 10, 12, 207, 80, 221, 34, 175, 48, 243, 245, 187})

	def test_countAllRelEquiClasses(self):
		# permutation, reflection, shift, and scaling
		ca_equi = CAEquivalence(2,3)
		self.assertEqual(ca_equi.countAllRelEquiClasses(), 81)

	def test_getAllRelEquiClasses(self):
		# permutation, reflection, shift, and scaling
		ca_equi = CAEquivalence(2,3)
		clazzes = ca_equi.getAllRelEquiClasses()
		self.assertEqual(len(clazzes), 81) 

	def test_diff(self):
		ca_equi = CAEquivalence(2,3)
		clazzes_1 = ca_equi.getSymClasses()
		clazzes_2 = ca_equi.getAllRelEquiClasses()
		clazzes_diff_1 = clazzes_1.difference(clazzes_2)
		clazzes_diff_2 = clazzes_2.difference(clazzes_1)
		# print(clazzes_diff_1)
		# print(clazzes_diff_2)

	def test_countIrrClasses_1(self):
		ca_equi = CAEquivalence(2,3)
		clazzes = ca_equi.getSymClasses()
		counter = 0 
		for clazz in clazzes: 
			r = ca_equi.decRule(clazz[0])
			if len(ca_equi.support(r)) == 3:
				if (len(clazz) == 4): counter += 1
		self.assertEqual(counter, 38)

if __name__ == '__main__':
	unittest.main()
