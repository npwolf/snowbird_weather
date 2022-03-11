<template>
  <div class="hello">
    <table v-if="weatherData.length" class="styled-table">
        <tr>
            <th>State</th>
            <th>City</th>
            <th>Jan</th>
        </tr>
        <tr v-for="(weather, index) in weatherData" :key="index">
            <td>{{ weather.state}}</td>
            <td>{{ weather.name }}</td>
            <!-- <td><WeatherEmoji too_hot="85" too_low="32" high="65" low="33"/></td> -->
            <td><WeatherEmoji :too_hot="too_hot" :too_cold="too_cold" :high="weather.january_high" :low="weather.january_low"/></td>
        </tr>
    </table>
  </div>
</template>

<script>
import WeatherEmoji from './WeatherEmoji.vue'

export default {
  name: 'MonthlyWeather',
  data() {
      return {
          too_hot: 85,
          too_cold: 32
      }
  },
  props: {
    weatherData:  { 
        type: Array,
        required: true,
    }
  },
  components: {
      WeatherEmoji,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.styled-table {
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
.styled-table thead tr {
    background-color: #009879;
    color: #ffffff;
    text-align: left;
}
.styled-table th,
.styled-table td {
    padding: 12px 15px;
}
.styled-table tbody tr {
    border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
    border-bottom: 2px solid #009879;
}
.styled-table tbody tr.active-row {
    font-weight: bold;
    color: #009879;
}


</style>
