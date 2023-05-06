# Level 5a
# Question:
# Given the sizes of a grid and the number of states possible in a cell,
# return the number of non-equivalent tables.
# Equavilent: can be obtained by exchanging rows or columns as much as we want

#!/usr/bin/env python2.7

from fractions import Fraction
from fractions import gcd
import math

def set_partition(n):
    partitions = []

    for i in range(n):
        part = [[i+1]]
        for j in range(i):
            for k in partitions[j]:
                p = [i-j] + k
                p.sort(reverse=True)
                if p not in part:
                    part.append(p)
        partitions.append(part)

    return partitions[n-1]

def calc_term_coeff(c, n_fact):
    # Formula is given here: https://groupprops.subwiki.org/wiki/Conjugacy_class_size_formula_in_symmetric_group
    denominator = 1
    for i in range(len(c)):
        if i == c.index(c[i]):
            count = c.count(c[i])
            denominator *= math.factorial(count) * (c[i] ** count)
    return Fraction(n_fact, denominator)

def cycle_index(n):
    '''
    This calculates the cycle index of a symmetric group: https://en.wikipedia.org/wiki/Cycle_index#Symmetric_group_Sn
    Rows and columns are SYMMETRIC GROUPs "whose elements are all the bijections from the set to itself,
    and whose group operation is the composition of functions". See https://en.wikipedia.org/wiki/Symmetric_group for details.
    First five indexes are given here: http://mathworld.wolfram.com/SymmetricGroup.html
    '''
    n_fact = math.factorial(n)

    # Find the general coefficient: Divide the whole equation by 1/n!
    coefficient = Fraction(1, n_fact)

    # Find the cycles: https://en.wikipedia.org/wiki/Partition_of_a_set
    cycles = set_partition(n)

    # Find the each term coefficient multiplied by the general coefficient
    coeffs = []
    for c in cycles:
        coeffs.append(calc_term_coeff(c, n_fact) * coefficient)

    return [cycles, coeffs]

def cycle_index_for_matrix(row_ci, col_ci):
    # Formula given here: https://math.stackexchange.com/a/2114252
    terms = []
    coeffs = []

    for row_coeff, row_cycle in zip(row_ci[1], row_ci[0]):
        for col_coeff, col_cycle in zip(col_ci[1], col_ci[0]):

            # Calculate the coeff for each pair
            coeff = row_coeff * col_coeff
            coeffs.append(coeff)

            # Calculate the term for each pair
            term = []
            for l1_i in range(len(row_cycle)):
                if l1_i == row_cycle.index(row_cycle[l1_i]):
                    # Get the each variable in term
                    l1 = row_cycle[l1_i]
                    count1 = row_cycle.count(l1)

                    for l2_i in range(len(col_cycle)):
                        if l2_i == col_cycle.index(col_cycle[l2_i]):
                            # Get the each variable in 2nd term
                            l2 = col_cycle[l2_i]
                            count2 = col_cycle.count(l2)

                            # Calculate new variable
                            lcm = (l1*l2) // gcd(l1, l2)
                            count = (l1*l2*count1*count2) // lcm

                            # Add new variable to the term
                            cycles = [lcm] * count
                            term += cycles

            # Append new term into the equation
            # There might be the same term occuring more than once...
            # It's no problem for these calculations. No need to add up.
            terms.append(term)
        
    return [terms, coeffs]

def calc_index(cycle_index, states):
    total = 0

    for coeff, cycle in zip(cycle_index[1], cycle_index[0]):
        total += coeff * (states ** len(cycle))

    return total

def solution(w, h, s):

    # Step 1: Calculate the cycle indexes for the set of rows and columns
    row_ci = cycle_index(w)
    col_ci = cycle_index(h)
    
    # Step 2: Calculate the cycle index for the matrix
    matrix_ci = cycle_index_for_matrix(row_ci, col_ci)
    
    # Step 3: Plug the number of states into the equation
    count = calc_index(matrix_ci, s)

    return str(count)


### TEST CASES ###
print(solution(2, 2, 2)) #7
print(solution(2, 3, 4)) #430
print(solution(3, 3, 3)) #738
