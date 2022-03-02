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
		utils.MetaCommand('xyplot curve select "'+window_name+'" "'+ID+'"')
		utils.MetaCommand('xyplot curve rfunction differ forward "'+window_name+'" '+ID+'')
		utils.MetaCommand('xyplot curve rfunction differ forward "'+window_name+'" '+ID+'')
		
if __name__ == '__main__':
	main()				