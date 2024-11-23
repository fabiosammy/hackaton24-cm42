<script lang="ts">
	import type { Snippet } from 'svelte';
	import type { HTMLButtonAttributes } from 'svelte/elements';

	let { children, ...rest }: { children: Snippet } & HTMLButtonAttributes = $props();
</script>

<button
	{...rest}
	class={`rounded-full bg-red-700 px-6 py-2 text-lg font-bold text-white transition-colors duration-200 hover:bg-red-800 ${rest.class} ${rest.disabled && 'cursor-not-allowed bg-zinc-600 text-zinc-400 hover:bg-zinc-600'}`}
>
	{@render children()}
</button>
