import { defineNuxtConfig } from "nuxt/config";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  css: ["@/assets/css/tailwind.css"],
  modules: ["@nuxtjs/tailwindcss", '@pinia/nuxt'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  nitro: {
    plugins: ["~/server/index.ts"],
  },
  runtimeConfig: {
    public: {
      fastApiUri: process.env.FASTAPI_URI || 'http://localhost:5000',
    },
  },
  
});
