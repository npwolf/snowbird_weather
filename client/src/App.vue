<template>
  <div class="container-lg">
<div class="px-3 py-2 bg-dark text-white">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a href="/" class="d-flex align-items-center my-2 my-lg-0 me-lg-auto text-white text-decoration-none">
            <span class="fs-4">Snowbird Weather</span>
          </a>

          <ul class="nav col-12 col-lg-auto my-2 justify-content-center my-md-0 text-small">
            <li>
              <a href="#" class="nav-link text-white">
                About
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  <div class="row">
    <CitiesForm @cities-changed="citiesChanged"/>
  </div>
  <div class="row">
  </div>
  <MonthlyWeather :weatherData="weatherData"/>
  </div>
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
}
</style>
