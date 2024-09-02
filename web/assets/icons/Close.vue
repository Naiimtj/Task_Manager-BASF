<template>
  <svg
    :width="width"
    :height="height"
    viewBox="0 0 24 24"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M18 6 6 18M6 6l12 12" />
  </svg>
</template>

<script setup>
defineProps({
  width: { type: Number, default: 24 },
  height: { type: Number, default: 24 },
});
</script>
