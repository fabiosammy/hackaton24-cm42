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
	<Input label="Filtrar" class="md:w-96" />

	<div
		class="relative flex h-full w-full flex-col overflow-scroll rounded-lg bg-white bg-clip-border text-gray-700 shadow-md"
	>
		<table class="w-full min-w-max table-auto text-left text-slate-800">
			<thead>
				<tr class="border-b border-slate-300 bg-slate-50 text-slate-500">
					<th class="p-4">
						<p class="text-sm font-normal leading-none">Project Name</p>
					</th>
					<th class="p-4">
						<p class="text-sm font-normal leading-none">Start Date</p>
					</th>
					<th class="p-4">
						<p class="text-sm font-normal leading-none">End Date</p>
					</th>
					<th class="p-4">
						<p class="text-sm font-normal leading-none">Owner</p>
					</th>
					<th class="p-4">
						<p class="text-sm font-normal leading-none">Budget</p>
					</th>
					<th class="p-4">
						<p></p>
					</th>
				</tr>
			</thead>
			<tbody>
				<tr class="hover:bg-slate-50">
					<td class="p-4">
						<p class="text-sm font-bold">Project Alpha</p>
					</td>
					<td class="p-4">
						<p class="text-sm">01/01/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">30/06/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">John Michael</p>
					</td>
					<td class="p-4">
						<p class="text-sm">$50,000</p>
					</td>
					<td class="p-4">
						<a href="#" class="text-sm font-semibold"> Edit </a>
					</td>
				</tr>
				<tr class="hover:bg-slate-50">
					<td class="p-4">
						<p class="text-sm font-bold">Beta Campaign</p>
					</td>
					<td class="p-4">
						<p class="text-sm">15/02/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">15/08/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">Alexa Liras</p>
					</td>
					<td class="p-4">
						<p class="text-sm">$75,000</p>
					</td>
					<td class="p-4">
						<a href="#" class="text-sm font-semibold"> Edit </a>
					</td>
				</tr>
				<tr class="hover:bg-slate-50">
					<td class="p-4">
						<p class="text-sm font-bold">Campaign Delta</p>
					</td>
					<td class="p-4">
						<p class="text-sm">01/03/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">01/09/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">Laurent Perrier</p>
					</td>
					<td class="p-4">
						<p class="text-sm">$60,000</p>
					</td>
					<td class="p-4">
						<a href="#" class="text-sm font-semibold"> Edit </a>
					</td>
				</tr>
				<tr class="hover:bg-slate-50">
					<td class="p-4">
						<p class="text-sm font-bold">Gamma Outreach</p>
					</td>
					<td class="p-4">
						<p class="text-sm">10/04/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">10/10/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">Michael Levi</p>
					</td>
					<td class="p-4">
						<p class="text-sm">$80,000</p>
					</td>
					<td class="p-4">
						<a href="#" class="text-sm font-semibold"> Edit </a>
					</td>
				</tr>
				<tr class="hover:bg-slate-50">
					<td class="p-4">
						<p class="text-sm font-bold">Omega Strategy</p>
					</td>
					<td class="p-4">
						<p class="text-sm">01/05/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">01/11/2024</p>
					</td>
					<td class="p-4">
						<p class="text-sm">Richard Gran</p>
					</td>
					<td class="p-4">
						<p class="text-sm">$100,000</p>
					</td>
					<td class="p-4">
						<a href="#" class="text-sm font-semibold"> Edit </a>
					</td>
				</tr>
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
