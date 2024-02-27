<script setup lang="ts">
import { storageDemo } from '~/logic/storage';

function openWebApp() {
  browser.tabs.create({ url: 'http://localhost:5173' });
}
</script>

<template>
  <main class="w-[300px] px-4 py-5 text-center text-gray-700">
    <Logo />
    <SharedSubtitle />

    <button class="btn mt-2" @click="openWebApp">Open Web App</button>
    <div class="mt-2">
      <span class="opacity-50">Storage:</span> {{ storageDemo }}
    </div>
  </main>
</template>
