<template>
  <!-- SEEN OR NOT SEEN TASKS -->
  <button
    type="button"
    class="flex justify-center gap-1 w-full p-2 rounded-lg hover:bg-gray-700 hover:text-white font-semibold"
    @click="isGroupOpen()"
  >
    {{ group.name }}
    <div v-if="openGroups">
      <ArrowUp class="fill-white" />
    </div>
    <div v-else>
      <ArrowDown class="fill-white" />
    </div>
  </button>
  <!-- LIST TASKS -->
  <div v-if="openGroups" class="text-center overflow-y-auto max-h-[120px]">
    <ListTaskOneGroup :group="group" />
  </div>
</template>

<script lang="ts" setup>
import { ref, watchEffect } from "vue";
import { useCloseAllTaskGroupStore } from "~/store/useTaskGroupStore";
import { ArrowDown, ArrowUp } from "~/assets/icons";
import ListTaskOneGroup from "./ListTaskOneGroup.vue";

const props = defineProps({
  group: {
    type: Object,
    default: {},
  },
});

const { group } = props;

const openGroups = ref(false);

const isGroupOpen = () => {
  openGroups.value = !openGroups.value;
};

const taskGroupStore = useCloseAllTaskGroupStore();

watchEffect(() => {
  if (taskGroupStore.closeAllGroups) {
    openGroups.value = false;
  }
});
</script>

<style scoped></style>
