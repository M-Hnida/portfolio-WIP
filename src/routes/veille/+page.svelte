<script lang="ts">
</script>

<svelte:head>
	<title>Veille Technologique | Portfolio</title>
	<meta name="description" content="Veille technologique et informationnelle" />
</svelte:head>

<div class="page-container">
	<section class="hero-simple">
		<div class="container">
			<h1 class="title">Veille <span class="accent">Informationnelle</span></h1>
			<p class="subtitle">Dispositifs et thématiques de ma veille technologique</p>
		</div>
	</section>

	<section class="veille-section">
		<div class="container">
			<div class="dispositif-box">
				<h2>Mon Dispositif de Veille</h2>
				<p>
					La veille technologique est essentielle dans le domaine du développement pour rester à jour sur les nouvelles technologies, les failles de sécurité et les bonnes pratiques.
				</p>
				<p>Pour assurer ma veille, j'utilise différents outils :</p>
				<ul class="tools-list">
					<li><strong>Agrégateurs de flux RSS</strong> (Feedly) pour suivre les blogs techniques et sites d'actualité.</li>
					<li><strong>Réseaux sociaux professionnels</strong> (LinkedIn, Twitter/X) en suivant des experts du domaine.</li>
					<li><strong>Newsletters spécialisées</strong> (TLDR Web Dev, JavaScript Weekly).</li>
					<li><strong>Plateformes de développement</strong> (GitHub Trending, Stack Overflow).</li>
				</ul>
			</div>

			<h2 class="themes-title">Thèmes Surveillés</h2>
			
			<div class="themes-grid">
				<article class="theme-card">
					<div class="theme-icon">🚀</div>
					<h3>L'évolution des frameworks JavaScript/TypeScript</h3>
					<p>
						L'écosystème web front-end et back-end évolue très rapidement. Je surveille particulièrement les nouveautés concernant Svelte/SvelteKit, React, et l'adoption croissante de TypeScript.
					</p>
					<p class="theme-reason">
						<strong>Pourquoi ce choix ?</strong> En tant que futur développeur (spécialité SLAM), maîtriser les frameworks modernes et comprendre leurs évolutions me permet de choisir les meilleurs outils pour chaque projet et de maintenir des compétences attractives sur le marché du travail.
					</p>
				</article>

				<article class="theme-card">
					<div class="theme-icon">🔒</div>
					<h3>La sécurité des applications web (OWASP)</h3>
					<p>
						Je me tiens informé des nouvelles vulnérabilités découvertes, des failles courantes et des meilleures pratiques pour sécuriser le code (authentification, protection contre les injections, gestion des données sensibles).
					</p>
					<p class="theme-reason">
						<strong>Pourquoi ce choix ?</strong> La sécurité ("Security by design") est un enjeu majeur aujourd'hui. Concevoir des applications robustes dès le départ est une compétence indispensable pour un développeur SLAM professionnel.
					</p>
				</article>
			</div>
		</div>
	</section>
</div>

<style>
	.page-container {
		min-height: 100vh;
		background-color: var(--color-background);
		padding-top: 5rem;
	}

	.hero-simple {
		padding: 4rem 0 2rem;
		text-align: center;
	}

	.container {
		max-width: 75rem;
		margin: 0 auto;
		padding: 0 1.5rem;
	}

	.title {
		font-family: var(--font-heading);
		font-size: clamp(2rem, 5vw, 3.5rem);
		font-weight: 700;
		color: var(--color-text);
		margin-bottom: 1rem;
	}

	.accent {
		color: #c0c0c0;
	}

	.subtitle {
		color: var(--color-text-muted);
		font-size: 1.125rem;
	}

	.veille-section {
		padding: 3rem 0 6rem;
	}

	.dispositif-box {
		background: rgba(255, 255, 255, 0.02);
		border: 1px solid var(--color-border);
		border-radius: 1rem;
		padding: 2.5rem;
		margin-bottom: 4rem;
	}

	.dispositif-box h2 {
		font-family: var(--font-heading);
		font-size: 1.75rem;
		color: #c0c0c0;
		margin-bottom: 1.5rem;
	}

	.dispositif-box p {
		color: var(--color-text-muted);
		line-height: 1.7;
		margin-bottom: 1rem;
	}

	.tools-list {
		list-style-type: none;
		padding: 0;
		margin-top: 1.5rem;
	}

	.tools-list li {
		color: var(--color-text-muted);
		padding: 0.75rem 0;
		border-bottom: 1px solid rgba(255,255,255,0.05);
		display: flex;
		align-items: flex-start;
	}

	.tools-list li strong {
		color: var(--color-text);
		margin-right: 0.5rem;
	}

	.tools-list li::before {
		content: "▹";
		color: #c0c0c0;
		margin-right: 0.75rem;
		margin-top: 0.1rem;
	}

	.themes-title {
		font-family: var(--font-heading);
		font-size: 2rem;
		color: var(--color-text);
		text-align: center;
		margin-bottom: 3rem;
	}

	.themes-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2rem;
	}

	@media (min-width: 768px) {
		.themes-grid {
			grid-template-columns: 1fr 1fr;
		}
	}

	.theme-card {
		background-color: var(--color-surface);
		border: 1px solid var(--color-border);
		border-radius: 0.75rem;
		padding: 2rem;
		transition: transform 0.3s ease, border-color 0.3s ease;
	}

	.theme-card:hover {
		transform: translateY(-5px);
		border-color: rgba(192, 192, 192, 0.3);
	}

	.theme-icon {
		font-size: 2.5rem;
		margin-bottom: 1.5rem;
	}

	.theme-card h3 {
		font-family: var(--font-heading);
		font-size: 1.25rem;
		color: #c0c0c0;
		margin-bottom: 1rem;
		line-height: 1.4;
	}

	.theme-card p {
		color: var(--color-text-muted);
		line-height: 1.6;
		margin-bottom: 1.5rem;
	}

	.theme-reason {
		font-size: 0.9375rem;
		background: rgba(0, 0, 0, 0.2);
		padding: 1rem;
		border-radius: 0.5rem;
		border-left: 3px solid #c0c0c0;
		margin-bottom: 0 !important;
	}

	.theme-reason strong {
		color: var(--color-text);
		display: block;
		margin-bottom: 0.25rem;
	}
</style>