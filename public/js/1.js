webpackJsonp([1],{

/***/ 94:
/***/ (function(module, exports, __webpack_require__) {

var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(96),
  /* template */
  __webpack_require__(97),
  /* scopeId */
  null,
  /* cssModules */
  null
)
Component.options.__file = "/home/rinzler/Desktop/sites/interprises.test/resources/assets/js/components/Pages/Register.vue"
if (Component.esModule && Object.keys(Component.esModule).some(function (key) {return key !== "default" && key !== "__esModule"})) {console.error("named exports are not supported in *.vue files.")}
if (Component.options.functional) {console.error("[vue-loader] Register.vue: functional components are not supported with templates, they should use render functions.")}

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-b1c8f868", Component.options)
  } else {
    hotAPI.reload("data-v-b1c8f868", Component.options)
  }
})()}

module.exports = Component.exports


/***/ }),

/***/ 96:
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
                name: '',
                email: '',
                pass: '',
                passRepeat: ''
            }
        };
    },

    methods: {
        getAuthStatus: function getAuthStatus() {
            var _this = this;

            __WEBPACK_IMPORTED_MODULE_0_axios___default.a.get('/backend/get_auth_status').then(function (response) {
                _this.$store.state.authState = response.data;
            }).catch(function (error) {
                console.log(error);
            });
        },
        getToken: function getToken() {
            var _this2 = this;

            __WEBPACK_IMPORTED_MODULE_0_axios___default.a.get('/backend/get_token').then(function (response) {
                _this2.token = response.data;
            }).catch(function (error) {
                console.log(error);
            });
        },
        postForm: function postForm() {
            var _this3 = this;

            __WEBPACK_IMPORTED_MODULE_0_axios___default.a.post('/register', {
                name: this.formData.name,
                email: this.formData.email,
                password: this.formData.pass,
                password_confirmation: this.formData.passRepeat
                // _token: this.token
            }).then(function (response) {
                console.log(response);
                _this3.$store.state.authState = 'auth';
            }).catch(function (error) {
                console.log(error.response);
                _this3.formErrors = error.response.data.errors;
            });
        },
        logOut: function logOut() {
            __WEBPACK_IMPORTED_MODULE_0_axios___default.a.post('/logout', {
                _token: this.token
            }).then(function (response) {
                this.$store.state.authState = 'guest';
            }).catch(function (error) {
                console.log(error);
            });
        }
    },
    created: function created() {
        this.getToken();
        this.getAuthStatus();
    }
});

/***/ }),

/***/ 97:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', [_c('div', {
    staticClass: "container"
  }, [_c('div', {
    staticClass: "row"
  }, [_c('div', {
    staticClass: "col-xs-6 col-xs-offset-3"
  }, [(_vm.$store.state.authState == 'guest') ? _c('div', [_c('form', {
    on: {
      "submit": function($event) {
        $event.preventDefault();
        _vm.postForm()
      }
    }
  }, [(_vm.formErrors != null) ? _c('div', {
    staticStyle: {
      "border": "2px solid red",
      "padding": "15px"
    }
  }, [_vm._m(0), _vm._v(" "), _vm._l((_vm.formErrors), function(error) {
    return _c('p', {
      staticStyle: {
        "color": "red"
      }
    }, [_vm._v("\n                                " + _vm._s(error[0]) + "\n                            ")])
  })], 2) : _vm._e(), _vm._v(" "), _c('h2', {
    staticClass: "text-center"
  }, [_vm._v("Зарегистрироваться")]), _vm._v(" "), _c('div', {
    staticClass: "hidden",
    domProps: {
      "innerHTML": _vm._s(_vm.token)
    }
  }), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    attrs: {
      "for": "field_1"
    }
  }, [_vm._v("Введите имя")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.formData.name),
      expression: "formData.name"
    }],
    staticClass: "form-control",
    attrs: {
      "required": "",
      "type": "text",
      "id": "field_1",
      "placeholder": "Введите имя..."
    },
    domProps: {
      "value": (_vm.formData.name)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.$set(_vm.formData, "name", $event.target.value)
      }
    }
  })]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    attrs: {
      "for": "field_2"
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
      "id": "field_2",
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
      "for": "field_3"
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
      "id": "field_3",
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
  })]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('label', {
    attrs: {
      "for": "field_4"
    }
  }, [_vm._v("Повторите пароль")]), _vm._v(" "), _c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.formData.passRepeat),
      expression: "formData.passRepeat"
    }],
    staticClass: "form-control",
    attrs: {
      "required": "",
      "type": "password",
      "id": "field_4",
      "placeholder": "Повторите пароль..."
    },
    domProps: {
      "value": (_vm.formData.passRepeat)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.$set(_vm.formData, "passRepeat", $event.target.value)
      }
    }
  })]), _vm._v(" "), _c('br'), _c('br'), _c('br'), _c('br'), _vm._v(" "), _c('div', {
    staticClass: "form-group text-center"
  }, [_c('input', {
    staticClass: "button button-primary",
    attrs: {
      "type": "submit",
      "value": "Зарегистрироваться"
    }
  }), _vm._v(" "), _c('br'), _c('br'), _vm._v(" "), _c('span', [_vm._v("Или")]), _vm._v(" "), _c('br'), _c('br'), _vm._v(" "), _c('router-link', {
    staticClass: "button button-primary",
    attrs: {
      "to": {
        name: 'login'
      }
    }
  }, [_vm._v("\n                                Войти\n                            ")])], 1)])]) : _c('div', [_c('h2', {
    staticClass: "text-center"
  }, [_vm._v("Вы успешно вошли в систему")])])])])])])
},staticRenderFns: [function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('p', {
    staticStyle: {
      "color": "red"
    }
  }, [_c('b', [_vm._v("Ошибки")])])
}]}
module.exports.render._withStripped = true
if (false) {
  module.hot.accept()
  if (module.hot.data) {
     require("vue-hot-reload-api").rerender("data-v-b1c8f868", module.exports)
  }
}

/***/ })

});