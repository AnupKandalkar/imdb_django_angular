from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest,HttpResponse
from django.http import JsonResponse as json_response
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
# from django.contrib.auth.views import logout as log_out
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

# Create your views here.

@csrf_exempt
def register(request):
  print "registrer login "
  if request.method == 'POST':
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    if username is not None and password is not None:
      try:
        user = User.objects.create_user(username, None, password)
        user = authenticate(username=username, password=password)
        if user is not None:
          if user.is_active:
            auth_login(request, user)
      except IntegrityError:
        return json_response({
                  'error': 'User already exists'
              }, status=400)
      return json_response({               
            'username': user.username,
            'isSuperUser': user.is_superuser,
        })
    else:
      return json_response({
            'error': 'Invalid Data'
        }, status=400)

	# elif request.method == 'OPTIONS':
	# 	return json_response({})
	# else:
	# 	return json_response({
	#         'error': 'Invalid Method'
	#     }, status=405)


@csrf_exempt
def login(request):
  if request.method == 'GET':
    pass
    # return json_response({
    #         'error': 'Invalid Method'
    #     }, status=405)

  elif request.method == 'POST':
    # import pdb
    # pdb.set_trace()
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    print "username",username

    if username is not None and password is not None:
      user = authenticate(username=username, password=password)

      
      if user is not None:
        if user.is_active:
          auth_login(request, user)
          # token, created = Token.objects.get_or_create(user=user)
          return json_response({
                        # 'token': token.token,
                        'username': user.username,
                        'isSuperUser': user.is_superuser,
                    })
        else:
            return json_response({
                'error': 'Invalid User'
                }, status=400)
 
     
			# else:
			# 	return json_response({
			#         'error': 'Invalid Username/Password'
			#     }, status=400)
   #      else:
   #          return json_response({
   #              'error': 'Invalid Data'
   #          }, status=400)
   #  elif request.method == 'OPTIONS':
   #      return json_response({})
   #  else:
   #      return json_response({
   #          'error': 'Invalid Method'
   #      }, status=405)

# @csrf_exempt
# # @token_required
# def logout(request):
#     print "lotout method"
#     if request.method == 'POST':
#         # request.token.delete()
#         log_out(request)
#         return json_response({
#             'status': 'success'
#         })
#     elif request.method == 'OPTIONS':
#         return json_response({})
#     else:
#         return json_response({
#             'error': 'Invalid Method'
#         }, status=405)

def log_out(request):
    logout(request)
    # messages.info(request, Messages.Login.LOGOUT)
    return redirect('home')