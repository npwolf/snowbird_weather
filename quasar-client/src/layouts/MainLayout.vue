<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title> Snowbird Weather </q-toolbar-title>
        <div class="row items-center justify-center q-gutter-md">
          <div class="col">
            <a href="https://www.instagram.com/roadship.enterprise/">
              <img
                src="~assets/instagram.svg"
                style="width: 25px; height: 25px"
                alt="Instagram"
            /></a>
          </div>
          <div class="col">
            <a href="" @click.prevent="showAboutBox = true">
              <img
                src="~assets/info.svg"
                style="width: 25px; height: 25px"
                alt="Instagram"
            /></a>
          </div>
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container class="flex window-height window-width justify-center">
      <q-dialog v-model="showAboutBox">
        <q-card>
          <q-card-section>
            <div class="text-h6">About</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <img
              src="~assets/profile2.jpg"
              class="profile"
              style="width: 75px; height: 75px"
              align="left"
            />
            Hello! I'm Parker and I live fulltime in an RV. When you live in an
            RV, extreme temperatures are the enemy. While it's certainly
            possible to live in an RV in Phoenix in the summer and Wyoming in
            the winter, it comes with a lot of challenges. If your home is on
            wheels, why not just follow the pleasant weather?
            <br /><br />
            I created this app to make it easier to follow that pleasant
            weather! Just add cities you're interested in visiting and you can
            quickly see what months might be more ideal to visit in. You can
            adjust your ideal temperatures and the emojis will change
            accordingly. The cities and temperatures are saved in your browser's
            cache so you don't need to start over if you come back later.
            <br /><br />
            I hope you find the site useful!
            <br /><br />
            -Parker
            <a href="https://www.instagram.com/roadship.enterprise/">
              <img
                src="~assets/instagram.svg"
                style="width: 25px; height: 25px"
                alt="Instagram"
            /></a>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="OK" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";

export default {
  name: "MainLayout",
  components: {},
  data() {
    return {
      showAboutBox: false,
    };
  },
};
</script>

<style scoped>
.profile {
  border-radius: 50%;
  margin-right: 10px;
}
</style>
