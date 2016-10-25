(function () {
  "use strict";

  angular
    .module('booktrade.routes')
    .config(config);

    config.$inject = ['$routeProvider'];

  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'RegisterController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/register.html'
    }).otherwise('/');
  }
})();
