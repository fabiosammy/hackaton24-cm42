<script lang="ts">
	let { data } = $props();
</script>

<h1>Hello World</h1>
<pre>{JSON.stringify(data.todos, null, 2)}</pre>
