(function () {
  "use strict";

  angular
    .module('booktrade', [
      'booktrade.routes',
      'booktrade.authentication'
      ]);

  angular
    .module('booktrade.routes', ['ngRoute']);
})();
