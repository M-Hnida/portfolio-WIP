<script>
	import '../app.postcss';
	import Navigation from '$lib/components/Navigation.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<div class="hero-bg"></div>
<div class="vignette" style="position: fixed; inset: 0; z-index: 1; pointer-events: none; background: radial-gradient(circle at center, transparent 30%, rgba(0, 0, 0, 0.8) 100%);"></div>

<div class="app-layout">
	<Navigation />
	<main class="main-content">
		<slot />
		<Footer />
	</main>
</div>
