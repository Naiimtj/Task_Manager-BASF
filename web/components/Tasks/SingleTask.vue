<template>
  <div>
    <tr>
      <td>
        {{ props.Task.title }}
      </td>
      <td>{{ props.Task.description }}</td>
      <td>{{ props.Task.priority }}</td>
      <td>{{ props.Task.labels }}</td>
      <td>{{ props.Task.completed }}</td>
    </tr>
  </div>
</template>

<script lang="ts" setup>
import type { ITask } from "~/interfaces/ITask";

const props = defineProps({
  Task: {
    type: Object as () => ITask,
    default: {},
  },
});
</script>

<style scoped></style>
