<template>
  <div class="col">
    <q-table
      class="weather-table"
      :rows="weatherStore.cities"
      :columns="columns"
      row-key="name"
      title="Average Weather"
      :wrap-cells="true"
      :hide-pagination="true"
      :rows-per-page-options="[0]"
      :dense="true"
    >
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="delete" :props="props">
            <q-btn
              dense
              round
              flat
              color="grey"
              @click="deleteRow(props)"
              icon="delete"
            ></q-btn>
          </q-td>
          <q-td key="name" :props="props">
            {{ props.row.name }}
          </q-td>
          <q-td key="state" :props="props">
            {{ props.row.state }}
          </q-td>

          <q-td key="january" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.january_high"
              :low="props.row.january_low"
            />
          </q-td>
          <q-td key="february" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.february_high"
              :low="props.row.february_low"
            />
          </q-td>
          <q-td key="march" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.march_high"
              :low="props.row.march_low"
            />
          </q-td>
          <q-td key="april" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.april_high"
              :low="props.row.april_low"
            />
          </q-td>
          <q-td key="may" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.may_high"
              :low="props.row.may_low"
            />
          </q-td>
          <q-td key="june" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.june_high"
              :low="props.row.june_low"
            />
          </q-td>
          <q-td key="july" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.july_high"
              :low="props.row.july_low"
            />
          </q-td>
          <q-td key="august" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.august_high"
              :low="props.row.august_low"
            />
          </q-td>
          <q-td key="september" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.september_high"
              :low="props.row.september_low"
            />
          </q-td>
          <q-td key="october" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.october_high"
              :low="props.row.october_low"
            />
          </q-td>
          <q-td key="november" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.november_high"
              :low="props.row.november_low"
            />
          </q-td>
          <q-td key="december" :props="props">
            <WeatherEmoji
              :tooHot="tooHot"
              :tooCold="tooCold"
              :high="props.row.december_high"
              :low="props.row.december_low"
            />
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script>
import WeatherEmoji from "./WeatherEmoji.vue";
import { useWeatherStore } from "./../stores/weather";
import { mapStores } from "pinia";

export default {
  name: "MonthlyWeather",
  data() {
    return {
      columns: [
        {
          name: "delete",
          align: "center",
          label: "",
          field: "delete",
        },
        {
          name: "name",
          required: true,
          label: "City",
          align: "left",
          field: (row) => row.name,
          format: (val) => `${val}`,
          sortable: true,
        },
        {
          name: "state",
          align: "center",
          label: "State",
          field: "state",
          sortable: true,
        },
        { name: "january", align: "center", label: "J", field: "january" },
        {
          name: "february",
          align: "center",
          label: "F",
          field: "february",
        },
        { name: "march", align: "center", label: "M", field: "march" },
        { name: "april", align: "center", label: "A", field: "april" },
        { name: "may", align: "center", label: "M", field: "may" },
        { name: "june", align: "center", label: "J", field: "june" },
        { name: "july", align: "center", label: "J", field: "july" },
        { name: "august", align: "center", label: "A", field: "august" },
        {
          name: "september",
          align: "center",
          label: "S",
          field: "september",
        },
        {
          name: "october",
          align: "center",
          label: "O",
          field: "october",
        },
        {
          name: "november",
          align: "center",
          label: "N",
          field: "november",
        },
        {
          name: "december",
          align: "center",
          label: "D",
          field: "december",
        },
      ],
    };
  },

  components: {
    WeatherEmoji,
  },
  methods: {
    deleteRow(props) {
      console.log("Delete row: " + JSON.stringify(props));
      this.weatherStore.cities.splice(
        this.weatherStore.cities.indexOf(props.row),
        1
      );
    },
  },
  computed: {
    ...mapStores(useWeatherStore),
    tooHot() {
      return this.weatherStore.tempMax;
    },
    tooCold() {
      return this.weatherStore.tempMin;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="sass">
.temp-range-slider
  min-width: 300px
.table-title
  font-size: 20px
  letter-spacing: 0.005em
  font-weight: 400
.weather-table
  max-width: 800px
  thead tr:nth-child(2) th:nth-child(2)
    background-color: #fff
    opacity: 1

  td:nth-child(2)
    background-color: white

  td:nth-child(2)
    position: sticky
    left: 0
    z-index: 1
</style>
