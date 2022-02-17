<script setup>
import { storeToRefs } from 'pinia';
import { onMounted } from 'vue';
import Gauge from '../components/Gauge.vue';
import {useSensorStore} from "../stores/sensor.js"

const store = useSensorStore()
const {temp, humi} = storeToRefs(store)
onMounted(async() => {
  await store.getNodeDate()
})



</script>

<template>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Dashboard</h1>
        <div class="btn-toolbar mb-2 mb-md-0">
          <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle">
            <span data-feather="calendar"></span>
            This week
          </button>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12 col-lg-4">
          <div class="row">
            <div class=" col-md-6 col-lg-12">
              <Gauge id="g1" :value="temp"/>
            </div>
            <div class="col-md-6 col-lg-12">
              <Gauge id="g2" :value="humi"/>
            </div>
          </div>
        </div>
      </div>
    </main>
</template>

<style>

</style>
