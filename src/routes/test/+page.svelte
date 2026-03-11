<script lang="ts">
	function printsmth(): void {
		console.log("smth");
	}
	let range = $state(0);
</script>

<svelte:head>
	<title>Portfolio | Creative Developer</title>
	<meta
		name="description"
		content="Portfolio of a creative developer specializing in modern web applications"
	/>
</svelte:head>

<form action="">
	<label for="range">Range</label>
	<input type="range" bind:value={range} onclick={printsmth} id="range" />
	{range}
</form>

<style>
	form {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		height: 100vh;
		gap: 1rem;
	}
</style>
