<template>
    <div>
        <site-header></site-header>

        <keep-alive>

            <router-view>

            </router-view>

        </keep-alive>

        <site-footer></site-footer>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {}
        },
        methods: {
            getAuthStatus() {
                axios.get('/backend/get_auth_status')
                    .then((response) => {
                        this.$store.state.authState = response.data;
                        console.log(this.$store.state.authState);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
        },
        created() {
            this.getAuthStatus();
        }
    }
</script>

