<template>
<div v-if="trip">
  <h3>Day to Day - {{trip.name}} <a href="/admin/itineraries/itinerary/add/" target="_blank" class="glyphicon glyphicon-plus" aria-hidden="true"></a></h3>
  <div class="row" v-for="groupItinerary in trip.itineraries">
    <div class="col-sm-2 itinerary" v-for="itinerary in groupItinerary">
      <div class="date">{{itinerary.date}}
        <a href="/admin/activities/activity/add/" target="_blank" class="glyphicon glyphicon-plus" aria-hidden="true"></a>
      </div>
      <div class="name">{{itinerary.name}}</div>
      <div class="list-group">
        <div v-for="activity in itinerary.activities" class="activity list-group-item">
          <div class="row">
            <div class="col-sm-6 time">{{activity.start_time}} - {{activity.end_time}}</div>
            <div class="col-sm-6">
              <i :class="'pull-right fa ' + activity.icon"></i>
            </div>
          </div>
          <a :href="activity.url" target="_blank">{{activity.name}}</a>
          <div class="description">{{activity.description}}</div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'itineraries',
  data () {
    return {
    }
  },
  props: ['trip'],
}
</script>

<style>
div.col-sm-2 {
  padding: 0;
}

div.itinerary div.date {
  border: 2px solid #ddd;
  font-weight: bold;
  text-align: center;
}

div.itinerary div.name {
  border: 1px solid #ddd;
  border-top: none;
  font-size: 90%;
  text-align: center;
}

div.activity div.description {
  font-size: 80%;
  white-space: pre-wrap;
}

div.activity div.time {
  font-size: 70%;
  font-weight: bold;
}
</style>
