# PYTHON script
import meta
from meta import utils
from meta import windows

def main():
	
	w = windows.ActiveWindow()
	
	if w:
		print(w.name)
		window_name = w.name
		ID = utils.MetaGetVariable('CurveIDs')
		utils.MetaCommand('xyplot curve rfunction differ forward "'+window_name+'" '+ID+'')
		utils.MetaCommand('xyplot curve rfunction differ forward "'+window_name+'" '+ID+'')
		utils.MetaCommand('xyplot curve rfunction scale y "'+window_name+'" "'+ID+'" 101.971621')


if __name__ == '__main__':
	main()		