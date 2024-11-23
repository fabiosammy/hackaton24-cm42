<script lang="ts">
	import CopyIcon from '$lib/assets/icons/CopyIcon.svelte';
	import Clipboard from '$lib/components/shared/Clipboard.svelte';
	import Input from '$lib/components/shared/Input.svelte';
	import type { AppCredential } from '$lib/types';

	let { credentials }: { credentials: AppCredential[] } = $props();

	let tableHeading = ['Nome', 'Descrição', 'Senha'];

	console.log(credentials)
</script>

<div class="flex flex-col items-center gap-8">
	<Input label="Filtrar" class="md:w-96" />


	<div
		class="relative flex h-full w-full flex-col overflow-scroll rounded-lg bg-slate-800 bg-clip-border text-slate-800 shadow-md"
	>
		<table class="w-full min-w-max table-auto text-left text-zinc-200">
			<thead>
				<tr class="border-b border-slate-300 bg-slate-50 text-zinc-800">
					{#each tableHeading as t}
					<th class="p-4">
						<p class="text-sm font-normal leading-none">{t}</p>
					</th>
					{/each}
				</tr>
			</thead>
			<tbody>
				{#each credentials as credential}
				<tr class="">
					{#each Object.values(credential) as cr}
					<td class="p-4">
						<p class="text-sm font-bold">{cr}</p>
						<Clipboard content={JSON.stringify(cr)} />
					</td>
					{/each}
				</tr>
				{/each}
			</tbody>
		</table>
	</div>

	<!-- <div class="relative overflow-x-auto">
		<table class="table-fixed border border-white">
			<thead>
				<tr>
					{#each tableHeading as columnHeading}
						<th class="bg-red-700 py-2 font-bold text-white">{columnHeading}</th>
					{/each}
				</tr>
			</thead>
			<tbody>
				{#each tableData as row}
					<tr class="border border-white">
						{#each Object.values(row) as cell}
							<td class="px-8 py-2"
								><div class="flex gap-2">
									{cell}
									<CopyIcon />
								</div>
							</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		</table>
	</div> -->
</div>
