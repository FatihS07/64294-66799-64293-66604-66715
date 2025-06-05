// src/router/index.ts veya index.js
import { createRouter, createWebHistory } from 'vue-router'
import GameView from '@/views/GameView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: GameView,
  },
  // Diğer route'lar buraya
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
