<template>
  <div id="app">
    <div v-for="trip in trips">
      <trip :trip="trip"></trip>
    </div>
  </div>
</template>

<script>
import Trip from './components/Trip.vue'

export default {
  name: 'app',
  components: {
    Trip
  },
  data() {
    return {
      trips: []
    }
  },
  mounted: function() {
    this.$http.get('/trips/').then(response => {
      var data = response.data;
      console.log(data.trips[0].name);
      this.trips = data.trips;
    }, response => {
     
    });
  }
}
</script>
