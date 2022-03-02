# PYTHON script
import meta
from meta import windows
from meta import plot2d
from meta import utils
def main():
	y_label = utils.MetaGetVariable('plot_y_axis_label')
	w = windows.ActiveWindow()
	if w:
		print(w.name)
		window_name = w.name
		plot_id = 0
		axis_type = 'yaxis'
		axis_id = 0
		axis_label = y_label
		plot2d.SetLabelOfPlotAxis(window_name, plot_id, axis_type, axis_id, axis_label) 
		
if __name__ == '__main__':
	main()