<template>
    <div>
        {{msg}}
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Ping',
    data(){
        return {
            msg: ''
        }
    },
    methods: {        
        pong(){
            const path = 'http://localhost:5000/ping';
            axios.get(path).then((res) => {
                this.msg = res.data
            })
            .catch((err) => {
                console.log(err);
            })            
        }
    },
    created(){
        this.pong()
    }
}
</script>