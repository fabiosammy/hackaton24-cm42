<script lang="ts">
	import CopyIcon from '$lib/assets/icons/CopyIcon.svelte';
	import { scale } from 'svelte/transition';

	const NOTIFICATION_DELAY_MS = 3000;

	let copied = $state(false);
	let timeoutId: NodeJS.Timeout | null = null;
	let { content }: { content: string } = $props();

	const handleCopy = () => {
		if (!content) return;

		if (timeoutId) {
			clearTimeout(timeoutId);
		}

		navigator.clipboard.writeText(content);

		copied = true;

		timeoutId = setTimeout(() => {
			copied = false;
			timeoutId = null;
		}, NOTIFICATION_DELAY_MS);
	};
</script>

<button class="relative p-4" onclick={handleCopy}>
	{#if copied}
		<span class="absolute top-2 text-xs" transition:scale>Copiado!</span>
	{/if}
	<CopyIcon />
</button>
