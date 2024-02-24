<script setup lang="ts">
</script>

<template>
  <div class="section-container">
    <textarea placeholder="Input the text you want to check" rows="10"></textarea>
    <button>Check grammar</button>
    <textarea placeholder="Corrected text will appear here" readonly rows="10"></textarea>
  </div>
</template>

<style scoped>
textarea {
  width: 100%;
  height: 100%;
  padding: 1rem;
  font-size: 1.2rem;
  border: 1px solid var(--color-border);
  border-radius: 5px;
  background-color: var(--vt-c-black);
  color: white;
}

button {
  padding: 1rem 2rem;
  font-size: 1.2rem;
  border: 1px solid var(--color-border);
  border-radius: 5px;
  background-color: var(--vt-c-blue);
  color: white;
  cursor: pointer;
  align-self: center;
}

.section-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  margin-top: 2rem;
}
</style>
