<template>
    <div class="cart_item">
        <div class="cart_column column_1">
            <el-checkbox class="my_el_checkbox" v-model="course.selected"></el-checkbox>
        </div>
        <div class="cart_column column_2">
            <img :src="course.course_img" alt="">
            <span><router-link :to="'/course/detail/'+course.id">{{course.name}}</router-link></span>
        </div>
        <div class="cart_column column_3">
            <el-select v-model="course.expire_id" size="mini" placeholder="请选择购买有效期" class="my_el_select">
                <el-option
                    :label="item.expire_text" :value="item.id" :key="item.id" v-for="item in course.expire_list">
                </el-option>
            </el-select>
        </div>
        <div class="cart_column column_4">{{course.real_price}}</div>
        <div class="cart_column column_4" @click="delete_course">删除</div>

    </div>
</template>

<script>
    export default {
        name: "CartItem",
        //接受父组件的数据
        props: ["course"],
        watch: {
            // 通过监测select的变化来改变当前的选中状态
            'course.selected': function () {
                this.change_select()
            },
            // 切换课程有效期
            'course.expire_id': function () {
                // 后台发送请求切换状态
                this.change_expire()
            }
        },
        data() {
            return {
                expire: "1",
            }
        },
        methods: {
            // 状态切换
            change_select() {
                let token = localStorage.user_token || sessionStorage.user_token;
                this.$axios.patch(`${this.$settings.HOST}cart/option/`, {
                    selected: this.course.selected,
                    course_id: this.course.id,
                }, {
                    headers: {
                        "Authorization": "jwt " + token,
                    }
                }).then(res => {
                    this.$message.success(res.data.message);
                    this.$emit('change_expire');
                }).catch(error => {
                    console.log(error.response);
                })
            },
            delete_course() {
                let token = localStorage.user_token || sessionStorage.user_token;
                this.$axios({
                    url:this.$settings.HOST+"cart/option/",
                    method:"delete",
                    data:{
                        course_id:this.course.id,
                    },
                    headers: {
                        "Authorization": "jwt " + token,
                    },
                }).then(res => {
                    this.$emit('delete_course');
                    this.$message.success(res.data.message);
                }).catch(error => {
                    console.log(error);
                })
            },

            // 改变redis中的课程有效期
            change_expire() {
                let token = sessionStorage.user_token || localStorage.user_token;
                this.$axios.put(`${this.$settings.HOST}cart/option/`, {
                    expire_id: this.course.expire_id,
                    course_id: this.course.id
                }, {
                    headers: {
                        "Authorization": "jwt " + token,
                    }
                }).then(response => {
                    console.log(response.data);
                    // 更新切换有效期后课程的价格
                    this.course.real_price = response.data.real_price;
                    this.$message.success("切换有效期成功");
                    this.$emit('change_expire');
                }).catch(error => {
                    console.log(error);
                })
            },

        }
    }
</script>

<style scoped>
    .cart_item::after {
        content: "";
        display: block;
        clear: both;
    }

    .cart_column {
        float: left;
        height: 250px;
    }

    .cart_item .column_1 {
        width: 88px;
        position: relative;
    }

    .my_el_checkbox {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        top: 0;
        margin: auto;
        width: 16px;
        height: 16px;
    }

    .cart_item .column_2 {
        padding: 67px 10px;
        width: 520px;
        height: 116px;
    }

    .cart_item .column_2 img {
        width: 175px;
        height: 115px;
        margin-right: 35px;
        vertical-align: middle;
    }

    .cart_item .column_3 {
        width: 197px;
        position: relative;
        padding-left: 10px;
    }

    .my_el_select {
        width: 117px;
        height: 28px;
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto;
    }

    .cart_item .column_4 {
        padding: 67px 10px;
        height: 116px;
        width: 142px;
        line-height: 116px;
    }
</style>
