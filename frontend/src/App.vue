<script setup>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import ReservaModal from "@/components/ReservaModal.vue";
</script>

<template>
  <main id="page">
    <Navbar v-if="$route.name !== 'not-found'" />
    <div id="content">
      <router-view />
    </div>
    <Footer v-if="$route.name !== 'not-found'" />
    <ReservaModal />
  </main>
</template>

<style>

</style>
