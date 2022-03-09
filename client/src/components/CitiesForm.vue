<template>
  <div class="cities-form">
    <div class="form-group">
      <form class="form-inline" @submit.prevent="onSubmit">
        <label for="citiesBox">Enter Cities</label>
        <textarea
          class="form-control"
          id="citiesBox"
          rows="15"
          v-bind:value="citiesList"
        ></textarea>
        <button type="submit" class="btn btn-success btn-sm">
          Get Weather
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "CitiesForm",
  data() {
    return {
      citiesList: "Mesa, AZ",
      server_base_url: "",
    };
  },
  methods: {
    onSubmit() {
      const url = `${this.server_base_url}/weather`;
      console.log(url)
      axios
        .get(url)
        .then((res) => {
          this.$emit('cities-changed', res.data)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  emits: ["cities-changed"],
  created() {
    if (typeof process.env.VUE_APP_SERVER_BASE_URL !== 'undefined') {
      this.server_base_url = process.env.VUE_APP_SERVER_BASE_URL;
    } else {
      console.log("Using local dev url. Set SERVER_BASE_URL if different.")
      this.server_base_url = "http://localhost:8000";
    }
  }
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
