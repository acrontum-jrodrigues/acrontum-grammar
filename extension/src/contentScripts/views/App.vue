<script setup lang="ts">
import { useToggle } from "@vueuse/core";
import axios from 'axios';
import { debounce } from "lodash";
import "uno.css";

const [show, toggle] = useToggle(false);

// Function to perform grammar check
function performGrammarCheck(text: string, input: Element) {
  axios.post('http://localhost:5000/grammar', { text })
    .then((response: any) => {
      const editedText = response.data.edited_text;
      console.log(editedText);
      if (editedText !== text) {
        highlightDifferences(editedText, text, input);
      }
    })
    .catch((error: any) => {
      alert(error.message);
    });
}

// Function to highlight differences between original and edited text
function highlightDifferences(editedText: string, originalText: string, input: Element) {
  const originalWords = originalText?.split(" ");
  const editedWords = editedText.split(" ");
  const differences = originalWords?.map((word, index) => {
    if (word !== editedWords[index]) {
      return `<span style="background-color: yellow">${editedWords[index]}</span>`;
    }
    return word;
  });
  const highlightedText = differences?.join(" ");
  input!.innerHTML = highlightedText;
}

// Watch for changes in user input
function watchAllInputs() {
  const inputs = document.querySelectorAll("input[type='text'], textarea");
  inputs.forEach((input) => {
    input.addEventListener("input", debounce((event) => {
      const newValue = event.target.value;
      if (newValue.length < 3) return;
      performGrammarCheck(newValue, input);
    }, 400));
  });
}

watchAllInputs();
</script>

<template>
  <div class="fixed right-0 bottom-0 m-5 z-100 flex items-end font-sans select-none leading-1em">
    <div class="bg-white text-gray-800 rounded-lg shadow w-max h-min" p="x-4 y-2" m="y-auto r-2"
      transition="opacity duration-300" :class="show ? 'opacity-100' : 'opacity-0'">
      <h1 class="text-lg">
        Acrontum Grammar
      </h1>
      <SharedSubtitle />
    </div>
    <button class="flex w-10 h-10 rounded-full shadow cursor-pointer border-none justify-center" bg="white hover:gray-300"
      @click="toggle()">
      <img src="/assets/acrontum_logo.ico" class="m-auto" alt="extension icon" width="32" height="32">
    </button>
  </div>
</template>
