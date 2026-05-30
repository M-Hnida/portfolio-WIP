<script>
	import Hero from "$lib/components/Hero.svelte";
	import About from "$lib/components/About.svelte";
	import Parcours from "$lib/components/Parcours.svelte";
	import Projects from "$lib/components/Projects.svelte";
	import Skills from "$lib/components/Skills.svelte";
	import Contact from "$lib/components/Contact.svelte";
</script>

<svelte:head>
	<title>Portfolio | Backend, Data Science & Applications</title>
	<meta
		name="description"
		content="Portfolio orienté développement backend, data science, machine learning et applications desktop."
	/>
</svelte:head>

<div class="page-container">
	<Hero />
	
	<div class="unified-panel">
		<div class="panel-row-top">
			<About />
		</div>
		<div class="panel-grid-bottom">
			<div class="panel-col-left">
				<Skills />
			</div>
			<div class="panel-col-right">
				<Parcours />
			</div>
		</div>
	</div>

	<Projects />
	<Contact />
</div>

<style>
	.page-container {
		padding: 1.5rem;
		max-width: 1400px;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
	}

	.unified-panel {
		background: rgba(10, 10, 10, 0.6);
		backdrop-filter: blur(16px);
		-webkit-backdrop-filter: blur(16px);
		border: 1px solid var(--color-border);
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
		margin-bottom: 2rem;
		border-radius: var(--radius-lg);
	}

	.panel-row-top {
		border-bottom: 1px solid var(--color-border);
		padding: 2.5rem;
	}

	.panel-grid-bottom {
		display: grid;
		grid-template-columns: 1fr;
	}

	.panel-col-left {
		padding: 2.5rem;
	}

	.panel-col-right {
		padding: 2.5rem;
	}

	@media (min-width: 768px) {
		.page-container {
			padding: 2.5rem;
		}
	}

	@media (min-width: 1024px) {
		.page-container {
			padding: 3rem 2.5rem;
		}

		.panel-grid-bottom {
			grid-template-columns: 1.15fr 0.85fr;
		}

		.panel-col-left {
			border-right: 1px solid var(--color-border);
		}
	}
</style>
