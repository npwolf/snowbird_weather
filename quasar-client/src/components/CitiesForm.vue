<template>
  <div class="city-temp q-gutter-md">
    <q-card class="col">
      <q-card-section>
        <q-form @submit.prevent="addCity" class="">
          <div class="row items-center justify-center q-gutter-sm">
            <div class="col-8 seventy">
              <q-input
                class="col"
                type="text"
                ref="cityRef"
                lazy-rules
                :rules="cityValidations"
                v-model="city"
                placeholder="City, ST"
                autofocus="autofocus"
                @keyup="typingCity"
              >
                <template v-slot:prepend> <q-icon name="place" /> </template
              ></q-input>
            </div>
            <div class="col no-wrap">
              <q-btn
                ref="addCityRef"
                color="primary"
                type="submit"
                label="Add City"
                :disabled="!this.city.length"
              />
            </div>
          </div>
        </q-form>
      </q-card-section>
    </q-card>
    <IdealTemp />
  </div>
</template>

<script>
import axios from "axios";
import process from "process";
import IdealTemp from "./IdealTemp.vue";

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
      server_base_url: "",
      cityValidations: [],
    };
  },
  methods: {
    typingCity() {
      if (this.city.length) {
        this.cityValidations = [
          (val) =>
            val.match(/^[a-z ]{3,40},\s*[a-z]{2}$/i) ||
            "Must be in format City, ST",
        ];
      } else {
        this.cityValidations = [];
        this.$refs.cityRef.resetValidation();
      }
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
          this.notifyError("Oh no, something went wrong. Try again?");
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
  emits: ["cities-changed", "city-added"],
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

  components: {
    IdealTemp,
  },
};
</script>
<style scoped>
.city-temp {
  display: flex;
  flex-direction: row;
}

.seventy {
  min-width: 70%;
}

/* Responsive layout - makes a one column layout instead of a two-column layout */
@media (max-width: 800px) {
  .city-temp {
    flex-direction: column;
  }
}
</style>
