from django.shortcuts import render, redirect
import random

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
        found_money = random.randint(10, 20)
        gold += found_money
        request.session['gold'] = gold
        context = {
                'gold' : gold
            }
        return render(request, "index.html", context)
    elif request.POST['process_money_form'] == 'cave':
        found_money = random.randint(5, 10)
        gold += found_money
        request.session['gold'] = gold
        context = {
                'gold' : gold
            }
        return render(request, "index.html", context)
    elif request.POST['process_money_form'] == 'house':
        found_money = random.randint(2, 5)
        gold += found_money
        request.session['gold'] = gold
        context = {
                'gold' : gold
            }
        return render(request, "index.html", context)
    else:
        found_money = random.randint(-50, 50)
        gold += found_money
        request.session['gold'] = gold
        context = {
                'gold' : gold
            }
        return render(request, "index.html", context)