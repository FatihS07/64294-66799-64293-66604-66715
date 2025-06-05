<!-- views/GameView.vue -->
<template>
    <v-container fluid class="background-pattern fill-height pa-0 ma-0">
      <v-row align="center" justify="center" class="fill-height">
        <v-col cols="12">
          <v-card elevation="24" class="game-card pa-8" rounded="xl">
              <TheSpinWheel/>
          </v-card>
          <vue-particles id="tsparticles" :options="confettiOptions" @load="onConfettiLoad" />
        </v-col>
      </v-row>
  

    

    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted, provide } from 'vue'
  import TheSpinWheel from '@/components/TheSpinWheel.vue'  
  </script>
  