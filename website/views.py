from django.shortcuts import render
from random import randint
# Create your views here.
def home(request):
    return render(request,'home.html',{})
def add(request):

    num1=randint(0,10)
    num2=randint(0,10)

    if request.method == "POST":
        a=int(request.POST['answer'])
        old1=int(request.POST['old1'])
        old2=int(request.POST['old2'])
        correct= old1 + old2
        if a == correct:
            result='Correct'
        else:
            result='Incorrect'
        return render(request,'add.html',{'answer':a, 'result':result,'num_1':num1 , 'num_2':num2 })
    return render(request,'add.html', {'num_1':num1 , 'num_2':num2})
def substract(request):
    num1=randint(0,10)
    num2=randint(0,10)
    if num1<num2:
        num1,num2=num2,num1
    if request.method=='POST':
        sub_ans=int(request.POST['answer'])
        old1=int(request.POST['old1'])
        old2=int(request.POST['old2'])
        correct=old1-old2
        if sub_ans == correct:
            result='Correct'
        else:
            result='Incorrect'
        return render(request,'substract.html',{'answer':sub_ans, 'result':result,'num_1':num1 , 'num_2':num2 })
    return render(request,'substract.html', {'num_1':num1 , 'num_2':num2})

    return render(request,'substract.html',{})
def divide(request):
    num1=randint(1,10)
    num2=randint(1,10)
    num1=num1*num2
    div=str(num1)
    if num1 >10:
        a,b=int(div[0]),int(div[1])
    else:
        a=0
        b=num1
    if request.method=='POST':
        div_ans=int(request.POST['answer'])
        old1=int(request.POST['old1'])
        old2=int(request.POST['old2'])
        correct=old1/old2
        if div_ans == correct:
            result='Correct'
        else:
            result='Incorrect'
        return render(request,'divide.html',{'answer':div_ans, 'result':result,'num_1':num1 , 'num_2':num2 ,'a': a, 'b': b})
    return render(request,'divide.html', {'num_1':num1 , 'num_2':num2 , 'a': a, 'b': b})

def multipy(request):
    num1=randint(0,10)
    num2=randint(0,10)
    if request.method=='POST':
        mul_ans=int(request.POST['answer'])
        old1=int(request.POST['old1'])
        old2=int(request.POST['old2'])
        correct=old1*old2
        if mul_ans == correct:
            result='Correct'
        else:
            result='Incorrect'
        return render(request,'multipy.html',{'answer':mul_ans, 'result':result,'num_1':num1 , 'num_2':num2 })
    return render(request,'multipy.html', {'num_1':num1 , 'num_2':num2})
