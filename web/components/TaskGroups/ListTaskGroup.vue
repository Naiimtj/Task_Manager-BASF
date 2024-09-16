<template>
  <div class="relative flex justify-center">
    <h3 class="text-center font-bold text-4xl mb-4">Task Groups</h3>
    <p>({{ listTaskGroup.length }})</p>
    <!-- CLOSE ALL MENUS -->
    <button
      class="absolute flex items-center right-0 bottom-0 text-center"
      @click="triggerCloseAllTasks"
    >
      <CloseMenu class="fill-gray-400 hover:fill-white" />
    </button>
  </div>
  <!-- List Task Groups -->
  <div class="grid grid-cols-4 overflow-y-auto max-h-[200px]">
    <div
      v-for="group in listTaskGroup"
      :key="group.id"
      class="p-2 rounded-lg border border-gray-400"
    >
      <SingleGroup :group="group" />
      <!-- ADD TASK OR DELETE -->
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
import {
  useCloseAllTaskGroupStore,
  useAddTaskGroupStore,
} from "~/store/useTaskGroupStore";
import type { ITaskGroup } from "~/interfaces/ITaskGroup";
import { deleteTaskGroup, getAllGroups } from "~/server/FastApi/api-service";
import { CloseMenu, Delete } from "~/assets/icons";
import SingleGroup from "./SingleGroup.vue";

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
const listTaskGroup = ref<ITaskGroup[]>([]);

const setDeleteOneTaskGroup = () => {
  deleteOneTaskGroup.value = !deleteOneTaskGroup.value;
};

const closeAllTaskGroupStore = useCloseAllTaskGroupStore();

const triggerCloseAllTasks = () => {
  closeAllTaskGroupStore.triggerCloseAllGroups();
  setTimeout(() => closeAllTaskGroupStore.triggerCloseAllGroups(), 500);
};

const addTaskGroupStore = useAddTaskGroupStore();

watchEffect(async () => {
  if (addTaskGroupStore.addTaskGroup || deleteOneTaskGroup.value) {
    try {
      const data = (await getAllGroups()) as unknown as ITaskGroup[];
      listTaskGroup.value = data;
      addTaskGroupStore.triggerAddTaskGroup();
      deleteOneTaskGroup.value = false;
    } catch (error) {
      console.error("Error fetching task groups:", error);
    }
  }
  if (listTaskGroup.value.length === 0) {
    onMounted(async () => {
      try {
        const data = (await getAllGroups()) as unknown as ITaskGroup[];
        listTaskGroup.value = data;
        deleteOneTaskGroup.value = false;
      } catch (error) {
        console.error("Error fetching task groups:", error);
      }
    });
  }
});

const handleDeleteTaskGroup = (groupId: number) => {
  deleteTaskGroup(groupId)
    .then(() => {
      addTaskGroupStore.triggerAddTaskGroup();
    })
    .catch((err) => {
      console.error("Error delete task:", err);
    });
};
</script>

<style scoped></style>
