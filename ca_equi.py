import itertools as it

class CAEquivalence:

	def __init__(self, k, n):
		"""
		:param k: 	number of states
		:param n: 	number of neighbours
		""" 
		self.k = k
		self.n = n
		self.s = tuple(range(k))		# state set (0,1,..,k-1)
		self.rfl_pairs = [(self.enc(w),self.enc(w[::-1])) for w in it.product(self.s, repeat=self.n) 
			if w != w[::-1]]			# pairs (i,j), w_j = rw_i != w_i
		self.scale_nbhs = {(0,1), (1,2), (0,2)}

	def enc(self, w):
		"""
		Encodes a word (given as a list of k-symbols)
		:param w:	the word
		:return:	the encoded word as integer: w[0]*k^(n-1)+..+w[n-1] 
		"""
		v = 0
		for a in w : v = self.k*v+a
		return v

	def dec(self, s, n) :
		"""
		Decodes an integer into a list of symbols
		:param s: 	the code
		:param n: 	the length of the returned list
		:return: 	if s=a_{n-1}k^{n-1}+..+a_0 then [a_{n-1},..,a_0] is returned
		"""
		res = []
		for i in range(n):
			res.append(s%self.k)
			s //= self.k
		return res[::-1]

	def encRule(self, f):
		assert len(f) == self.k**self.n
		return self.enc(f[::-1])

	def decRule(self, f):
		return self.dec(f, self.k**self.n)[::-1]


	def reflectRule(self, f):
		"""
		Returns the reflected rule (as tuple)
		:param f:	a lcoal rule
		:return: 	the reflected rule (as tuple)
		"""
		g = list(f)					# copy f
		for (i,j) in self.rfl_pairs : g[i] = f[j]
		return tuple(g)

	def permutateRule(self, f, perm) :	# returns permutated rule
		"""
		Returns the permutated rule (as tuple)
		:param f: 		a local rule
		:param perm:	a permutation (a sequence of length k)
		:return:		the permutatad rule (as tuple)
		"""
		g = [0] * self.k**self.n
		for w in it.product(self.s, repeat=self.n) :
			g[self.enc([perm[a] for a in w])] = perm[f[self.enc(w)]]
		return tuple(g)

	def is_dependent(self, f, i):
		"""
		Does rule f depend on coordinate i?
		:param f:	a local rule
		:param i:	the coordinate of the neighborhood, 0 <= i < n
		:return:	True if f depends on i, False otherwise
		"""
		for v in it.product(self.s,repeat=self.n-1) :
			values = set()  
			for x in range(self.k) : 
				w = list(v)
				w.insert(i, x)
				#print(w, "->", self.enc(w), "->",  f[self.enc(w)])
				values.add(f[self.enc(w)])
				if len(values) > 1 :
					return True
		return False

	def support(self, f):
		"""
		Determines the support of a local rule, that is the list of dependent coordinates
		:param f:	a local rule
		:return:	the orderedlist of dependent coordinates 
		"""
		res = []
		for i in range(self.n):
			if self.is_dependent(f, i):
				res.append(i)
		return res

	def cycle(self, w, i) :   # [0,1,..,n-1]  => [n-i,..n-1,0,..n-i-1] 
		"""
		Rotates a list to the right
		:param w: 	the input list
		:param i:	the number of positions to rotate
		:return:	returns the list [w[n-i],...,w[n-1], w[0],...,w[n-i-1]]
		"""
		res = list(w[-i:])
		res.extend(w[:-i])
		return res

	def shiftRule(self, f, i):
		"""
		Shifts a rule within the neighborhood
		:param f: 	a local rule
		:param i: 	the number of positions to shift (the shifted rule must be within the neighbourhood)
		:return:	the shifted rule that is shift-equivalent to f
		"""
		g = [0] * self.k**self.n
		for v in it.product(self.s, repeat=self.n) :
			w = self.cycle(v,i) 
			g[self.enc(w)] = f[self.enc(v)]
		return g

	def symClass(self, f):
		"""
		Determines the equivalence class of a rule based on reflection and permuation (the symmetry transformations)
		:param f:	a local rule
		:return:	the equivalence class as tuple, that is the set of reflected and permutated rules (and their 
					combination)
		"""
		c = set()
		for perm in it.permutations(self.s) :
			pf = self.permutateRule(f,perm)
			c.update({self.encRule(pf), self.encRule(self.reflectRule(pf))})
		return tuple(sorted(c))

	def shiftClass(self, f):
		"""
		Determines the equivalence class of a rule based on and only on shift-equivalence
		:param f:	a local rule
		:return:	the equivalence class as set
		""" 
		res = set()
		res.add(self.enc(f))
		supp = self.support(f)
		if supp == [] : return res
		for i in range(supp[0]) :
			g = self.shiftRule(f,-i-1)
			res.add(self.enc(g))
		for i in range(supp[-1]+1, self.n) :
			g = self.shiftRule(f,self.n-i) 
			res.add(self.enc(g))
		return res

	def shiftSymClass(self, f) :
		"""
		Determines the equivalence class of a rule based on shift, reflection, and permutation
		:param f:	a local rule
		:return:	the equivalence class as set
		"""
		res = set(self.symClass(f))
		supp = self.support(f)
		if len(supp) == 0 or len(supp) == self.n : 
			return res
		res.update(self.symClass(f))
		for i in range(supp[0]) : 
			g = self.shiftRule(f,-i-1)
			res.update(self.symClass(g))
		for i in range(supp[-1]+1, self.n) :
			g = self.shiftRule(f,self.n-i)
			res.update(self.symClass(g))
		return res

	def countSymClasses(self):
		"""
		Determines the number of equivalence classes based on reflection and permutation
		:return:	the number of equivalence classes
		"""
		processed = set() 			# keep track of processed rules
		count = 0
		for f in it.product(self.s,repeat=self.k**self.n) :
			if self.encRule(f) not in processed:
				count += 1
				processed.update(self.symClass(f))
		return count

	def getSymClasses(self):
		"""
		Determines the equivalence classes based on reflection and permutation
		:return:	the number of equivalence classes
		"""
		processed = set() 			# keep track of processed rules
		res = set()
		count = 0
		for f in it.product(self.s,repeat=self.k**self.n) :
			if self.encRule(f) not in processed:
				count += 1
				clazz = self.symClass(f)
				processed.update(clazz)
				res.add(tuple(sorted(clazz)))
		return res



	def countShiftSymClasses(self):
		"""
		Determines the number of equivalence classes based on shift, reflection, and permutation
		:return:	the number of equivalence classes
		"""
		processed = set() 			# keep track of processed rules
		count = 0
		for f in it.product(self.s,repeat=self.k**self.n) :
			if self.encRule(f) not in processed:
				count += 1
				processed.update(self.shiftSymClass(f))
		return count

	def getShiftSymClasses(self):
		"""
		Determines the number of equivalence classes based on shift, reflection, and permutation
		:return:	the list of equivalence classes
		"""
		processed = set() 			# keep track of processed rules
		res = []
		count = 0
		for f in it.product(self.s,repeat=self.k**self.n) :
			if self.encRule(f) not in processed:
				count += 1
				cls = self.shiftSymClass(f)
				processed.update(cls)
				res.append(cls)			
		return res

	def minRule(self, f):
		"""
		Determines the local rule on the support
		:param f:	a local rule
		:return:	the local rule on the support
		"""
		supp = self.support(f)
		m = len(supp)
		g = [0] * self.k**m
		cfg_f = [0] * self.n
		for cfg_g in it.product(self.s,repeat=m):
			for i in range(m):
				cfg_f[supp[i]] = cfg_g[i]
				g[self.enc(cfg_g)] = f[self.enc(cfg_f)]
		return g

	def moveRule(self, f, nbh):
		"""
		Moves a rule to a different neighbourhood
		:param f:		a local rule with neighbourhood [0,1,..,m-1], m <= n
		:param nbh:		the new neighbourhood [i_0,..,i_{m-1}]
		:return:		the local rule f applied to the new neighbourhood
		"""
		g = [0] * self.k**self.n
		for cfg_g in it.product(self.s, repeat=self.n):
			cfg_f = []
			for i in nbh:
				cfg_f.append(cfg_g[i])
			v = f[self.enc(cfg_f)]
			g[self.enc(cfg_g)] = v
		return tuple(g) 

	def scaleClass(self, f): 
		"""
		Determines the equivalence class of a rule based on scaling. 
		If the local rule can be scaled, shifting is also included
		:param f:	a local rule
		:return:	the equivalence class
		"""
		res = {tuple(f)}
		supp = self.support(f)
		if tuple(supp) in self.scale_nbhs:
			f_min = self.minRule(f)
			for nbh in self.scale_nbhs:
				res.add(self.moveRule(f_min, nbh))
		return res

	def allRelEquiClass(self, f) :
		"""
		Determines the equivalence class of a rule based on scaling, shift, reflection, and permutation
		:param f:	a local rule
		:return:	the equivalence class as set
		"""
		scaled = self.scaleClass(f)
		res = set()
		for f in scaled:
			res.update(self.shiftSymClass(f))
		return res

	def encRuleSeq(self, rules):
		return {self.encRule(rule) for rule in rules}

	def countAllRelEquiClasses(self):
		"""
		Determines the number of equivalence classes based on shift, reflection, and permutation
		:return:	the number of equivalence classes
		"""
		processed = set() 			# keep track of processed rules
		count = 0
		for f in it.product(self.s,repeat=self.k**self.n) :
			if self.encRule(f) not in processed:
				count += 1
				processed.update(self.allRelEquiClass(f))
		return count

	def getAllRelEquiClasses(self):
		"""
		Determines the equivalence classes based on shift, reflection, and permutation
		:return:	the equivalence classes
		"""
		processed = set() 			# keep track of processed rules
		res = set()
		count = 0
		for f in it.product(self.s,repeat=self.k**self.n) :
			if self.encRule(f) not in processed:
				count += 1
				clazz = self.allRelEquiClass(f)
				processed.update(clazz)
				res.add( tuple(sorted(clazz)) )
		return res
