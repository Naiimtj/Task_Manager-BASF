<template>
  <h3 class="text-lg">Labels:</h3>
  <!-- List of labels -->
  <div class="flex flex-wrap">
    <div
      v-for="(label, index) in labels"
      :key="index"
      class="bg-gray-200 text-gray-800 rounded-lg mr-2 mt-2 px-2 flex items-center"
    >
      <span class="mr-1">{{ label }}</span>
      <button
        type="button"
        @click="removeLabel(index)"
        class="text-red-500 hover:text-red-700"
      >
        &times;
      </button>
    </div>
  </div>
  <!-- Field to add the label -->
  <div class="mb-4">
    <input
      v-model="newLabel"
      @keydown.enter.prevent="addLabel"
      type="text"
      placeholder="Type a label and press Enter"
      class="border border-gray-300 p-2 rounded w-full text-black"
      id="labels"
    />
  </div>
</template>

<script setup>
import { ref, watch, toRefs } from "vue";

const props = defineProps({
  labels: Array,
  default: [],
});

const { labels } = toRefs(props); // Hacemos reactivo el prop
const newLabel = ref("");

// Función para añadir una etiqueta
const addLabel = () => {
  if (newLabel.value.trim() !== "" && !labels.value.includes(newLabel.value)) {
    labels.value.push(newLabel.value.trim());
    newLabel.value = "";
  }
};

// Función para eliminar una etiqueta
const removeLabel = (index) => {
  labels.value.splice(index, 1);
};
</script>

<style scoped></style>
