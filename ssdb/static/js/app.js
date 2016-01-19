moviesApp = angular.module('moviesApp',['ui.router', 'ngCookies']).
	config(function($stateProvider, $urlRouterProvider, $httpProvider){

	  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
		
	  $urlRouterProvider.otherwise("");	  
	  $stateProvider
	  	.state('main', {
	  		url: "",
	      	templateUrl: "/static/partials/auth.html",	      	
      		controller: 'AuthCtrl'
	  	})
	    .state('dashboard', {
	      url: "/dashboard",
	      templateUrl: "/static/partials/dashboard.html",
	      controller:'moviesCtrl'
	    })

	    .state('newMovie', {
	      url: "movies",
	      templateUrl: "/static/partials/addMovies.html",
	      controller:'newMovieCtrl'
	    })

	    .state('newUser', {
	    	url: "guest",
	    	templateUrl: "/static/partials/register.html",
	    	controller: 'newUserCtrl'

	    })

	    .state('genre', {
	    	url: "/genre",
	    	templateUrl: "/static/partials/genreList.html",
	    	controller: "genreCtrl"
	    })

	    .state('newGenre', {
	    	url: "newgenre",
	    	templateUrl: "/static/partials/addGenre.html",
	    	controller: 'newGenreCtrl'
	    })
	   
	});
