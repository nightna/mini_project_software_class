import { defineStore } from 'pinia'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5000';

export const useSensorStore = defineStore({
  id: 'sensor',
  state: () => ({
    sensorData: []
  }),
  actions: {
    getSensorData()
    {
      return axios.get("/api/sensor_data").then(res => {
        this.sensorData = res.data
        console.log(res.data);
      }).catch(e => {
        console.log(e);
      })
    }
  }
})
