import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/Login";
import Register from "../components/Register";
import Course from "../components/Course";
import CourseDetail from "../components/CourseDetail";
import Cart from "../components/Cart";
import CartItem from "../components/CartItem";
import Order from "../components/Order";


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/home',
            name: 'Home',
            component: Home
        },
        {
            path: '/user/login/',
            name: 'login',
            component: Login
        },
        {
            path: '/user/register/',
            name: 'register',
            component: Register
        },
        {
            path: '/python',
            name:"Course",
            component: Course
        },
        {
            path: '/course/detail',
            name:"Detail",
            component: CourseDetail
        },
        {
            path: '/cart',
            name:"Cart",
            component: Cart
        },
        {
            path: '/cartitem',
            name:"CartItem",
            component: CartItem
        },
        {
            path: '/order',
            name:"Order",
            component: Order
        },
    ]
})
