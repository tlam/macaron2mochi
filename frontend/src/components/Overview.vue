<template>
<div v-if="trip">
  <h3>Trip Overview - {{trip.name}}</h3>
  <ul>
    <div v-for="groupItinerary in trip.itineraries">
      <li v-for="itinerary in groupItinerary">
        {{itinerary.name}}<span v-if="itinerary.description">: {{itinerary.description}}</span>
      </li>
    </div>
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
