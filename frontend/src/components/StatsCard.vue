<!-- components/StatsCard.vue -->
<template>
    <v-card class="stats-card pa-4 mt-4">
      <div class="d-flex justify-space-between">
        <div>
          <div class="text-caption">Total Draws</div>
          <div class="text-h5">{{ totalDraws }}</div>
        </div>
        <v-divider vertical class="mx-4"></v-divider>
        <div>
          <div class="text-caption">Most Frequent</div>
          <div class="text-h5">{{ mostCommonNumber || '-' }}</div>
        </div>
      </div>
    </v-card>
  </template>
  
  <script setup>
  defineProps(['totalDraws', 'mostCommonNumber'])
  </script>
  