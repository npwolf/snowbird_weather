<template>
  <q-page class="q-pa-sm main-page">
    <div class="col">
      <div class="city-temp q-gutter-md">
        <AddCity />
        <IdealTemp />
      </div>
      <div class="row justify-center">&nbsp;</div>
      <div class="row-auto">
        <MonthlyWeather />
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import AddCity from "./../components/AddCity.vue";
import MonthlyWeather from "./../components/MonthlyWeather.vue";
import IdealTemp from "./../components/IdealTemp.vue";

export default defineComponent({
  name: "PageIndex",
  data() {
    return {};
  },
  components: {
    AddCity,
    IdealTemp,
    MonthlyWeather,
  },
});
</script>

<style>
.main-page {
  max-width: 100%;
}

.city-temp {
  display: flex;
  flex-direction: row;
}

/* Responsive layout - makes a one column layout instead of a two-column layout */
@media (max-width: 800px) {
  .city-temp {
    flex-direction: column;
  }
}
</style>
