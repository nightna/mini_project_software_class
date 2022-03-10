import { defineStore } from 'pinia'
import axios from 'axios'
import "../assets/gauge"

axios.defaults.baseURL = 'http://127.0.0.1:5000'

export const useSensorStore = defineStore({
  id: 'sensor',
  state: () => ({
    sensorData: [],
    avr: {
      temp: 0,
      humi: 0
    },
    temp: 0,
    humi: 0
  }),
  getters: {
    chartData: function (state) {
      return {
        datasets: [
            {
                label:"temperature",
                data: state.sensorData.map(e => (
                  {
                    x: e.created_at,
                    y: e.temperature
                  }
                )),
                fill: false,
                backgroundColor: 'rgba(255, 99, 132, 0.8)',
                borderColor:'rgba(255, 99, 132, 0.8)',
          },
          {
              label:"humidity",
              data: state.sensorData.map(e => (
                {
                  x: e.created_at,
                  y: e.humidity
                }
              )),
              fill: false,
              backgroundColor: 'rgba(255, 159, 64, 0.8) ',
              borderColor:'rgba(255, 159, 64, 0.8)',   
          },
          {
            label:"avr temp.",
            data: state.avr.temp,
            fill: false,
            backgroundColor: 'rgba(0, 128, 128, 0.8) ',
            borderColor:'rgba(0, 128, 128, 0.8)',   
          },
          {
            label:"avr humi.",
            data: state.avr.humi,
            fill: false,
            backgroundColor: 'rgba(153, 204, 0, 0.8) ',
            borderColor:'rgba(153, 204, 0, 0.8)',   
          }
        ]
      }
    }
  },
  actions: {
    getSensorData(mode)
    {
      return axios.get("/api/sensor_data?mode="+mode).then(res => {
        this.avr.temp = 0
        this.avr.humi = 0
        this.sensorData = res.data
        this.sensorData.forEach(e => {
          this.avr.temp += e.temperature
          this.avr.humi += e.humidity
        });
        
        let t = []
        let h = []

        this.avr.temp /= this.sensorData.length
        this.avr.humi /= this.sensorData.length

        this.sensorData.forEach(e => {
          t.push(this.avr.temp)
          h.push(this.avr.humi)
        })
        
        this.avr = {
          temp: t,
          humi: h
        }

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


