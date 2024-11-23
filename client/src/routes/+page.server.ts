import { error, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const actions = {
	createCredential: async (event) => {
		console.log(event.request.method);
	}
} satisfies Actions;

export const load: PageServerLoad = async () => {
	try {
		const response = await fetch('http://localhost:7777/hello');
		const r = await response.text();

		const test = r;

		return {
			test
		};
	} catch (e) {
		// TODO deal with errors
		console.error(e);
		error(404, { message: 'not found placeholder' });
	}
};
