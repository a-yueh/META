# PYTHON script
import meta
from meta import plot2d
from meta import windows
from meta import utils

def main():
	title_name = utils.MetaGetVariable('enter_plot_title')
	w = windows.ActiveWindow()
	if w:
		window_name = w.name
		plot_id = 0
		title = title_name
		plot2d.SetTitleOfPlot(window_name, plot_id, title)


if __name__ == '__main__':
	main()