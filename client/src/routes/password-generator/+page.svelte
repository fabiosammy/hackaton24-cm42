<script lang="ts">
	import Button from '$lib/components/shared/Button.svelte';
	import Clipboard from '$lib/components/shared/Clipboard.svelte';
	import { LOWERCASE, NUMBERS, SPECIAL_CHARS, UPPERCASE } from '$lib/constants/characters';
	import { generatePassword } from '$lib/utils/passwordGenerator';

	const MIN_PASSWORD_LENGTH = 12;
	const MAX_PASSWORD_LENGTH = 128;

	let generatedPassword = $state('');
	let passwordLength = $state(MIN_PASSWORD_LENGTH);
	let useLowercase = $state(true);
	let useUppercase = $state(true);
	let useNumbers = $state(true);
	let useSpecialChars = $state(true);

	const handleGeneratePassword = () => {
		generatedPassword = generatePassword({
			length: passwordLength,
			useLowercase,
			useUppercase,
			useNumbers,
			useSpecialChars
		});
	};
</script>

<div class="flex flex-col items-center justify-center p-4">
	<div class="container flex flex-col items-center">
		<h1 class="my-4 text-2xl">Gerador de Senhas</h1>

		<div class="flex flex-col gap-2">
			<div class="flex items-center gap-2">
				<input
					type="checkbox"
					class="transition-colors duration-300 checked:bg-red-600 hover:checked:bg-red-700 focus:ring-red-500 focus:checked:bg-red-600"
					name="lowercase"
					id="lowercase"
					bind:checked={useLowercase}
				/>
				<label class="select-none" for="lowercase"> Usar {LOWERCASE} </label>
			</div>

			<div class="flex items-center gap-2">
				<input
					type="checkbox"
					class="transition-colors duration-300 checked:bg-red-600 hover:checked:bg-red-700 focus:ring-red-500 focus:checked:bg-red-600"
					name="uppercase"
					id="uppercase"
					bind:checked={useUppercase}
				/>
				<label class="select-none" for="uppercase"> Usar {UPPERCASE} </label>
			</div>

			<div class="flex items-center gap-2">
				<input
					type="checkbox"
					class="transition-colors duration-300 checked:bg-red-600 hover:checked:bg-red-700 focus:ring-red-500 focus:checked:bg-red-600"
					name="numbers"
					id="numbers"
					bind:checked={useNumbers}
				/>
				<label class="select-none" for="numbers"> Usar {NUMBERS} </label>
			</div>

			<div class="flex items-center gap-2">
				<input
					type="checkbox"
					class="transition-colors duration-300 checked:bg-red-600 hover:checked:bg-red-700 focus:ring-red-500 focus:checked:bg-red-600"
					name="specials"
					id="specials"
					bind:checked={useSpecialChars}
				/>
				<label class="select-none" for="specials"> Usar {SPECIAL_CHARS} </label>
			</div>
			<label for="length" class="flex flex-col gap-2">
				Comprimento da senha
				<div>
					<input
						class="w-20 text-xl font-bold text-zinc-600"
						type="number"
						min={MIN_PASSWORD_LENGTH}
						max={MAX_PASSWORD_LENGTH}
						onchange={(e) => {
							const value = Number((e.target as HTMLInputElement).value);
							passwordLength = Math.max(MIN_PASSWORD_LENGTH, Math.min(value, MAX_PASSWORD_LENGTH));
						}}
						bind:value={passwordLength}
					/>
					<input
						type="range"
						name="length"
						id="length"
						class="accent-red-600"
						min={MIN_PASSWORD_LENGTH}
						max={MAX_PASSWORD_LENGTH}
						bind:value={passwordLength}
					/>
				</div>
			</label>
			<Button class="max-w-fit self-center" onclick={handleGeneratePassword}>Gerar Senha</Button>
		</div>

		{#if generatedPassword}
			<div class="items-center4 flex flex-col md:flex-row">
				<p class="my-6 flex items-center gap-4">
					<span class="text-wrap break-all text-2xl font-bold text-white">{generatedPassword}</span>
				</p>
				<Clipboard content={generatedPassword} />
			</div>
		{/if}
	</div>
</div>
