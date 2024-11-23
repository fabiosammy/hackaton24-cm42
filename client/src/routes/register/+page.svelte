<script lang="ts">
	import { enhance } from '$app/forms';
	import Button from '$lib/components/shared/Button.svelte';
	import Input from '$lib/components/shared/Input.svelte';
</script>

<div class="m-4 flex flex-col items-center">
	<h1 class="my-4 text-2xl">Crie uma Conta</h1>

	<form method="POST" action="?/login" use:enhance>
		<div class="flex flex-col gap-4">
			<Input label="Usuário" />
			<Input type="password" label="Senha" />
			<Input type="password" label="Confirme sua senha" />

			<Button class="max-w-fit self-center">Registre-se</Button>
		</div>
	</form>
</div>
