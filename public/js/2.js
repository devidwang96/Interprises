webpackJsonp([2],{

/***/ 13:
/***/ (function(module, exports, __webpack_require__) {

var Component = __webpack_require__(1)(
  /* script */
  __webpack_require__(76),
  /* template */
  __webpack_require__(82),
  /* scopeId */
  null,
  /* cssModules */
  null
)
Component.options.__file = "/home/rinzler/Desktop/sites/interprises.test/resources/assets/js/components/Pages/Home.vue"
if (Component.esModule && Object.keys(Component.esModule).some(function (key) {return key !== "default" && key !== "__esModule"})) {console.error("named exports are not supported in *.vue files.")}
if (Component.options.functional) {console.error("[vue-loader] Home.vue: functional components are not supported with templates, they should use render functions.")}

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-f80506f0", Component.options)
  } else {
    hotAPI.reload("data-v-f80506f0", Component.options)
  }
})()}

module.exports = Component.exports


/***/ }),

/***/ 76:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
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
            query: ''
        };
    },

    methods: {
        search: function search() {
            this.$router.push({ name: 'search', query: { query: this.query } });
        }
    },
    watch: {
        '$route.query.query': function $routeQueryQuery() {
            this.query = this.$route.query.query;
        }
    },
    created: function created() {
        this.query = this.$route.query.query || '';
    }
});

/***/ }),

/***/ 82:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "page page-welcome"
  }, [_c('div', {
    staticClass: "page-section section-search text-center"
  }, [_c('div', {
    staticClass: "container"
  }, [_c('h1', {
    staticClass: "page-section__title"
  }, [_vm._v("Поиск предприятий")]), _vm._v(" "), _c('form', {
    on: {
      "submit": function($event) {
        $event.preventDefault();
        return _vm.search($event)
      }
    }
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('input', {
    directives: [{
      name: "model",
      rawName: "v-model",
      value: (_vm.query),
      expression: "query"
    }],
    staticClass: "search",
    attrs: {
      "type": "text",
      "placeholder": "Искать предприятие..."
    },
    domProps: {
      "value": (_vm.query)
    },
    on: {
      "input": function($event) {
        if ($event.target.composing) { return; }
        _vm.query = $event.target.value
      }
    }
  }), _vm._v(" "), _c('input', {
    staticClass: "button button-primary",
    attrs: {
      "type": "submit",
      "value": "Искать"
    }
  })])])])]), _vm._v(" "), _vm._m(0), _vm._v(" "), _c('div', {
    staticClass: "page-section section-reg text-center"
  }, [_c('div', {
    staticClass: "container"
  }, [_c('h1', {
    staticClass: "page-section__title"
  }, [_vm._v("Чего ты ждешь? Зарегистрируйся скорее и получи расширенный доступ к нашим возможностям!")]), _vm._v(" "), _c('form', {
    on: {
      "submit": function($event) {
        $event.preventDefault();
        return _vm.search($event)
      }
    }
  }, [_vm._m(1)])])])])
},staticRenderFns: [function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "page-section section-adventages text-center"
  }, [_c('div', {
    staticClass: "container"
  }, [_c('h1', {
    staticClass: "page-section__title"
  }, [_vm._v("Лучший сервис для поиска информации о предприятии")]), _vm._v(" "), _c('div', {
    staticClass: "page-section__blocks"
  }, [_c('div', {
    staticClass: "block"
  }, [_c('div', {
    staticClass: "block__preview"
  }, [_c('img', {
    attrs: {
      "src": "/images/search-icon.png",
      "alt": ""
    }
  })]), _vm._v(" "), _c('h3', {
    staticClass: "block__title"
  }, [_vm._v("Актуальные данные")]), _vm._v(" "), _c('p', {
    staticClass: "block__description"
  }, [_vm._v("Наши базы предприятий обновляются каждый день")])]), _vm._v(" "), _c('div', {
    staticClass: "block"
  }, [_c('div', {
    staticClass: "block__preview"
  }, [_c('img', {
    attrs: {
      "src": "/images/success.png",
      "alt": ""
    }
  })]), _vm._v(" "), _c('h3', {
    staticClass: "block__title"
  }, [_vm._v("Довольные клиенты")]), _vm._v(" "), _c('p', {
    staticClass: "block__description"
  }, [_vm._v("Наши клиенты всегда находят здесь то что ищут")])]), _vm._v(" "), _c('div', {
    staticClass: "block"
  }, [_c('div', {
    staticClass: "block__preview"
  }, [_c('img', {
    attrs: {
      "src": "/images/easy.png",
      "alt": ""
    }
  })]), _vm._v(" "), _c('h3', {
    staticClass: "block__title"
  }, [_vm._v("Удобно использовать")]), _vm._v(" "), _c('p', {
    staticClass: "block__description"
  }, [_vm._v("Наш сервис очень прост и легок в использовании")])])])])])
},function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "form-group"
  }, [_c('input', {
    staticClass: "reg",
    attrs: {
      "type": "text",
      "placeholder": "Введите ваш E-mail..."
    }
  }), _vm._v(" "), _c('input', {
    staticClass: "button button-primary",
    attrs: {
      "type": "submit",
      "value": "Зарегистрироваться"
    }
  })])
}]}
module.exports.render._withStripped = true
if (false) {
  module.hot.accept()
  if (module.hot.data) {
     require("vue-hot-reload-api").rerender("data-v-f80506f0", module.exports)
  }
}

/***/ })

});