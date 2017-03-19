<template>
  <div id="app">
    <div v-for="trip in trips">
      <trip :trip="trip" v-on:tripSelected="setSelectedTrip"></trip>
    </div>
    <ul class="nav nav-tabs">
      <li role="presentation" class="active"><a href="#">Overview</a></li>
      <li role="presentation"><a href="#">Day to Day</a></li>
      <li role="presentation"><a href="#">Map</a></li>
    </ul>
    <overview :trip="selectedTrip"></overview>
    <itineraries :trip="selectedTrip"></itineraries>
  </div>
</template>

<script>
import Itineraries from './components/Itineraries.vue'
import Overview from './components/Overview.vue'
import Trip from './components/Trip.vue'

export default {
  name: 'app',
  components: {
    Itineraries,
    Overview,
    Trip
  },
  data() {
    return {
      selectedTrip: null,
      trips: []
    }
  },
  mounted: function() {
    this.$http.get('/trips/').then(response => {
      var data = response.data;
      console.log(data.trips[0].name);
      this.trips = data.trips;
    }, response => {
      this.trips = [{"id": 1, "itineraries_url": "/trips/1/itineraries", "name": "Cinque Terre and Florence"}];
    });
  },
  methods: {
    setSelectedTrip: function() {
      this.selectedTrip = this.$store.state.selectedTrip;
    }
  }
}
</script>
