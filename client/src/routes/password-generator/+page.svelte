<script lang="ts">
	import { LOWERCASE, NUMBERS, SPECIAL_CHARS, UPPERCASE } from '$lib/constants/characters';

	const MIN_PASSWORD_LENGTH = 12;
	const MAX_PASSWORD_LENGTH = 128;

	let passwordLength = $state(MIN_PASSWORD_LENGTH);
</script>

<div class="m-8 flex flex-col items-center justify-center border border-red-500 p-4">
	<div class="container m-4">
		<h1 class="my-8 text-4xl font-bold text-white">Gerador de Senhas</h1>

		<div class="flex flex-col gap-2">
			<div class="flex items-center gap-2">
				<input type="checkbox" name="lowercase" id="lowercase" />
				<label class="select-none" for="lowercase"> Usar {LOWERCASE} </label>
			</div>

			<div class="flex items-center gap-2">
				<input type="checkbox" name="uppercase" id="uppercase" />
				<label class="select-none" for="uppercase"> Usar {UPPERCASE} </label>
			</div>

			<div class="flex items-center gap-2">
				<input type="checkbox" name="numbers" id="numbers" />
				<label class="select-none" for="numbers"> Usar {NUMBERS} </label>
			</div>

			<div class="flex items-center gap-2">
				<input type="checkbox" name="specials" id="specials" />
				<label class="select-none" for="specials"> Usar {SPECIAL_CHARS} </label>
			</div>
			<label for="length">
				Comprimento da senha
				<input
					type="range"
					name="length"
					id="length"
					min={MIN_PASSWORD_LENGTH}
					max={MAX_PASSWORD_LENGTH}
					bind:value={passwordLength}
				/>
				<input
					class="w-20 font-bold text-zinc-600"
					type="number"
					min={MIN_PASSWORD_LENGTH}
					max={MAX_PASSWORD_LENGTH}
					onchange={(e) => {
						const value = Number((e.target as HTMLInputElement).value);

						passwordLength = Math.max(MIN_PASSWORD_LENGTH, Math.min(value, MAX_PASSWORD_LENGTH));
					}}
					bind:value={passwordLength}
				/>
			</label>
		</div>
	</div>
</div>
