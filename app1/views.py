from django.shortcuts import render,redirect

# Create your views here.
from app1.models import Movie

from app1.forms import MovieForm
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})

class Index(ListView):
    model=Movie
    template_name = "home.html"
    context_object_name = "movie"

    def get_queryset(self):
        qs=super().get_queryset()
        # queryset=qs.filter(title__icontains="Thunder")
        queryset = qs.filter(year__lt=2020)
        return queryset

        #lookups - icontains,contains,gt,lt,startswith

        #get_context_data or extra_context
    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['name']="abhishek"
    #     context['age']=21
    #     return context

    extra_context={'name':'abhishek','age':21}

# def addmovies(request):#form using built in function
#     if(request.method=="POSt"):
#
#         form=MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     form=MovieForm() #empty form object is created
#     context={'form':form}
#     return render(request,'add1.html',context)

# def addmovies(request):#form using built in function
#     if(request.method=="POSt"):
#         name=request.POST.get('name')
#         desc=request.POST.get('desc')
#         year=request.POST.get('year')
#         img=request.Files['img']
#         movie=Movie(name=name,desc=desc,year=year,img=img)
#         movie.save()
#         return redirect("/")
#         return render(request,'add1.html')

class Addmovie(CreateView):
    model = Movie
    fields = ['title','description','year','language','image']
    template_name = 'add.html'
    success_url = reverse_lazy('app1:home')

# def add(request):
#     if(request.method=="POST"):
#         t = request.POST['title']
#         d = request.POST['description']
#         y = request.POST['year']
#         l = request.POST['language']
#         i = request.FILES.get('image')
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')
#
# def detail(request,i):
#     k=Movie.objects.get(id=i)
#     return render(request,'detail.html',{'movie':k})
#

class Detail(DetailView):
    model=Movie
    template_name='detail.html'
    context_object_name="movie"



# def delete(request,i):
#     k=Movie.objects.get(id=i)
#     k.delete()
#     return redirect(reverse_lazy('app1:home'))
class Delete(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url=reverse_lazy('app1:home')

class Update(UpdateView):
    model = Movie
    fields = ['title','description','year','language','image']
    template_name = 'edit.html'
    success_url = reverse_lazy('app1:home')

# def edit(request,i):
#     k = Movie.objects.get(id=i)
#     if(request.method=="POST"):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES.get('i')
#         k.save()
#         # return home(request)
#     return render(request,'edit.html',{'movie':k})