<template>
  <div class="relative flex justify-center">
    <h3 class="text-center font-bold text-4xl mb-4">Task Groups</h3>
    <p>({{ listTaskGroup.length }})</p>
    <button
      class="absolute flex items-center right-0 bottom-0 text-center"
      @click="closeAllTasks"
    >
      <CloseMenu class="fill-gray-400 hover:fill-white" />
    </button>
  </div>

  <div class="grid grid-cols-4">
    <div
      v-for="group in listTaskGroup"
      @click.prevent="toggleTaskList(group.id)"
      :key="group.id"
      class="p-2 rounded-lg border border-gray-400"
    >
      <button
        type="button"
        class="flex justify-center gap-1 w-full p-2 rounded-lg hover:bg-gray-700 hover:text-white font-semibold"
      >
        {{ group.name }}
        <div v-if="isGroupOpen(group.id)">
          <ArrowUp class="fill-white" />
        </div>
        <div v-else>
          <ArrowDown class="fill-white" />
        </div>
      </button>
      <div v-if="isGroupOpen(group.id)" class="text-center">
        <div v-for="task in tasks[group.id]" :key="task.id">
          <SingleTaskBasic :Task="task" @taskDeleted="toggleTaskList" />
        </div>
      </div>
      <div class="flex justify-around">
        <button
          @click="navigateToUrl(group.id)"
          class="text-center text-gray-400 hover:text-gray-200 mt-2"
        >
          + Add Task
        </button>
        <button
          class="flex gap-1 text-center text-red-400 hover:text-gray-200 mt-2 hover:fill-white fill-red-400"
          @click="handleDeleteTaskGroup(group.id)"
        >
          <Delete class="scale-75" />
          Delete Group
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watchEffect } from "vue";
import { useRouter } from "vue-router";
import type { ITask } from "~/interfaces/ITask";
import type { ITaskGroup } from "~/interfaces/ITaskGroup";
import { getAllGroups, getTaskOfGroup, deleteTaskGroup } from "~/server/fastApi/api-service";
import { CloseMenu, ArrowDown, ArrowUp, Delete } from "~/assets/icons";
import SingleTaskBasic from "../Tasks/SingleTaskBasic.vue";

const router = useRouter();

const navigateToUrl = (groupId: number) => {
  router.push(`/task/${groupId}`);
};

const props = defineProps({
  addNewTaskGroup: {
    type: Boolean,
    default: false,
  },
});
const deleteOneTaskGroup = ref(false);

const openGroups = ref<number[]>([]);

const listTaskGroup = ref<ITaskGroup[]>([]);
const tasks = ref<ITask[]>([]);

watchEffect(async () => {
  if (props.addNewTaskGroup || deleteOneTaskGroup.value) {
    try {
      const data = (await getAllGroups()) as unknown as ITaskGroup[];
      listTaskGroup.value = data;
      deleteOneTaskGroup.value = false
    } catch (error) {
      console.error("Error fetching task groups:", error);
    }
  }
  if (listTaskGroup.value.length === 0) {
    onMounted(async () => {
      try {
        const data = (await getAllGroups()) as unknown as ITaskGroup[];
        listTaskGroup.value = data;
        deleteOneTaskGroup.value = false
    } catch (error) {
        console.error("Error fetching task groups:", error);
      }
    });
  }
});

const toggleTaskList = (groupId: number) => {
  const index = openGroups.value.indexOf(groupId);
  if (index === -1) {
    openGroups.value.push(groupId);
    getTaskOfGroup(groupId)
      .then((data: unknown) => {
        tasks.value[groupId] = data as ITask[];
      })
      .catch((error) => {
        console.error("Error fetching tasks for group:", error);
      });
  } else {
    openGroups.value.splice(index, 1);
    delete tasks.value[groupId];
  }
};

const isGroupOpen = (groupId: number) => openGroups.value.includes(groupId);

const closeAllTasks = () => {
  openGroups.value = [];
  tasks.value = {};
};

const handleDeleteTaskGroup = (groupId: number) => {
  deleteTaskGroup(groupId)
    .then(() => {
      deleteOneTaskGroup.value = !deleteOneTaskGroup.value
    })
    .catch((err) => {
      error.value = err.response.data.message;
      console.error("Error delete task:", err);
    });
};
</script>

<style scoped></style>
