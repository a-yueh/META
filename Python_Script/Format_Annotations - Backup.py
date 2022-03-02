# PYTHON script
import meta
from meta import annotations
from meta import windows
def main():
	all_windows = windows.Windows()
	
	for w in all_windows:
		print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		window_name = w.name
		annotation_settings=list()
		annotation_settings.append('title_font,Calibri,16,-1,5,75,0,0,0,0,0')
		annotation_settings.append('anchor_pointer,-10,87')
		ret = annotations.SetSettingsOfAllAnnotations(window_name, annotation_settings)
		window_annotations = annotations.AnnotationsOfWindow(window_name)
		
		for a in window_annotations:
			annotation_id = a.id
			anno_type = annotations.TypeOfAnnotationPointer(annotation_id)
			print(anno_type)
			if anno_type == 'empty':
				text = a.text
				annotation_settings.append('anchor_scrtopright,65.000000,15.000000')
				annotation_settings.append('background_color,242_204_0_252')
				ret = annotations.SetSettingsOfAnnotation(annotation_id, annotation_settings)
			else:
				if anno_type == 'element':
					text = '\$sval'
				else:
						if anno_type == 'node':
							text = '$val'
						else:
								text ='x=$x, y=$y'   
						
			annotations.SetTextOnAnnotation(a.id, text) 
			print(a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected)		 
        			 	
if __name__ == '__main__':
	main()