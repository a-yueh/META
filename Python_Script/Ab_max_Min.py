# PYTHON script
import meta
from meta import utils
from meta import windows
from meta import results

def main():
	max = utils.MetaGetVariable('model')
	model_id = float(max)
	Count=0
	all_resultsets = results.Resultsets(model_id)
	for res in all_resultsets:
		Count=Count+1
	subcase_no=Count-1	
	##print(subcase_no)
	Max=utils.MetaCommand('0:function maximum perlabel scalar "1-{}"'.format(subcase_no))
	min=utils.MetaCommand('0:function minimum perlabel scalar "1-{}"'.format(subcase_no))
	max_scalar=Count 
	min_scalar=Count+1
	##print(max_scalar,min_scalar)
	utils.MetaCommand('function create scalar "Absolute_Max" "" "max(abs(s'+str(max_scalar)+'.sf),abs(s'+str(min_scalar)+'.sf))"')
	
	
if __name__ == '__main__':
	main()	