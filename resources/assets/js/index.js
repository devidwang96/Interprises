import Vue from 'vue';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import VeeValidate from 'vee-validate';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

Vue.use(VeeValidate)
Vue.use(VueRouter);
Vue.use(VueResource);

Vue.component(
    'app',
    require('./components/App.vue')
);
