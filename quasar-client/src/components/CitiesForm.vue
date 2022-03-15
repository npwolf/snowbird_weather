<template>
  <q-card class="form-card">
    <q-card-actions align="center">
      <q-form @submit.prevent="addCity" class="">
        <div class="row items-center q-gutter-md">
          <q-input
            class="col-grow"
            type="text"
            ref="cityRef"
            lazy-rules
            :rules="cityValidations"
            v-model="city"
            placeholder="City, ST"
            autofocus="autofocus"
          />
          <q-btn color="primary" type="submit" label="Add City" />
        </div>
        <div class="row items-center q-gutter-md">
          <label class="q-ma-md">Ideal Temperature Range</label>
          <q-range
            v-model="tempRange"
            :min="0"
            :max="100"
            :left-label-value="'Low: ' + tempRange.min + 'F'"
            :right-label-value="'High: ' + tempRange.max + 'F'"
            label-always
            color="red"
            @change="setTempBounds"
          />
        </div>
      </q-form>
    </q-card-actions>
  </q-card>
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
      city: "",
      autofocus: true,
      tooLow: 33,
      tooHigh: 80,
      tempRange: { min: 33, max: 80 },
      server_base_url: "",
      cityValidations: [
        (val) => !!val || "Field is required",
        (val) =>
          val.match(/^[a-z ]{3,40},\s*[a-z]{2}$/i) ||
          "Must be in format City, ST",
      ],
    };
  },
  methods: {
    setTempBounds() {
      const tempBounds = { high: this.tempRange.max, low: this.tempRange.min };
      this.$emit("temp-bounds-changed", tempBounds);
    },
    notifyError(error) {
      this.$q.notify({
        type: "negative",
        message: error,
      });
    },
    isValidCityResponse(res) {
      if ("january_high" in res) {
        console.log("valid city");
        return true;
      } else {
        console.log("invalid city");
        return false;
      }
    },
    addCity() {
      Loading.show({
        message: "Getting Weather...",
      });
      const cityStateParts = this.city.split(/\s*,\s*/);
      const cityMap = {
        name: cityStateParts[0],
        state: cityStateParts[1],
      };
      const url = `${this.server_base_url}/city_weather`;
      console.log("City: " + JSON.stringify(cityMap));
      axios
        .post(url, cityMap)
        .then((res) => {
          console.log("Response: " + JSON.stringify(res.data));
          if (!this.isValidCityResponse(res.data)) {
            this.notifyError(
              "Unable to find weather for " +
                this.city +
                ". Try a different city."
            );
          } else {
            this.$emit("city-added", res.data);
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
        .finally(() => {
          Loading.hide();
          this.city = "";
          this.$refs.cityRef.resetValidation();
          this.$refs.cityRef.focus();
        });
    },
  },
  emits: ["cities-changed", "temp-bounds-changed", "city-added"],
  created() {
    if (typeof process.env.VUE_APP_SERVER_BASE_URL !== "undefined") {
      this.server_base_url = process.env.VUE_APP_SERVER_BASE_URL;
    } else {
      console.log(
        "Using local dev url. Set VUE_APP_SERVER_BASE_URL if different."
      );
      this.server_base_url = "http://localhost:8000";
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.temp-picker {
  max-width: 50px;
}
</style>
