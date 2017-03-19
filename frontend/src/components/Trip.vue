<template>
<div>
  <a href="#" v-on:click="selectTrip">{{trip.name}}</a>
</div>
</template>

<script>
export default {
  name: 'trip',
  data () {
    return {
    }
  },
  props: ['trip'],
  methods: {
    selectTrip: function() {
      this.$http.get(this.trip.itineraries_url).then(response => {
        this.$store.commit('setSelectedTrip', {
          trip: response.data
        });
        this.$emit('tripSelected');
      }, response => {
        //this.trips = [{"id": 1, "itineraries_url": "/trips/1/itineraries", "name": "Cinque Terre and Florence"}];
      });
    }
  }
}
</script>
