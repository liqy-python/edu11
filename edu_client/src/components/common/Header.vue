<template>
    <div class="header-box">
        <div class="header">
            <div class="content">
                <div class="logo full-left">
                    <router-link to="/"><img src="/static/image/logo.png" alt=""></router-link>
                </div>
                <ul class="nav full-left" v-for="(nav,index) in Nav_list" :key="index">
                    <li v-if="nav.position == '1'">
                        <span><router-link :to="nav.link">{{nav.title}}</router-link></span>
                    </li>
                </ul>
                <!--          用户存在      -->
                <div class="login-bar full-right" v-if="token">
                    <div class="shop-cart full-left">
                        <img src="/static/image/" alt="">
                        <span><router-link to="/cart">{{this.$store.state.cart_length}}购物车</router-link></span>
                    </div>
                    <div class="login-box full-left">
                        <router-link to="/order/list/">个人中心</router-link>
                        &nbsp;|&nbsp;
                        <span @click="quit">退出登录</span>
                    </div>
                </div>
                <!--          用户不存在      -->
                <div class="login-bar full-right" v-else>
                    <div class="shop-cart full-left">
                        <img src="/static/image/" alt="">
                        <span><router-link to="/cart">购物车</router-link></span>
                    </div>
                    <div class="login-box full-left">
                        <router-link to="/user/login/">登录</router-link>
                        &nbsp;|&nbsp;
                        <router-link to="/user/register/">注册</router-link>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Header",
        data() {
            return {
                Nav_list: [],
                token: "",
            }
        },
        methods: {
            get_token() {
                this.token = localStorage.user_token || sessionStorage.user_token;
                // return this.token;
            },
            get_all_Nav() {
                this.$axios({
                    url: this.$settings.HOST + 'home/nav/',
                    method: "get",
                }).then(res => {
                    // 当前请求的返回值可以通过res接受到
                    console.log(res.data);
                    this.Nav_list = res.data;
                }).catch(error => {
                    console.log(error);
                })
            },
            quit(){
                localStorage.clear();
                sessionStorage.clear();
                this.$router.push("/user/login/")

            },
        },
        // 在当前页面渲染之前将数据获取并赋值给 data
        created() {
            this.get_all_Nav();
            this.get_token()
        }
    }
</script>

<style scoped>
    .header-box {
        height: 80px;
    }

    .header {
        width: 100%;
        height: 80px;
        box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        margin: auto;
        z-index: 99;
        background: #fff;
    }

    .header .content {
        max-width: 1200px;
        width: 100%;
        margin: 0 auto;
    }

    .header .content .logo {
        height: 80px;
        line-height: 80px;
        margin-right: 50px;
        cursor: pointer; /* 设置光标的形状为爪子 */
    }

    .header .content .logo img {
        vertical-align: middle;
    }

    .header .nav li {
        float: left;
        height: 80px;
        line-height: 80px;
        margin-right: 30px;
        font-size: 16px;
        color: #4a4a4a;
        cursor: pointer;
    }

    .header .nav li span {
        padding-bottom: 16px;
        padding-left: 5px;
        padding-right: 5px;
    }

    .header .nav li span a {
        display: inline-block;
    }

    .header .nav li .this {
        color: #4a4a4a;
        border-bottom: 4px solid #ffc210;
    }

    .header .nav li:hover span {
        color: #000;
    }

    .header .login-bar {
        height: 80px;
    }

    .header .login-bar .shop-cart {
        margin-right: 20px;
        border-radius: 17px;
        background: #f7f7f7;
        cursor: pointer;
        font-size: 14px;
        height: 28px;
        width: 100px;
        margin-top: 30px;
        line-height: 32px;
        text-align: center;
    }

    .header .login-bar .shop-cart:hover {
        background: #f0f0f0;
    }

    .header .login-bar .shop-cart img {
        width: 15px;
        margin-right: 4px;
        margin-left: 6px;
    }

    .header .login-bar .shop-cart span {
        margin-right: 6px;
    }

    .header .login-bar .login-box {
        margin-top: 33px;
    }

    .header .login-bar .login-box span {
        color: #4a4a4a;
        cursor: pointer;
    }

    .header .login-bar .login-box span:hover {
        color: #000000;
    }

    a {
        text-decoration: none;
        color: #333;
    }

    .member {
        display: inline-block;
        height: 34px;
        margin-left: 20px;
    }

    .member img {
        width: 26px;
        height: 26px;
        border-radius: 50%;
        display: inline-block;
    }

    .member img:hover {
        border: 1px solid yellow;
    }

    .header .login-bar .login-box1 {
        margin-top: 16px;
    }

    a:hover {
        display: inline-block;
    }
</style>
