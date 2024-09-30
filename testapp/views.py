from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import MarkdownFile
import markdown

# Create your views here.

def test(request):
    files = MarkdownFile.objects.all()
 
    if request.method == "POST":
        filename = request.POST.get("title")
        content = request.POST.get("content")
        file = MarkdownFile.objects.create(file_name=filename, content=content)
        file.save()
    return render(request,"slide_form.html",{"files":files})


def slide_form_view(request, file_id):
 
    markdown_content = get_object_or_404(MarkdownFile, id=file_id)
   
    file_name = markdown_content.file_name
    content = markdown_content.content
    slides = content.split("---")
    total_slides=[]
    for slide in slides:
        html_content = markdown.markdown(slide)
        total_slides.append(html_content)
   
   
    return render(request, 'slide_presentation.html', {'file_name':file_name,'slides': total_slides})


def update(request,file_id):
    file = get_object_or_404(MarkdownFile, id=file_id)
    if request.method == "POST":
        file.file_name = request.POST.get("title")
        file.content = request.POST.get("content")
        file.save()

    return redirect("/")


def delete(request,file_id):
    file = get_object_or_404(MarkdownFile, id=file_id)
    file.delete()

    return redirect("/")