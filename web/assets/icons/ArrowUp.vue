<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="width"
    :height="height"
  >
    <path fill="none" d="M0 0h24v24H0V0z" />
    <path
      d="M16 14.5a1 1 0 0 1-.71-.29L12 10.9l-3.3 3.18a1 1 0 0 1-1.41 0 1 1 0 0 1 0-1.42l4-3.86a1 1 0 0 1 1.4 0l4 4a1 1 0 0 1 0 1.42 1 1 0 0 1-.69.28Z"
    />
  </svg>
</template>

<script setup>
defineProps({
  width: { type: Number, default: 24 },
  height: { type: Number, default: 24 },
});
</script>
