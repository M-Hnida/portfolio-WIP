<script lang="ts">
	import { reveal } from "$lib/actions/reveal";

	type ProjectPreview = {
		type: "image" | "video";
		src: string;
		alt: string;
		poster?: string;
	};

	type Project = {
		title: string;
		date: string;
		description: string;
		detailedDescription: string;
		tags: string[];
		category: string;
		github?: string;
		preview?: ProjectPreview;
	};

	let selectedProject: number | null = null;

	const projects: Project[] = [
		{
			title: "Site E-commerce Full-stack",
			date: "2025",
			description:
				"Plateforme e-commerce complète avec backend, base de données et logique métier. Gestion des produits, panier, commandes et paiement.",
			detailedDescription:
				"Projet de formation permettant de maîtriser les technologies fullstack. Implémentation d'une API REST avec Node.js et Express, utilisation de Medusajs pour la gestion e-commerce, base de données PostgreSQL, et frontend avec Svelte. Gestion de l'authentification, du panier, des commandes et de l'interface d'administration.",
			tags: [
				"Typescript",
				"Node.js",
				"Medusajs",
				"PostgreSQL",
				"Svelte",
				"API REST",
			],
			category: "WEB",
			github: "https://github.com/M-Hnida/ecommerce",
		},
		{
			title: "Bot Discord Automation",
			date: "2024",
			description:
				"Bot Discord automatisé avec commandes personnalisées, gestion d'événements et architecture modulaire. Gestion de serveur complète.",
			detailedDescription:
				"Bot Discord développé en Python utilisant la bibliothèque discord.py. Implémentation de commandes slash, système de modération automatique, gestion des rôles et permissions, système de logs et d'événements. Architecture modulaire permettant une extension facile des fonctionnalités.",
			tags: ["Python", "Discord API", "Asyncio"],
			category: "AUTOMATION",
			github: "https://github.com/M-Hnida/discord-bot",
		},
		{
			title: "Backtesting Trading Algorithmique",
			date: "2024",
			description:
				"Système de backtesting pour stratégies de trading sur données financières. Optimisation et visualisation des performances.",
			detailedDescription:
				"Outil de backtesting développé en Python permettant de tester des stratégies de trading sur des données historiques. Utilisation de Vectorbt et NautilusTrader pour l'analyse, Pandas et NumPy pour le traitement des données, Matplotlib et Plotly pour la visualisation. Implémentation de multiples stratégies et optimisation des paramètres.",
			tags: ["Python", "NautilusTrader", "Pandas", "NumPy", "Plotly"],
			category: "DATA",
			github: "https://github.com/M-Hnida/trading-backtest",
		},
	];

	let activeProject: Project | null = null;
	$: activeProject =
		selectedProject === null ? null : projects[selectedProject];

	function openProject(index: number) {
		selectedProject = selectedProject === index ? null : index;
	}

	function closeProject() {
		selectedProject = null;
	}
</script>

