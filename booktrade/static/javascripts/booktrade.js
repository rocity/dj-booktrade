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
})();
