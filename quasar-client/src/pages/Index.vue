<template>
  <q-page class="flex flex-center" id="top-level">
    <CitiesForm
      @cities-changed="citiesChanged"
      @city-added="cityAdded"
      @temp-bounds-changed="tempBoundsChanged"
    />

    <div class="row">
      <MonthlyWeather
        :weatherData="weatherData"
        :tooCold="tempBounds['low']"
        :tooHot="tempBounds['high']"
      />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import CitiesForm from "./../components/CitiesForm.vue";
import MonthlyWeather from "./../components/MonthlyWeather.vue";

export default defineComponent({
  name: "PageIndex",
  data() {
    return {
      weatherData: [],
      tempBounds: { low: 33, high: 85 },
    };
  },
  components: {
    CitiesForm,
    MonthlyWeather,
  },
  methods: {
    citiesChanged(weatherData) {
      this.weatherData = weatherData;
    },
    cityAdded(cityWeatherData) {
      this.weatherData.push(cityWeatherData);
    },
    tempBoundsChanged(tempBounds) {
      this.tempBounds = tempBounds;
    },
  },
});
</script>

<style>
#top-level {
  border: 50px;
}
</style>
