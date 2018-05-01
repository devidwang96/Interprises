<template>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-xs-6 col-xs-offset-3">
                    <div v-if="$store.state.authState == 'guest'">


                        <div style="border:2px solid red; padding:15px;" v-if="formErrors != null">
                            <p style="color:red"><b>Ошибки</b></p>
                            <p style="color:red" v-for="error in formErrors">
                                {{ error[0] }}
                            </p>
                        </div>


                        <form @submit.prevent="postForm()">
                            <h2 class="text-center">Войти в систему</h2>
                            <div v-html="token" class="hidden">

                            </div>

                            <div class="form-group">
                                <label for="auth-email">Введите e-mail</label>
                                <input required type="email" id="auth-email" class="form-control" v-model="formData.email" placeholder="Введите e-mail...">
                            </div>

                            <div class="form-group">
                                <label for="auth-password">Введите пароль</label>
                                <input required type="password" id="auth-password" class="form-control" v-model="formData.pass" placeholder="Введите пароль...">
                            </div>

                            <div class="form-group text-center">
                                <br><br>
                                <input class="button button-primary" type="submit" value="Войти в систему">
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
                    email: '',
                    pass: '',
                }
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
            postForm() {
                axios.post('/login', {
                    password: this.formData.pass,
                    email: this.formData.email,
                })
                    .then((response) => {
                        this.$store.state.authState = 'auth';
                    })
                    .catch((error) => {
                        this.formErrors = error.response.data.errors;
                    });
            },
        },
        created() {
            this.getToken();
        },
    }
</script>