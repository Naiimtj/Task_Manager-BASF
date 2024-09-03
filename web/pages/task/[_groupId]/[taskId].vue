<template>
  <h1 class="text-5xl text-center underline underline-offset-8 mb-6">
    EDIT TASK
  </h1>
  <div v-for="task in tasks">
    <FormAddTask :isEdit="true" :task="task" />
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import FormAddTask from "../../../components/Tasks/FormAddTask";
import type { ITask } from "~/interfaces/ITask";
import { getTask } from "../../../server/FastApi/api-service";

const route = useRoute();

const groupId = route.params.groupId;
const taskId = route.params.taskId;

const tasks = ref<ITask[]>([]);

if (tasks.value.length === 0) {
  onMounted(async () => {
    try {
      const data = (await getTask(taskId)) as unknown as ITask[];
      tasks.value = data;
    } catch (error) {
      console.error("Error fetching task:", error);
    }
  });
}
</script>

<style scoped></style>
