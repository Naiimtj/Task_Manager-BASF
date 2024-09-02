import axios from "axios";

const config = useRuntimeConfig();

const service = axios.create({
  withCredentials: true,
  baseURL: `${config.public.fastApiUri}`,
});

service.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// < TASK GROUP
// . POST
export async function createTaskGroup(body) {
  try {
    const response = await service.post("/task-groups", body);
    return response;
  } catch (error) {
    console.error("Error in Post Task Group:", error);
    throw error;
  }
}
