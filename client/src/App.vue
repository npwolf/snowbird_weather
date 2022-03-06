<template>
  <h1>Snowbird Weather</h1>
  <CitiesForm @cities-changed="citiesChanged"/>
  <MonthlyWeather :weatherData="weatherData"/>
</template>

<script>
import MonthlyWeather from './components/MonthlyWeather.vue'
import CitiesForm from './components/CitiesForm.vue'

export default {
  name: 'App',
  data() {
    return {
      weatherData: [],  
    }
  },
  components: {
    MonthlyWeather,
    CitiesForm,
  },
  methods: {
    citiesChanged(weatherData) {
      console.log(JSON.stringify(event))
      this.weatherData = weatherData
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
  /* Center child horizontally*/
  display: flex;
  justify-content: center;    
}
</style>
