from django.shortcuts import render, redirect
from .models import Contributions, Loans, WholeAccounts
from django.contrib import messages
import datetime
from django.db import connection
from django.db.models import Sum

def new(request):
    contribution = Contributions.objects.count()
    result = Contributions.objects.aggregate(sum_of_ab=Sum("amount_contributed"))
    return render(request, 'index1.html', {'number':contribution, 'result':result['sum_of_ab']})


def new_table(request):
    contribution = Contributions.objects.all()
    return render(request,  'table-basic.html', {'contribution':contribution})




def addmember(request):
    if request.method == "POST":
        name= request.POST['Name']
        amount =request.POST['amount']
        if Contributions.objects.filter(name=name).exists():
            obj1 = Contributions.objects.get(name = name)
            obj1.amount_contributed =str( int(obj1.amount_contributed) + int(amount))
            obj1.save()
        else:
            now=datetime.datetime.now()
            format_date= datetime.datetime.strftime(now, '%Y-%m-%d')
            obj = Contributions.objects.create(name=name, amount_contributed=amount, date=format_date)
            obj.save()
        messages.info(request, "saved successfully")
        return redirect('/')
    else:
        return render(request, 'addmember.html')

def deletemember(request):
    if request.method == "POST":
        name= request.POST['Name']
        try:
            obj=Contributions.objects.get(name=name)
            obj.delete()
            return redirect('/')
            
        except:
            messages.info(request, 'member does not exist')
            return redirect('deletemember')
        
    else:
        return render(request, 'deletemember.html')
    

def loan(request):
    if request.method == "POST":
        name= request.POST['Name']
        types=request.POST['types']
        try:
            if Loans.objects.filter(name=Contributions.objects.get(name=name)).exists():
                    obj1 =Loans.objects.get(name=Contributions.objects.get(name=name))
                    if types == "pay":
                        amount_paid = request.POST['paid']
                        obj1.amount_paid = str(int(obj1.amount_paid) + int(amount_paid))
                        if float(obj1.expected_amount_to_be_paid) - float(obj1.amount_paid) <= 0: 
                            obj1.balance_carried_forward = str(0)
                            obj1.save()
                        else:
                            obj1.balance_carried_forward = str(float(obj1.expected_amount_to_be_paid) - float(obj1.amount_paid))
                            obj1.save()
                        return redirect('/')
                    else:
                        amount_loaned= request.POST['loaned']
                        obj1.amount_loaned = str(int(obj1.amount_loaned) + int(amount_loaned))
                        obj1.expected_amount_to_be_paid = str(int(obj1.amount_loaned) * 1.05)
                        obj1.balance_carried_forward = str(float(obj1.expected_amount_to_be_paid) - float(obj1.amount_paid))
                        obj1.save()
                        return redirect('/')
            else:
                date=datetime.datetime.now()
                formatted_date=datetime.datetime.strftime(date, '%Y-%m-%d')
                amount_loaned = request.POST['loaned']
                amount_paid = 0
                expected_amount= str(int(amount_loaned) * 1.05)
                obj = Loans.objects.create(name=Contributions.objects.get(name=name), amount_loaned= amount_loaned, expected_amount_to_be_paid=expected_amount, 
                amount_paid=amount_paid, balance_carried_forward=str(float(expected_amount)- float(amount_paid)), date=formatted_date)
                obj.save()
                messages.info(request, "saved successfully")
                return redirect('/loan')
        except:
            messages.info(request, "member does not exist")
            return redirect('loan')
    else:
        return render(request, 'loanform.html')

def table(request):
    loans = Loans.objects.all()
    return render(request, 'generaltable.html', {'loans': loans})


def accounts(request):
    Contribution = Contributions.objects.all()
    loan = Loans.objects.all()
    return render(request, 'accounts.html')