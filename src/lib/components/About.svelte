<script lang="ts">
</script>

<div id="about">
	<h2 class="section-title">À propos de <span class="accent">moi</span></h2>
	
	<div class="about-content">
		<div class="presentation-section">
			<h3 class="sub-title">Présentation</h3>
			<p class="desc-text">
				Après l'obtention de mon Baccalauréat général (spécialités NSI et Sciences de l'Ingénieur), j'ai intégré le BTS SIO. Je m'oriente principalement vers la data science, le machine learning et le développement backend. J'apprécie particulièrement les projets qui demandent de structurer une logique métier solide, de manipuler des données et de concevoir des outils utiles.
			</p>
			<p class="desc-text">
				J'ai également de l'expérience avec Svelte pour construire des interfaces lorsque le projet en a besoin, mais mes domaines de prédilection restent Python, les langages backend et le développement d'applications desktop.
			</p>
		</div>

		<div class="jobs-section">
			<h3 class="sub-title">Métiers visés</h3>
			<ul class="jobs-list">
				<li>
					<span>Développeur backend</span>
					<a href="/carte-heuristique?job=backend" class="job-link" title="Voir la carte heuristique">Heuristique</a>
				</li>
				<li>
					<span>Développeur d'applications desktop</span>
					<a href="/carte-heuristique?job=desktop" class="job-link" title="Voir la carte heuristique">Heuristique</a>
				</li>
				<li>
					<span>Data scientist junior</span>
					<a href="/carte-heuristique?job=data" class="job-link" title="Voir la carte heuristique">Heuristique</a>
				</li>
				<li>
					<span>Ingénieur machine learning junior</span>
					<a href="/carte-heuristique?job=ml" class="job-link" title="Voir la carte heuristique">Heuristique</a>
				</li>
			</ul>
		</div>
	</div>
</div>

<style>
	.section-title {
		font-family: var(--font-heading);
		font-size: 1.75rem;
		margin-bottom: 2rem;
		color: var(--color-text);
		font-weight: 600;
	}

	.accent {
		color: var(--color-primary);
	}

	.about-content {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2rem;
	}

	@media (min-width: 768px) {
		.about-content {
			grid-template-columns: 1.2fr 0.8fr;
			gap: 3rem;
		}
	}

	.sub-title {
		font-family: var(--font-heading);
		font-size: 1.25rem;
		color: var(--color-primary);
		margin-bottom: 1rem;
		font-weight: 600;
	}

	.desc-text {
		color: var(--color-text-muted);
		font-size: 0.9375rem;
		line-height: 1.6;
		margin-bottom: 1rem;
	}

	.desc-text:last-child {
		margin-bottom: 0;
	}

	.jobs-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.jobs-list li {
		color: var(--color-text-muted);
		font-size: 0.9rem;
		padding: 0.5rem 0;
		border-bottom: 1px solid rgba(255, 255, 255, 0.05);
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.jobs-list li::before {
		content: "▹";
		color: var(--color-primary);
		margin-right: 0.5rem;
	}

	.jobs-list li span {
		flex: 1;
	}

	.job-link {
		font-size: 0.8rem;
		color: var(--color-primary);
		text-decoration: none;
		opacity: 0.8;
		border: 1px solid rgba(212, 168, 83, 0.3);
		padding: 0.15rem 0.5rem;
		border-radius: var(--radius-sm);
		transition: all 0.2s ease;
	}

	.job-link:hover {
		opacity: 1;
		background: rgba(212, 168, 83, 0.1);
		border-color: var(--color-primary);
	}
</style>
