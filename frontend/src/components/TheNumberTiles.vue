<template>
    <div class="d-flex align-center justify-center ga-4">
    <div
       v-for="(number, index) in computedNumbers"
      :key="index"
    >
      <v-card class="fixed-card pa-4" >
        <span v-if="number !== 0" class="display-2">{{ convertToTwoDigit(number)}}</span>
      </v-card>
    </div>
    </div>
  </template>
  
  <script setup>
  import { ref,computed } from 'vue'

  const convertToTwoDigit = (number) => {
    return number.toLocaleString('en-US', {
      minimumIntegerDigits: 2,
      useGrouping: false
    });
  };

  const props = defineProps({
    numbers: {
      type: Array,
      default: () => []
    }
  });

  const computedNumbers = computed(() => {
    if(props?.numbers?.length) return props.numbers
    return Array(6).fill(0);
  });


  </script>