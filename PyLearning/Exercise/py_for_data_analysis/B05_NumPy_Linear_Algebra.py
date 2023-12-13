import numpy as np
import warnings

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.



##### Linear Algebra #####

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print('Oriented arrays:', x, y, sep='\n')

# Inner product / np.dot() / @
dotted = np.dot(x, y) # Equivalent to x.dot(y)
print('Inner prod:', dotted, sep='\n')
print('Inner prod (Use x @ y):', x @ y, sep='\n') # Inner prod symbol: @.

# numpy.linalg library.
from numpy import linalg as lag

Y = np.random.randint(-4,4,(3,3))
X = Y.T.dot(Y) # Y^TY
Q, R = lag.qr(X)
lmda, ksi = lag.eig(X)
U, S_diag, VH = lag.svd(X)
S = np.empty((3, 3), 'f')
np.fill_diagonal(S, S_diag)

try:
    lag.inv(X)
    lag.inv(Y)
except lag.LinAlgError as err:
    if 'Singular matrix' in str(err):
        print(f'|X|= {int(lag.det(X))}',
              'X^+= (Moore-Penrose pseudo-inverse)', lag.pinv(X), sep='\n')
        print(f'|Y|= {int(lag.det(Y))}',
              'Y^+= (Moore-Penrose pseudo-inverse)', lag.pinv(Y), sep='\n')
    else:
        raise
else:
    print('', 'X=', X, 'Y=', Y,
          f'|X|= {np.round(lag.det(X), 0)}',
          f'|Y|= {np.round(lag.det(Y), 0)}',
          f'diag(X)= {np.diag(X)}',
          f'tr(X)= {np.trace(X)}',
          "X^'=", lag.inv(X),
          "Y^'=", lag.inv(Y),
          'XX^{-1}=', X.dot(lag.inv(X)),
          'X=QR=', Q, '*', R,
          'λ & ξ=', lmda, ksi,
          'X=U @ S @ VH', U, '*', S, '*', VH,
          'U @ S @ VH=', np.around(lag.multi_dot([U, S, VH]), 0),
          sep='\n')

# Solve linear algebra.
A = np.random.randint(-10,10,(5,5))
b = np.random.randint(-10,10,5)
x = lag.solve(A, b)
print('', 'A=', A, 'b=', b, 'x=', x, 'Ax=', A@x, sep='\n')

# Least-squares solution.