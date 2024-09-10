from django.shortcuts import render

# Create your views here.

def set(request):
    data=render (request,'set.html')
    data.set_cookie('name','surya', max_age=5*24*60*60, httponly= True, secure=True)
    data.set_cookie('age','24',max_age=4*24*60*60,httponly= True ,secure=True)
    data.set_cookie('city','bhopal',max_age=3*24*60*60,httponly= True, secure=True)
    return data
    
    
    
def get(request):
    print(request.COOKIES)
    nm=request.COOKIES['name']
    ag=request.COOKIES['age']
    ct=request.COOKIES['city']
    data= {
        'name':nm,
        'age':ag,
        'city':ct
    }
    return render(request,'get.html',data)

def delete(request):
    data= render(request,'delete.html')
    data.delete_cookie('name')
    data.delete_cookie('age')
    data.delete_cookie('city')
    return data
    