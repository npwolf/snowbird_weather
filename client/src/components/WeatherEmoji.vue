<template>
  <div class="emoji-weather" :title="getTitle">
      {{ getWeatherEmoji }}
  </div>
</template>

<script>
export default {
  name: 'WeatherEmoji',
  props: {
    high: {
        required: true
    },
    low: {
        required: true
    },
    too_hot: {
        required: true
    },
    too_cold: {
        required: true
    },
  },
  computed: {
      getWeatherEmoji() {
          if (this.low < this.too_cold) {
              return '🥶'
          }
          if (this.high > this.too_hot) {
              return '🥵'
          }
          return '😎'
      },
      getTitle() {
          return `H: ${this.high} / L: ${this.low}`
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
