from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse

# Imaginary function to handle an uploaded file.
from .controller import handle_uploaded_file

# import logging
# logger = logging.getLogger('development')

def success(request):
    return render(request, 'fileupload/success.html')

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = request.FILES['file']
            # logger.info(file_obj.name)
            handle_uploaded_file(file_obj)
            return HttpResponseRedirect('/fileupload/success/')
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/index.html', {'form': form})
