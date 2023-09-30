from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileUploadForm  # Import your form definition

# Create your views here.

def home_view(request):
    return render(request, 'index.html', {'page_title': 'Home'})

def write_view(request):
    return render(request, 'write.html', {'page_title': 'Write to AI'})

def ask_view(request):
    return render(request, 'ask.html', {'page_title': 'Ask AI'})

def docs_view(request):
    return render(request, 'docs.html', {'page_title': 'Documents'})





def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the uploaded file here
            uploaded_file = form.cleaned_data['file']
            # Process the file as needed
            # For example, you can save it to a specific location
            # with a unique name
            # file_name = 'your_logic_to_generate_unique_name'
            # with open(file_name, 'wb+') as destination:
            #     for chunk in uploaded_file.chunks():
            #         destination.write(chunk)
            
            # Redirect to a success page or return a response
            return HttpResponseRedirect('success/')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})