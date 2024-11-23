<script lang="ts">
	import CopyIcon from '$lib/assets/icons/CopyIcon.svelte';
	import Input from '$lib/components/shared/Input.svelte';
	import type { AppCredential } from '$lib/types';

	let { credentials }: { credentials: AppCredential[] } = $props();

	let tableHeading = ['Nome', 'Usuário', 'Senha'];
	let tableData = [
		{
			name: 'Github',
			username: 'jv-vogler',
			password: 'asGjk39asl'
		},
		{
			name: 'Amazon',
			username: 'jv',
			password: 'qweqweqwe'
		},
		{
			name: 'Codeminer42',
			username: 'joao.vogler',
			password: '1234'
		}
	];
</script>

<div class="flex flex-col items-center gap-8">
	<Input label="Filtrar" class="w-96" />

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
</div>
