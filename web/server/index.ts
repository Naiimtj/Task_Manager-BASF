import axios from "axios";
import { Nitro } from "nitropack";

export default async (_nitroApp: Nitro) => {
  const config = useRuntimeConfig();
  try {
    await axios.get(`${config.public.fastApiUri}`);
    console.info("Successfully connected to the FastApi ✅");
  } catch (error) {
    console.error("Failed to connect to the API ❌");
  }
};
