from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest,HttpResponse
from django.http import JsonResponse as json_response
from django.contrib.auth import authenticate

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
			except IntegrityError:
				return json_response({
                    'error': 'User already exists'
                }, status=400)
 			return json_response({               
                'username': user.username
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
	print "Login request"
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		print "username",username

		if username is not None and password is not None:
			print 'user naem pass'
			user = authenticate(username=username, password=password)
			print "user",user
			if user is not None:
				if user.is_active:
					token, created = Token.objects.get_or_create(user=user)
					return json_response({
                        # 'token': token.token,
                        'username': user.username
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

@csrf_exempt
# @token_required
def logout(request):
    if request.method == 'POST':
        request.token.delete()
        return json_response({
            'status': 'success'
        })
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({
            'error': 'Invalid Method'
        }, status=405)