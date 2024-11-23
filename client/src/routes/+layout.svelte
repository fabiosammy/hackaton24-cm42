<script lang="ts">
	import '../app.css';
	import { i18n } from '$lib/i18n';
	import { ParaglideJS } from '@inlang/paraglide-sveltekit';
	import Header from '$lib/components/layout/Header.svelte';
	let { children } = $props();
</script>

<ParaglideJS {i18n}>
	<div class="min-h-screen bg-amber-800 text-zinc-200">
		<Header />

		{@render children()}
	</div>
</ParaglideJS>
