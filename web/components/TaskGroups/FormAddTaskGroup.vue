<template>
  <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-sm">
    <div class="mb-4">
      <h3 class="block text-gray-700 text-lg font-bold mb-2 text-center">
        Task Group Name
      </h3>
      <input
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type="text"
        placeholder="Name"
        v-model="taskGroup.name"
      />
    </div>
    <div class="flex items-center justify-center">
      <button
        class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        type="submit"
        @click="handleAddTaskGroup()"
      >
        Save
      </button>
    </div>
    <div>
      {{ error }}
    </div>
  </form>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { createTaskGroup } from "~/server/fastApi/api-service";
import type { IAddTaskGroup } from "~/interfaces/ITaskGroup";

const props = defineProps({
  toggleNewTaskGroup: {
    type: Function,
    default: () => {},
  },
});

let taskGroup = ref<IAddTaskGroup>({
  name: "",
});
const error = ref(null);
const handleAddTaskGroup = () => {
  if (taskGroup.value.name !== "") {
    createTaskGroup({ name: taskGroup.value.name })
      .then((response) => {
        if (response) {
          props.toggleNewTaskGroup();
          taskGroup.value.name = "";
        }
      })
      .catch((err) => {
        error.value = err.response.data.message;
      });
  }
};
</script>

<style scoped></style>
