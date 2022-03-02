import meta     
from meta import utils  
from meta import windows
def main():     
	model_1 = utils.MetaGetVariable('geo_1')       
	result_1 = utils.MetaGetVariable('fat_1')      
	utils.MetaCommand('read geom Nastran "'+model_1+'"')   
	utils.MetaCommand('read onlyfun fefatigue "'+result_1+'" all GeneralResult,Damage,MaxofTopBottom')     
	       
	window_name = 'Window1'
	w = windows.Create3DWindow(window_name)
	w = windows.ActivateWindow(window_name)
	model_2 = utils.MetaGetVariable('geo_2')       
	result_2 = utils.MetaGetVariable('fat_2')      
	utils.MetaCommand('read geom Nastran "'+model_2+'"')   
	utils.MetaCommand('read onlyfun fefatigue "'+result_2+'" all GeneralResult,Damage,MaxofTopBottom')     
	       
	window_name = 'Window2'
	w = windows.Create3DWindow(window_name)
	w = windows.ActivateWindow(window_name)
	model_3 = utils.MetaGetVariable('geo_3')       
	result_3 = utils.MetaGetVariable('fat_3')      
	utils.MetaCommand('read geom Nastran "'+model_3+'"')   
	utils.MetaCommand('read onlyfun fefatigue "'+result_3+'" all GeneralResult,Damage,MaxofTopBottom')     
	       
	       
if __name__ == '__main__':      
                main()