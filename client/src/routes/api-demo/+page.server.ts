import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const response = await fetch('https://jsonplaceholder.typicode.com/todos');
  const todos = await response.json()

	return {
		todos
	};
};
