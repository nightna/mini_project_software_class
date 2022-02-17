import { defineStore } from 'pinia'


export const useGaugeStore = defineStore({
    id: 'gauge',
    state: () => ({
      gauge: []
    }),
    actions: {
      initGuage(id)
      {
        const gauge =  new Gauge(document.getElementById(id),
        {
          min: 0,
          max: 100,
          dialStartAngle: 180,
          dialEndAngle: 0,
          value: 0,
          viewBox: "0 0 100 70",
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
        })

        this.gauge.push({
          id: id,
          gauge: gauge
        })
      },
      setGauge(id, value){
        const gauge = this.gauge.filter((e) => e.id === id)[0].gauge
        gauge.setValueAnimated(value,3)
      }

    }
  })

  
  