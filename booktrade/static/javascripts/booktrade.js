(function () {
  "use strict";

  angular
    .module('booktrade', [
      'booktrade.config',
      'booktrade.routes',
      'booktrade.authentication'
      ]);

  angular
    .module('booktrade.routes', ['ngRoute']);

  angular
    .module('booktrade.config', []);

  angular
    .module('booktrade')
    .run(run)

  run.$inject = ['$http'];


  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $htto.defaults.xsrfCookieName = 'csrftoken';
  }

})();
