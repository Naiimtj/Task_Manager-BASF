<template>
  <NuxtLayout name="task">
    <h1 class="text-5xl text-center underline underline-offset-8 mb-6">
      ADD TASK
    </h1>
    <FormAddTask :isEdit="false" />
  </NuxtLayout>
</template>

<script lang="ts" setup>
import FormAddTask from "../../components/Tasks/FormAddTask";
import { useRoute } from "vue-router";

const route = useRoute();
const groupId = route.params.groupId;

definePageMeta({
  layout: "default",
});
</script>

<style scoped></style>
