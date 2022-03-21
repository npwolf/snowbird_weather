<template>
  <div class="ideal-temp q-gutter-md">
    <q-card class="">
      <q-card-section align="center">
        <div class="row items-center q-gutter-md">
          <label class="q-ma-md">Ideal Temperature Range</label>
          <q-range
            v-model="tempRange"
            :min="0"
            :max="100"
            :left-label-value="'Low: ' + tempRange.min + 'F'"
            :right-label-value="'High: ' + tempRange.max + 'F'"
            label-always
            color="green"
            left-label-color="blue"
            right-label-color="red"
            @change="changeTemp"
          />
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { useWeatherStore } from "./../stores/weather";
import { mapStores } from "pinia";

export default {
  name: "IdealTemp",
  data() {
    return {
      tempRange: null,
    };
  },
  computed: {
    ...mapStores(useWeatherStore),
  },
  created() {
    this.tempRange = {
      min: this.weatherStore.tempMin,
      max: this.weatherStore.tempMax,
    };
  },
  methods: {
    changeTemp(newTemp) {
      // The reason to set these here is when I tried
      // a computed variable, it updated too frequently
      // and created a sluggish interface
      if (this.weatherStore.tempMin != newTemp.min) {
        this.weatherStore.tempMin = newTemp.min;
      }
      if (this.weatherStore.tempMax != newTemp.max) {
        this.weatherStore.tempMax = newTemp.max;
      }
    },
  },
};
</script>
<style scoped>
.ideal-temp {
  display: flex;
  flex-direction: row;
}
</style>
