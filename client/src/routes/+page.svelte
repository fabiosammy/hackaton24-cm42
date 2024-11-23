<script lang="ts">
	import { store } from '$lib/state/store.svelte';

	let { data } = $props();
</script>

<title>Lobo-Guará: O Guardião de suas senhas, e Protetor da sua sanidade.</title>

<div class="flex flex-col items-center">
	{#if !store.isLoggedIn}
		Faça seu Login
	{:else}
		<div class="container m-4 border border-red-500">
			<div>New Credential Form</div>
			<div>Credentials List</div>
		</div>
	{/if}
</div>
