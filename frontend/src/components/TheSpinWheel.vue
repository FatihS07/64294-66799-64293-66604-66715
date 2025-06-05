<template>
   <TheHeader :lastDrawCount="statisticsRef.lastDrawCount"  />
    <div class="d-flex flex-column align-center gap-4">
     <TheNumberTiles :numbers="generatedNumbers" />
     <v-btn 
       block size="x-large" :loading="loading"
       class="generate-button" variant="tonal"
       @click="onSpinClick"
     >
       <template #prepend>
         <v-avatar size="40" class="mr-2">
           <v-img :src="slotMachineGif"></v-img>
         </v-avatar>
       </template>
       Spin the Wheel
     </v-btn>
      <StatsCard :totalDraws="statisticsRef.totalDraws" :mostCommonNumber="statisticsRef.mostCommonNumber" />
    </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import { fetchStatistics, fetchGenerateNumbers } from '@/services'
import StatsCard from '@/components/StatsCard.vue'
import TheHeader from '@/components/TheHeader.vue'
import TheNumberTiles from '@/components/TheNumberTiles.vue'
import slotMachineGif from '@/assets/slot-machine.gif'

// Importing audio files
import clickSoundFile from '@/assets/sounds/click.mp3'
import winSoundFile from '@/assets/sounds/win.mp3'


const statisticsRef = ref({
    totalDraws: 0,
    lastDrawCount: 0,
    mostCommonNumber: null
  })
  const loading = ref(false)
  const generatedNumbers = ref([]);

onMounted(async () => {
  loading.value = true
   handleFetchStatistics()
   loading.value = false
}) 

async function handleFetchStatistics() {
    const response = await fetchStatistics()
    if(response.status ===200){
        statisticsRef.value = {
            totalDraws: response.data.total_draws,
            lastDrawCount: response.data.last_24h,
            mostCommonNumber: response.data.most_common
        }
    }
}
async function handleFetchGeneratedNumbers() {
    const response = await fetchGenerateNumbers()
    if (response.status === 200) {
      generatedNumbers.value = response.data.numbers
      playWinningSound()
    } else {
      console.error('Error fetching generated numbers:', response.statusText)
      return []
    }
}

function playClickSound(){
  const playSound = new Audio(clickSoundFile);
  playSound.play();
}
function playWinningSound(){
  const winningSound = new Audio(winSoundFile);
  winningSound.play();
}

async function onSpinClick (){
    playClickSound();
    loading.value = true;
    handleFetchGeneratedNumbers();    
    handleFetchStatistics();
    loading.value = false;
}
</script>
