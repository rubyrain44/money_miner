from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    turns = 20
    print('a')
    if 'turns' in request.session:
        turns = request.session['turns']
        print(turns)
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
    # print(request.session['turns'])
    if request.POST['process_money_form'] == 'farm':
        found_money = random.randint(10, 20)
        gold += found_money
        request.session['gold'] = gold
        # request.session['turns'] -= 1
        context = {
                'gold' : gold,
                'activity' : f"You found {found_money} gold from the farm!"
            }
        return render(request, "index.html", context)
    elif request.POST['process_money_form'] == 'cave':
        found_money = random.randint(5, 10)
        gold += found_money
        request.session['gold'] = gold
        context = {
                'gold' : gold,
                'activity' : f"You found {found_money} gold from the cave!"
            }
        return render(request, "index.html", context)
    elif request.POST['process_money_form'] == 'house':
        found_money = random.randint(2, 5)
        gold += found_money
        request.session['gold'] = gold
        context = {
                'gold' : gold,
                'activity' : f"You found {found_money} gold from the house!"
            }
        return render(request, "index.html", context)
    else:
        found_money = random.randint(-50, 50)
        gold += found_money
        request.session['gold'] = gold
        if found_money > 0:
            context = {
                    'gold' : gold,
                    'activity' : f"You won {found_money} gold from the casino!"
                }
        else:
            context = {
                'gold' : gold,
                'activity' : f"You lost {found_money} gold from the casino. Whomp whomp."
            }
        return render(request, "index.html", context)