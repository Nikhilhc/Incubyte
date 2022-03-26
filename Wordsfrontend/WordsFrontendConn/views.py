from django.shortcuts import render
from django.views import View
from .constant import backend_server_url
from .constant import api_call


# Create your views here.

class WordsView(View):

    def get(self,request):
        params = {'id':request.GET.get('id')}
        if 'delete' in request.GET:
            output = api_call(backend_server_url+str(params['id']), method="DELETE", **params)
        output = api_call(backend_server_url, method='GET')
        context = {'output': output}
        return render(request,'Words_Sample.html',context=context)

    def post(self,request):
        word = request.POST.get('words')
        params = {'words':word}
        output = api_call(backend_server_url, method="POST", **params)
        output = api_call(backend_server_url, method='GET')
        context = {'output': output}
        return render(request, 'Words_Sample.html', context=context)

class WordsDetailView(View):

    def get(self,request,pk):
        params = {'id':pk}
        output = api_call(backend_server_url+str(pk),method='GET')
        context = {'output':output}
        return render(request,'Word_detail.html',context=context)

    def post(self,request,pk):
        word = request.POST.get('words')
        params = {'words':word}
        output = api_call(backend_server_url+str(pk), method="PATCH", **params)
        output = api_call(backend_server_url+str(pk), method='GET')
        context = {'output': output}
        return render(request, 'Word_detail.html', context=context)
