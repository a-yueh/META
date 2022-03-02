# PYTHON script
import meta
from meta import annotations
from meta import windows
from meta import utils

def main():
	
	all_windows = windows.Windows()

	model_title = utils.MetaGetVariable('model_annotation')
	w = windows.ActiveWindow()
	
	if w:
		print(w.name)
		window_name = w.name
		text = model_title
		a = annotations.CreateEmptyAnnotation(window_name, text)
		window_annotations = annotations.AnnotationsOfWindow(window_name)
		
		for a in window_annotations:
			annotation_id = a.id
			anno_type = annotations.TypeOfAnnotationPointer(annotation_id)
			print(anno_type)
			if anno_type == 'empty':
				text = a.text
				annotation_settings=list()
				annotation_settings.append('anchor_scrtopright,65.000000,15.000000')
				annotation_settings.append('background_color,242_204_0_252')
				annotation_settings.append('title_font,Calibri,16,-1,5,75,0,0,0,0,0')
				annotation_settings.append('border_color,0_0_0_0')
				ret = annotations.SetSettingsOfAnnotation(annotation_id, annotation_settings)		
				
if __name__ == '__main__':
	main()