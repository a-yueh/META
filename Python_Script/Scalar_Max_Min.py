# PYTHON script
import meta
from meta import windows
from meta import utils
 
def main():
	max = utils.MetaGetVariable('upper_limit')
	min = utils.MetaGetVariable('lower_limit')
	w = windows.ActiveWindow()
	min_scalar_limit = float(min)
	max_scalar_limit = float(max)
	print( min_scalar_limit, max_scalar_limit)
	if w:
		window_name = w.name
		print(window_name)
		windows.SetScalarLimitsOfWindow(window_name, min_scalar_limit, max_scalar_limit)	
if __name__ == '__main__':
	main()
	