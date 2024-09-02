<template>
  <div class="my-2 flex flex-col items-center">
    <h1 class="text-5xl underline underline-offset-8 mb-4">Hello World</h1>
    <p>This is my Task List Manager</p>
    <p>You can create your Group Tasks</p>
    <!-- ADD TASK GROUP -->
    <button
      v-if="!formVisible"
      @click="toggleForm"
      class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded my-4 justify-center"
    >
      Create Task Group
    </button>
    <div v-else class="relative my-4">
      <FormAddTaskGroup :toggleNewTaskGroup="toggleNewTaskGroup" />
      <Close
        @click="toggleForm"
        class="absolute top-0 right-0 cursor-pointer stroke-black hover:stroke-red-500 stroke-2"
      />
    </div>
  </div>
  <!-- SEARCH -->
  <!-- Button -->
  <div v-if="seeAllTasks & (tasks != 'Empty')">
    <button
      type="button"
      class="hover:bg-gray-700 underline underline-offset-2 text-white font-bold py-1 px-2 rounded justify-end"
      @click="toggleSeeAllTasks"
    >
      Clean
    </button>
  </div>
  <div v-else>
    <button
      type="button"
      class="hover:bg-gray-700 underline underline-offset-2 text-white font-bold py-1 px-2 rounded justify-end"
      @click="toggleSeeAllTasks"
    >
      See All Tasks
    </button>
  </div>
  <!-- Bar Search -->
  <label class="relative block">
    <span class="sr-only">Search</span>
    <span class="absolute inset-y-0 left-0 flex items-center pl-2">
      <Search class="fill-slate-300" />
    </span>
    <input
      class="placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-gray-500 focus:ring-gray-500 focus:ring-1 sm:text-sm text-gray-700"
      placeholder="Search task..."
      type="text"
      name="search"
      v-model="query"
    />
  </label>
  <!-- Search List Tasks -->
  <div
    v-if="(tasks.length > 0) & (tasks != 'Empty')"
    class="overflow-y-auto max-h-[200px]"
  >
    <div
      v-for="task in tasks"
      :key="task.id"
      class="p-2 rounded-lg border border-gray-400"
    >
      <SingleTask :Task="task" />
    </div>
  </div>
  <div v-else>
    <div v-if="tasks != 'Empty'">
      <tr
        class="p-2 rounded-lg border border-gray-400 flex items-center gap-4 hover:bg-gray-700"
      >
        <td
          class="flex flex-row items-center justify-between w-full gap-2 px-2"
        >
          <div class="flex flex-row items-center cursor-pointer w-full">
            No Results
          </div>
        </td>
      </tr>
    </div>
  </div>
  <!-- LIST TASK GROUP -->
  <div class="w-full border border-white/10 rounded-xl p-4">
    <div class="flex flex-col gap-4">
      <ListTaskGroup :addNewTaskGroup="addNewTaskGroup" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watchEffect } from "vue";
import FormAddTaskGroup from "./TaskGroups/FormAddTaskGroup.vue";
import ListTaskGroup from "./TaskGroups/ListTaskGroup.vue";
import { Search, Close } from "~/assets/icons";
import { searchTaskTitle } from "../server/FastApi/api-service.js";
import SingleTask from "./Tasks/SingleTask";

const formVisible = ref(false);
const toggleForm = () => {
  formVisible.value = !formVisible.value;
};

const addNewTaskGroup = ref(false);
const toggleNewTaskGroup = () => {
  addNewTaskGroup.value = !addNewTaskGroup.value;
  formVisible.value = !formVisible.value;
};

let taskGroup = ref<ITask>({
  title: "",
});

const seeAllTasks = ref(false);
const toggleSeeAllTasks = async () => {
  seeAllTasks.value = !seeAllTasks.value;
  if (seeAllTasks.value) {
    try {
      const data = await searchTaskTitle("allTasks");
      tasks.value = data;
    } catch (error) {
      console.error("Error fetching query task:", error);
    }
  } else {
    tasks.value = "Empty";
    query.value = "";
  }
};

const query = ref<string>("");
const tasks = ref<ITask[]>([]);

watchEffect(async () => {
  if (query.value) {
    try {
      const data = await searchTaskTitle(query.value);
      tasks.value = data;
      seeAllTasks.value = true;
    } catch (error) {
      console.error("Error fetching query task:", error);
    }
  } else {
    tasks.value = "Empty";
    seeAllTasks.value = false;
  }
});
</script>

<style scoped></style>
