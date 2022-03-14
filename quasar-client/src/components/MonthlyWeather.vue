<template>
  <div class="hello">
    <table v-if="weatherData.length" class="styled-table">
      <tr>
        <th>State</th>
        <th>City</th>
        <th>Jan</th>
        <th>Feb</th>
        <th>Mar</th>
        <th>Apr</th>
        <th>May</th>
        <th>Jun</th>
        <th>Jul</th>
        <th>Aug</th>
        <th>Sep</th>
        <th>Oct</th>
        <th>Nov</th>
        <th>Dec</th>
      </tr>
      <tr v-for="(weather, index) in weatherData" :key="index">
        <td>{{ weather.state }}</td>
        <td>{{ weather.name }}</td>
        <template v-if="'january_high' in weather">
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.january_high"
              :low="weather.january_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.february_high"
              :low="weather.february_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.march_high"
              :low="weather.march_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.april_high"
              :low="weather.april_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.may_high"
              :low="weather.may_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.june_high"
              :low="weather.june_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.july_high"
              :low="weather.july_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.august_high"
              :low="weather.august_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.september_high"
              :low="weather.september_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.october_high"
              :low="weather.october_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.november_high"
              :low="weather.november_low"
            />
          </td>
          <td>
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="weather.december_high"
              :low="weather.december_low"
            />
          </td>
        </template>
        <template v-if="!('january_high' in weather)">
          <td colspan="12">
            Unable to find weather for location. Try a different city.
          </td>
        </template>
      </tr>
    </table>
  </div>
</template>

<script>
import WeatherEmoji from "./WeatherEmoji.vue";

export default {
  name: "MonthlyWeather",
  props: {
    weatherData: {
      type: Array,
      required: true,
    },
    tooHot: {
      type: Number,
      required: true,
    },
    tooCold: {
      type: Number,
      required: true,
    },
  },
  components: {
    WeatherEmoji,
  },
};
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
