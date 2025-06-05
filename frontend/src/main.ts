import './assets/main.css'
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createApp } from 'vue'
import { createPinia } from 'pinia'


import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'

import VueParticles from 'vue3-particles'
const app = createApp(App)
app.use(vuetify)         // Vuetify ilk sırada olabilir
app.use(createPinia())
app.use(router)
app.use(VueParticles) // ← Burası önemli
app.mount('#app')
