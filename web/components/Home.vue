<template>
  <div class="my-2 flex flex-col items-center">
    <h1 class="text-5xl underline underline-offset-8 mb-4">Hello World</h1>
    <p>This is my Task List Manager</p>
    <p>You can create your Group Tasks</p>
    <!-- ADD TASK GROUP -->
    <!-- <div v-if="!formVisible" class="flex gap-2">Create Task Group</div> -->
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
  <label class="relative block">
    <span class="sr-only">Search</span>
    <span class="absolute inset-y-0 left-0 flex items-center pl-2">
      <Search class="fill-slate-300" />
    </span>
    <input
      class="placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-gray-500 focus:ring-gray-500 focus:ring-1 sm:text-sm"
      placeholder="Search task..."
      type="text"
      name="search"
    />
  </label>
  <!-- LIST TASK GROUP -->
  <div class="w-full border border-white/10 rounded-xl p-4">
    <div class="flex flex-col gap-4">
      <ListTaskGroup :addNewTaskGroup="addNewTaskGroup" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import FormAddTaskGroup from "./TaskGroups/FormAddTaskGroup.vue";
import ListTaskGroup from "./TaskGroups/ListTaskGroup.vue";
import { Search, Close } from "~/assets/icons";

const formVisible = ref(false);
const toggleForm = () => {
  formVisible.value = !formVisible.value;
};

const addNewTaskGroup = ref(false);
const toggleNewTaskGroup = () => {
  addNewTaskGroup.value = !addNewTaskGroup.value;
  formVisible.value = !formVisible.value;
};
</script>

<style scoped></style>
