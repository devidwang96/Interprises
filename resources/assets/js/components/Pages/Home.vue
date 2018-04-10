<template>
    <div>
        <h1>Поиск предприятий</h1>
        <form @submit.prevent="search">
            <input type="text"
                   v-model="query"
                   placeholder="Искать предприятие...">
            <input type="submit" value="Искать">
        </form>
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