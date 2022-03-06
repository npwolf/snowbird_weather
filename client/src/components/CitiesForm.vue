<template>
  <div class="cities-form">
    <div class="form-group">
    <form class="form-inline" @submit.prevent="onSubmit">
        <label for="citiesBox">Enter Cities</label>
        <textarea class="form-control" id="citiesBox" rows="15" v-bind:value="citiesList"></textarea>
        <button type="submit" class="btn btn-success btn-sm">Get Weather</button>
    </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CitiesForm',
  data() {
      return {
          citiesList: "Mesa, AZ",
          weatherData: [
          { 
            state: 'AZ',
            city: 'Mesa',
            january: { 
                high: 60, 
                low: 45
                },
          },
          {
            state: 'MT',
            city: 'Bozeman',
            january: { 
                high: 45, 
                low: 20
                },
          },  
      ],  
      }
  },
  methods: {
      onSubmit() {
          this.$emit('cities-changed', this.weatherData)
      }
  },
  emits: ['cities-changed']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cities-form {
  padding: 1.5rem;
  margin-right: 0;
  margin-left: 0;
  border-width: .2rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  text-align: left;  
}
</style>
