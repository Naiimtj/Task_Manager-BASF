<template>
  <div class="my-2 flex flex-col gap-6 items-center">
    <div class="text-5xl underline underline-offset-8">CONTACT</div>
    <p>
      Contact to me if you need help:
      <a
        :href="mailtoLink"
        class="text-white underline underline-offset-2 font-semibold"
        >Naiim.tj@gmail.com</a
      >
    </p>
  </div>
</template>

<script lang="ts" setup>
import { computed } from "vue";
const mailtoLink = computed(() => {
  return `mailto:naiim.tj@gmail.com`;
});
</script>

<style scoped></style>
