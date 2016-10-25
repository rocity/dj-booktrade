(function () {
  "use strict";

  angular
    .module('booktrade.authentication', [
      'booktrade.authentication.controllers',
      'booktrade.authentication.services'
      ]);

  angular
    .module('booktrade.authentication.controllers', []);

  angular
    .module('booktrade.authentication.services', ['ngCookies']);

})();
