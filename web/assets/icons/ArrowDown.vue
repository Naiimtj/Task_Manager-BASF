<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="width"
    :height="height"
  >
    <path fill="none" d="M0 0h24v24H0V0z" />
    <path
      d="M12 15.5a1 1 0 0 1-.71-.29l-4-4a1 1 0 1 1 1.42-1.42L12 13.1l3.3-3.18a1 1 0 1 1 1.38 1.44l-4 3.86a1 1 0 0 1-.68.28Z"
    />
  </svg>
</template>

<script setup>
defineProps({
  width: { type: Number, default: 24 },
  height: { type: Number, default: 24 },
});
</script>
