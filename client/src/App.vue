<template>
  <div id='app'>
    <time-zone @time='submitTime'></time-zone>
  </div>
</template>

<script>
import TimeZone from './components/TimeZone.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    TimeZone
  },
  methods: {
    submitTime(value) {
      let { hour, minute, isPM } = value;
      if (isPM) {
        hour += 12
      } 
      hour = hour.toString().padStart(2, '0')
      minute = minute.toString().padStart(2, '0')
      const datetime = `2021-01-27 ${hour}:${minute}`
      const payload = {
        datetime,
        'from_TZ': 'Asia/Dacca',
        'to_TZ': 'America/Porto_Acre'
      }
      axios.post('http://localhost:9123/convert', payload)
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
