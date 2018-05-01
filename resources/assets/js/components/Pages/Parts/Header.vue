<template>
    <div class="header">
        <div class="container">
            <div class="header__logo pull-left">
                <router-link :to="{ name: 'home'}">
                    <img src="/images/logo.png" alt="">
                </router-link>
            </div>
            <div class="header__tools pull-right">

                <router-link v-if="$store.state.authState == 'guest'" class="button button-primary" :to="{ name: 'login'}">
                    Войти
                </router-link>

                <router-link v-if="$store.state.authState == 'guest'" class="button button-primary" :to="{ name: 'register'}">
                    Зарегистрироваться
                </router-link>

                <a @click.prevent="logOut()" href="#" v-if="$store.state.authState == 'auth'" class="button button-primary">
                    Выйти из системы
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data(){
            return {
                token: '',
            }
        },
        methods: {
            getToken() {
                axios.get('/backend/get_token')
                    .then((response) => {
                        this.token = response.data;
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
            logOut(){
                axios.post('/logout', {
                    // _token: this.token
                })
                    .then((response) => {
                        this.$store.state.authState= 'guest';
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        },
        created() {
            this.getToken();
        },
    }
</script>