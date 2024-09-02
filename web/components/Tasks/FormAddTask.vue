<template>
  <div class="modal-content flex justify-center">
    <form @submit.prevent="submitForm" class="flex flex-col gap-4 w-80">
      <!-- TASK NAME -->
      <div class="grid grid-cols-6 gap-6">
        <label for="taskTitle" class="col-span-2">Task Name:</label>
        <input
          type="text"
          id="taskTitle"
          v-model="taskTitle"
          required
          class="col-span-4 bg-gray-400/10 hover:bg-gray-400/50 pl-2 w-full rounded-md"
        />
      </div>
      <!-- DESCRIPTION -->
      <div class="grid grid-cols-6 gap-6">
        <label for="taskDescription" class="col-span-2">Description:</label>
        <textarea
          id="taskDescription"
          v-model="taskDescription"
          class="col-span-4 bg-gray-400/10 hover:bg-gray-400/50 pl-2 w-full rounded-md"
        ></textarea>
      </div>
      <!-- PRIORITY -->
      <label for="taskPriority">Priority:</label>
      <select
        id="taskPriority"
        v-model="taskPriority"
        class="bg-gray-400/10 hover:bg-gray-400/50 rounded-md cursor-pointer"
      >
        <option
          v-for="priority in prioritys"
          :key="priority.code"
          :value="priority.name"
          class="bg-gray-700 cursor-pointer"
        >
          {{ priority.name }}
        </option>
      </select>
      <!-- LABELS -->
      <AddLabels :labels="labels" />
      <!-- SUBMIT -->
      <div class="flex justify-between">
        <button
          type="button"
          @click="closeModal"
          class="hover:bg-red-600 bg-gray-900 py-1 w-20 rounded-lg"
        >
          Cancel
        </button>
        <button
          type="submit"
          class="bg-green-400 hover:bg-green-700 py-1 w-20 rounded-lg text-gray-900 hover:text-white font-semibold"
        >
          Save
        </button>
      </div>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { createTask, editTask } from "../../server/fastApi/api-service";
import { ref } from "vue";
import { useRouter } from "vue-router";
import AddLabels from "./AddLabels";

const props = defineProps({
  isEdit: {
    type: Boolean,
    default: false,
  },
  task: {
    type: Object,
    default: {},
  },
});
const { isEdit, task } = props;

let prioritys = ref([
  { code: "1", name: "High" },
  { code: "2", name: "Medium" },
  { code: "3", name: "Low" },
]);

const router = useRouter();
const route = useRoute();

const labels = ref<Array>(isEdit ? task.labels : []);
const taskTitle = ref<string>(isEdit ? task.title : "");
const taskDescription = ref<string>(isEdit ? task.description : "");
const taskPriority = ref<string>(isEdit ? task.priority : "Low");

const closeModal = () => {
  router.push("/");
};
const groupId = route.params.groupId;
const taskId = route.params.taskId;

const error = ref(null);

const submitForm = () => {
  if (isEdit) {
    editTask(taskId, {
      title: taskTitle.value,
      description: taskDescription.value,
      priority: taskPriority.value,
      labels: labels.value,
      group_id: Number(groupId),
    })
      .then((response) => {
        if (response) {
          // Reset form and close
          taskTitle.value = "";
          taskDescription.value = "";
          taskPriority.value = "Low";
          (labels.value = []), closeModal();
        }
      })
      .catch((err) => {
        error.value = err.response.data.message;
        console.error("Error updating task:", err);
      });
  } else {
    createTask({
      title: taskTitle.value,
      description: taskDescription.value,
      priority: taskPriority.value,
      labels: labels.value,
      group_id: Number(groupId),
    })
      .then((response) => {
        if (response) {
          // Reset form and close
          taskTitle.value = "";
          taskDescription.value = "";
          taskPriority.value = "Low";
          (labels.value = []), closeModal();
        }
      })
      .catch((err) => {
        error.value = err.response.data.message;
      });
  }
};
</script>

<style scoped></style>
