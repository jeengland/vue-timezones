<template>
  <div id='app'>
    <time-zone></time-zone>
  </div>
</template>

<script>
import TimeZone from './components/TimeZone.vue'

export default {
  name: 'App',
  components: {
    TimeZone
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
