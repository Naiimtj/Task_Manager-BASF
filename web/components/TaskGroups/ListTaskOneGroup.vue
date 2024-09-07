<template>
  <div v-for="(task, index) in tasks" :key="index">
    <SingleTaskBasic :Task="task" @taskDeleted="toggleTaskList" />
  </div>
</template>

<script lang="ts" setup>
import SingleTaskBasic from "../Tasks/SingleTaskBasic.vue";
import type { ITask } from "~/interfaces/ITask";
import { getTaskOfGroup } from "~/server/FastApi/api-service";

const props = defineProps({
  group: {
    type: Object,
    default: {},
  },
});

const { group } = props;

const tasks = ref<ITask[]>([]);

if (tasks.value.length === 0) {
  getTaskOfGroup(group.id)
    .then((data: unknown) => {
      tasks.value = data as ITask[];
    })
    .catch((error) => {
      console.error("Error fetching All Tasks for One Group:", error);
    });
}
const toggleTaskList = () => {
  getTaskOfGroup(group.id)
    .then((data: unknown) => {
      tasks.value = data as ITask[];
    })
    .catch((error) => {
      console.error("Error fetching All Tasks for One Group:", error);
    });
};
</script>

<style scoped></style>
