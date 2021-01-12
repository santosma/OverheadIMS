from django.shortcuts import render
from .form import UploadOcrFile
from .ocr import ocr_processing

def upload_view(request):
	parsed_text = None
	if request.method == 'POST':
		form = UploadOcrFile(request.POST, request.FILES)
		if form.is_valid():	
			parsed_text = ocr_processing(request.FILES['file'])
	else:
		form = UploadOcrFile()		

	context = {
		'form' : form,
		'parsed_text' : parsed_text
	}

	return render(request, "ocrreader/upload.html", context)
