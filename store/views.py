from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from store.forms import ProfileForm
from store.models import Category, Heri, Heritage, Product, Profile, Tradition, tradi
from django.contrib.auth.decorators import login_required

def home(request):
    trending_products= Product.objects.filter(trending=1)
    trending_heritages=Heri.objects.filter(trending=1)
    context={
        'trending_products':trending_products,
        'trending_heritages':trending_heritages
    }
    return render(request, "store/index.html", context)

def collections(request):
    category = Category.objects.filter(status=0)
    context={
        'category':category
    }
    return render(request, 'store/collections.html',context)

def heritages(request):
    heritages = Heritage.objects.filter(status=0)
    context={
        'heritages':heritages
    }
    return render(request, 'store/heritages.html',context)

def traditions(request):
    traditions = Tradition.objects.filter(status=0)
    context={
        'traditions':traditions
    }
    return render(request, 'store/traditions.html',context)

def collectionsview(request, slug):
    if Category.objects.filter(slug=slug, status=0).exists():
        products = Product.objects.filter(category__slug=slug)

        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        if min_price:
            products = products.filter(selling_price__gte=min_price)
        if max_price:
            products = products.filter(selling_price__lte=max_price)

        category = Category.objects.get(slug=slug)
        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')
    
def heritagesview(request, slug):
    if Heritage.objects.filter(slug=slug, status=0).exists():
        heri = Heri.objects.filter(heritage__slug=slug)


        heritages = Heritage.objects.get(slug=slug)
        context = {
            'heri': heri,
            'heritages': heritages,
        }
        return render(request, 'store/heritages/index.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('heritages')
    
def traditionsview(request, slug):
    if Tradition.objects.filter(slug=slug, status=0).exists():
        tradi_p = tradi.objects.filter(tradition__slug=slug)


        traditions = Tradition.objects.get(slug=slug)
        context = {
            'tradi_p': tradi_p,
            'traditions': traditions,
        }
        return render(request, 'store/traditons/index.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('traditions')
    

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()

            context={
                'products':products
            }
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
        
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    
    return render(request,'store/products/view.html', context)   

def heriview(request, heritages_slug, heri_slug):
    if(Heritage.objects.filter(slug=heritages_slug, status=0)):
        if(Heri.objects.filter(slug=heri_slug, status=0)):
            heri = Heri.objects.filter(slug=heri_slug, status=0).first()
            context={
                'heri':heri
            }
        else:
            messages.error(request, "No such product found")
            return redirect('heritages')
        
    else:
        messages.error(request, "No such category found")
        return redirect('heritages')
    
    return render(request,'store/heritages/view.html', context)  

def tradview(request, traditions_slug, tradi_p_slug):
    if(Tradition.objects.filter(slug=traditions_slug, status=0)):
        if(tradi.objects.filter(slug=tradi_p_slug, status=0)):
            tradi_p = tradi.objects.filter(slug=tradi_p_slug, status=0).first()
            context={
                'tradi_p':tradi_p
            }
        else:
            messages.error(request, "No such product found")
            return redirect('traditions')
        
    else:
        messages.error(request, "No such category found")
        return redirect('traditions')
    
    return render(request,'store/traditons/view.html', context)    
    
def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productslist = list(products)
    
    return JsonResponse(
        productslist, safe=False)

def searchproduct(request):
    if request.method == "POST":
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()
            
            
            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
            
        
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        # Assuming you have a form to handle profile updates
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')  # redirect to a success page
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'store/update_profile.html', {'form': form})

def productcatg(request, data=None):
    if data == None:
        filt=Product.objects.filter()
        