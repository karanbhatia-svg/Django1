from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import student
import csv
from django.utils.encoding import smart_str


# Create your views here.

def home(request):
    return render(request, 'index.html')

def email(request):
    return render(request, 'email.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

class Invest(View):
	def get(self, request):
		form = InvestmentForm()
		return render(request, 'invest.html', {'form': form})

	def post(self, request):
		form = InvestmentForm(request.POST)

		if form.is_valid():
			total_result = form.cleaned_data['starting_amount']
			total_interest = 0
			yearly_results = {}

			for i in range(1, int(form.cleaned_data['number_of_years'] + 1)):
				yearly_results[i] = {}

				# calculate the interest
				interest = total_result * (form.cleaned_data['return_rate'] / 100)
				total_result += interest
				total_interest += interest

				# add additional contribution
				total_result += form.cleaned_data['annual_additional_contribution']

				# set yearly_results
				yearly_results[i]['interest'] = round(total_interest, 2)
				yearly_results[i]['total'] = round(total_result, 2)

				# create context
				context = {
					'total_result': round(total_result, 2),
					'yearly_results': yearly_results,
					'number_of_years': int(form.cleaned_data['number_of_years'])
				}

			# render the template
			return render(request, 'result.html', context)

def add(request):
	jam = "ggg"
	wy = jam
	yw ={'wy':wy}

	return render(request, 'add.html', yw)

def add1(request):
	if 'b1' in request.GET:
		val1 = int(request.GET['num1'])
		val2 = int(request.GET['num2'])
		sum = val1 + val2
		sum = f"{val1} + {val2} = {sum}."
		res = {'sum': sum}
		return render(request, 'result1.html', res)

	elif 'b2' in request.GET:
			val1 = int(request.GET['num1'])
			val2 = int(request.GET['num2'])
			sum = val1 - val2
			sum = f"{val1} - {val2} = {sum}."
			res = {'sum': sum}
			return render(request, 'result1.html', res)

	elif 'b3' in request.GET:
			val1 = int(request.GET['num1'])
			val2 = int(request.GET['num2'])
			sum = val1 * val2
			sum = f"{val1} * {val2} = {sum}."
			res = {'sum': sum}
			return render(request, 'result1.html', res)

	elif 'b4' in request.GET:
			val1 = int(request.GET['num1'])
			val2 = int(request.GET['num2'])
			sum = val1 / val2
			sum = f"{val1} / {val2} = {sum}."
			res = {'sum': sum}
			return render(request, 'result1.html', res)

def evenodd(request):
	return render(request, 'evenodd.html')

def evenorodd(request):
	if 'b1' in request.GET:
		num1 = int(request.GET['num1'])
		if num1%2==0:
			ans = f"{num1} is Even number."
		else:
			ans = f"{num1} is Odd Number."
		res = {'ans':ans}
		return render(request, 'result1.html', res)

def form(request):
		return render(request, 'form.html')


def signup_student(request):
    return render(request, 'signup_student.html')

def signup_student_output(request):
	en=student(name=request.POST.get('name'),
			   cl=request.POST.get('class'),
			   gender= request.POST.get('gender'))
	en.save()
	str1  = "Data inserted to student table" + str(en.id)
	return render(request, 'thanks.html',{'msg':str1})

def showall(request):
	mymember = student.objects.all().values()
	return render(request, 'Showall.html',{'mymember':mymember})

def delete_record(request):

	return render(request, 'delete.html')
def delete(request):
	i=int(request.POST['sid'])
	r=student.objects.get(id=i)
	r.delete()
	return redirect('showall')

def csv(request):
	# response content type
	response = HttpResponse(content_type='text/csv')
	#decide the file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.csv"'

	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))

	#write the headers
	writer.writerow([
		smart_str(u"Name"),
		smart_str(u"class"),
		smart_str(u"gender"),

	])
	#get data from database or from text file....
	mymember = student.objects.all().values() #dummy function to fetch data
	for item in mymember:
		writer.writerow([
			smart_str(item.name),
			smart_str(item.start_date_time),
			smart_str(item.end_date_time),
			smart_str(item.notes),
		])
	return response

def update_record(request):


	return render(request, 'update.html',)

def update(request):
	i = int(request.POST['sid'])
	r = student.objects.get(id=i)
	return render(request,'update_page.html',{'record':r})

def final_update(request,id):
	n = request.POST['name']
	c =request.POST['class']
	g= request.POST['gender']
	r = student.objects.get(id=id)
	r.name=n
	r.cl=c
	r.gender=g
	r.save()

	return redirect('showall')








