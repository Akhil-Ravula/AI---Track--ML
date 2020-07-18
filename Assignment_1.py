from scipy.optimize import linprog
obj = [-50 , -120]
lhs_eq = [[7000 , 2000] , [10 , 30]]
rhs_eq = [700000 , 1200]
bnd = [(0 , float("inf")) , (0 , float("inf"))]
opt = linprog(c = obj , A_ub = lhs_eq , b_ub = rhs_eq , bounds = bnd , method = "simplex")
opt