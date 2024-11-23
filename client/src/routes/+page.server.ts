import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const response = await fetch('http://localhost:7777/hello');
	const r = await response.text();

	console.log(r);

	const test = r;

	return {
		test
	};
};
