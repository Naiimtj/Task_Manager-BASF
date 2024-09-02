<template>
  <div @click.stop>
    <tr
      :class="
        props.Task.completed
          ? 'flex items-center gap-4 hover:bg-gray-700'
          : `flex items-center gap-4 ${PriorityColor}`
      "
    >
      <td class="flex flex-row items-center justify-between w-full gap-2 px-2">
        <div class="flex flex-row items-center">
          <input
            type="checkbox"
            v-model="props.Task.completed"
            class="custom-checkbox h-5 w-5 cursor-pointer mr-2"
            @chick="handleEditTask"
          />
          <p
            :class="
              props.Task.completed
                ? 'line-through text-gray-200'
                : 'text-gray-200'
            "
          >
            {{ props.Task.title }} ({{ props.Task.description }})
          </p>
        </div>
        <button
          type="button"
          class="rounded-lg hover:fill-white fill-gray-400 hover:text-white font-semibold"
        >
          <Delete />
        </button>
      </td>
    </tr>
  </div>
</template>

<script lang="ts" setup>
import { watch } from "vue";
import type { ITask } from "~/interfaces/ITask";
import { editTask } from "~/server/fastApi/api-service";
import { Delete } from "../../assets/icons";

const props = defineProps({
  Task: {
    type: Object as () => ITask,
    default: {},
  },
});

let PriorityColor = "";
switch (props.Task.priority) {
  case "Hight":
    PriorityColor = "bg-red-500 hover:bg-red-700";
    break;
  case "Medium":
    PriorityColor = "bg-orange-500 hover:bg-orange-700";
    break;
  case "Low":
    PriorityColor = "hover:bg-gray-700";
    break;

  default:
    PriorityColor = "hover:bg-gray-700";
    break;
}
const error = ref(null);
watch(
  () => props.Task.completed,
  async (newValue) => {
    handleEditTask(await newValue);
  }
);

const handleEditTask = (newCompletedValue: boolean) => {
  editTask(props.Task.id, { completed: newCompletedValue })
    .then(() => {})
    .catch((err) => {
      error.value = err.response.data.message;
      console.error("Error updating task:", err);
    });
};
</script>

<style scoped>
.custom-checkbox {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-color: #f3f4f6; /* Fondo normal del checkbox */
  border: 2px solid #9ca3af; /* Borde normal */
  border-radius: 0.25rem;
  width: 1.25rem;
  height: 1.25rem;
  display: inline-block;
  position: relative;
  cursor: pointer;
}

.custom-checkbox:checked {
  background-color: #a6f9ac; /* Fondo verde cuando está seleccionado */
  border-color: #a6f9ac; /* Borde verde cuando está seleccionado */
}
</style>
