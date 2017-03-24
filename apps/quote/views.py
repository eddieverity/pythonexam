from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import User, Quote, Favorite
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
import bcrypt
from django.db.models import Count



# Create your views here.
def home(request):
  return render(request, 'quote/home.html')


def quotes(request):
  curr_user=request.session['id']
  context = {
    'curr_user' : request.session['id'],
    'users' : User.objects.all(),
    'quotes': Quote.objects.exclude(quote_fav__user_favorite=curr_user),
    'favorites' : Favorite.objects.filter(user_favorite=request.session['id'])
  }


  return render(request, 'quote/quotes.html', context)
  pass


def user_display(request, user_id):
  
  context = {

    'users' : User.objects.filter(id=user_id),
    'quotes': Quote.objects.filter(poster_id=user_id),
    'quote_count': Quote.objects.filter(poster_id=user_id).count()
 
  }
  return render(request, 'quote/users.html', context)


def register(request):
  is_valid = True
  name = request.POST['name']
  alais = request.POST['alias']
  email = request.POST['email']
  date_of_birth = request.POST['date_of_birth']
  password = request.POST['password'].encode(encoding="utf-8")
  confirm = request.POST['confirm']
  pw_hash=bcrypt.hashpw(password, bcrypt.gensalt())

  if ValidateEmail(email) != True:
    messages.error(request, 'email address not valid')
    is_valid = False

  if DupEmail(email):
    messages.error(request, 'email address in use')
    is_valid= False

  # if badname_regex(name):
  #   messages.error(request, 'name must contain letters only')
  #   return redirect('quote:home')  
  
  if len(name) < 2:
    messages.error(request, 'name must be at least 2 characters long')
    is_valid = False


  if len(password) < 8:
    messages.error(request, 'password must be at least 8 characters long')
    is_valid = False
  if password != confirm:
    messages.error(request, 'passwords do not match')
    is_valid = False
    
  if is_valid:

    curr_user= User.objects.create(
      name=request.POST['name'],
      alias=request.POST['alias'],
      email=request.POST['email'],
      date_of_birth=request.POST['date_of_birth'],
      password= pw_hash
      )


    request.session['alias']=request.POST['alias']
    request.session['id']=curr_user.id
    return redirect('quote:quotes')
   

  else:
    return redirect('quote:home')

def ValidateEmail( email ):    
  try:
    validate_email( email )
    return True
  except ValidationError:
    return False

def badname_regex(name):
  reggie=re.compile(r'^[a-zA-Z]+$')
  if reggie.match(name) is None:
    return True

def DupEmail(email):
  try:
    User.objects.get(email = email)
    return True
  #tried ValidationError
  except User.DoesNotExist:
    return False


def login(request):
  l_email=request.POST['l_email']
  try:
    curr_user=User.objects.get(email = l_email)

    # print pw_hash
    # print curr_user.password
    # it's not 'if this hashed password = entered hashed password'
    l_password=request.POST['l_password'].encode(encoding="utf-8")
    if bcrypt.hashpw(l_password, curr_user.password.encode("utf-8")) == curr_user.password:
      request.session['alias']=curr_user.alias
      request.session['id']=curr_user.id

      return redirect('quote:quotes')
    else:
      messages.error(request, 'password does not match registered user')
      return redirect('quote:home')
  except User.DoesNotExist:
    messages.error(request, 'email does not exist in database, please register')
    return redirect('quote:home')

def post_quote(request):
  pass
  is_valid = True
  quoted_by = request.POST['quoted_by']
  description = request.POST['description']
  poster = request.session['id']

  if len(quoted_by) < 3:
    messages.error(request, 'Quoters name should be more than 3 characters')
    is_valid = False

  if len(description) < 10:
    messages.error(request, 'Quotation should be more than 10 characters')
    is_valid = False

  if is_valid:

    curr_quote= Quote.objects.create(
      quoted_by=request.POST['quoted_by'],
      description=request.POST['description'],
      poster_id=request.session['id'],
    )



    return redirect('quote:quotes')
   

  else:
    return redirect('quote:quotes')

def add_favorite(request, quote_id):

  user_favorite=request.session['id']
  quote_favorite=quote_id
  favorite= Favorite.objects.create(
    quote_favorite_id=quote_favorite,
    user_favorite_id=request.session['id']

    )

  return redirect('quote:quotes')

def remove_favorite(request, quote_id):
  
  delted=Favorite.objects.filter(id=quote_id).delete()

  return redirect('quote:quotes')
  pass

def logout(request):
  request.session.clear()
  return redirect('quote:home')
