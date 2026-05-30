<script lang="ts">
	import { reveal } from "$lib/actions/reveal";
	import { Code2 } from "@lucide/svelte";

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
		context: string;
		competencies: string[];
		github?: string;
		preview?: ProjectPreview;
	};

	let selectedProject: number | null = null;

	const projects: Project[] = [
		{
			title: "C# : Gestion des habilitations",
			date: "2026",
			description: "Module de contrôle d'accès utilisateur basé sur les rôles avec architecture MVC et MySQL.",
			detailedDescription: "Développement d'un service d'habilitation pour une application d'entreprise. Implémentation d'une architecture MVC (Modèle-Vue-Contrôleur) avec connexion à une base de données MySQL. Gestion de l'authentification sécurisée, hachage des mots de passe et contrôle des droits d'accès.",
			tags: ["C#", "Visual Studio", "MySQL", "MVC", "Sécurité"],
			category: "DESKTOP",
			context: "Scolaire (Atelier)",
			competencies: [
				"Gérer le patrimoine informatique (Mettre en place et vérifier les niveaux d'habilitation associés à un service - *compétence clé*)",
				"Gérer le patrimoine informatique (Exploiter des référentiels, normes et standards - patron MVC, modélisation de données)",
				"Répondre aux incidents et aux demandes d'assistance et d'évolution"
			],
			preview: {
				type: "image",
				src: "/projets/habilitations/image.png",
				alt: "C# : Gestion des habilitations"
			}
		},
		{
			title: "PHP/JS : Site d'articles",
			date: "2026",
			description: "Interventions d'évolution, conformité RGPD et déploiement d'un site de présentation d'articles.",
			detailedDescription: "Interventions sur un site responsive existant. Réalisation de corrections de bugs, mise en conformité réglementaire (bandeau cookies, mentions légales RGPD), optimisation pour le référencement naturel (SEO) et déploiement sur serveur d'hébergement.",
			tags: ["PHP", "Netbeans", "HTML/CSS", "Javascript", "RGPD", "SEO"],
			category: "WEB",
			context: "Scolaire (Atelier)",
			competencies: [
				"Développer la présence en ligne de l'organisation (Participer à la valorisation de l'image, conformité au cadre juridique et RGPD)",
				"Développer la présence en ligne de l'organisation (Référencer les services en ligne et mesurer leur visibilité SEO)",
				"Développer la présence en ligne de l'organisation (Participer à l'évolution d'un site Web exploitant les données)",
				"Mettre à disposition des utilisateurs un service informatique (Déployer un service)"
			],
			preview: {
				type: "image",
				src: "/projets/articles/image.png",
				alt: "PHP/JS : Site d'articles"
			},
			github: "https://github.com/M-Hnida/chocolatein"
		},
		{
			title: "WordPress : Site E-commerce",
			date: "2026",
			description: "Création d'une boutique en ligne complète sous WordPress pour une organisation.",
			detailedDescription: "Mise en place d'un CMS WordPress avec l'extension WooCommerce. Configuration du catalogue produits, intégration des solutions de paiement, gestion du panier et personnalisation du thème pour répondre aux besoins de l'organisation. Déploiement et mesure d'audience.",
			tags: ["WordPress", "CMS", "WooCommerce", "E-commerce"],
			category: "CMS",
			context: "Scolaire (Atelier)",
			competencies: [
				"Développer la présence en ligne de l'organisation (Participer à l'évolution d'un site Web exploitant les données de l'organisation)",
				"Mettre à disposition des utilisateurs un service informatique (Déployer un service, accompagner les utilisateurs dans la prise en main)",
				"Gérer le patrimoine informatique (Vérifier le respect des règles d'utilisation des ressources numériques)"
			],
			preview: {
				type: "image",
				src: "/projets/wordpress/image.png",
				alt: "WordPress : Site E-commerce"
			},
			github: "https://github.com/M-Hnida/centredeformationinformatique"
		},
		{
			title: "Java : Jeu de combat 2D Client/Serveur",
			date: "2025",
			description: "Jeu multijoueur synchrone avec interface graphique Swing et communication par Sockets.",
			detailedDescription: "Conception et programmation d'un jeu de combat 2D en réseau. Implémentation d'une architecture Client/Serveur multithreadée utilisant les Sockets Java. Interface graphique développée avec Swing, respectant le pattern MVC pour séparer la logique de jeu de l'affichage en temps réel.",
			tags: ["Java", "Eclipse", "Sockets", "Swing", "Multithreading", "Client-Serveur"],
			category: "JEU/RESEAU",
			context: "Scolaire (Atelier)",
			competencies: [
				"Gérer le patrimoine informatique (Exploiter des référentiels, normes et standards - patrons d'architecture, protocole réseau)",
				"Répondre aux incidents et aux demandes d'assistance (Traiter des demandes concernant les services réseau et système, applicatifs)",
				"Mettre à disposition des utilisateurs un service informatique (Réaliser les tests d'intégration et d'acceptation du service)"
			],
			preview: {
				type: "image",
				src: "/projets/jeu/image.png",
				alt: "Java : Jeu de combat 2D Client/Serveur"
			}
		},
		{
			title: "Site E-commerce Full-stack",
			date: "2026",
			description: "Plateforme e-commerce moderne avec MedusaJS, SvelteKit et PostgreSQL.",
			detailedDescription: "Projet personnel d'apprentissage avancé. Création d'un site e-commerce moderne en architecture headless. Utilisation de MedusaJS pour le moteur backend e-commerce, PostgreSQL pour la base de données relationnelle et SvelteKit pour une interface utilisateur rapide, animée et optimisée.",
			tags: ["Typescript", "MedusaJS", "PostgreSQL", "SvelteKit", "API REST"],
			category: "WEB",
			context: "Personnel",
			competencies: [
				"Développer la présence en ligne de l'organisation (Participer à l'évolution d'un site Web exploitant les données)",
				"Mettre à disposition des utilisateurs un service informatique (Réaliser les tests d'intégration et d'acceptation, Déployer un service)",
				"Travailler en mode projet (Planifier les activités, évaluer le suivi du projet)"
			],
			preview: {
				type: "image",
				src: "/projets/ecommerce/image.png",
				alt: "Site E-commerce Full-stack"
			}
		},
		{
			title: "Bot Discord Automation",
			date: "2024",
			description: "Bot de modération et d'automatisation de serveur Discord développé en Python.",
			detailedDescription: "Bot Discord développé en Python à l'aide de la bibliothèque discord.py. Intègre des commandes slash interactives, un système de modération automatique, la gestion automatisée des rôles et des salons, ainsi que la journalisation des événements du serveur.",
			tags: ["Python", "PyCharm", "Discord API", "Asyncio"],
			category: "AUTOMATION",
			context: "Personnel",
			competencies: [
				"Répondre aux incidents et aux demandes d'assistance et d'évolution (Traiter des demandes concernant les applications)",
				"Mettre à disposition des utilisateurs un service informatique (Accompagner les utilisateurs dans la mise en place du service)"
			],
			github: "https://github.com/M-Hnida/discord-bot",
			preview: {
				type: "image",
				src: "/projets/discord/image.png",
				alt: "Bot Discord Automation"
			}
		},
		{
			title: "Backtesting Trading Algorithmique",
			date: "2025",
			description: "Moteur de simulation de stratégies de trading en Python avec visualisation interactive.",
			detailedDescription: "Outil de recherche quantitative et de backtesting développé en Python. Utilise le framework NautilusTrader pour la simulation d'ordres en temps historique, Pandas et NumPy pour la manipulation de gros volumes de données financières, et Plotly pour générer des rapports de performance interactifs.",
			tags: ["Python", "NautilusTrader", "Pandas", "NumPy", "Plotly"],
			category: "DATA",
			context: "Personnel / Recherche",
			competencies: [
				"Organiser son développement professionnel (Mettre en place son environnement d'apprentissage personnel, auto-formation sur la data science)",
				"Gérer le patrimoine informatique (Exploiter des référentiels, normes et standards de traitement de données)"
			],
			github: "https://github.com/M-Hnida/trading-backtest",
			preview: {
				type: "video",
				src: "/projets/backtest/nauttrader.mp4",
				poster: "/projets/backtest/image.png",
				alt: "Backtesting Trading Algorithmique",
			},
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

<section id="projects" class="section-card">
	<h2 class="section-title">
		Projets & <span class="accent">Réalisations</span>
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
							<div class="card-meta">
								<span class="date">{p.date}</span>
								<span class="context-tag" class:context-scolaire={p.context.includes("Scolaire")} class:context-stage={p.context.includes("Stage")} class:context-perso={p.context.includes("Personnel")}>{p.context}</span>
							</div>
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
								Cadre : {activeProject.context}
							</p>
						</div>
					{/if}
				</div>

				<div class="details-copy">
					<div class="details-meta-header">
						<span class="date">{activeProject.date}</span>
						<span class="context-tag active-context" class:context-scolaire={activeProject.context.includes("Scolaire")} class:context-stage={activeProject.context.includes("Stage")} class:context-perso={activeProject.context.includes("Personnel")}>{activeProject.context}</span>
					</div>
					<h3 class="panel-title">{activeProject.title}</h3>
					<p class="detailed-desc">
						{activeProject.detailedDescription}
					</p>

					{#if activeProject.competencies && activeProject.competencies.length > 0}
						<div class="competencies-section">
							<h4>Compétences BTS SIO Bloc 1</h4>
							<ul class="competencies-list">
								{#each activeProject.competencies as comp}
									<li>{comp}</li>
								{/each}
							</ul>
						</div>
					{/if}

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
								<Code2 size={20} />
								Voir sur GitHub
							</a>
						{:else}
							<button
								class="github-link disabled"
								disabled
								aria-disabled="true"
							>
								<Code2 size={20} />
								Code Privé
							</button>
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
</section>

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

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
		gap: 1.5rem;
	}

	.card {
		background-color: var(--color-surface);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
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
		border-radius: var(--radius-sm);
	}

	.card-content {
		padding: 1.5rem;
		display: flex;
		flex-direction: column;
		flex: 1;
	}

	.card-meta {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 0.75rem;
	}

	.date {
		font-size: 0.75rem;
		color: var(--color-text-subtle);
		display: block;
	}

	.context-tag {
		font-size: 0.7rem;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		padding: 0.15rem 0.4rem;
		border-radius: var(--radius-sm);
		font-weight: 500;
		border: 1px solid transparent;
	}

	.context-scolaire {
		background: rgba(100, 150, 235, 0.1);
		color: #8baffc;
		border-color: rgba(100, 150, 235, 0.2);
	}

	.context-stage {
		background: rgba(235, 120, 90, 0.1);
		color: #fc9f8b;
		border-color: rgba(235, 120, 90, 0.2);
	}

	.context-perso {
		background: rgba(76, 175, 80, 0.1);
		color: #81c784;
		border-color: rgba(76, 175, 80, 0.2);
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
		border-radius: var(--radius-sm);
	}

	.details-panel {
		margin-top: 1.5rem;
		background: var(--color-surface);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-lg);
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

	.details-meta-header {
		display: flex;
		align-items: center;
		gap: 1rem;
	}

	.active-context {
		font-size: 0.75rem;
		padding: 0.25rem 0.6rem;
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
		margin-bottom: 0.5rem;
	}

	.competencies-section {
		margin-top: 0.5rem;
		border-top: 1px solid var(--color-border);
		padding-top: 1rem;
		margin-bottom: 0.5rem;
	}

	.competencies-section h4 {
		font-family: var(--font-heading);
		font-size: 0.85rem;
		color: var(--color-text);
		margin-bottom: 0.5rem;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.competencies-list {
		list-style-type: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
	}

	.competencies-list li {
		font-size: 0.85rem;
		color: var(--color-text-muted);
		display: flex;
		align-items: flex-start;
		line-height: 1.4;
	}

	.competencies-list li::before {
		content: "✦";
		color: var(--color-primary);
		margin-right: 0.5rem;
		font-size: 0.75rem;
		margin-top: 0.15rem;
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

	.github-link.disabled {
		opacity: 0.4;
		cursor: not-allowed;
		background: none;
		border: none;
		padding: 0;
		font-family: inherit;
	}

	.github-link.disabled:hover {
		color: var(--color-text);
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
		border-radius: var(--radius-sm);
		transition: all 0.2s ease;
	}

	.close-btn:hover {
		border-color: var(--color-text-subtle);
		color: var(--color-text);
	}
</style>
