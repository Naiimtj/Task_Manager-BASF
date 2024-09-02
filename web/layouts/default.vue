<template>
  <div
    class="h-full min-h-screen flex flex-col relative text-black dark:text-white top-0 bottom-0 w-full bg-gray-50 dark:bg-gray-950 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(37,45,117,0.5),rgba(255,255,255,0.9))] dark:bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(37,45,117,0.5),rgba(255,255,255,0))] px-6 items-center"
  >
    <head
      class="absolute z-50 flex gap-6 mt-5 backdrop-blur-md p-2 rounded-xl text-gray-400"
    >
      <NuxtLink
        v-for="link in links"
        :key="link.name"
        :to="link.path"
        :class="isActive(link.path)"
        >{{ link.name }}</NuxtLink
      >
    </head>
    <body class="mt-14 w-full">
      <slot />
    </body>
  </div>
</template>

<script lang="ts" setup>
useHead({
  meta: [{ name: "description", content: "Gestor de tareas avanzado" }],
});
import { useRoute } from "nuxt/app";

const links = [
  { name: "Home", path: "/" },
  { name: "Contact", path: "/contact" },
  // { name: "Login", path: "/login" },
];

const route = useRoute();

const isActive = (path: string): string => {
  return route.path === path
    ? "font-bold text-gray-200"
    : "hover:font-bold text-gray-200";
};
</script>

<style scoped></style>
