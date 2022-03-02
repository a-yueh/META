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
		##window_name = guitk.UserInput("Enter window name")       
		utils.MetaCommand('xyplot curve rfunction integr "'+window_name+'" '+ID+'')
 
if __name__ == '__main__':
                main()
