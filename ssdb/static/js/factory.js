moviesApp.factory('moviesFactory', function($http){
	var urlBase = '/api/movies/';
	var _moviesService = {};

	_moviesService.getMoviesList = function(){		
		return $http.get(urlBase);
	}

	_moviesService.getMovie = function(movieId){
		if(movieId){			
			return $http.put(urlBase+movieId);
		}
		return $http.get(urlBase);
	}

	_moviesService.creaeMovie = function(moviesdata){
		alert("create movierrrrrrrrrrrrr",moviesdata);
		return $http.post(urlBase, moviesdata);
	}

	_moviesService.deleteLeave = function(movie){		
		return $http.delete(urlBase+movie.id);
	}
	

	return _moviesService;
});


moviesApp.factory('genreFactory', function($http){
	var urlBase = '/api/genre/';
	var _genreService = {};

	_genreService.getGenre = function(genreId){
		if(genreId){
			return $http.get(urlBase+genreId);	
		}
		return $http.get(urlBase);
	}

	_genreService.getGenreList = function(){		
		return $http.get(urlBase);
	}
	
	return _genreService;
});


moviesApp.factory('AuthService', function($http){
	var _authService = {}

	var url = '/api/register/';
	var login_url = '/api/login/'
	var logout_url = '/api/logout/'

	_authService.login = function (username, password) {
		alert("login",username);
		return $http.post(login_url, username, password);
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