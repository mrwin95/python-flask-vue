import Vue from 'vue';
import vueRouter from 'vue-router';
import Ping from '../components/Ping.vue';
import BookList from '../components/books/ListBook.vue';

Vue.use(vueRouter);

export default new vueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'BookList',
            component: BookList
        },
    
        {
            path: '/ping',
            name: 'Ping',
            component: Ping
        }
    ]
});

