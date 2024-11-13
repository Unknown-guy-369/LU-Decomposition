# To print L and U matrix
import numpy as np
#add the library to import lu
A = np.array(eval(input()))
#add the code to get the L and U matrix
import numpy as np
from scipy.linalg import lu
matrix=np.array(eval(input()))
piv,l_matrix,u_matrix=lu(matrix)
print(l_matrix)
print(u_matrix)


# To print X matrix (solution to the equations)
import numpy as np
#add the library to import lu_factor, lu_solve
A = np.array(eval(input()))
b = np.array(eval(input()))
#add the code to get the solution of the matrix
import numpy as np
from scipy.linalg import lu_factor,lu_solve
matrix=np.array(eval(input()))
b=np.array(eval(input()))
x=lu_factor(matrix)
solution=lu_solve(x,b)
print(solution)