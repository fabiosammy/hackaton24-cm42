import { error, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { AppCredential, CredentialDTO } from '$lib/types';
import { API_BASE_URL } from '$env/static/private';

export const actions = {
	createCredential: async (event) => {
		console.log(event.request.method);
	}
} satisfies Actions;

export const load: PageServerLoad = async () => {
	try {
		const response = await fetch(`${API_BASE_URL}/vaults`);
		const data: CredentialDTO[] = await response.json();
		const credentials: AppCredential[] = data.map((credential) => ({
			id: credential.vault_id,
			name: credential.name,
			username: credential.username,
			password: credential.password,
			tags: credential.tags
		}));

		return {
			credentials
		};
	} catch (e) {
		// TODO deal with errors
		console.error(e);
		error(404, { message: 'not found placeholder' });
	}
};
