<template>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-xs-6 col-xs-offset-3">

                    <div v-if="$store.state.authState == 'guest'">


                        <form @submit.prevent="postForm()">

                            <div style="border:2px solid red; padding:15px;" v-if="formErrors != null">
                                <p style="color:red"><b>Ошибки</b></p>
                                <p style="color:red" v-for="error in formErrors">
                                    {{ error[0] }}
                                </p>
                            </div>

                            <h2 class="text-center">Зарегистрироваться</h2>

                            <div v-html="token" class="hidden">

                            </div>

                            <div class="form-group">
                                <label for="field_1">Введите имя</label>
                                <input required type="text" id="field_1" class="form-control" v-model="formData.name"
                                       placeholder="Введите имя...">
                            </div>
                            <div class="form-group">
                                <label for="field_2">Введите e-mail</label>
                                <input required type="email" id="field_2" class="form-control" v-model="formData.email"
                                       placeholder="Введите e-mail...">
                            </div>
                            <div class="form-group">
                                <label for="field_3">Введите пароль</label>
                                <input required type="password" id="field_3" class="form-control" v-model="formData.pass"
                                       placeholder="Введите пароль...">
                            </div>
                            <div class="form-group">
                                <label for="field_4">Повторите пароль</label>
                                <input required type="password" id="field_4" class="form-control" v-model="formData.passRepeat"
                                       placeholder="Повторите пароль...">
                            </div>
                            <br><br><br><br>
                            <div class="form-group text-center">
                                <input class="button button-primary" type="submit" value="Зарегистрироваться">
                                <br><br>
                                <span>Или</span>
                                <br><br>

                                <router-link class="button button-primary" :to="{ name: 'login'}">
                                    Войти
                                </router-link>
                            </div>

                        </form>


                    </div>

                    <div v-else>
                        <h2 class="text-center">Вы успешно вошли в систему</h2>
                    </div>

                </div>
            </div>

        </div>

    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                token: '',
                formErrors: null,
                formData: {
                    name: '',
                    email: '',
                    pass: '',
                    passRepeat: '',
                }
            }
        },
        methods: {
            getAuthStatus() {
                axios.get('/backend/get_auth_status')
                    .then((response) => {
                        this.$store.state.authState = response.data;
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
            getToken() {
                axios.get('/backend/get_token')
                    .then((response) => {
                        this.token = response.data;
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
            postForm() {
                axios.post('/register', {
                    name: this.formData.name,
                    email: this.formData.email,
                    password: this.formData.pass,
                    password_confirmation: this.formData.passRepeat,
                    // _token: this.token
                })
                    .then((response) => {
                        console.log(response);
                        this.$store.state.authState = 'auth';
                    })
                    .catch((error) => {
                        console.log(error.response);
                        this.formErrors = error.response.data.errors;
                    });
            },
            logOut() {
                axios.post('/logout', {
                    _token: this.token
                })
                    .then(function (response) {
                        this.$store.state.authState = 'guest';
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        },
        created() {
            this.getToken();
            this.getAuthStatus();
        },
    }
</script>