<section id="projects" class="projects">
	<div class="container">
		<h2 class="title">
			Projets <span class="accent">Personnels</span>
		</h2>
		<div class="grid">
			{#each projects as p, i}
				<article
					class="card"
					class:active={selectedProject === i}
					use:reveal={{ delay: i * 150 }}
				>
					<button
						class="card-button"
						type="button"
						on:click={() => openProject(i)}
						aria-expanded={selectedProject === i}
						aria-controls="project-preview-panel"
					>
						<div class="card-thumbnail">
							{#if p.preview}
								{#if p.preview.type === "video"}
									<video
										src={p.preview.src}
										poster={p.preview.poster}
										muted
										loop
										autoplay
										playsinline
									></video>
								{:else}
									<img
										src={p.preview.src}
										alt={p.preview.alt}
									/>
								{/if}
							{/if}

							<div class="thumbnail-overlay">
								<span class="category">{p.category}</span>
								<span class="thumbnail-note">
									{#if p.preview}
										Aperçu du projet
									{:else}
										Zone prête pour GIF ou vidéo
									{/if}
								</span>
							</div>
						</div>
						<div class="card-content">
							<span class="date">{p.date}</span>
							<h3 class="card-title">{p.title}</h3>
							<p class="card-desc">{p.description}</p>
							<div class="tags">
								{#each p.tags as t}
									<span class="tag">{t}</span>
								{/each}
							</div>
							<span class="card-cta">
								{selectedProject === i
									? "Masquer le détail"
									: "Voir le détail du projet"}
							</span>
						</div>
					</button>
				</article>
			{/each}
		</div>

		{#if activeProject}
			<article id="project-preview-panel" class="details-panel">
				<div class="details-media">
					{#if activeProject.preview}
						{#if activeProject.preview.type === "video"}
							<video
								src={activeProject.preview.src}
								poster={activeProject.preview.poster}
								muted
								loop
								autoplay
								playsinline
								controls
							></video>
						{:else}
							<img
								src={activeProject.preview.src}
								alt={activeProject.preview.alt}
							/>
						{/if}
					{:else}
						<div class="details-fallback">
							<span class="category"
								>{activeProject.category}</span
							>
							<h3>{activeProject.title}</h3>
							<p>
								Ajoute ici un GIF, une image ou une courte vidéo
								pour montrer rapidement le projet.
							</p>
						</div>
					{/if}
				</div>

				<div class="details-copy">
					<span class="date">{activeProject.date}</span>
					<h3 class="panel-title">{activeProject.title}</h3>
					<p class="detailed-desc">
						{activeProject.detailedDescription}
					</p>
					<div class="tags panel-tags">
						{#each activeProject.tags as tag}
							<span class="tag">{tag}</span>
						{/each}
					</div>
					<div class="panel-actions">
						{#if activeProject.github}
							<a
								href={activeProject.github}
								target="_blank"
								rel="noopener noreferrer"
								class="github-link"
							>
								<svg
									viewBox="0 0 24 24"
									fill="currentColor"
									width="20"
									height="20"
								>
									<path
										d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"
									/>
								</svg>
								Voir sur GitHub
							</a>
						{/if}
						<button
							class="close-btn"
							type="button"
							on:click={closeProject}
						>
							Fermer
						</button>
					</div>
				</div>
			</article>
		{/if}
	</div>
</section>

<style>
	.projects {
		padding: 4rem 0;
		background-color: var(--color-background);
	}

	.container {
		max-width: 80rem;
		margin: 0 auto;
		padding: 0 1.5rem;
	}

	.title {
		font-family: var(--font-heading);
		font-size: clamp(1.75rem, 4vw, 2.5rem);
		text-align: center;
		margin-bottom: 3rem;
		color: var(--color-text);
	}

	.accent {
		color: #c0c0c0;
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
		gap: 1.5rem;
	}

	.card {
		background-color: var(--color-surface);
		border: 1px solid var(--color-border);
		border-radius: 0.5rem;
		overflow: hidden;
		transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
		position: relative;
		visibility: hidden; /* Initial state for reveal action */
	}

	.card:hover {
		border-color: rgba(212, 168, 83, 0.4);
		transform: translateY(-8px);
		box-shadow:
			0 20px 40px rgba(0, 0, 0, 0.4),
			0 0 20px rgba(212, 168, 83, 0.1);
	}

	.card.active {
		border-color: var(--color-primary);
	}

	.card-button {
		width: 100%;
		height: 100%;
		text-align: left;
		background: none;
		border: none;
		padding: 0;
		cursor: pointer;
		display: flex;
		flex-direction: column;
	}

	.card-button:focus-visible {
		outline: 2px solid rgba(212, 168, 83, 0.75);
		outline-offset: -2px;
	}

	.card-thumbnail {
		height: 180px;
		position: relative;
		background: linear-gradient(
			135deg,
			var(--color-surface-elevated) 0%,
			var(--color-surface) 100%
		);
		border-bottom: 1px solid var(--color-border);
		overflow: hidden;
	}

	.card-thumbnail img,
	.card-thumbnail video,
	.details-media img,
	.details-media video {
		width: 100%;
		height: 100%;
		object-fit: cover;
		display: block;
	}

	.thumbnail-overlay {
		position: absolute;
		inset: 0;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		padding: 1rem;
		background: linear-gradient(
			180deg,
			rgba(5, 5, 5, 0.2) 0%,
			rgba(5, 5, 5, 0.78) 100%
		);
	}

	.thumbnail-note {
		font-size: 0.8rem;
		color: rgba(255, 255, 255, 0.82);
	}

	.category {
		font-size: 0.75rem;
		color: var(--color-primary);
		text-transform: uppercase;
		letter-spacing: 0.1em;
		background: rgba(212, 168, 83, 0.1);
		padding: 0.25rem 0.5rem;
		border-radius: 0.25rem;
	}

	.card-content {
		padding: 1.5rem;
		display: flex;
		flex-direction: column;
		flex: 1;
	}

	.date {
		font-size: 0.75rem;
		color: var(--color-text-subtle);
		display: block;
		margin-bottom: 0.5rem;
	}

	.card-title {
		font-family: var(--font-heading);
		font-size: 1.125rem;
		color: #c0c0c0;
		margin-bottom: 0.5rem;
	}

	.card-desc {
		color: var(--color-text-muted);
		font-size: 0.9375rem;
		margin-bottom: 1rem;
		line-height: 1.5;
	}

	.tags {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
	}

	.card-cta {
		display: inline-flex;
		align-items: center;
		margin-top: 1rem;
		font-size: 0.875rem;
		color: var(--color-primary);
	}

	.tag {
		font-size: 0.75rem;
		color: var(--color-text-subtle);
		border: 1px solid var(--color-border);
		padding: 0.25rem 0.5rem;
		border-radius: 0.25rem;
	}

	.details-panel {
		margin-top: 1.5rem;
		background: var(--color-surface);
		border: 1px solid var(--color-border);
		border-radius: 0.75rem;
		overflow: hidden;
		display: grid;
		grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
	}

	@media (max-width: 900px) {
		.details-panel {
			grid-template-columns: 1fr;
		}
	}

	.details-media {
		min-height: 260px;
		background: linear-gradient(
			135deg,
			var(--color-surface-elevated) 0%,
			var(--color-surface) 100%
		);
	}

	.details-fallback {
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: flex-end;
		gap: 0.75rem;
		padding: 1.5rem;
		background: radial-gradient(
				circle at top right,
				rgba(212, 168, 83, 0.2),
				transparent 45%
			),
			linear-gradient(
				135deg,
				rgba(255, 255, 255, 0.04),
				rgba(255, 255, 255, 0.01)
			);
	}

	.details-fallback h3 {
		font-family: var(--font-heading);
		font-size: 1.5rem;
		color: var(--color-text);
	}

	.details-fallback p {
		color: var(--color-text-muted);
		line-height: 1.6;
	}

	.details-copy {
		padding: 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.panel-title {
		font-family: var(--font-heading);
		font-size: clamp(1.4rem, 2.5vw, 1.8rem);
		color: var(--color-text);
	}

	.panel-tags {
		margin-top: 0.25rem;
	}

	.detailed-desc {
		color: var(--color-text-muted);
		font-size: 0.9375rem;
		line-height: 1.6;
		margin-bottom: 1rem;
	}

	.github-link {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		color: var(--color-text);
		text-decoration: none;
		font-size: 0.875rem;
		transition: color 0.2s ease;
	}

	.github-link:hover {
		color: var(--color-primary);
	}

	.panel-actions {
		display: flex;
		gap: 0.75rem;
		flex-wrap: wrap;
		margin-top: auto;
	}

	.close-btn {
		background: none;
		border: 1px solid var(--color-border);
		color: var(--color-text-muted);
		padding: 0.5rem 1rem;
		font-size: 0.8125rem;
		cursor: pointer;
		border-radius: 0.25rem;
		transition: all 0.2s ease;
	}

	.close-btn:hover {
		border-color: var(--color-text-subtle);
		color: var(--color-text);
	}
</style>
