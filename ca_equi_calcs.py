# contains the calculations

import math
from enum import Enum


def num_supp(n):
	res = 0
	for i in range(n+1):
		res += (-1)**(n-i) * math.comb(n,i) * 2**(2**i)
	return res

class Type(Enum):
	T_1 = 0
	T_c = 1
	T_r = 2
	T_cr = 3
	T_c_r = 4

def num_orbits(t, n):
	m = n//2 
	if n==0: 
		if (t == Type.T_r): return 1 # constant functions form 1 orbit of type r
		else: return 0
	if t == Type.T_1:
		if n%2 == 0: return orbit_type_s2r_even_1(m) 
		else: return orbit_type_s2r_odd_1(m)
	if t == Type.T_c:
		if n%2 == 0: return orbit_type_s2r_even_01(m) 
		else: return orbit_type_s2r_odd_01(m)
	if t == Type.T_r:
		if n%2 == 0: return orbit_type_s2r_even_r(m) 
		else: return orbit_type_s2r_odd_r(m)
	if t == Type.T_cr:
		if n%2 == 0: return 0 
		else: return orbit_type_s2r_odd_01r(m)
	if t == Type.T_c_r:
		if n%2 == 0: return 0
		else: return orbit_type_s2r_odd_s2r(m)

def num_all_orbits(n):
	m = n//2
	if n%2 == 0: return orbit_count_s2r_even(m)
	else: return orbit_count_s2r_odd(m)


def orbit_count_s2r_odd (m) : 
	return ( 2* 2**2**(2*m) + 2**(2**m*(2**m+1)) + 2**2**(2*m+1) ) / 4

def orbit_count_s2r_even(m) : 
	return ( 2**(2**(m-1)*(2**m +1)) + 2**2**(2*m-1) + 2**2**(2*m) ) / 4

def orbit_type_s2r_odd_s2r(m) :
	return 2**(2**(m-1)*(2**m+1))

def orbit_type_s2r_odd_01(m) : 
	return ( 2**(2**(2*m)) - 2**(2**(m-1)*(2**m+1)) ) / 2

def orbit_type_s2r_odd_01r(m) : 
	return ( 2**(2**(2*m)) - 2**(2**(m-1)*(2**m+1)) ) / 2

def orbit_type_s2r_odd_r(m) : 
	return ( 2**(2**m * (2**m + 1)) - 2**(2**(m-1)*(2**m+1)) ) / 2

def orbit_type_s2r_odd_1(m) : 
	return (2**(2**(2*m+1)) + 2 * 2**(2**(m-1)*(2**m+1)) - 2 * 2**(2**(2*m)) 
  		- 2**(2**m * (2**m + 1)) ) / 4

def orbit_type_s2r_even_01(m) : 
	return 2**(2**(2*m-1)) / 2

def orbit_type_s2r_even_r(m) : 
	return 2**(2**(m-1)*(2**m+1)) / 2

def orbit_type_s2r_even_1(m) : 
	return ( 2**(2**(2*m)) -2**(2**(2*m-1)) -  2**(2**(m-1)*(2**m+1)) ) / 4 

def num_irreducible(n):
	res = 0
	for i in range (n+1):
		res += (-1)**(n-i) * math.comb(n,i) * 2**(2**i)
	return res

def alpha(n,m): 
	if n%2 == 0 and m%2 == 1: return 0
	else: return math.comb(n//2, m//2)

def beta(n,m):
	return math.comb(n,m) - alpha(n,m)

def num_orbits_irr(t, n):
	if t == Type.T_c_r: return num_orbits_irr_c_r(n) 
	if t == Type.T_r: return num_orbits_irr_r(n) 
	if t == Type.T_cr: return num_orbits_irr_cr(n) 
	if t == Type.T_c: return num_orbits_irr_c(n) 
	if t == Type.T_1: return num_orbits_irr_1(n) 

def num_orbits_irr_c_r(n):
	res = num_orbits(Type.T_c_r, n)
	for m in range(n):
		res -= alpha(n,m) * num_orbits_irr(Type.T_c_r, m)
	return res

def num_orbits_irr_r(n):
	res = num_orbits(Type.T_r, n)
	for m in range(n):
		res -= alpha(n,m) * num_orbits_irr(Type.T_r, m)
	return res

def num_orbits_irr_c(n):
	res = num_orbits(Type.T_c, n)
	for m in range(n):
		res -= math.comb(n,m) * num_orbits_irr(Type.T_c, m)
		res -= 1/2 * beta(n,m) * num_orbits_irr(Type.T_c_r, m)
	return res

def num_orbits_irr_cr(n):
	res = num_orbits(Type.T_cr, n)
	for m in range(n):
		res -= alpha(n,m) * num_orbits_irr(Type.T_cr, m)
	return res

def num_orbits_irr_1(n):
	res = num_orbits(Type.T_1, n)
	for m in range(n):
		res -= math.comb(n,m) * num_orbits_irr(Type.T_1, m)
		res -= 1/2 * beta(n,m) * (num_orbits_irr(Type.T_r, m) + num_orbits_irr(Type.T_cr, m))
	return res

def num_all_orbits_irr(n):
	return num_orbits_irr(Type.T_c_r, n) + num_orbits_irr(Type.T_cr, n) + num_orbits_irr(Type.T_c, n) + num_orbits_irr(Type.T_r, n) + num_orbits_irr(Type.T_1, n)
