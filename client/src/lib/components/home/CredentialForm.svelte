<script lang="ts">
	import { enhance } from '$app/forms';
	import Button from '$lib/components/shared/Button.svelte';
</script>

<div class="flex flex-col items-center">
	<form method="POST" action="?/createCredential" use:enhance>
		<div>Form</div>
		<Button>Salvar</Button>
	</form>
</div>
