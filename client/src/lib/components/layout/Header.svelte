<script lang="ts">
	import src from '$lib/assets/lobo.png';
	import { page } from '$app/stores';
	import { store } from '$lib/state/store.svelte';

	const logIn = () => {
		store.isLoggedIn = true;
	};

	const logOut = () => {
		store.isLoggedIn = false;
	};
</script>

<header
	class="flex flex-col items-center justify-between gap-4 p-4 md:flex-row"
>
	<div class="flex items-center gap-4">
		<img
			{src}
			class="h-28 rounded-full"
			alt="Logo com desenho de um lobo-guará, animal da fauna brasileira de coloração alaranjada"
		/>
		<div class="flex flex-col gap-1">
			<h1 class="text-3xl font-bold text-white">Lobo-Guará</h1>
			<p class="max-w-[250px] text-sm">
				Lobo-Guará: O Guardião de suas senhas, e Protetor da sua sanidade.
			</p>
		</div>
	</div>

	<nav class="flex gap-4">
		<a
			href="/"
			class={`transition-all duration-300 p-2 hover:text-white ${$page.url.pathname === '/' && 'font-bold text-white underline'}`}
			aria-current={$page.url.pathname === '/'}
		>
			Início
		</a>

		<a
			href="/password-generator"
			class={`transition-all duration-300 p-2 hover:text-white ${$page.url.pathname === '/password-generator' && 'font-bold text-white underline'}`}
			aria-current={$page.url.pathname === '/password-generator'}
		>
			Gerador de Senhas
		</a>

		<div class="flex w-16 justify-center">
			{#if store.isLoggedIn}
				<button class="transition-colors duration-300 hover:text-white p-2" onclick={logOut}
					>Sair</button
				>
			{:else}
				<button class="transition-colors duration-300 hover:text-white p-2" onclick={logIn}
					>Entrar</button
				>
			{/if}
		</div>
	</nav>
</header>
