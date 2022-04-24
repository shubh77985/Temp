from django.shortcuts import render
from main.models import Contact
from main.models import User
from main.models import Feedback


def index (request): 
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        print(name,email,phoneno)
        u=User(name=name,email=email,phoneno=phoneno)
        u.save()
    return render(request, 'main/index.html')


def project (request): 
    return render(request, 'main/project.html')

def getPredictions(Gender,SSC,HSC,Phy,Chem,Bio,Maths,NatureWork,Literacy,Living,Finance,hrs,CreativeThink,SelfLearn,Coding,Pubskill,Comp,Extracurr,Teams,Sports,ReadWrite,Subject,HWSW,gap):
    #import pickle
    return SSC
    # model = pickle.load(open("main/CareerModel.sav","rb"))
    #prediction = model.predict([[Gender,SSC,HSC,Phy,Chem,Bio,Maths,NatureWork,Literacy,Living,Finance,hrs,CreativeThink,SelfLearn,Coding,Pubskill,Comp,Extracurr,Teams,Sports,ReadWrite,Subject,HWSW,gap]])
    print(Gender,SSC,HSC)

result="fu"

def service (request): 
    result=None
    if request.method=="POST":
        Gender = request.POST['input1']
        SSC = request.POST['input2']
        HSC = request.POST['input3']
        Phy = request.POST['input4']
        Chem = request.POST['input5']
        Bio = request.POST['input6']
        Maths = request.POST['input7']
        NatureWork = request.POST['input8']
        Literacy = request.POST['input9']
        Living = request.POST['input10']
        Finance = request.POST['input11']
        hrs = request.POST['input12']
        CreativeThink = request.POST['input13']
        SelfLearn = request.POST['input14']
        Coding =request.POST['input15']
        Pubskill = request.POST['input16']
        Comp = request.POST['input17']
        Extracurr = request.POST['input18']
        Teams = request.POST['input19']
        Sports = request.POST['input20']
        ReadWrite =request.POST['input21']
        Subject = request.POST['input22']
        HWSW = request.POST['input23']
        gap = request.POST['input24']
        print(Gender,SSC,HSC,Phy,Chem,Bio,Maths,hrs,CreativeThink,SelfLearn,Coding,Pubskill,ReadWrite,gap)
        ins=Contact(Gender=Gender,SSC=SSC,HSC=HSC,Phy=Phy,Chem=Chem,Bio=Bio,Maths=Maths,NatureWork=NatureWork,Literacy=Literacy,Living=Living,Finance=Finance,hrs=hrs,CreativeThink=CreativeThink,SelfLearn=SelfLearn,Coding=Coding,Pubskill=Pubskill,Comp=Comp,Extracurr=Extracurr,Teams=Teams,Sports=Sports,ReadWrite=ReadWrite,Subject=Subject,HWSW=HWSW,gap=gap)
        ins.save()       
        result=getPredictions(Gender,SSC,HSC,Phy,Chem,Bio,Maths,NatureWork,Literacy,Living,Finance,hrs,CreativeThink,SelfLearn,Coding,Pubskill,Comp,Extracurr,Teams,Sports,ReadWrite,Subject,HWSW,gap)
        #result=SSC
        return result
    return render(request, 'main/service.html',{'result':result})

def prediction (request): 
    result=service(request)
    print("SSC",result)
    return render(request, 'main/prediction.html',{'result':result})

def contact (request): 
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        fb=Feedback(name=name,email=email,message=message)
        fb.save()
    return render(request, 'main/contact.html')

