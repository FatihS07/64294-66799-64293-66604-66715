<template>
  <div class="d-flex align-center justify-space-between mb-8">
        <h1 class="d-flex align-center text-h2 ga-5 font-weight-black text-orange-accent-3">
          Lotto Number Generator
          <v-icon size="70" class="ml-4 spin-icon grad">mdi-slot-machine</v-icon>
        </h1>
      </div>
      <div class="d-flex align-center justify-space-between">
        <v-chip variant="outlined" color="secondary" class="mt-2">
          <v-icon>mdi-history</v-icon>
          Draws in the Last 24 Hours: {{ lastDrawCount }}
        </v-chip>
        <ToggleTheme/>
      </div>
</template>

<script setup>
import ToggleTheme from './ToggleTheme.vue'
defineProps({
      lastDrawCount: {
        type: Number,
        default : 0
      }
})


</script>