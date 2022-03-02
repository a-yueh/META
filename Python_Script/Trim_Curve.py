# PYTHON script
import meta
from meta import utils
from meta import windows

def main():
	
	w = windows.ActiveWindow()
	
	if w:
		print(w.name)
		window_name = w.name
		max = utils.MetaGetVariable('Xmin')
		min = utils.MetaGetVariable('Xmax')
		ID = utils.MetaGetVariable('CurveID')
		utils.MetaCommand('xyplot range set "'+window_name+'" '+max+'. '+min+'.')
		utils.MetaCommand('xyplot curve function userdef "Trim-Curve ID'+ID+'" "c'+ID+'.x" "c'+ID+'.y" "'+window_name+'"')
		utils.MetaCommand('xyplot range disable '+window_name+'')

if __name__ == '__main__':
	main()