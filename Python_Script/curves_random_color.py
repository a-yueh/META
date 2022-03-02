import meta
from meta import windows
from meta import plot2d
from random import randint
w = windows.ActiveWindow()
window_name = w.name
print(window_name)
plot_curves = plot2d.CurvesOfWindow(window_name)
for c in plot_curves :
	print(c.id, c.name, c.plot_id)
	curve_id = c.id
	red = randint(0, 255)
	green = randint(0, 255)
	blue = randint(0, 255)
	alpha = randint(0, 255)
	plot2d.SetColorOfCurve(window_name, curve_id, red, green, blue, alpha)