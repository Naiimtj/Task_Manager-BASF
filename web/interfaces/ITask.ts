export interface ITask {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  priority: string;
  labels: string[];
  group_id: number;
}

export interface IAddTask {
  title: string;
  description: string;
  completed: boolean;
  priority: string;
  labels: string[];
  group_id: number;
}
