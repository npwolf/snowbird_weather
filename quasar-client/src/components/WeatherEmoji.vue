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
    tooHot: {
        required: true
    },
    tooCold: {
        required: true
    },
  },
  computed: {
      getWeatherEmoji() {
          if (this.low < this.tooCold) {
              return '🥶'
          }
          if (this.high > this.tooHot) {
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
