<template>
    <div class="page page-welcome">

        <div class="page-section section-search text-center">
            <div class="container">
                <h1 class="page-section__title">Поиск предприятий</h1>
                <form @submit.prevent="search">

                    <div class="form-group">
                        <input type="text"
                               class="search"
                               v-model="query"
                               placeholder="Искать предприятие...">
                        <input class="button button-primary" type="submit" value="Искать">
                    </div>

                </form>
            </div>
        </div>

        <div class="page-section section-adventages text-center">
            <div class="container">
                <h1 class="page-section__title">Лучший сервис для поиска информации о предприятии</h1>
                <div class="page-section__blocks">
                    <div class="block">
                        <div class="block__preview"><img src="/images/search-icon.png" alt=""></div>
                        <h3 class="block__title">Актуальные данные</h3>
                        <p class="block__description">Наши базы предприятий обновляются каждый день</p>
                    </div>
                    <div class="block">
                        <div class="block__preview"><img src="/images/success.png" alt=""></div>
                        <h3 class="block__title">Довольные клиенты</h3>
                        <p class="block__description">Наши клиенты всегда находят здесь то что ищут</p>
                    </div>
                    <div class="block">
                        <div class="block__preview"><img src="/images/easy.png" alt=""></div>
                        <h3 class="block__title">Удобно использовать</h3>
                        <p class="block__description">Наш сервис очень прост и легок в использовании</p>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="$store.state.authState == 'guest'" class="page-section section-reg text-center">
            <div class="container">
                <h1 class="page-section__title">Чего ты ждешь? Зарегистрируйся скорее и получи расширенный доступ к нашим возможностям!</h1>
                <router-link v-if="$store.state.authState == 'guest'" class="button button-primary" :to="{ name: 'register'}">
                    Зарегистрироваться
                </router-link>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        data(){
            return {
                query : ''
            }
        },
        methods:{
            search(){
                this.$router.push({name : 'search', query : {query : this.query}})
            },
        },
        watch : {
            '$route.query.query'(){
                this.query = this.$route.query.query;
            },
        },
        created(){
            this.query = this.$route.query.query || '';
        },

    }
</script>