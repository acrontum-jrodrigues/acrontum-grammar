<script setup lang="ts">
import { webAppUrl } from '~/env';

function openWebApp() {
  browser.tabs.create({ url: webAppUrl });
}
</script>

<template>
  <main class="w-[300px] px-4 py-5 text-center text-gray-700">
    <Logo />
    <SharedSubtitle />

    <button class="btn mt-2" @click="openWebApp">Open Web App</button>
  </main>
</template>
