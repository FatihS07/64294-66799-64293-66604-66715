<template>
    <v-btn :icon="icon" @click="toggleTheme" variant="text" size="x-large" >
    </v-btn>
</template>

<script setup>
import { inject,computed } from 'vue';
  const theme = inject('theme', 'dark');
  const toggleTheme = inject('toggleTheme', () => {});

  const icon = computed(() => {
    return theme.value === 'dark' ? 'mdi-weather-sunny' : 'mdi-weather-night';
  });

</script>
