<template>
  <div class="cities-form">
    <form class="form-inline" @submit.prevent="onSubmit">
        <h1><label>Enter Cities</label></h1>
        <textarea class="input" v-bind:value="citiesList"></textarea>
        <button type="submit" class="btn btn-success btn-sm">Get Weather</button>
    </form>
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

</style>
