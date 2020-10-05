from django.shortcuts import render, redirect
from home.models import User,Profile,Address
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def profile(request):
	email = request.user.email
	flag = Profile.objects.filter(user = User.objects.get(email = email))
	if len(flag) == 1:
		prof = Profile.objects.get(user = User.objects.get(email = email))
		address = prof.address.get()
		dic = {
		       'dob' :  prof.date_of_birth,
		       'line1' : address.line1,
		       'line2' : address.line2,
		       'city' : address.city,
		       'state' :address.state,
		       'country' : address.country,
		       'pincode' : address.pincode,
		       'gender' : prof.gender,
		       'height' : prof.height,
		       'weight' : prof.weight,
		       'bio' :prof.bio,
		       		       }
		if request.method == 'POST':
			name = request.POST['name']
			email = request.POST['email']
			dob = request.POST['dob']
			line1 = request.POST['line1']
			try:
			    line2 = request.POST['line2']
			except:
				line2 = None
			city = request.POST['city']
			state = request.POST['state']
			country = request.POST['country']
			gender = request.POST['gender']
			mobile = request.POST['mobile']
			height = request.POST['height']
			weight = request.POST['weight']
			pincode = request.POST['pincode']
			bio = request.POST['bio']
			user = User.objects.get(email = email)
			prof = Profile.objects.get(user = user)
			prof.user = user
			prof.gender = gender
			prof.date_of_birth = dob
			prof.height = height
			prof.weight = weight
			prof.bio = bio
			prof.save()
			user.mobile = mobile
			user.name = name
			user.save()
			addr = prof.address.get()
			addr.line1 = line1
			if line2:
			    addr.line2 = line2
			addr.city = city
			addr.state = state
			addr.country = country
			addr.pincode = pincode
			addr.save()
			prof = Profile.objects.get(user = user)
			prof.address.add(addr)
			prof.save()
			return redirect('/dashboard/profile')
	else:
		dic = {
		       'dob' :  '',
		       'line1' : '',
		       'line2' : '',
		       'city' : '',
		       'state' : '',
		       'country' : '',
		       'pincode' : '',
		       'gender' : '',
		       'height' : '',
		       'weight' : '',
		       'bio' : '',
		       		       }
		if request.method == 'POST':
			name = request.POST['name']
			email = request.POST['email']
			dob = request.POST['dob']
			line1 = name = request.POST['line1']
			try:
			    line2 = request.POST['line2']
			except:
				line2= None
			city = request.POST['city']
			state = request.POST['state']
			country = request.POST['country']
			gender = request.POST['gender']
			mobile = request.POST['mobile']
			height = request.POST['height']
			weight = request.POST['weight']
			pincode = request.POST['pincode']
			bio = request.POST['bio']
			user = User.objects.get(email = email)
			prof = Profile()
			prof.user = user
			prof.gender = gender
			prof.date_of_birth = dob
			prof.height = height
			prof.weight = weight
			prof.bio = bio
			prof.save()
			addr = Address()
			addr.line1 = line1
			if line2:
			    addr.line2 = line2
			addr.city = city
			addr.state = state
			addr.country = country
			addr.pincode = pincode
			addr.save()
			prof = Profile.objects.get(user = user)
			prof.address.add(addr)
			prof.save()
			return redirect('/dashboard/profile')
	return render(request, 'dashboard/profile.html',context = dic)

def newpass(request):
	if request.method == 'POST':
		currpass = request.POST['currpass']
		newpass = request.POST['newpass']
		confirmpass = request.POST['confirmpass']
		user = User.objects.get(email = request.user.email)
		flag = user.check_password(currpass)
		if flag:
			if newpass != confirmpass:
				messages.info(request,'Password Mismatch')
			else:
				messages.info(request,'Password Changed')
				user.set_password(newpass)
				user.save()
		else:
			messages.info(request,'Wrong Password Entered')
	return redirect('/dashboard/profile')

def image(request):
	email = request.user.email
	user = User.objects.get(email = email)
	if request.method == 'POST':
		img = request.FILES['profile']
		user.avatar = img 
		user.save()
	return redirect('/dashboard/profile')		
 