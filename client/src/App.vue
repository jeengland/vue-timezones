<template>
  <div class='bg-secondary' id='app'>
    <time-zone @time='submitTime'></time-zone>
    <div class='card m-1 mx-auto mt-3 bg-dark text-light' style='width: 40rem' v-if='response'>
      <div class='card-body text-center'>
        <p style='font-size: 1.5rem'>At</p>
        <p style='font-size: 1.2rem'>{{ input.hour }}:{{ input.minute.toString().padStart(2, '0') }} {{ input.isPM ? 'PM' : 'AM' }} on {{ input.date }} in the {{ input.from_TZ }} timezone</p>
        <p style='font-size: 1.5rem'>it is</p>
        <p style='font-size: 1.2rem'>{{ conHour }}:{{ conMin }} on {{ response.time.slice(0, 10) }} in the {{ input.to_TZ }} timezone.</p>
        <div class='d-flex row justify-content-center'>
          <label class="sr-only">Reload page</label>
          <button class='btn btn-secondary' @click="reloadPage">Convert Again</button>
        </div>
      </div>
    </div>
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
  data() {
    return {
      input: null,
      response: null,
      conHour: null,
      conMin: null
    }
  },
  methods: {
    submitTime(value) {
      this.response = ''
      this.input = value
      let { hour, minute, isPM, from_TZ, to_TZ, date } = value;
      if (isPM) {
        hour = parseInt(hour) + 12
      } 
      hour = hour.toString().padStart(2, '0')
      minute = minute.toString().padStart(2, '0')
      const datetime = `${date} ${hour}:${minute}`
      const payload = {
        datetime,
        from_TZ,
        to_TZ
      }
      axios.post('http://localhost:9123/convert', payload)
        .then((response) => {
          console.log(response.data)
          this.response = response.data
          let conHour = parseInt(response.data.time.slice(11, 13))
          let pm = 'AM'
          if (conHour > 11) {
              pm = 'PM'
          }
          if (conHour > 12) {
              conHour -= 12
          }
          if (conHour == 0) {
              conHour = 12;
          }
          let conMin = response.data.time.slice(14, 16) + ' ' + pm
          this.conHour = conHour
          this.conMin = conMin
        })
        .catch((error) => {
          console.error(error)
        })
    },
    reloadPage() {
      location.reload()
    }
  }
}
</script>

