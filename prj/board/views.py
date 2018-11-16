#from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
from django.shortcuts import redirect

from django.views.generic.list import ListView

class PostDeleteView(TemplateView):
	template_name = "deleteview.html"
	def get_context_data(self, **kwargs):
		try:
			p = Post.objects.get(pk=kwargs.get('pk',None))
			return {'title': p.title, 'content': p.content, 'author': p.author}
		except ObjectDoesNotExist:
			return {'title': 'Error', 'content': None}

	def post(self, request, *args, **kwargs):
		pw = request.POST.get('pw')
		if pw:
			p = Post.objects.get(pk=kwargs.get('pk',None))
			if pw == p.pw:
				p.delete()

				return redirect("../")
			else:
				return HttpResponse("<h1>비밀번호가 틀렸습니다.</h1>\n" +
	                    '<a href="./">이전으로</a>')
		else:
			return HttpResponse("<h1>비밀번호를 입력하세요.</h1>\n" +
					'<a href="./">이전으로</a>')


class PostUpdateView(TemplateView):
	template_name = "editview.html"

	def get_context_data(self, **kwargs):
		try:
			p = Post.objects.get(pk=kwargs.get('pk',None))
			return {'title': p.title, 'content': p.content, 'author': p.author}
		except ObjectDoesNotExist:
			return {'title': 'Untilted', 'content': None}

	def post(self, request, *args, **kwargs):
		title = request.POST.get('title')
		author = request.POST.get('author')
		content = request.POST.get('content')
		pw = request.POST.get('pw')

		if title and author and content and pw :
			p = Post.objects.get(pk=kwargs.get('pk',None))
			print("Series A")
			if pw == p.pw :
				p.title = title
				p.author = author
				p.content = content
				p.save()
				return redirect(f"/{p.pk}")
			else :
				return HttpResponse("<h1>비밀번호가 틀렸습니다.</h1>\n" +
	                    '<a href="./">이전으로</a>')
		else:
			return HttpResponse("<h1>빈칸이 있습니다. 빈칸을 채워주세요.</h1>\n" +
                    '<a href="./">이전으로</a>')

class PostListView(ListView):
	model = Post
	paginate_by = 10
	template_name = "listview.html"

class DetailView(TemplateView):
	template_name = "detailview.html"
	def get_context_data(self, **kwargs):
		try:
			p = Post.objects.get(pk=kwargs.get('pk',None))
			return {'title': p.title, 'content': p.content, 'author': p.author, 'created_at': p.created_at, 'modified_at': p.modified_at}
		except ObjectDoesNotExist:
			return {'title': 'Untilted', 'content': None}

class WriteView(TemplateView):
	template_name = "create.html"
	def post(self, request, *args, **kwargs):
		title = request.POST.get('title')
		author = request.POST.get('author')
		content = request.POST.get('content')
		pw = request.POST.get('pw')

		if title and author and content and pw :
			p = Post.objects.create(
                title=title,
                author=author,
                content=content,
				pw=pw
            )
			return redirect(f"/{p.pk}")
		else:
			return HttpResponse("<h1>빈칸이 있습니다. 빈칸을 채워주세요.</h1>\n" +
                    '<a href="./">이전으로</a>')

class IndexView(TemplateView):
    template_name = "create.html"

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        if title and author and content:    # simple verification
            p = Post.objects.create(
                title=title,
                author=author,
                content=content
            )
            return redirect(f"/detail/{p.pk}")
        else:
            return HttpResponse("<h1>빈칸이 있습니다. 빈칸을 채워주세요.</h1>\n" +
                    '<a href="./">이전으로</a>')

# Create your views here.
def index(request):
	return HttpResponse("<h1>Hello World!</h1>")

def detail(request):
	template = loader.get_template(template_name='index.html')
	context = {
		'title' : 'Untitled',
		'content' : None
	}
	return HttpResponse(template.render(context,request))
