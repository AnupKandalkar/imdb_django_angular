moviesApp.factory('moviesFactory', function($http, $cookies){
	var urlBase = '/api/movies/';
	var _moviesService = {};

	var cookies_val = $cookies.get('csrftoken');	
	var header_val = {'X-CSRFToken':cookies_val, 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'};

	// $http.defaults.headers.post['My-Header']=header_val;

	_moviesService.getMoviesList = function(){		
		return $http.get(urlBase);
	}

	_moviesService.getMovie = function(movieId){
		if(movieId){	
			alert(movieId);		
			return $http.put(urlBase+movieId, {headers: header_val});
		}
		return $http.get(urlBase);
	}

	_moviesService.updateMovie = function(movieVals){	
		
		if(movieVals){					
			return $http.put(urlBase+movieVals.id, $.param(movieVals), {headers: header_val});
		}
		return $http.get(urlBase);
	}



	_moviesService.creaeMovie = function(moviesdata){		
		console.log("create move", moviesdata);
		return $http.post(urlBase, $.param(moviesdata), {headers: header_val});
	}

	_moviesService.deleteLeave = function(movie){		
		return $http.delete(urlBase+movie.id, {headers: header_val});
	}
	

	return _moviesService;
});


moviesApp.factory('genreFactory', function($http, $cookies){
	var urlBase = '/api/genre/';
	var _genreService = {};

	var cookies_val = $cookies.get('csrftoken');	
	var header_val = {'X-CSRFToken':cookies_val ,'Content-Type': 'application/x-www-form-urlencoded'}

	_genreService.getGenre = function(genreId){
		if(genreId){
			return $http.get(urlBase+genreId, {headers: header_val});	
		}
		return $http.get(urlBase);
	}

	_genreService.getGenreList = function(){		
		return $http.get(urlBase);
	}

	_genreService.deleteGenre = function(genre){
		return $http.delete(urlBase+genre.id, {headers: header_val});
	}

	_genreService.creaeGenre = function(genredata){		
		return $http.post(urlBase, $.param(genredata), {headers: header_val});
	}
	
	return _genreService;
});


moviesApp.factory('AuthService', function($http){
	var _authService = {}

	var url = '/api/register/';
	var login_url = '/api/login/'
	var logout_url = '/api/logout/'

	_authService.login = function (username, password) {
		console.log("login",username);
		var cred = {username: username,password: password};
		return $http.post(login_url, $.param(cred), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}});
		// return $http.post(login_url, ,$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';);
	};

	_authService.register = function (userData) {
		console.log("login",userData);
		// var cred = {username: username,password: password};
		return $http.post(url, $.param(userData), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}});
		// return $http.post(login_url, ,$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';);
	};



	_authService.logout = function () {		
		return $http.post(logout_url);
	};

	return _authService;

 //  	var register = function (username, password) {  	
	// $http.post(url, {
	//   username: username,
	//   password: password
	// }, {
	//   headers: {
	//     'Content-Type': 'application/json'
	//   }
	// }).then(
	//   function (response) {

	//   	// var token = response.data.token;
	// 	var username = response.data.username;

	// 	if (username) {
	// 	  // $window.localStorage.token = token;
	// 	  $window.localStorage.username = username;
	// 	  //success 
	// 	} else {
	// 	  // error
	// 	}
	//     // success callback
	//   },
	//   function (response) {
	//     // error callback
	//   });
	//     // Registration logic goes here
	//  };

 //  return {
 //    register: function (username, password) {
 //      return register(username, password);
 //    }};

});