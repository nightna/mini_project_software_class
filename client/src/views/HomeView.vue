<script setup>
import { storeToRefs } from 'pinia';
import { onMounted } from 'vue';
import MyLineChart from "../components/MyLineChart.vue"
import Gauge from '../components/Gauge.vue';
import {useSensorStore} from "../stores/sensor.js"

const store = useSensorStore()
store.$reset()

const {temp, humi} = storeToRefs(store)

onMounted(async() => {
  await store.getNodeDate()
  await store.getSensorData()
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
        <div class="col-md-12 col-lg-3">
          <div class="row">
            <div class=" col-md-6 col-lg-12">
              <div class="card">
                <div class="card-body pb-0 pt-1 px-0">
                  <p class="card-title text-center fw-bolder fs-5 my-0 ">Temperature</p>
                  <Gauge id="g1" :value="temp"/>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-12">
              <div class="card mt-2">
                <div class="card-body pb-0 pt-1 px-0">
                    <p class="card-title text-center fw-bolder fs-5 my-0 ">Humidity</p>
                    <Gauge id="g2" :value="humi"/>
                  </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-12 col-lg-9">
            <div class="card px-2 py-4">
              <MyLineChart />
            </div>
        </div>
      </div>
    </main>
</template>

<style>

</style>
