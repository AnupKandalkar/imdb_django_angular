moviesApp = angular.module('moviesApp',['ui.router']).
	config(function($stateProvider, $urlRouterProvider){
		
	  $urlRouterProvider.otherwise("");	  
	  $stateProvider
	  	.state('main', {
	  		url: "",
	      	templateUrl: "/static/partials/auth.html",	      	
      		controller: 'AuthCtrl'
	  	})
	    .state('dashboard', {
	      url: "dashboard",
	      templateUrl: "/static/partials/dashboard.html",
	      controller:'moviesCtrl'
	    })

	    .state('newMovie', {
	      url: "movies",
	      templateUrl: "/static/partials/addMovies.html",
	      controller:'newMovieCtrl'
	    })
	   
	});
