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
        <div
          class="flex flex-row items-center cursor-pointer w-full"
          @click="toggleCheck"
        >
          <input
            type="checkbox"
            v-model="props.Task.completed"
            class="custom-checkbox h-5 w-5 mr-2"
          />
          <p
            :class="
              props.Task.completed
                ? 'line-through text-gray-200'
                : 'text-gray-200'
            "
          >
            {{ props.Task.title }}
          </p>
        </div>
        <div class="flex gap-1">
          <button
            type="button"
            @click="navigateToUrl(props.Task.group_id, props.Task.id)"
            class="rounded-lg hover:fill-white fill-gray-400 hover:text-white font-semibold"
          >
            <Edit />
          </button>
          <button
            type="button"
            class="rounded-lg hover:fill-white fill-red-400/60 font-semibold"
            @click="handleDeleteTask"
          >
            <Delete />
          </button>
        </div>
      </td>
    </tr>
  </div>
</template>

<script lang="ts" setup>
import { watch } from "vue";
import { useRouter } from "vue-router";
import type { ITask } from "~/interfaces/ITask";
import { editTask, deleteTask } from "~/server/FastApi/api-service";
import { Delete, Edit } from "../../assets/icons";

const emit = defineEmits(["taskDeleted"]);

const props = defineProps({
  Task: {
    type: Object as () => ITask,
    default: {},
  },
});

const router = useRouter();

const navigateToUrl = (groupId: number, taskId: number) => {
  router.push(`/task/${groupId}/${taskId}`);
};

let PriorityColor = "";
switch (props.Task.priority) {
  case "High":
    PriorityColor = "bg-red-500/30 hover:bg-gray-700/30";
    break;
  case "Medium":
    PriorityColor = "bg-orange-500/30 hover:bg-gray-700/30";
    break;
  case "Low":
    PriorityColor = "hover:bg-gray-700/30";
    break;

  default:
    PriorityColor = "hover:bg-gray-700";
    break;
}

const toggleCheck = () => {
  props.Task.completed = !props.Task.completed;
};

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

const handleDeleteTask = (newCompletedValue: boolean) => {
  deleteTask(props.Task.id)
    .then(() => {
      emit("taskDeleted", props.Task.group_id);
    })
    .catch((err) => {
      error.value = err.response.data.message;
      console.error("Error delete task:", err);
    });
};
</script>

<style scoped>
.custom-checkbox {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-color: #f3f4f6;
  border: 2px solid #9ca3af;
  border-radius: 0.25rem;
  width: 1.25rem;
  height: 1.25rem;
  display: inline-block;
  position: relative;
  cursor: pointer;
}

.custom-checkbox:checked {
  background-color: #a6f9ac;
  border-color: #a6f9ac;
}
</style>
