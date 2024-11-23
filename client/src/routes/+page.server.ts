import { error, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { Vault } from '$lib/types';
import { API_BASE_URL } from '$env/static/private';

export const actions = {
	createCredential: async (event) => {
		console.log(event.request.method);
	}
} satisfies Actions;

export const load: PageServerLoad = async () => {
	try {
		const response = await fetch(`${API_BASE_URL}/vaults`);
		const data: Vault[] = await response.json();

		return {
			vaults: data
		};
	} catch (e) {
		// TODO deal with errors
		console.error(e);
		error(404, { message: 'not found placeholder' });
	}
};
