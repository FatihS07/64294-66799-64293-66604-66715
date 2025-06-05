<template>
    <v-overlay v-model="globalLoading" class="align-center justify-center" opacity="0.9">
      <v-progress-circular indeterminate size="64" color="primary"></v-progress-circular>
    </v-overlay>
</template>

<script setup>
import { inject } from 'vue';
 const globalLoading = inject('globalLoading');
</script>
