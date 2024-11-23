<script lang="ts">
	import { enhance } from '$app/forms';
	import Button from '$lib/components/shared/Button.svelte';
	import Input from '$lib/components/shared/Input.svelte';
</script>

<div class="flex flex-col items-center">
	<h1 class="text-2xl my-4">Adicione uma Credencial</h1>
	<form method="POST" action="?/createCredential" use:enhance>
		<div class="flex flex-col gap-4">
			<Input label="URL dos Sites" />

			<div class="flex gap-4 flex-col md:flex-row">
				<Input label="Usuário" />
				<Input label="Senha" />
			</div>

			<Button class="max-w-fit self-center">Salvar</Button>
		</div>
	</form>
</div>
