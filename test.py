import doctest
def newton_raphson(f, x0, TOL = 1e-5):
	'''Computes the zero of a function using the newton raphson method
	Args:
		func f
		float x0
	Returns:
		float x
	Examples:
	>>> abs(newton_raphson(lambda x: x*x-9, 2)-3)<1e-5
	True
	'''
	def _deriv(func, xval, tol = 1e-4):
		'''Returns the derivative of a given function

			Inputs:
			f - function
			x - value at which derivative should be computed
			h - infinitesimal step, used for derivative computation
				default value is 1e-4
		'''
		return (func(xval + tol) - func(xval))/tol

	x = x0
	while abs(f(x))>TOL:
		x = x - (f(x) / _deriv(tol = 1e-5, xval = x, func = f))
	return x

if __name__ == '__main__':
	doctest.testmod(verbose = True)
	print(newton_raphson(lambda x: x * x - 9, 2))