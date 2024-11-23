<script lang="ts">
	import { enhance } from '$app/forms';
	import Button from '$lib/components/shared/Button.svelte';
	import Input from '$lib/components/shared/Input.svelte';
</script>

<div class="flex flex-col items-center">
  <h1 class="text-2xl my-4">Faça seu Login</h1>
	<form method="POST" action="?/login" use:enhance>
    
		<div class="flex flex-col gap-4">
			<Input label="Usuário" />
			<Input label="Senha" />

			<Button class="max-w-fit self-center">Salvar</Button>
			<p>
				Não possui uma conta? <a
					href="register"
					class="font-bold text-zinc-300 underline transition-colors duration-300 hover:text-white"
					>Registre-se!</a
				>
			</p>
		</div>
	</form>
</div>
