<template>
  <div class="cities-form">
    <div class="form-group">
      <form class="form-inline" @submit.prevent="onSubmit">
        <div class="row">
          <div class="col">
            <label>Low Temperature</label>
          </div>
          <div class="col">
            <input
              type="number"
              @change="setTempBounds"
              v-model.number="tooLow"
              class="form-control"
              placeholder="Low Temperature"
            />
          </div>
          <div class="col">
            <label for="citiesBox">High Temperature</label>
          </div>
          <div class="col">
            <input
              type="number"
              @change="setTempBounds"
              v-model.number="tooHigh"
              class="form-control"
              placeholder="High Temperature"
            />
          </div>
        </div>
        <label for="citiesBox">Enter Cities</label>
        <textarea
          class="form-control"
          id="citiesBox"
          rows="15"
          v-model="citiesList"
        ></textarea>
        <button type="submit" class="btn btn-success btn-sm">
          Get Weather
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CitiesForm",
  data() {
    return {
      citiesList: "Phoenix, AZ\nOrlando, FL\nColumbia Falls, MT",
      tooLow: 33,
      tooHigh: 85,
      server_base_url: "",
    };
  },
  methods: {
    setTempBounds() {
      const tempBounds = { high: this.tooHigh, low: this.tooLow };
      this.$emit("temp-bounds-changed", tempBounds);
    },
    getCityMap() {
      let citiesListMap = [];
      const lines = this.citiesList.split(/\r?\n/);
      for (let i in lines) {
        const cityStateParts = lines[i].split(/\s*,\s*/);
        citiesListMap.push({
          name: cityStateParts[0],
          state: cityStateParts[1],
        });
      }
      return citiesListMap;
    },
    onSubmit() {
      const url = `${this.server_base_url}/cities_weather`;
      console.log(url);
      const cities = this.getCityMap();
      let disable = false;
      if (!disable) {
        axios
          .post(url, cities)
          .then((res) => {
            this.$emit("cities-changed", res.data);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    },
  },
  emits: ["cities-changed", "temp-bounds-changed"],
  created() {
    if (typeof process.env.VUE_APP_SERVER_BASE_URL !== "undefined") {
      this.server_base_url = process.env.VUE_APP_SERVER_BASE_URL;
    } else {
      console.log("Using local dev url. Set SERVER_BASE_URL if different.");
      this.server_base_url = "http://localhost:8000";
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cities-form {
  padding: 1.5rem;
  margin-right: 0;
  margin-left: 0;
  border-width: 0.2rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  text-align: left;
}
</style>
