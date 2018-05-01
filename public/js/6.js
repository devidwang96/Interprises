webpackJsonp([6],{

/***/ 14:
/***/ (function(module, exports, __webpack_require__) {

var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(77),
  /* template */
  __webpack_require__(81),
  /* scopeId */
  null,
  /* cssModules */
  null
)
Component.options.__file = "/home/rinzler/Desktop/sites/interprises.test/resources/assets/js/components/Pages/Search.vue"
if (Component.esModule && Object.keys(Component.esModule).some(function (key) {return key !== "default" && key !== "__esModule"})) {console.error("named exports are not supported in *.vue files.")}
if (Component.options.functional) {console.error("[vue-loader] Search.vue: functional components are not supported with templates, they should use render functions.")}

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-59ba8091", Component.options)
  } else {
    hotAPI.reload("data-v-59ba8091", Component.options)
  }
})()}

module.exports = Component.exports


/***/ }),

/***/ 77:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios__ = __webpack_require__(56);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_axios__);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//



/* harmony default export */ __webpack_exports__["default"] = ({
    data: function data() {
        return {
            query: '',
            localQuery: '',
            results: '',
            status: 'empty'
        };
    },

    methods: {
        localSearch: function localSearch() {
            if (this.localQuery != '') {
                this.query = this.localQuery;
                this.$router.push({ name: 'search', query: { query: this.query } });
                this.findRequest();
            }
        },
        search: function search() {
            if (this.$route.query.query != undefined && this.$route.query.query.length > 0) {
                this.status = "searching";
                this.query = this.$route.query.query;
                this.localQuery = this.$route.query.query;
                this.findRequest();
            }
        },
        findRequest: function findRequest() {
            var _this = this;

            __WEBPACK_IMPORTED_MODULE_0_axios___default.a.get('/backend/search/' + this.query).then(function (response) {
                _this.results = response.data.data;
                _this.results.length == 0 ? _this.status = 'not-found' : _this.status = 'loaded';
            }).catch(function (error) {
                console.log(error);
                this.status = 'error';
            });
        }
    },
    created: function created() {
        this.search();
    },

    watch: {
        '$route.query.query': function $routeQueryQuery() {
            this.search();
        }
    },
    mounted: function mounted() {
        console.log('mount');
    }
});

/***/ }),

/***/ 81:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', [_c('div', {
    staticClass: "container"
  }, [_c('div', {
    staticClass: "search"
  }, [_c('form', {
    on: {
      "submit": function($event) {
        $event.preventDefault();
        return _vm.localSearch($event)
      }
    }
  }, [_c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.localQuery),
      expression: "localQuery"
    }],
    attrs: {
      "type": "text",
      "placeholder": "Искать предприятие..."
    },
    domProps: {
      "value": (_vm.localQuery)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.localQuery = $event.target.value
      }
    }
  }), _vm._v(" "), _c('input', {
    staticClass: "button button-primary",
    attrs: {
      "type": "submit",
      "value": "Искать"
    }
  })])]), _vm._v(" "), _c('h1', [_vm._v("Результаты поиска")]), _vm._v(" "), _c('div', {
    staticClass: "results"
  }, [(_vm.status == 'searching') ? _c('div', {
    staticClass: "searching"
  }, [_vm._v("\n                Обработка запроса...\n            ")]) : _vm._e(), _vm._v(" "), (_vm.status == 'not-found') ? _c('div', {
    staticClass: "not-found"
  }, [_vm._v("\n                По вашему запросу ничего не найдено\n            ")]) : _vm._e(), _vm._v(" "), _vm._l((_vm.results), function(item, index) {
    return (_vm.status == 'loaded') ? _c('div', {
      staticClass: "result"
    }, [_c('h2', {
      staticClass: "result__name"
    }, [_c('router-link', {
      attrs: {
        "to": {
          name: 'company',
          params: {
            companyBin: item.BIN
          }
        }
      }
    }, [_vm._v("\n                        " + _vm._s(item.name_ru) + "\n                    ")])], 1), _vm._v(" "), _c('p', {
      staticClass: "result__activity"
    }, [_c('b', [_vm._v(_vm._s(item.activity_ru))])]), _vm._v(" "), _c('p', {
      staticClass: "result__address"
    }, [_vm._v("\n                    Юридический адрес: " + _vm._s(item.address) + "\n                ")]), _vm._v(" "), _c('p', {
      staticClass: "result__ceo"
    }, [_vm._v("\n                    Руководитель: " + _vm._s(item.CEO) + "\n                ")]), _vm._v(" "), _c('p', {
      staticClass: "result__date"
    }, [_vm._v("\n                    Дата основания: " + _vm._s(item.register_date) + "\n                ")]), _vm._v(" "), _c('p', {
      staticClass: "result__bin"
    }, [_vm._v("\n                    БИН: " + _vm._s(item.BIN) + "\n                ")]), _vm._v(" "), _c('p', {
      staticClass: "result__oked"
    }, [_vm._v("\n                    ОКЭД: " + _vm._s(item.economic_activity_code) + "\n                ")]), _vm._v(" "), _c('p', {
      staticClass: "result__kato"
    }, [_vm._v("\n                    КАТО: " + _vm._s(item.territory_code) + "\n                ")]), _vm._v(" "), _c('p', {
      staticClass: "result__status"
    }, [_vm._v("\n                    Статус:\n                    "), (item.active == 1) ? _c('span', {
      staticClass: "active"
    }, [_vm._v("В работе")]) : _c('span', [_vm._v("Не работает")])]), _vm._v(" "), _c('br'), _c('br'), _c('br')]) : _vm._e()
  })], 2)])])
},staticRenderFns: []}
module.exports.render._withStripped = true
if (false) {
  module.hot.accept()
  if (module.hot.data) {
     require("vue-hot-reload-api").rerender("data-v-59ba8091", module.exports)
  }
}

/***/ })

});