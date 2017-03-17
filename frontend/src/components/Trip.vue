<template>
<div>
  <a :href="trip.itineraries_url">{{trip.name}}</a>
</div>
</template>

<script>
export default {
  name: 'trip',
  data () {
    return {
    }
  },
  props: ['trip']
}
</script>
