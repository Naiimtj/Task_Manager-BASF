<template>
  <div class="my-2 flex flex-col items-center">
    <h1 class="text-5xl underline underline-offset-8 mb-4">To Do</h1>
    <p>This is my Task List Manager</p>
    <p>You can create your Group Tasks</p>
    <!-- ADD TASK GROUP -->
    <FormAddTaskGroup />
  </div>
  <!-- SEARCH -->
  <!-- Button -->
  <div v-if="seeAllTasks && tasks.length > 0">
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
      type="search"
      name="search"
      v-model="query"
    />
  </label>
  <!-- Search List Tasks -->
  <div v-if="tasks.length > 0" class="overflow-y-auto max-h-[200px]">
    <div
      v-if="tasks[0].title === 'Empty'"
      class="p-2 rounded-lg border border-gray-400 hover:bg-gray-700 flex flex-row items-center justify-between w-full gap-2 px-2"
    >
      No Results
    </div>
    <div
      v-else
      v-for="task in tasks"
      :key="task.id"
      class="border-b border-b-gray-400"
    >
      <SingleTask :Task="task" />
    </div>
  </div>
  <div v-else>
    <div v-if="tasks.length === 0"></div>
  </div>
  <!-- LIST TASK GROUP -->
  <div class="w-full border border-white/10 rounded-xl p-4">
    <div class="flex flex-col gap-4">
      <ListTaskGroup />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, watchEffect } from "vue";
import FormAddTaskGroup from "./TaskGroups/FormAddTaskGroup.vue";
import ListTaskGroup from "./TaskGroups/ListTaskGroup.vue";
import { Search } from "~/assets/icons";
import { searchTaskTitle } from "../server/FastApi/api-service.js";
import SingleTask from "./Tasks/SingleTask.vue";
import type { ITask } from "~/interfaces/ITask";

const query = ref<string>("");
const tasks = ref<ITask[]>([]);
// - SEARCH ALL TASKS
const seeAllTasks = ref(false);
const toggleSeeAllTasks = async () => {
  seeAllTasks.value = !seeAllTasks.value;
  if (seeAllTasks.value) {
    query.value = "";
    try {
      const data = await searchTaskTitle("allTasks");
      tasks.value = data as ITask[];
    } catch (error) {
      console.error("Error fetching query task:", error);
    }
  } else {
    tasks.value = [];
    query.value = "";
  }
};
// - SEARCH A TITLE
watchEffect(async () => {
  if (query.value) {
    try {
      const data = await searchTaskTitle(query.value);
      tasks.value = data as ITask[];
    } catch (error) {
      console.error("Error fetching query task:", error);
    }
  } else {
    tasks.value = [];
  }
});
</script>

<style scoped></style>
