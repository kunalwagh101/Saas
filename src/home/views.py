from django.http import HttpResponse 
from django.shortcuts import render
import pathlib
import os
home_folder = pathlib.Path(__file__).resolve().parent
file_path  = os.path.dirname(os.path.abspath(__file__))

def inhome(request,*args ,**kwargs):
    new_path =  home_folder/"home.html"

    # loc =  "".join(file_path,"home.html")
    # print("loc", loc)

    # print("Current Working Directory:", os.getcwd())
    # print("__file__:", __file__)
    # print("Script Directory:", os.path.dirname(os.path.abspath(__file__)))
    # value =  new_path.read_text()
    # print("hoime_folder = ","file_path=",file_path,new_path,flush=True)
    # new_path  = os.path.dirname(os.path.abspath(__file__))
    # new_file =  os.path.join(new_path,"home.html")

    # with open(new_file, "r",encoding='utf-8') as file :
    #     content = file.read()
    # print(new_file,"new_file")
    context  = { "value":"5o" }
    var  = "chome.html"
    return render(request , var , context)


