<template>
  <NuxtLayout name="task">
    <h1 class="text-5xl text-center underline underline-offset-8 mb-6">ADD TASK</h1>
    <FormAddTask />
  </NuxtLayout>
</template>

<script lang="ts" setup>
import FormAddTask from "../../components/Tasks/FormAddTask"

definePageMeta({
  layout: "default",
});

</script>

<style scoped></style>
