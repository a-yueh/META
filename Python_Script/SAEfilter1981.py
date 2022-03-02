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
		utils.MetaCommand('unitsystem apply mmkms')
		utils.MetaCommand('xyplot curve rfunction saefilter1981 60channelclass "'+window_name+'" '+ID+'')

if __name__ == '__main__':
	main()		