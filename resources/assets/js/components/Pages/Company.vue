<template>
    <div>
        <div class="company-card">
            <div v-if="status == 'loading'" class="loading">
                Загрузка...
            </div>
            <div v-if="status == 'not-found'" class="not-found">
                По вашему запросу ничего не найдено
            </div>
            <div v-if="status == 'done'" class="company">
                <h1 class="company__name">
                    {{ results.company.name_ru }}
                </h1>
                <p class="company__activity">
                    <b>{{ results.company.activity_ru }}</b>
                </p>
                <p class="company__address">
                    Юридический адрес: {{ results.company.address }}
                </p>
                <p class="company__ceo" @click="ceoInfo()">
                    Руководитель: {{ results.company.CEO }}
                </p>
                <div v-if="this.ceoInfoOpen">
                    <div class="director">
                        <hr>
                        <h3 class="director__title"> {{ results.company.CEO }}</h3>
                        <p class="director__old">Старый директор:
                            <span v-if="results.old[0].CEO != results.company.CEO">
                                    <b>{{ results.old[0].CEO }}</b>
                                </span>
                            <span v-else>
                                    Нет
                                </span>
                        </p>
                        <p class="director__terror">
                            В базе террористов :
                            <!--<span v-if="results.bad == 0" class="green">Нет</span>-->
                            <!--<span v-else class="red">Есть</span>-->
                        </p>
                        <hr>
                    </div>
                </div>

                <p class="company__date">
                    Дата основания: {{ results.company.register_date }}
                </p>
                <p class="company__bin">
                    БИН: {{ results.company.BIN }}
                </p>
                <p class="company__oked">
                    ОКЭД: {{ results.company.economic_activity_code }}
                </p>
                <p class="company__kato">
                    КАТО: {{ results.company.territory_code }}
                </p>
                <p class="company__status">
                    Статус:
                    <span v-if="results.company.active == 1" class="active">В работе</span>
                    <span v-else>Не работает</span>
                </p>
                <br><br><br>

                <p class="company__bad">
                    В базе ненадежных компаний :
                    <span v-if="results.bad == 0" class="green">Нет</span>
                    <span v-else class="red">Есть</span>
                </p>

                <p class="company__bankrot">
                    В базе банкротов :
                    <span v-if="results.bankrot == 0" class="green">Нет</span>
                    <span v-else class="red">Есть</span>
                </p>

                <p class="company__exbankrot">
                    В базе бывших банкротов :
                    <span v-if="results.exbankrot == 0" class="green">Нет</span>
                    <span v-else class="red">Есть</span>
                </p>

                <p class="company__good">
                    В базе надежных предприятий :
                    <span v-if="results.good == 0" class="orange">Нет</span>
                    <span v-else class="green">Есть</span>
                </p>

                <p class="company__lie">
                    В базе лжепредприятий :
                    <span v-if="results.lie == 0" class="green">Нет</span>
                    <span v-else class="red">Есть</span>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        data(){
            return {
                companyId: '',
                status: 'empty',
                results: {
                    company: {},
                },
                ceoInfoOpen: false,
            }
        },
        methods: {
            getData() {
                this.status = 'loading';
                this.companyId = this.$route.params.companyId;

                axios.get('/backend/company/' + this.companyId)
                    .then((response) => {
                        this.results = response.data;
                        this.results.length == 0 ? this.status = 'not-found' : this.status = 'done';
                        console.log(this.results);
                    })
                    .catch(function (error) {
                        console.log(error);
                        this.status = 'error';
                    });

            },
            ceoInfo(){
                this.ceoInfoOpen = !this.ceoInfoOpen;


            }
        },
        created() {
            this.getData();
        },
        watch : {
            '$route.params.companyId'(){
                this.getData();
            }
        },
    }
</script>