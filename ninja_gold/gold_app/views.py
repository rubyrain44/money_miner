from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'gold' in request.session:
        gold = request.session['gold']
        context = {
            'gold' : gold
        }
    else:
        request.session['gold'] = 0
        context = {
            'gold' : request.session['gold']
        }
    return render(request, "index.html", context)

def process(request):
    gold = request.session['gold']
    if request.POST['process_money_form'] == 'farm':
        pass
    elif request.POST['process_money_form'] == 'cave':
        pass
    elif request.POST['process_money_form'] == 'house':
        pass
    else:
        pass
    return redirect('/')