<script lang="ts">
	import CredentialForm from '$lib/components/home/CredentialForm.svelte';
	import CredentialList from '$lib/components/home/CredentialList.svelte';
	import LoginForm from '$lib/components/home/LoginForm.svelte';
	import { store } from '$lib/state/store.svelte';

	let { data } = $props();
</script>

<title>Lobo-Guará: O Guardião de suas senhas, e Protetor da sua sanidade.</title>

<div class="flex flex-col items-center">
	<pre>{JSON.stringify(data.credentials, null, 2)}</pre>
	<div class="container m-4 flex flex-col gap-16">
		{#if !store.isLoggedIn}
			<LoginForm />
		{:else}
			<CredentialForm />
			<CredentialList credentials={[]} />
		{/if}
	</div>
</div>
