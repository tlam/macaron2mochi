<template>
<div v-if="trip">
  <h3>Trip Overview - {{trip.name}}</h3>
  <ul>
    <li v-for="itinerary in trip.itineraries">
      {{itinerary.name}}
    </li>
  </ul>
</div>
</template>

<script>
export default {
  name: 'overview',
  data () {
    return {
    }
  },
  props: ['trip'],
}
</script>
