<script setup>
import { storeToRefs } from 'pinia';
import { useSensorStore } from '../stores/sensor';
import moment from 'moment'

const store = useSensorStore()
store.$reset()

const {sensorData} = storeToRefs(store)
store.getSensorData()

</script>

<template>
      <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Table</h1>
        <div class="btn-toolbar mb-2 mb-md-0">
          <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle">
            <span data-feather="calendar"></span>
            This week
          </button>
        </div>

      </div>
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">node id</th>
              <th scope="col">temperature</th>
              <th scope="col">humidity</th>
              <th scope="col">timestamp</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="s in sensorData">
              <td>{{s.id}}</td>
              <td>{{s.node_id}}</td>
              <td>{{s.temperature}}</td>
              <td>{{s.humidity}}</td>
              <td>{{moment(s.created_at).format("HH:mm:ss DD/MM/YY")}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
</template>

<style>
</style>
