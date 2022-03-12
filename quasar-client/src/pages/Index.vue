<template>
  <q-page class="flex flex-center">
    <div class="row">
      <CitiesForm
        @cities-changed="citiesChanged"
        @temp-bounds-changed="tempBoundsChanged"
      />
    </div>
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
      bob: "hi bob",
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
    tempBoundsChanged(tempBounds) {
      this.tempBounds = tempBounds;
    },
  },
});
</script>
