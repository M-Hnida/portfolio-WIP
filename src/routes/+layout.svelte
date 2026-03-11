<script>
	import '../app.postcss';
	import Navigation from '$lib/components/Navigation.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<div style="min-height: 100vh; display: flex; flex-direction: column; background-color: var(--color-background);">
	<Navigation />
	<main style="flex: 1; width: 100%;">
		<slot />
	</main>
	<Footer />
</div>
