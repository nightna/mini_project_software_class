import { defineStore } from 'pinia'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5000';

export const useSensorStore = defineStore({
  id: 'sensor',
  state: () => ({
    sensorData: [],
    temp: 0,
    humi: 0
  }),
  actions: {
    getSensorData()
    {
      return axios.get("/api/sensor_data").then(res => {
        this.sensorData = res.data
        // console.log(res.data);
      }).catch(e => {
        console.log(e);
      })
    },
    async getNodeDate()
    {
      try {
        const {data} = await axios.get("/api/node_data")
        this.temp = data[0].temperature
        this.humi = data[0].humidity
      } catch (error) {
        console.log(error);
      }
    }
  }
})
