<script lang="ts">
	import { Target, Search, Rocket, ShieldCheck, Code2, MessageSquare, Hash, Play } from "@lucide/svelte";
</script>

<svelte:head>
	<title>Méthode & Veille Technologique | Portfolio</title>
	<meta name="description" content="Démarche, outils et thèmes de ma veille technologique pour le BTS SIO" />
</svelte:head>

<div class="page-container">
	<section class="hero-simple">
		<h1 class="title">Veille <span class="accent">Informationnelle</span></h1>
		<p class="subtitle">Organisation, méthodologie et thématiques de ma veille technologique</p>
	</section>

	<div class="methodology-grid">
		<div class="methodology-card">
			<div class="card-icon">
				<Target size={28} />
			</div>
			<h2>Démarche & Gestion des Risques</h2>
			<p>
				Ma veille est planifiée pour rester compétent face aux évolutions rapides du développement logiciel, tout en maîtrisant deux risques majeurs :
			</p>
			<ul class="methodology-list">
				<li>
					<strong>La sous-information :</strong> Évitée grâce à une veille continue et quotidienne sur mes technologies cibles, garantissant la détection rapide de failles de sécurité majeures.
				</li>
				<li>
					<strong>L'infobésité (surinformation) :</strong> Évitée en délimitant un périmètre précis (30 minutes par jour max) et en filtrant mes abonnements pour ne conserver que des sources à haute valeur ajoutée.
				</li>
			</ul>
		</div>

		<div class="methodology-card">
			<div class="card-icon">
				<Search size={28} />
			</div>
			<h2>Validation & Recherche Avancée</h2>
			<p>
				Pour valider chaque information collectée, j'applique la méthode du <strong>QQOQCCP</strong> :
			</p>
			<p class="qqoqccp-detail">
				<strong>Qui</strong> a publié ? (crédibilité de l'auteur) | <strong>Quoi</strong> ? (fiabilité des faits) | <strong>Quand</strong> ? (fraîcheur de la publication) | <strong>Pourquoi</strong> ? (visée commerciale ou technique).
			</p>
			<p>
				J'optimise mes recherches de bugs et de documentations avec des <strong>opérateurs de recherche avancée</strong> :
			</p>
			<code class="code-example">site:github.com "CVE-2026"</code>
			<code class="code-example">filetype:pdf "SQL Server configuration"</code>
		</div>
	</div>

	<div class="dispositif-box">
		<h2>Mon Dispositif de Collecte</h2>
		<p>
			J'utilise une sélection de plateformes ciblées pour capter les tendances open-source, les partages d'expériences et les tutoriels pratiques :
		</p>
		<div class="sources-grid">
			<div class="source-item">
				<span class="source-icon">
					<Code2 size={22} />
				</span>
				<div class="source-info">
					<h3>GitHub</h3>
					<p>Suivi des dépôts populaires (Trending) et des releases de frameworks pour surveiller l'adoption réelle de nouvelles technologies.</p>
				</div>
			</div>
			<div class="source-item">
				<span class="source-icon">
					<MessageSquare size={22} />
				</span>
				<div class="source-info">
					<h3>Reddit</h3>
					<p>Lecture active des subreddits spécialisés (r/programming, r/webdev, r/python) pour observer les retours d'expérience et débats techniques.</p>
				</div>
			</div>
			<div class="source-item">
				<span class="source-icon">
					<Hash size={22} />
				</span>
				<div class="source-info">
					<h3>Twitter / X</h3>
					<p>Suivi de créateurs et développeurs influents pour capter instantanément les annonces majeures et "signaux faibles".</p>
				</div>
			</div>
			<div class="source-item">
				<span class="source-icon">
					<Play size={22} />
				</span>
				<div class="source-info">
					<h3>YouTube</h3>
					<p>Visionnage de tutoriels, revues de code et conférences techniques pour approfondir et voir en pratique les nouvelles architectures.</p>
				</div>
			</div>
		</div>
	</div>

	<h2 class="themes-title">Thèmes Surveillés</h2>
	
	<div class="themes-grid">
		<article class="theme-card">
			<div class="theme-icon">
				<Rocket size={32} />
			</div>
			<h3>L'évolution des frameworks JavaScript/TypeScript</h3>
			<p>
				L'écosystème web front-end et back-end évolue très rapidement. Je surveille particulièrement les nouveautés concernant Svelte/SvelteKit et l'adoption croissante de TypeScript.
			</p>
			<p class="theme-reason">
				<strong>Pourquoi ce choix ?</strong> En tant que futur développeur (spécialité SLAM), maîtriser les frameworks modernes me permet de choisir les meilleurs outils pour chaque projet et de maintenir des compétences attractives sur le marché du travail.
			</p>
		</article>

		<article class="theme-card">
			<div class="theme-icon">
				<ShieldCheck size={32} />
			</div>
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

<style>
	.page-container {
		padding: 1.5rem;
		max-width: 1200px;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 2rem;
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
	}

	.hero-simple {
		padding: 2rem 0;
		text-align: left;
	}

	.title {
		font-family: var(--font-heading);
		font-size: clamp(2rem, 5vw, 3rem);
		font-weight: 700;
		color: var(--color-text);
		margin-bottom: 0.5rem;
	}

	.accent {
		color: var(--color-primary);
	}

	.subtitle {
		color: var(--color-text-muted);
		font-size: 1.125rem;
	}

	.methodology-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2rem;
	}

	@media (min-width: 768px) {
		.methodology-grid {
			grid-template-columns: 1fr 1fr;
		}
	}

	.methodology-card {
		background: rgba(10, 10, 10, 0.6);
		backdrop-filter: blur(16px);
		-webkit-backdrop-filter: blur(16px);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-lg);
		padding: 2.5rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
	}

	.methodology-card h2 {
		font-family: var(--font-heading);
		font-size: 1.5rem;
		color: #ffffff;
		font-weight: 600;
	}

	.card-icon {
		color: var(--color-primary);
		display: flex;
		align-items: center;
	}

	.methodology-list {
		list-style: none;
		padding: 0;
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	.methodology-list li {
		font-size: 0.95rem;
		color: var(--color-text-muted);
		line-height: 1.6;
		position: relative;
		padding-left: 1.25rem;
	}

	.methodology-list li::before {
		content: "▹";
		color: var(--color-primary);
		position: absolute;
		left: 0;
		top: 0;
	}

	.qqoqccp-detail {
		font-size: 0.85rem;
		background: rgba(0, 0, 0, 0.3);
		padding: 0.75rem 1rem;
		border-radius: var(--radius-md);
		border-left: 2px solid var(--color-primary);
		color: var(--color-text-muted);
		line-height: 1.6;
	}

	.code-example {
		font-family: monospace;
		font-size: 0.85rem;
		color: var(--color-primary);
		background: rgba(212, 168, 83, 0.08);
		padding: 0.4rem 0.8rem;
		border-radius: var(--radius-sm);
		border: 1px solid rgba(212, 168, 83, 0.15);
		width: fit-content;
	}

	.dispositif-box {
		background: rgba(10, 10, 10, 0.6);
		backdrop-filter: blur(16px);
		-webkit-backdrop-filter: blur(16px);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-lg);
		padding: 2.5rem;
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
	}

	.dispositif-box h2 {
		font-family: var(--font-heading);
		font-size: 1.75rem;
		color: #ffffff;
		margin-bottom: 1.5rem;
		font-weight: 600;
	}

	.dispositif-box p {
		color: var(--color-text-muted);
		line-height: 1.7;
		margin-bottom: 1.5rem;
	}

	.sources-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 1.5rem;
		margin-bottom: 2rem;
	}

	@media (min-width: 768px) {
		.sources-grid {
			grid-template-columns: 1fr 1fr;
		}
	}

	.source-item {
		display: flex;
		gap: 1rem;
		align-items: flex-start;
		background: rgba(0, 0, 0, 0.25);
		padding: 1.25rem;
		border-radius: var(--radius-md);
		border: 1px solid var(--color-border);
		transition: border-color 0.3s ease;
	}

	.source-item:hover {
		border-color: rgba(212, 168, 83, 0.3);
	}

	.source-icon {
		color: var(--color-primary);
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.source-info h3 {
		font-size: 1.1rem;
		color: var(--color-text);
		margin-bottom: 0.25rem;
		font-weight: 600;
	}

	.source-info p {
		font-size: 0.875rem;
		color: var(--color-text-muted);
		line-height: 1.5;
		margin-bottom: 0;
	}



	.themes-title {
		font-family: var(--font-heading);
		font-size: 1.75rem;
		color: var(--color-text);
		margin-top: 1rem;
		font-weight: 600;
	}

	.themes-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2rem;
		margin-bottom: 2rem;
	}

	@media (min-width: 768px) {
		.themes-grid {
			grid-template-columns: 1fr 1fr;
		}
	}

	.theme-card {
		background: rgba(10, 10, 10, 0.6);
		backdrop-filter: blur(16px);
		-webkit-backdrop-filter: blur(16px);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-lg);
		padding: 2.5rem;
		transition: transform 0.3s ease, border-color 0.3s ease;
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
	}

	.theme-card:hover {
		transform: translateY(-5px);
		border-color: rgba(212, 168, 83, 0.3);
	}

	.theme-icon {
		color: var(--color-primary);
		margin-bottom: 1.5rem;
		display: flex;
		align-items: center;
	}

	.theme-card h3 {
		font-family: var(--font-heading);
		font-size: 1.25rem;
		color: #ffffff;
		margin-bottom: 1rem;
		line-height: 1.4;
		font-weight: 600;
	}

	.theme-card p {
		color: var(--color-text-muted);
		line-height: 1.6;
		margin-bottom: 1.5rem;
	}

	.theme-reason {
		font-size: 0.9375rem;
		background: rgba(0, 0, 0, 0.35);
		padding: 1rem;
		border-radius: var(--radius-md);
		border-left: 3px solid var(--color-primary);
		margin-bottom: 0 !important;
	}

	.theme-reason strong {
		color: var(--color-text);
		display: block;
		margin-bottom: 0.25rem;
	}
</style>