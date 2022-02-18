<script setup>
import { ref } from 'vue';
import {LineChart, useLineChart} from "vue-chart-3"
import {Chart, registerables} from "chart.js"
import zoomPlugin from 'chartjs-plugin-zoom';
import {useSensorStore} from '../stores/sensor'
import { storeToRefs } from 'pinia';

const store = useSensorStore()

Chart.register(...registerables, zoomPlugin)
const {chartData} = storeToRefs(store)


const options = ref({
    scales: {
        y: {
            min: 0,
            max: 100,
        },
    },
    plugins: {
      zoom: {
        zoom: {
          wheel: {
            enabled: true,
            mode: 'y'
          },
          drag: {
            enabled: true,
          },
          limit:{
            y: {min: 0, max: 100}
          },
        }
      }
    }
})

const {lineChartProps, lineChartRef} = useLineChart({
    chartData,
    options,
})

function resetZoom()
{
    lineChartRef.value.update()
    lineChartRef.value.chartInstance.resetZoom();
}
</script>

<template>
    <LineChart v-bind="lineChartProps"/>
    <div class="mt-2 row align-self-center">
        <div class="col-12  ">
            <button class="btn btn-primary"  @click="resetZoom">reset zoom</button>
        </div>
    </div>
</template>