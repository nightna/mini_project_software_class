<script setup>
import { onMounted, onUpdated, ref } from 'vue';

const props = defineProps({
  id: String,
  value: Number
})

const gauge = ref(null)

onMounted(() => {
   gauge.value = Gauge(
        document.getElementById(props.id),
        {
            min: -0,
            max: 100,
            dialStartAngle: 180,
            dialEndAngle: 0,
            value: props.value,
            viewBox: "0 0 100 57",
            color: function(value) {
                if(value < 20) {
                return "#5ee432";
                }else if(value < 40) {
                return "#fffa50";
                }else if(value < 60) {
                return "#f7aa38";
                }else {
                return "#ef4655";
                }
            }
        }
    )
})

onUpdated(() => {
    gauge.value.setValue(props.value)
})

</script>

<template>
    <div :id="props.id"  class="gauge-container two"></div>
</template>