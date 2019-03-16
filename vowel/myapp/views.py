from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import re
import os
def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fname = myfile.name
        print(fname)
        fname=fname.replace(" ","_")
        print(fname)
        filename = fs.save(fname, myfile)
        uploaded_file_url = fs.url(filename)
        filepath=settings.BASE_DIR+uploaded_file_url
        print(filepath)
        full_text=open(filepath,'r',encoding='utf8')

        text=[",".join(final3 for final3 in full_text)]
        text=text[0]
        total_num_vovels=len(re.findall("[aeoiu]",text))

        A_for=len(re.findall('a',text))
        E_for=len(re.findall('e',text))
        I_for=len(re.findall('i',text))
        O_for=len(re.findall('o',text))
        U_for=len(re.findall("u",text))

        return render(request,'home.html',{'filename':fname,'uploaded_file_url': uploaded_file_url,'total_num_vovels':total_num_vovels,'A_for':A_for,'E_for':E_for,'I_for':I_for,'O_for':O_for,"U_for":U_for})
    return render(request,'home.html')
#

def about(request):
    return render(request,"about.html")
