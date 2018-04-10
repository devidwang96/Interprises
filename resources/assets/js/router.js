import VueRouter from 'vue-router';
import { store } from './store';

const routes = [
    {
        path: '/',
        name: 'home',
        component: resolve => {
            require.ensure(['./components/Pages/Home.vue'], () => {
                resolve(require('./components/Pages/Home.vue'))
            })
        }
    },
    {
        path: '/search',
        name: 'search',
        component: resolve => {
            require.ensure(['./components/Pages/Search.vue'], () => {
                resolve(require('./components/Pages/Search.vue'))
            })
        }
    },
    {
        path: '/company/:companyId',
        name: 'company',
        component: resolve => {
            require.ensure(['./components/Pages/Company.vue'], () => {
                resolve(require('./components/Pages/Company.vue'))
            })
        }
    },
    {
        path: '/about',
        name: 'about',
        component: resolve => {
            require.ensure(['./components/Pages/About.vue'], () => {
                resolve(require('./components/Pages/About.vue'))
            })
        }
    },
    {
        path: '*',
        name: 'not-found',
        component: resolve => {
            require.ensure(['./components/Pages/404.vue'], () => {
                resolve(require('./components/Pages/404.vue'))
            })
        }
    },


];

export const router = new VueRouter({
    routes,
    store,
    linkActiveClass : 'active'
});