<template>
    <div class="page page-company">
        <div class="container">
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
                    <div class="row">
                        <div class="col-md-8 company__base-info">
                            <h3>Основная информация</h3>
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
                                    <!--<p class="director__old" v-if="results.old[0] != undefined">Старый директор:-->
                                    <!--<span v-if="results.old[0].CEO != results.company.CEO">-->
                                    <!--<b>{{ results.old[0].CEO }}</b>-->
                                    <!--</span>-->
                                    <!--<span v-else>-->
                                    <!--Нет-->
                                    <!--</span>-->
                                    <!--</p>-->
                                    <p class="director__terror">
                                        В базе террористов :
                                        <span v-if="results.ceo.terror == 0" class="marker green">Нет</span>
                                        <span v-else class="marker red">Есть</span>
                                    </p>

                                    <div v-if="results.ceo.interprises.length > 1" class="director__interprises">
                                        <h3>{{ results.company.CEO }} Также является владельцем следующих {{results.ceo.interprises.length}} предприятий ...</h3>
                                        <p v-for="(item, index) in results.ceo.interprises">
                                            <router-link :to="{ name: 'company', params: { companyBin: item.id }}">
                                                {{ item.name_ru }}
                                            </router-link>
                                        </p>
                                    </div>

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
                                <span v-if="results.company.active == 1" class="marker green active">В работе</span>
                                <span class="marker red" v-else>Не работает</span>
                            </p>


                            <div class="company__markers">
                                <p class="company__bad">
                                    В базе ненадежных компаний :
                                    <span v-if="results.bad == 0" class="marker green">Нет</span>
                                    <span v-else class="marker red">Есть</span>
                                </p>

                                <p class="company__bankrot">
                                    В базе банкротов :
                                    <span v-if="results.bankrot == 0" class="marker green">Нет</span>
                                    <span v-else class="marker red">Есть</span>
                                </p>

                                <p class="company__exbankrot">
                                    В базе бывших банкротов :
                                    <span v-if="results.exbankrot == 0" class="marker green">Нет</span>
                                    <span v-else class="marker red">Есть</span>
                                </p>

                                <p class="company__good">
                                    В базе надежных предприятий :
                                    <span v-if="results.good == 0" class="marker orange">Нет</span>
                                    <span v-else class="marker green">Есть</span>
                                </p>

                                <p class="company__lie">
                                    В базе лжепредприятий :
                                    <span v-if="results.lie == 0" class="marker green">Нет</span>
                                    <span v-else class="marker red">Есть</span>
                                </p>
                            </div>
                        </div>
                        <div class="col-md-4 company__history">
                            <h3>История компании</h3>
                            <p v-if="historyStatus == 'empty'">
                                У данной компании еще пока нет изменений
                            </p>
                            <div v-if="historyStatus == 'success'">
                                <div class="history" v-for="(item, index) in history">
                                    <button class="collapsed" data-toggle="collapse" :data-target="'#history_' + index">{{ item.date }}
                                    <i><img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkJz48c3ZnIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDUwIDUwIiBoZWlnaHQ9IjUwcHgiIGlkPSJMYXllcl8xIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA1MCA1MCIgd2lkdGg9IjUwcHgiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxyZWN0IGZpbGw9Im5vbmUiIGhlaWdodD0iNTAiIHdpZHRoPSI1MCIvPjxwb2x5Z29uIHBvaW50cz0iNDcuMjUsMTUgNDUuMTY0LDEyLjkxNCAyNSwzMy4wNzggNC44MzYsMTIuOTE0IDIuNzUsMTUgMjUsMzcuMjUgIi8+PC9zdmc+" alt=""></i></button>
                                    <div :id="'history_' + index" class="collapse">
                                        <p v-if="item.field == 'CEO'">
                                            Был директор: <br>
                                            <b>{{ item.oldValue }}</b>
                                        </p>
                                        <p v-if="item.field == 'name_ru'">
                                            Было название: <br>
                                            <b>{{ item.oldValue }}</b>
                                        </p>
                                        <p v-if="item.field == 'address'">
                                            Был адрес: <br>
                                            <b>{{ item.oldValue }}</b>
                                        </p>
                                        <p v-if="item.field == 'active'">
                                            Компания <b v-if="item.oldValue == 1"> работала</b><b v-if="item.oldValue == 0">не работала</b>
                                        </p>
                                        <p v-if="item.field == 'territory_code'">
                                        Был КАТО: <br>
                                            <b>{{ item.oldValue }}</b>
                                        </p>
                                        <p v-if="item.field == 'economic_activity_code'">
                                        Был ОКЭД: <br>
                                            <b>{{ item.oldValue }}</b>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import axios from "axios";
    export default {
        data(){
            return {
                companyBin: '',
                status: 'empty',
                results: {
                    company: {},
                },
                history: {

                },
                historyStatus: 'empty',
                ceoInfoOpen: false,
            }
        },
        methods: {
            getHistory(){
                this.historyStatus = 'loading';
                axios.get('/backend/history/' + this.companyBin)
                    .then((response) => {
                        let historyResponse = response.data;
                        let historyRows  = [
                            // {
                            //     field: 'CEO',
                            //     oldValue: 'КРЫКБАЕВ АСКАР САНАТОВИЧ',
                            //     date: '12.06.17'
                            // }
                        ];
                        let historyFields = [
                            'CEO',
                            'name_ru',
                            'address',
                            'active',
                            'territory_code',
                            'economic_activity_code',
                        ];


                        for(let i in historyResponse){
                            for(let j in historyFields){
                                if(historyResponse[i][historyFields[j]] != this.results.company[historyFields[j]]){
                                    let push = true;
                                    console.log(historyFields[j]);
                                    console.log(historyResponse[i][historyFields[j]]);
                                    console.log(historyResponse[i].update_date);
                                    // console.log(this.results.company[historyFields[j]]);

                                    for(let k in historyRows){
                                        if(historyRows[k].oldValue == historyResponse[i][historyFields[j]]){
                                            console.log('Нет! Такой уже есть');
                                            push = false;
                                        }
                                    }
                                    if(push){
                                        historyRows.push(
                                            {
                                                field: historyFields[j],
                                                oldValue: historyResponse[i][historyFields[j]],
                                                date: historyResponse[i].update_date,
                                            }
                                        );
                                    }
                                }
                            }
                        }

                        console.log('Сформированная история компании:');
                        console.log(historyRows);
                        console.log(historyRows.length)
                        if(historyRows.length > 0){
                            this.historyStatus = 'success';
                            this.history = historyRows;
                        } else {
                            this.historyStatus = 'empty';
                        }
                    })
                    .catch((error)=> {
                        console.log(error);
                        this.historyStatus = 'error';
                    });
            },
            getData() {
                this.status = 'loading';
                this.companyBin = this.$route.params.companyBin;

                axios.get('/backend/company/' + this.companyBin)
                    .then((response) => {
                        this.results = response.data;
                        this.results.length == 0 ? this.status = 'not-found' : this.status = 'done';
                        console.log(this.results);
                        this.getHistory();
                    })
                    .catch((error)=> {
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
            '$route.params.companyBin'(){
                this.getData();
            }
        },
    }
</script>