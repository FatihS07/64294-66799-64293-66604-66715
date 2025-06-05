<template>
  <v-app :theme="theme">
    <Loading/>
    <GameView />
  </v-app>
</template>

<script setup>
import GameView from './views/GameView.vue'
import Loading from './components/Loading.vue'
import { ref, provide } from 'vue'

const theme = ref('dark')
const toggleTheme = () => {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'
}
provide('theme', theme)
provide('toggleTheme', toggleTheme)

</script>
