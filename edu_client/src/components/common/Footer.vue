<template>
    <div class="footer">
        <ul class="footer ul">
            <li class="footer ul li"  v-for="(nav, key) in Nav_list" :key="key">
                <p v-if="nav.position!='1'" class="footer p">{{nav.title}}</p>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        data() {
            return {
                Nav_list: [],
            }
        },
        methods: {
            get_all_Nav() {
                this.$axios({
                    url: this.$settings.HOST + 'home/nav/',
                    method: "get",
                }).then(res => {
                    // 当前请求的返回值可以通过res接受到
                    this.Nav_list = res.data;
                }).catch(error => {
                    console.log(error);
                })
            },
        },
        // 在当前页面渲染之前将数据获取并赋值给 data
        created() {
            this.get_all_Nav();
        }
    }
</script>

<style scoped>
    .footer {
        width: 100%;
        height: 128px;
        background: #25292e;
        color: #fff;
    }

    .footer ul {
        margin: 0 auto 16px;
        padding-top: 38px;
        width: 810px;
    }

    .footer ul li {
        float: left;
        width: 112px;
        margin: 0 10px;
        text-align: center;
        font-size: 14px;
    }

    .footer ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .footer p {
        text-align: center;
        font-size: 12px;
    }
</style>
