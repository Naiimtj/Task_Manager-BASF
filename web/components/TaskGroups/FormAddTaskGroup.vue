<template>
  <!-- ADD TASK GROUP -->
  <button
    v-if="!formVisible"
    @click="toggleForm"
    class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded my-4 justify-center"
  >
    Create Task Group
  </button>
  <div v-else class="relative my-4">
    <form
      class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-sm"
      @submit.prevent="handleAddTaskGroup"
    >
      <div class="mb-4">
        <h3 class="block text-gray-700 text-lg font-bold mb-2 text-center">
          Task Group Name
        </h3>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          id="taskName"
          placeholder="Name"
          v-model="taskGroup.name"
        />
      </div>
      <div class="flex items-center justify-center">
        <button
          class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
        >
          Save
        </button>
      </div>
      <div>
        {{ error }}
      </div>
    </form>
    <Close
      @click="toggleForm"
      class="absolute top-0 right-0 cursor-pointer stroke-black hover:stroke-red-500 stroke-2"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { useAddTaskGroupStore } from "~/stores/useTaskGroupStore";
import { createTaskGroup } from "~/server/FastApi/api-service";
import type { IAddTaskGroup } from "~/interfaces/ITaskGroup";
import { Close } from "~/assets/icons";

const emit = defineEmits(["toggleNewTaskGroup"]);

const addTaskGroupStore = useAddTaskGroupStore();

const formVisible = ref(false);
const toggleForm = () => {
  formVisible.value = !formVisible.value;
};

let taskGroup = ref<IAddTaskGroup>({
  name: "",
});

const error = ref(null);

const handleAddTaskGroup = () => {
  if (taskGroup.value.name !== "") {
    createTaskGroup({ name: taskGroup.value.name })
      .then((response) => {
        if (response) {
          addTaskGroupStore.triggerAddTaskGroup()
          toggleForm();
          taskGroup.value.name = "";
        }
      })
      .catch((err) => {
        error.value = err;
      });
  }
};
</script>

<style scoped></style>
