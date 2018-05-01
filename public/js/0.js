webpackJsonp([0],{

/***/ 100:
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



/* harmony default export */ __webpack_exports__["default"] = ({
    data: function data() {
        return {
            token: '',
            formErrors: null,
            formData: {
                email: '',
                pass: ''
            }
        };
    },

    methods: {
        getToken: function getToken() {
            var _this = this;

            __WEBPACK_IMPORTED_MODULE_0_axios___default.a.get('/backend/get_token').then(function (response) {
                _this.token = response.data;
            }).catch(function (error) {
                console.log(error);
            });
        },
        postForm: function postForm() {
            var _this2 = this;

            __WEBPACK_IMPORTED_MODULE_0_axios___default.a.post('/login', {
                password: this.formData.pass,
                email: this.formData.email
            }).then(function (response) {
                _this2.$store.state.authState = 'auth';
            }).catch(function (error) {
                _this2.formErrors = error.response.data.errors;
            });
        }
    },
    created: function created() {
        this.getToken();
    }
});

/***/ }),

/***/ 93:
/***/ (function(module, exports, __webpack_require__) {

var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(100),
  /* template */
  __webpack_require__(95),
  /* scopeId */
  null,
  /* cssModules */
  null
)
Component.options.__file = "/home/rinzler/Desktop/sites/interprises.test/resources/assets/js/components/Pages/Login.vue"
if (Component.esModule && Object.keys(Component.esModule).some(function (key) {return key !== "default" && key !== "__esModule"})) {console.error("named exports are not supported in *.vue files.")}
if (Component.options.functional) {console.error("[vue-loader] Login.vue: functional components are not supported with templates, they should use render functions.")}

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-1996fb10", Component.options)
  } else {
    hotAPI.reload("data-v-1996fb10", Component.options)
  }
})()}

module.exports = Component.exports


/***/ }),

/***/ 95:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', [_c('div', {
    staticClass: "container"
  }, [_c('div', {
    staticClass: "row"
  }, [_c('div', {
    staticClass: "col-xs-6 col-xs-offset-3"
  }, [(_vm.$store.state.authState == 'guest') ? _c('div', [(_vm.formErrors != null) ? _c('div', {
    staticStyle: {
      "border": "2px solid red",
      "padding": "15px"
    }
  }, [_vm._m(0), _vm._v(" "), _vm._l((_vm.formErrors), function(error) {
    return _c('p', {
      staticStyle: {
        "color": "red"
      }
    }, [_vm._v("\n                            " + _vm._s(error[0]) + "\n                        ")])
  })], 2) : _vm._e(), _vm._v(" "), _c('form', {
    on: {
      "submit": function($event) {
        $event.preventDefault();
        _vm.postForm()
      }
    }
  }, [_c('h2', {
    staticClass: "text-center"
  }, [_vm._v("Войти в систему")]), _vm._v(" "), _c('div', {
    staticClass: "hidden",
    domProps: {
      "innerHTML": _vm._s(_vm.token)
    }
  }), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    attrs: {
      "for": "auth-email"
    }
  }, [_vm._v("Введите e-mail")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.formData.email),
      expression: "formData.email"
    }],
    staticClass: "form-control",
    attrs: {
      "required": "",
      "type": "email",
      "id": "auth-email",
      "placeholder": "Введите e-mail..."
    },
    domProps: {
      "value": (_vm.formData.email)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.$set(_vm.formData, "email", $event.target.value)
      }
    }
  })]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    attrs: {
      "for": "auth-password"
    }
  }, [_vm._v("Введите пароль")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.formData.pass),
      expression: "formData.pass"
    }],
    staticClass: "form-control",
    attrs: {
      "required": "",
      "type": "password",
      "id": "auth-password",
      "placeholder": "Введите пароль..."
    },
    domProps: {
      "value": (_vm.formData.pass)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.$set(_vm.formData, "pass", $event.target.value)
      }
    }
  })]), _vm._v(" "), _vm._m(1)])]) : _c('div', [_c('h2', {
    staticClass: "text-center"
  }, [_vm._v("Вы успешно вошли в систему")])])])])])])
},staticRenderFns: [function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('p', {
    staticStyle: {
      "color": "red"
    }
  }, [_c('b', [_vm._v("Ошибки")])])
},function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "form-group text-center"
  }, [_c('br'), _c('br'), _vm._v(" "), _c('input', {
    staticClass: "button button-primary",
    attrs: {
      "type": "submit",
      "value": "Войти в систему"
    }
  })])
}]}
module.exports.render._withStripped = true
if (false) {
  module.hot.accept()
  if (module.hot.data) {
     require("vue-hot-reload-api").rerender("data-v-1996fb10", module.exports)
  }
}

/***/ })

});