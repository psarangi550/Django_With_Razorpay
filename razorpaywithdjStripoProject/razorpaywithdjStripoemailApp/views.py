from django.shortcuts import render,HttpResponseRedirect
from .forms import CoffeeForm
from .models import Coffee
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.
def coffeview(request):
    if request.method == 'POST':
        form=CoffeeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            amount=form.cleaned_data["amount"]*100
            print(name)
            print(email)
            print(amount)
            client=razorpay.Client(auth=("rzp_test_34fF3UTYKtIcNu","vwsMRjInSNJrSlFhfebKW9N8"))
            data={
                "amount":amount,
                "currency":"INR",
                "payment_capture":'1',
            }
            payment=client.order.create(data=data)
            print(payment)
            Coffee.objects.create(name=name,email=email,amount=amount,order_id=payment['id'])
            return render(request,"razorpaywithdjStripoemailApp/index.html",{"payment":payment,"pay_id":payment["id"]})
    form=CoffeeForm()
    return render(request,"razorpaywithdjStripoemailApp/index.html",{"form":form})
@csrf_exempt
def success(request):
    return render(request,"razorpaywithdjStripoemailApp/thanks.html")
