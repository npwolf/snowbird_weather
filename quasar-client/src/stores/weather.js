import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export const useWeatherStore = defineStore("weather", {
  state: () => ({
    tempMin: useStorage("tempMin", 33),
    tempMax: useStorage("tempMax", 80),
  }),
  getters: {
    //doubleCount: (state) => state.counter * 2,
  },
  actions: {},
});
