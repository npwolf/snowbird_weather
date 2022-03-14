<template>
  <div class="zzz">
    <q-form @submit.prevent="addCity">
      <div class="column form-elements">
        <div class="row"></div>
        <label for="city">City</label>
        <q-input
          type="text"
          ref="cityRef"
          lazy-rules
          :rules="cityValidations"
          v-model="city"
          placeholder="City, ST"
        />
        <label>Low Temperature</label>
        <q-input
          type="number"
          @change="setTempBounds"
          v-model.number="tooLow"
          class="form-control"
          placeholder="Low Temperature"
        />
        <label>High Temperature</label>
        <q-input
          type="number"
          @change="setTempBounds"
          v-model.number="tooHigh"
          class="form-control"
          placeholder="High Temperature"
        />
      </div>
      <div class="column">
        <div class="row"></div>
        <q-btn color="primary" type="submit" label="Add City" />
        <q-btn
          label="Reset"
          type="reset"
          color="primary"
          flat
          class="q-ml-sm"
        />
      </div>
    </q-form>
    <div class="form-group"></div>
    <div class="form-group"></div>
    <div class="form-group"></div>
  </div>
</template>

<script>
import axios from "axios";
import process from "process";
import { ref } from "vue";
import {
  Loading,

  // optional!, for example below
  // with custom spinner
  QSpinnerGears,
} from "quasar";

export default {
  name: "CitiesForm",
  data() {
    return {
      citiesList: "Phoenix, AZ\nOrlando, FL\nColumbia Falls, MT",
      city: "",
      tooLow: 33,
      tooHigh: 85,
      server_base_url: "",
      cityValidations: [
        (val) => !!val || "Field is required",
        (val) =>
          val.match(/^[a-z]{3,23},\s*[a-z]{2}$/i) ||
          "Must be in format City, ST",
      ],
    };
  },
  methods: {
    setTempBounds() {
      const tempBounds = { high: this.tooHigh, low: this.tooLow };
      this.$emit("temp-bounds-changed", tempBounds);
    },
    addCity() {
      this.city = "";
      this.$refs.cityRef.resetValidation();
      this.$refs.cityRef.focus();
      Loading.show({
        message: "Getting Weather...",
      });
      const cityStateParts = this.city.split(/\s*,\s*/);
      const cityMap = {
        name: cityStateParts[0],
        state: cityStateParts[1],
      };
      const url = `${this.server_base_url}/city_weather`;
      axios
        .post(url, cityMap)
        .then((res) => {
          this.$emit("city-added", res.data);
          console.log("Response: " + JSON.stringify(res.data));
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
        .finally(() => {
          Loading.hide();
        });
    },
  },
  emits: ["cities-changed", "temp-bounds-changed", "city-added"],
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
/* .cities-form {
  padding: 1.5rem;
  margin-right: 0;
  margin-left: 0;
  border-width: 0.2rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  text-align: left;
} */
/* form specific formatting */
/* .form-group {
  display: flex;
  flex-direction: row;
}

.form-group label {
  flex: none;
  display: block;
  width: 125px;
  font-weight: bold;
  font-size: 1em;
}
.form-group label.right-inline {
  text-align: right;
  padding-right: 8px;
  padding-left: 10px;
  width: auto;
}

.form-group .input-control {
  flex: 1 1 auto;
  display: block;
  margin-bottom: 10px;
  margin-right: 8px;
  padding: 4px;
  margin-top: -4px;
} */
.zzz {
  display: flex;
}
</style>
