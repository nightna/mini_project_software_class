import { defineStore } from 'pinia'
import axios from 'axios'
import "../assets/gauge"

axios.defaults.baseURL = 'http://127.0.0.1:5000'

export const useSensorStore = defineStore({
  id: 'sensor',
  state: () => ({
    sensorData: [],
    temp: 0,
    humi: 0
  }),
  getters: {
    chartData: function (state) {
      return {
        labels: state.sensorData.map(e => e.created_at),
        datasets: [
            {
                label:"temperature",
                data: state.sensorData.map(e => e.temperature),
                fill: false,
                backgroundColor: 'rgba(255, 99, 132, 0.8)',
                borderColor:'rgba(255, 99, 132, 0.8)',
          },
          {
              label:"humidity",
              data: state.sensorData.map(e => e.humidity),
              fill: false,
              backgroundColor: 'rgba(255, 159, 64, 0.8) ',
              borderColor:'rgba(255, 159, 64, 0.8)',   
          }
        ]
      }
    }
  },
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
