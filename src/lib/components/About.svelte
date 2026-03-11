<script lang="ts">
	const education = [
		{
			year: "2025-2027",
			title: "BTS SIO - Option SLAM",
			subtitle: "Solutions Logicielles et Applications Métier",
			place: "CNED (Centre National d'Enseignement à Distance)",
			description:
				"Formation centrée sur la conception, le développement, les bases de données et la maintenance d'applications.",
		},
		{
			year: "2024",
			title: "Baccalauréat Général",
			subtitle: "Spécialités NSI et Sciences de l'Ingénieur",
			place: "Lycée Jean Cocteau, Miramas",
			description:
				"Baccalauréat général avec spécialités Numérique et Sciences Informatiques et Sciences de l'Ingénieur. Mention assez bien.",
		},
	];
</script>

<section id="about" class="about">
	<div class="container">
		<h2 class="section-title">
			Parcours <span class="accent">Formation</span>
		</h2>

		<div class="about-content">
			<div class="presentation-box">
				<h3>Présentation</h3>
				<p>
					Je m'oriente principalement vers la data science, le machine
					learning et le développement backend. J'apprécie
					particulièrement les projets qui demandent de structurer une
					logique métier solide, de manipuler des données et de
					concevoir des outils utiles.
				</p>
				<p>
					J'ai également de l'expérience avec Svelte pour construire
					des interfaces lorsque le projet en a besoin, mais mes
					domaines de prédilection restent Python, les langages
					backend et le développement d'applications desktop. Mon
					objectif est de créer des solutions fiables, claires et bien
					conçues, de l'analyse des données jusqu'à l'implémentation.
				</p>

				<h3 class="mt-8">Métiers visés</h3>
				<ul class="jobs-list">
					<li>Développeur backend</li>
					<li>Développeur d'applications desktop</li>
					<li>Data scientist junior</li>
					<li>Ingénieur machine learning junior</li>
				</ul>
			</div>

			<div class="timeline-container">
				<h3>Historique</h3>
				<div class="timeline">
					{#each education as e}
						<article class="timeline-item">
							<div class="timeline-marker"></div>
							<div class="timeline-content">
								<span class="year">{e.year}</span>
								<h3 class="title">{e.title}</h3>
								<p class="subtitle">{e.subtitle}</p>
								<p class="place">{e.place}</p>
								<p class="description">{e.description}</p>
							</div>
						</article>
					{/each}
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.about {
		padding: 4rem 0;
		background-color: var(--color-background);
	}

	.container {
		max-width: 75rem;
		margin: 0 auto;
		padding: 0 1.5rem;
	}

	.section-title {
		font-family: var(--font-heading);
		font-size: clamp(1.75rem, 4vw, 2.5rem);
		text-align: center;
		margin-bottom: 4rem;
		color: var(--color-text);
	}

	.accent {
		color: #c0c0c0;
	}

	.about-content {
		display: grid;
		grid-template-columns: 1fr;
		gap: 4rem;
		margin-bottom: 3rem;
	}

	@media (min-width: 1024px) {
		.about-content {
			grid-template-columns: 1fr 1fr;
		}
	}

	.presentation-box {
		background: rgba(255, 255, 255, 0.02);
		border: 1px solid var(--color-border);
		border-radius: 1rem;
		padding: 2.5rem;
	}

	.presentation-box h3 {
		font-size: 1.5rem;
		color: var(--color-primary);
		margin-bottom: 1.5rem;
		font-family: var(--font-heading);
	}

	.presentation-box .mt-8 {
		margin-top: 2.5rem;
	}

	.presentation-box p {
		color: var(--color-text-muted);
		line-height: 1.7;
		margin-bottom: 1.5rem;
	}

	.jobs-list {
		list-style-type: none;
		padding: 0;
		margin: 0;
	}

	.jobs-list li {
		color: var(--color-text-muted);
		padding: 0.75rem 0;
		border-bottom: 1px solid rgba(255, 255, 255, 0.05);
		display: flex;
		align-items: center;
	}

	.jobs-list li::before {
		content: "▹";
		color: var(--color-primary);
		margin-right: 0.75rem;
	}

	.timeline-container h3 {
		font-size: 1.5rem;
		color: var(--color-primary);
		margin-bottom: 2rem;
		font-family: var(--font-heading);
		text-align: center;
	}

	.timeline {
		position: relative;
		max-width: 48rem;
		margin: 0 auto;
	}

	.timeline::before {
		content: "";
		position: absolute;
		left: 0;
		top: 0;
		bottom: 0;
		width: 1px;
		background: var(--color-border);
	}

	.timeline-item {
		position: relative;
		padding-left: 2rem;
		padding-bottom: 2.5rem;
	}

	.timeline-item:last-child {
		padding-bottom: 0;
	}

	.timeline-marker {
		position: absolute;
		left: -4px;
		top: 0.25rem;
		width: 9px;
		height: 9px;
		background: var(--color-primary);
		border-radius: 50%;
	}

	.year {
		font-family: var(--font-heading);
		font-size: 0.875rem;
		color: var(--color-primary);
		letter-spacing: 0.05em;
		margin-bottom: 0.5rem;
		display: block;
	}

	.title {
		font-family: var(--font-heading);
		font-size: 1.25rem;
		color: var(--color-text);
		margin-bottom: 0.25rem;
	}

	.subtitle {
		font-size: 0.9375rem;
		color: var(--color-text-muted);
		margin-bottom: 0.5rem;
	}

	.place {
		font-size: 0.875rem;
		color: var(--color-text-subtle);
		margin-bottom: 0.75rem;
	}

	.description {
		color: var(--color-text-muted);
		font-size: 0.9375rem;
		line-height: 1.6;
		margin: 0;
	}
</style>
