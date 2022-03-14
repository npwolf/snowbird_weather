<template>
  <!-- <q-page class="flex flex-center" id="top-level"> -->
  <!-- <q-page
    class="flex-center q-pa-lg row items-start q-gutter-md justify-center"
  >
    <q-card class="my-card">
      <q-card-section class="bg-purple text-white">
        <div class="text-h6">Our Changing Planet</div>
        <div class="text-subtitle2">by John Doe</div>
      </q-card-section>

      <q-card-actions align="center">

        <q-form class="q-gutter-md">
          <q-input type="text" label="email" />
          <q-btn color="primary" type="submit" label="Add City" />

        </q-form>
      </q-card-actions>
    </q-card>
  </q-page> -->

  <!--
  <q-page class="window-height window-width row justify-center items-center">
    <div class="column">
      <div class="row">
        <h5 class="text-h5 text-black q-my-md">Company & Co</h5>
      </div>
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <label>Email</label>
            <q-form class="q-gutter-md">
              <q-input
                square
                filled
                clearable
                v-model="email"
                type="email"
                label="email"
              />
              <label>Password</label>
              <q-input
                square
                filled
                clearable
                v-model="password"
                type="password"
                label="password"
              />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-md">
            <q-btn
              unelevated
              color="light-green-7"
              size="lg"
              class="full-width"
              label="Login"
            />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none">
            <p class="text-grey-6">Not reigistered? Created an Account</p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
 -->
  <q-page
    class="flex-center q-pa-lg row items-start q-gutter-md justify-center"
  >
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

<style></style>
