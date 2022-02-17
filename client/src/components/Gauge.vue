<script setup>
import { onMounted, watch } from "vue";
import {useGaugeStore} from "../stores/gauge"

const props = defineProps({
  id: String,
  value: Number
})

const store = useGaugeStore()
const {initGuage, setGauge} = store

onMounted(() => {
    console.log(props);
    initGuage(props.id, props.value)
})

watch(() => props.value, (newValue, oldValue) => {
    setGauge(props.id,newValue)
})

</script>

<template>
    <div :id="props.id" class="gauge-container two"></div>
</template>