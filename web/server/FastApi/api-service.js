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

// - GET
export async function getAllGroups() {
  try {
    const response = await service.get("/task-groups");
    return response;
  } catch (error) {
    console.error("Error in Get All Task Group:", error);
    throw error;
  }
}

export async function getNameGroup(group_id) {
  try {
    const response = await service.get(`/task-groups/${group_id}`);
    return response;
  } catch (error) {
    console.error("Error in Get Name Task Group:", error);
    throw error;
  }
}

// ! DELETE
export async function deleteTaskGroup(group_id) {
  try {
    const response = await service.delete(`/task-groups/${group_id}`);
    return response;
  } catch (error) {
    console.error("Error in Delete One Task Groups:", error);
    throw error;
  }
}

// ! DELETE ALL TASK GROUP
export async function deleteAllTaskGroup() {
  try {
    const response = await service.delete(`/task-groups`);
    return response;
  } catch (error) {
    console.error("Error in Delete ALL Task Groups:", error);
    throw error;
  }
}

// < TASKS
// . POST
export async function createTask(body) {
  try {
    const response = await service.post("/tasks", body);
    return response;
  } catch (error) {
    console.error("Error in Create Task:", error);
    throw error;
  }
}
// - GET
export async function getAllTasks() {
  try {
    const response = await service.get("/tasks");
    return response;
  } catch (error) {
    console.error("Error in Get Tasks:", error);
    throw error;
  }
}
export async function getTaskOfGroup(idGroup) {
  try {
    const response = await service.get(`/task-groups/${idGroup}/tasks`);
    return response;
  } catch (error) {
    console.error(`Error in Get Tasks of Group idGroup:${idGroup}:`, error);
    throw error;
  }
}
export async function getTask(id) {
  try {
    const response = await service.get(`/tasks/${id}`);
    return response;
  } catch (error) {
    console.error("Error in Get Task:", error);
    throw error;
  }
}
// * PUT
export async function editTask(id, body) {
  try {
    const response = await service.put(`/tasks/${id}`, body);
    return response;
  } catch (error) {
    console.error("Error in Edit Task:", error);
    throw error;
  }
}
// ! DELETE
export async function deleteTask(id) {
  try {
    const response = await service.delete(`/tasks/${id}`);
    return response;
  } catch (error) {
    console.error("Error in Delete One Task:", error);
    throw error;
  }
}
