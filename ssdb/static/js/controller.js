moviesApp.controller("moviesCtrl", function($scope, $window, moviesFactory, genreFactory, AuthService){

	moviesFactory.getMoviesList().then(function(response){
		$scope.moviesList = response.data;
		console.log("Movies data",$scope.moviesList);
	})

	$scope.getMovieData = function(movieId){
		alert("Movie data");
		moviesFactory.getMovie(movieId).then(function(response){
			$scope.movieData = response.data;
		})
	}

	genreFactory.getGenre().then(function(response){
		$scope.genreList = response.data;
		console.log("Genre list",$scope.genreList)
		// $scope.leave.category = $scope.leaveTypes[0].value;
		// console.log("category val",$scope.leave.category);
	});

	$scope.removeMovie = function(movie){
		alert(movie);
		moviesFactory.deleteLeave(movie).then(function(response){
			console.log("Remove moview");

			moviesFactory.getMoviesList().then(function(response){
				$scope.moviesList = response.data;
				console.log("Movies data",$scope.moviesList);
			})

		})
	}


	$scope.logout = function () {
	  AuthService.logout().then(
	    function(response) {
	      $location.path('/');
	    },
	    function (error) {
	      $scope.error = error;
	    }
	  );
	};


	$scope.username = $window.localStorage.username;
	$scope.title = "SSDB";
});


moviesApp.controller("newMovieCtrl", function($scope, moviesFactory, genreFactory){	

	$scope.saveMovie = function(){
		$scope.moviesdata.name = $scope.moviesdata.name;
		$scope.moviesdata.director = $scope.moviesdata.director;
		$scope.moviesdata.stars = $scope.moviesdata.stars;
		$scope.moviesdata.ssdb_score = $scope.moviesdata.ssdb_score;
		$scope.moviesdata.popularity = $scope.moviesdata.popularity;
		$scope.moviesdata.description = $scope.moviesdata.description;
		$scope.moviesdata.genre = $scope.genreSelection;

		moviesFactory.creaeMovie($scope.moviesdata).then(function(response){
			console.log(response.data);		
			$scope.moviesdata = "";	
		})
	}

	genreFactory.getGenreList().then(function(response){
		$scope.genreListData = response.data;
		console.log("Genre list",$scope.genreListData)
		// $scope.leave.category = $scope.leaveTypes[0].value;
		// console.log("category val",$scope.leave.category);
	});

	

});

moviesApp.controller("AuthCtrl" , function($scope, $location, AuthService){

	$scope.login = function(){
	  $scope.username = $scope.loginUsername;
	  $scope.password = $scope.loginPassword;
	  alert("Usernaem",$scope.username);
	  if (username && password) {
	  	alert("hihi",username);
	    AuthService.login(username, password).then(
	      function(response){
	        $location.path('/dashboard');
	      },
	      function(error){
	        $scope.loginError = error;
	      });
	  } else {
	    $scope.error = 'Username and password required';
	  }
	}


  $scope.register = function(){
    var username = $scope.registerUsername;
    var password = $scope.registerPassword;

    if (username && password) {
      AuthService.register(username, password).then(
        function () {
          $location.path('/dashboard');
        },
        function (error) {
          $scope.registerError = error;
        }
      );
    } else {
      $scope.registerError = 'Username and password required';
    }
  };
});
