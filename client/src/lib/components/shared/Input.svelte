<script lang="ts">
	import type { HTMLInputAttributes } from 'svelte/elements';

	type LabelProps = {
		label?: string;
	};

	let { label, ...rest }: HTMLInputAttributes & LabelProps = $props();
</script>

<div class="flex flex-col gap-1">
	{#if label}
		<label for={rest.id} class="pl-4 text-sm font-bold text-white">{label}</label>
	{/if}
	<input
		{...rest}
		class={'rounded-full px-2 py-2 text-base font-bold text-zinc-700 transition-colors duration-200 focus:border-transparent focus:ring-red-600'}
	/>
</div>
