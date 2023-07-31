from django.shortcuts import render

# Create your views here.
import csv

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormInputJournal
from .models import journal

# Create your views here.
BLOG_POSTS_PER_PAGE = 25

def greetings(request):
    return render(request,'greetings.html')

def List(request):
    request.session.set_expiry(32400)
    request.session['user_sucsess'] = True
    list = journal.objects.order_by('-id')
    paginator = Paginator(list, BLOG_POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    try:
        pages0 = paginator.page(page_number)
    except PageNotAnInteger:
        pages0 = paginator.page(1)
    except EmptyPage:
        pages0 = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'pages0': pages0})

def FilterList(request):
    list_object = None
    list = None
    pages = None

    print('good')
    query_dict = request.GET
    query = query_dict.get("q")

    if query is not None:
        list_object = journal.objects.filter(Q(npp__icontains=query) |
                                                  Q(content__icontains=query) |
                                                  Q(executor__icontains=query)
                                                  )
        print('Good')

        paginator = Paginator(list_object, BLOG_POSTS_PER_PAGE)
        page_number = request.GET.get('page')
        try:
            pages = paginator.page(page_number)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

    return render(request, 'list.html', context={'list': list, "list_object": list_object, 'pages': pages})


def exportcsv(request):
    obj = journal.objects.all()
    # id_build = Building.objects.latest('id').id
    # print(id_build)
    #myFilter = exportCSV(request.GET, queryset=obj)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(['Порядковый номер','Дата регистрации приказа','Краткое содержание','Ответственный за исполнение приказа'])

    for e in obj.values_list('npp', 'dateReg','content','executor'):
        writer.writerow(e)
    return response

def Create(request):
    ls_id = journal.objects.last().id
    form = FormInputJournal(request.POST or None)
    if form.is_valid():
        try:
            instance = form.save()
            instance.npp = int(ls_id) +1
            instance.save()
            return redirect('/Регистрация приказов/Документы/')
        except Exception as e:
            print(e)
    else:
        form = FormInputJournal()
    return render(request, 'create.html', {'form': form})

def Detail(request,id):
    request.session['return_path'] = request.META.get('HTTP_REFERER', '/')

    if request.method == "GET":
        try:
            detail = journal.objects.get(id=id)
        except Exception as e:
            print(e)
    return render(request, 'detail.html',{'details': detail})


def Update(request,id):
    journals = journal.objects.get(id=id)

    form = FormInputJournal(instance=journals)
    if request.method == 'POST':
        form = FormInputJournal(request.POST or None, instance=journals)
        if form.is_valid() :
            try:
                instance = form.save()
                instance.npp = journals.id
                instance.save()
                #log = LoggerJournal(request.user, str(id))
                #log.update_record()
                return redirect(request.session['return_path'])
            except Exception as e:
                print(e)
        else:
            form = FormInputJournal()
    return render(request, 'update.html', {'form': form, 'journal': journal})


def Delete(request,id):
    pass

