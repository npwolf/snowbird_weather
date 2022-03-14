<template>
  <q-page
    class="flex-center q-pa-lg row items-start q-gutter-md justify-center"
  >
    <div class="column">
      <div class="row justify-center">
        <CitiesForm
          @cities-changed="citiesChanged"
          @city-added="cityAdded"
          @temp-bounds-changed="tempBoundsChanged"
        />
      </div>
      <div class="row flex">
        <MonthlyWeather
          :weatherData="weatherData"
          :tooCold="tempBounds['low']"
          :tooHot="tempBounds['high']"
        />
      </div>
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
      weatherData: [
        {
          january_high: 73,
          january_low: 67,
          february_high: 74,
          february_low: 69,
          march_high: 74,
          march_low: 70,
          april_high: 78,
          april_low: 75,
          may_high: 81,
          may_low: 78,
          june_high: 84,
          june_low: 81,
          july_high: 85,
          july_low: 82,
          august_high: 85,
          august_low: 83,
          september_high: 85,
          september_low: 82,
          october_high: 82,
          october_low: 79,
          november_high: 78,
          november_low: 74,
          december_high: 75,
          december_low: 71,
          name: "Key Largo",
          state: "FL",
        },
        {
          january_high: 60,
          january_low: 43,
          february_high: 61,
          february_low: 44,
          march_high: 66,
          march_low: 47,
          april_high: 72,
          april_low: 51,
          may_high: 78,
          may_low: 56,
          june_high: 89,
          june_low: 64,
          july_high: 93,
          july_low: 71,
          august_high: 93,
          august_low: 72,
          september_high: 87,
          september_low: 67,
          october_high: 77,
          october_low: 58,
          november_high: 67,
          november_low: 49,
          december_high: 58,
          december_low: 42,
          name: "Palm Springs",
          state: "CA",
        },
        {
          january_high: 47,
          january_low: 26,
          february_high: 53,
          february_low: 28,
          march_high: 59,
          march_low: 31,
          april_high: 66,
          april_low: 36,
          may_high: 73,
          may_low: 42,
          june_high: 81,
          june_low: 47,
          july_high: 90,
          july_low: 53,
          august_high: 89,
          august_low: 52,
          september_high: 83,
          september_low: 47,
          october_high: 74,
          october_low: 38,
          november_high: 58,
          november_low: 30,
          december_high: 47,
          december_low: 26,
          name: "Yosemite National Park",
          state: "CA",
        },
      ],
      tempBounds: { low: 33, high: 80 },
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

<style></style>
