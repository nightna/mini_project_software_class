import { defineStore } from 'pinia'
import axios from 'axios'

host_server = 'http://localhost:5000'

export const useSensorStore = defineStore({
  id: 'sensor',
  state: () => ({
    sensorData: 0
  }),
  actions: {
    async getSensorData() {
      try {
        res = await axios.get(host_server + '/api/sensor_data')\
        this.sensorData = res.data
        console.log(res.data);
      } catch (error) {
        console.log(error);
      }
    }
  }
})
