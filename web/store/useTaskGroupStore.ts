import { defineStore } from "pinia";
import { ref } from "vue";

export const useCloseAllTaskGroupStore = defineStore("Close All Task Groups", () => {
  const closeAllGroups = ref(false);

  const triggerCloseAllGroups = () => {
    closeAllGroups.value = !closeAllGroups.value;
  };

  return {
    closeAllGroups,
    triggerCloseAllGroups,
  };
});

export const useAddTaskGroupStore = defineStore("Add/Delete Task Group", () => {
  const addTaskGroup = ref(false);

  const triggerAddTaskGroup = () => {
    addTaskGroup.value = !addTaskGroup.value;
  };

  return {
    addTaskGroup,
    triggerAddTaskGroup,
  };
});
