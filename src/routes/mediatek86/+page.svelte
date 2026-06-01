<script lang="ts">
	import {
		FileText,
		Code2,
		Download,
		CheckCircle2,
		Layers,
		Database,
		Award,
		ExternalLink,
		BookOpen,
		Users,
		ArrowRight,
		Play,
		Server,
		ShieldCheck,
		Calendar
	} from "@lucide/svelte";

	let activeTab = "video";

	const tabs = [
		{ id: "video", label: "Vidéo Démo", desc: "Tutoriel guidé (5 min)" },
		{ id: "paquetages", label: "Architecture", desc: "Organisation MVC + DAL" },
		{ id: "mcd", label: "Schéma MCD", desc: "Modèle conceptuel" },
		{ id: "mld", label: "Schéma MLD", desc: "Modèle logique" },
		{ id: "connexion", label: "IHM Connexion", desc: "Authentification RH" },
		{ id: "personnel", label: "IHM Personnel", desc: "Gestion des agents" },
		{ id: "absences", label: "IHM Absences", desc: "Gestion des congés" }
	];

	const screenshots: Record<string, { src: string; title: string; caption: string }> = {
		paquetages: {
			src: "/projets/mediatek86/images/diagrammePaquetages.png",
			title: "Diagramme de Paquetages",
			caption: "L'application est structurée selon une architecture en 3 couches (MVC) complétée par une couche DAL (Data Access Layer) et un singleton d'accès générique BddManager. Cette séparation garantit la testabilité et l'indépendance vis-à-vis du SGBD."
		},
		mcd: {
			src: "/projets/mediatek86/images/mcd.png",
			title: "Modèle Conceptuel de Données (MCD)",
			caption: "Conçu sous Looping, ce modèle structure les entités clés : le personnel, son service d'affectation, ses absences et le motif associé. Une entité 'responsable' gère les comptes de connexion."
		},
		mld: {
			src: "/projets/mediatek86/images/mld.png",
			title: "Modèle Logique de Données (MLD)",
			caption: "Traduction du MCD en tables relationnelles optimisées pour MySQL, avec intégrité référentielle stricte (clés étrangères et contraintes ON DELETE CASCADE)."
		},
		connexion: {
			src: "/projets/mediatek86/images/frmConnexion.png",
			title: "Formulaire d'authentification",
			caption: "Interface de connexion sécurisée. Les mots de passe saisis sont hachés en SHA-256 côté client et comparés avec les empreintes stockées en BDD."
		},
		personnel: {
			src: "/projets/mediatek86/images/frmGestion.png",
			title: "Tableau de bord du personnel",
			caption: "Vue principale listant les agents du réseau. Elle permet les opérations CRUD (Ajout, Modification, Suppression) avec rafraîchissement dynamique et boîte de dialogue de confirmation."
		},
		absences: {
			src: "/projets/mediatek86/images/frmAbsences.png",
			title: "Module de gestion des absences",
			caption: "Permet de lister les absences d'un agent par ordre antichronologique. Un algorithme métier vérifie à la saisie qu'une nouvelle absence ne chevauche pas une absence existante."
		}
	};

	const steps = [
		{ num: "01", title: "Modélisation", desc: "Looping MCD/MLD, script initial, import MySQL, et jeu d'essai (10 personnels, 50 absences)." },
		{ num: "02", title: "Squelette MVC", desc: "Solution C# WinForms, architecture MVC, Git local, design visuel des formulaires." },
		{ num: "03", title: "DAL & Singleton", desc: "Singleton BddManager, classes Access (DAL), chiffrement de la chaîne MySQL." },
		{ num: "04", title: "Cas d'Utilisation", desc: "Login SHA-256, CRUD Personnel et module Absences avec contrôle anti-chevauchement." },
		{ num: "05", title: "Recette & Documentation", desc: "Documentation technique compilée Sandcastle (.CHM), manuel utilisateur, tutoriel vidéo." },
		{ num: "06", title: "Déploiement", desc: "Installeur final (.MSI), script SQL d'installation complet, livraison du dépôt GitHub." }
	];
</script>

<svelte:head>
	<title>Projet MediaTek86 | Portfolio</title>
	<meta
		name="description"
		content="Rapport technique et démonstration du projet MediaTek86 - Gestion du Personnel."
	/>
</svelte:head>

<div class="page-container">
	<!-- Top Breadcrumb & Badges -->
	<div class="meta-header">
		<span class="badge context-badge">SIO SLAM</span>
		<span class="badge tech-badge">C# .NET</span>
		<span class="badge db-badge">MySQL</span>
		<span class="badge score-badge">Devoir 2</span>
	</div>

	<!-- Title Section -->
	<header class="project-header">
		<h1 class="project-title">MediaTek<span class="accent">86</span></h1>
		<p class="project-tagline">Application de bureau Windows Forms de gestion du personnel et des absences.</p>
	</header>

	<!-- Consolidated Dashboard (Context + Mission + Deliverables) -->
	<section class="glass-card dashboard-card">
		<div class="card-title-bar">
			<BookOpen size={18} color="var(--color-primary)" />
			<h2>Contexte & Mission</h2>
		</div>
		<div class="dashboard-body">
			<div class="dashboard-columns">
				<div class="dash-col">
					<h3>Contexte du réseau</h3>
					<p>
						Le réseau <strong>MediaTek86</strong> gère les médiathèques de la Vienne. Il coordonne les prêts physiques et le développement numérique. Les équipes administratives ont besoin de centraliser la gestion du personnel sur un poste administratif (application lourde hors-ligne).
					</p>
				</div>
				<div class="dash-col">
					<h3>Objectifs du Projet</h3>
					<p>
						En tant que développeur d'applications junior pour l'ESN <strong>InfoTech Services 86</strong>, vous implémentez l'authentification sécurisée (SHA-256), la gestion complète (CRUD) des personnels et services, et le suivi des absences en bloquant les chevauchements de dates.
					</p>
				</div>
			</div>

			<!-- Consolidated Toolbar for Downloads -->
			<div class="deliverables-strip">
				<span class="strip-label">Livrables de la mission :</span>
				<div class="strip-actions">
					<a href="https://github.com/M-Hnida/mediatek" target="_blank" rel="noopener noreferrer" class="strip-btn highlight">
						<Code2 size={15} /> GitHub
					</a>
					<a href="/projets/mediatek86/compte-rendu.pdf" target="_blank" class="strip-btn">
						<FileText size={15} /> Rapport (PDF)
					</a>
					<a href="/projets/mediatek86/mediatek86.sql" download class="strip-btn">
						<Database size={15} /> Script SQL
					</a>
					<a href="/projets/mediatek86/documentation-technique.zip" download class="strip-btn">
						<Download size={15} /> Doc (ZIP)
					</a>
				</div>
			</div>
		</div>
	</section>

	<!-- Interactive Explorer: Left tabs / Right Preview Mockup -->
	<section class="glass-card explorer-card">
		<div class="card-title-bar">
			<Layers size={18} color="var(--color-primary)" />
			<h2>Démonstrations & Analyse Visuelle</h2>
		</div>
		<div class="explorer-layout">
			<!-- Vertical Tabs Sidebar -->
			<div class="explorer-sidebar">
				{#each tabs as tab}
					<button
						class="explorer-tab-btn"
						class:active={activeTab === tab.id}
						on:click={() => (activeTab = tab.id)}
					>
						<span class="tab-label">{tab.label}</span>
						<span class="tab-desc">{tab.desc}</span>
						<span class="tab-arrow"><ArrowRight size={13} /></span>
					</button>
				{/each}
			</div>

			<!-- Visual Preview Mockup Box -->
			<div class="explorer-preview">
				<div class="mockup-header">
					<div class="mockup-dots">
						<span class="dot red"></span>
						<span class="dot yellow"></span>
						<span class="dot green"></span>
					</div>
					<div class="mockup-title">
						{activeTab === "video" ? "Lecteur de démonstration" : screenshots[activeTab].title}
					</div>
				</div>
				<div class="mockup-viewport">
					{#if activeTab === "video"}
						<iframe
							src="https://drive.google.com/file/d/1qXzK9vB_-y4m1f44gEHprm2QR6H62x88/preview"
							title="Démonstration MediaTek86"
							class="mockup-video"
							allow="autoplay"
							allowfullscreen
						></iframe>
					{:else}
						<img
							src={screenshots[activeTab].src}
							alt={screenshots[activeTab].title}
							class="mockup-image"
						/>
					{/if}
				</div>
				<div class="mockup-footer">
					<p>
						{activeTab === "video" 
							? "Tutoriel complet montrant le cycle d'utilisation de l'application : Connexion, consultation et mise à jour du personnel, gestion des absences et validation algorithmique des chevauchements."
							: screenshots[activeTab].caption}
					</p>
				</div>
			</div>
		</div>
	</section>

	<!-- Split Columns: Steps Timeline (Left) & Competencies SIO (Right) -->
	<div class="split-layout">
		<!-- Steps Timeline Card -->
		<div class="glass-card timeline-card">
			<div class="card-title-bar">
				<Calendar size={18} color="var(--color-primary)" />
				<h2>Démarche & Étapes de Réalisation</h2>
			</div>
			<div class="timeline-body">
				<div class="compact-timeline">
					{#each steps as step}
						<div class="timeline-item">
							<div class="timeline-bullet">
								<span>{step.num}</span>
							</div>
							<div class="timeline-info">
								<h4>{step.title}</h4>
								<p>{step.desc}</p>
							</div>
						</div>
					{/each}
				</div>
			</div>
		</div>

		<!-- SIO Competencies Card -->
		<div class="glass-card competencies-card">
			<div class="card-title-bar">
				<Award size={18} color="var(--color-primary)" />
				<h2>Compétences BTS SIO (Bloc 1)</h2>
			</div>
			<div class="competencies-body">
				<div class="comp-list">
					<div class="comp-item">
						<span class="comp-bullet">✦</span>
						<div class="comp-desc">
							<strong>GP 1.2 : Exploiter des référentiels, normes et standards</strong>
							<p>Implémentation du pattern d'architecture MVC, typages C#, modélisation relationnelle de données (MCD/MLD) normalisée.</p>
						</div>
					</div>
					<div class="comp-item">
						<span class="comp-bullet">✦</span>
						<div class="comp-desc">
							<strong>GP 1.3 : Gérer les habilitations associés à un service</strong>
							<p>Contrôle d'accès à l'application via mot de passe responsable haché en SHA-256 en base de données.</p>
						</div>
					</div>
					<div class="comp-item">
						<span class="comp-bullet">✦</span>
						<div class="comp-desc">
							<strong>MS 5.1 : Réaliser les tests d'intégration et d'acceptation</strong>
							<p>Conception du plan de tests, validation de non-chevauchement des absences et sécurité de la base de données.</p>
						</div>
					</div>
					<div class="comp-item">
						<span class="comp-bullet">✦</span>
						<div class="comp-desc">
							<strong>MS 5.2 : Déployer un service</strong>
							<p>Création d'un installeur Windows (.MSI) auto-extractible gérant l'installation applicative et les dépendances DLL.</p>
						</div>
					</div>
					<div class="comp-item">
						<span class="comp-bullet">✦</span>
						<div class="comp-desc">
							<strong>MS 5.3 : Accompagner les utilisateurs (Vidéo)</strong>
							<p>Enregistrement d'un guide utilisateur vidéo de prise en main de l'IHM destiné aux gestionnaires RH.</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.page-container {
		padding: 0.5rem;
		max-width: 1300px;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 1rem;
		z-index: 2;
		position: relative;
	}

	@media (min-width: 768px) {
		.page-container {
			padding: 1rem;
			gap: 1.25rem;
		}
	}

	@media (min-width: 1024px) {
		.page-container {
			padding: 1.5rem 3rem;
			gap: 1.5rem;
		}
	}

	/* Meta Header Badges */
	.meta-header {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
		margin-bottom: -0.5rem;
	}

	.badge {
		font-size: 0.725rem;
		font-weight: 600;
		padding: 0.25rem 0.5rem;
		border-radius: var(--radius-sm);
		text-transform: uppercase;
		letter-spacing: 0.05em;
		border: 1px solid transparent;
	}

	.context-badge {
		background: rgba(212, 168, 83, 0.1);
		color: var(--color-primary);
		border-color: rgba(212, 168, 83, 0.2);
	}

	.tech-badge {
		background: rgba(100, 150, 235, 0.1);
		color: #8baffc;
		border-color: rgba(100, 150, 235, 0.2);
	}

	.db-badge {
		background: rgba(76, 175, 80, 0.1);
		color: #81c784;
		border-color: rgba(76, 175, 80, 0.2);
	}

	.score-badge {
		background: rgba(235, 120, 90, 0.15);
		color: #fc9f8b;
		border-color: rgba(235, 120, 90, 0.3);
	}

	/* Project Header */
	.project-header {
		text-align: left;
		border-bottom: 1px solid var(--color-border);
		padding-bottom: 0.75rem;
		display: flex;
		flex-direction: column;
		gap: 0.25rem;
	}

	.project-title {
		font-family: var(--font-heading);
		font-size: clamp(2.2rem, 5vw, 3.8rem);
		font-weight: 800;
		color: #ffffff;
		line-height: 1.1;
		margin: 0;
	}

	.accent {
		color: var(--color-primary);
	}

	.project-tagline {
		color: var(--color-text-muted);
		font-size: clamp(1rem, 1.8vw, 1.2rem);
		max-width: 900px;
		line-height: 1.4;
		font-weight: 400;
		margin: 0;
	}

	/* Glass Card Base */
	.glass-card {
		background: rgba(10, 10, 10, 0.55);
		backdrop-filter: blur(20px);
		-webkit-backdrop-filter: blur(20px);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-lg);
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
		overflow: hidden;
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
		padding: 0;
	}

	.glass-card:hover {
		border-color: rgba(212, 168, 83, 0.2);
		box-shadow: 0 10px 30px rgba(212, 168, 83, 0.02);
	}

	.card-title-bar {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		padding: 0.6rem 1.25rem;
		border-bottom: 1px solid var(--color-border);
		background: rgba(0, 0, 0, 0.25);
	}

	.card-title-bar h2 {
		font-family: var(--font-heading);
		font-size: 1.1rem;
		color: #ffffff;
		font-weight: 600;
		margin: 0;
	}

	/* Dashboard Card styling */
	.dashboard-body {
		padding: 1rem 1.25rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.dashboard-columns {
		display: grid;
		grid-template-columns: 1fr;
		gap: 1rem;
	}

	@media (min-width: 768px) {
		.dashboard-columns {
			grid-template-columns: 1fr 1fr;
		}
	}

	.dash-col h3 {
		font-size: 0.95rem;
		color: #ffffff;
		margin-bottom: 0.35rem;
		font-weight: 600;
	}

	.dash-col p {
		color: var(--color-text-muted);
		font-size: 0.875rem;
		line-height: 1.5;
		margin: 0;
	}

	/* Deliverables strip (Integrated Toolbar) */
	.deliverables-strip {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		padding-top: 1rem;
		border-top: 1px solid var(--color-border);
	}

	@media (min-width: 900px) {
		.deliverables-strip {
			flex-direction: row;
			align-items: center;
			justify-content: space-between;
		}
	}

	.strip-label {
		font-size: 0.85rem;
		font-weight: 600;
		color: var(--color-primary);
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.strip-actions {
		display: flex;
		flex-wrap: wrap;
		gap: 0.75rem;
	}

	.strip-btn {
		background: rgba(0, 0, 0, 0.45);
		border: 1px solid var(--color-border);
		color: var(--color-text-muted);
		padding: 0.45rem 1rem;
		font-size: 0.825rem;
		border-radius: var(--radius-sm);
		text-decoration: none;
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		font-weight: 500;
		transition: all 0.25s ease;
	}

	.strip-btn:hover {
		border-color: rgba(212, 168, 83, 0.35);
		color: #ffffff;
		transform: translateY(-1px);
	}

	.strip-btn.highlight {
		background: linear-gradient(135deg, rgba(212, 168, 83, 0.1) 0%, rgba(0, 0, 0, 0.5) 100%);
		border-color: rgba(212, 168, 83, 0.25);
		color: var(--color-primary);
	}

	.strip-btn.highlight:hover {
		border-color: var(--color-primary);
		color: #ffffff;
		box-shadow: 0 4px 12px rgba(212, 168, 83, 0.1);
	}

	/* Explorer Section layout */
	.explorer-card {
		margin: 0;
	}

	.explorer-layout {
		display: grid;
		grid-template-columns: 1fr;
		gap: 0;
	}

	@media (min-width: 900px) {
		.explorer-layout {
			grid-template-columns: 260px 1fr;
		}
	}

	.explorer-sidebar {
		display: flex;
		flex-direction: row;
		overflow-x: auto;
		gap: 0.5rem;
		scrollbar-width: none;
		padding: 0.75rem;
		background: rgba(0, 0, 0, 0.15);
		border-bottom: 1px solid var(--color-border);
	}

	.explorer-sidebar::-webkit-scrollbar {
		display: none;
	}

	@media (min-width: 900px) {
		.explorer-sidebar {
			flex-direction: column;
			overflow-x: visible;
			gap: 0.4rem;
			padding: 1rem 0.75rem;
			border-bottom: none;
			border-right: 1px solid var(--color-border);
		}
	}

	.explorer-tab-btn {
		flex-shrink: 0;
		width: 180px;
		background: rgba(15, 15, 15, 0.5);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-sm);
		padding: 0.5rem 0.75rem;
		text-align: left;
		cursor: pointer;
		display: flex;
		flex-direction: column;
		gap: 0.1rem;
		transition: all 0.2s ease;
		position: relative;
	}

	@media (min-width: 900px) {
		.explorer-tab-btn {
			width: 100%;
		}
	}

	.explorer-tab-btn:hover {
		border-color: rgba(212, 168, 83, 0.25);
		background: rgba(20, 20, 20, 0.7);
	}

	.explorer-tab-btn.active {
		background: linear-gradient(90deg, rgba(212, 168, 83, 0.1) 0%, rgba(15, 15, 15, 0.8) 100%);
		border-color: var(--color-primary);
	}

	.tab-label {
		font-size: 0.875rem;
		font-weight: 600;
		color: #ffffff;
	}

	.explorer-tab-btn.active .tab-label {
		color: var(--color-primary);
	}

	.tab-desc {
		font-size: 0.7rem;
		color: var(--color-text-muted);
	}

	.tab-arrow {
		position: absolute;
		right: 0.75rem;
		top: 50%;
		transform: translateY(-50%) translateX(-4px);
		color: var(--color-primary);
		opacity: 0;
		transition: all 0.2s ease;
		display: flex;
	}

	.explorer-tab-btn.active .tab-arrow {
		opacity: 1;
		transform: translateY(-50%) translateX(0);
	}

	/* Visual Mockup Box */
	.explorer-preview {
		background: #0d0d0d;
		display: flex;
		flex-direction: column;
	}

	.mockup-header {
		background: #141414;
		border-bottom: 1px solid var(--color-border);
		padding: 0.4rem 1rem;
		display: flex;
		align-items: center;
		position: relative;
	}

	.mockup-dots {
		display: flex;
		gap: 0.4rem;
	}

	.dot {
		width: 8px;
		height: 8px;
		border-radius: 50%;
		display: block;
	}

	.dot.red { background-color: #ff5f56; }
	.dot.yellow { background-color: #ffbd2e; }
	.dot.green { background-color: #27c93f; }

	.mockup-title {
		font-size: 0.75rem;
		color: var(--color-text-muted);
		position: absolute;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
		font-family: monospace;
	}

	.mockup-viewport {
		display: flex;
		justify-content: center;
		align-items: center;
		background: #070707;
		overflow: hidden;
		padding: 0.25rem;
	}

	.mockup-image {
		max-width: 100%;
		height: auto;
		max-height: 380px;
		object-fit: contain;
		border-radius: var(--radius-sm);
		box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
	}

	.mockup-video {
		width: 100%;
		height: auto;
		max-height: 380px;
		aspect-ratio: 16 / 9;
		background: #000;
		outline: none;
		border-radius: var(--radius-sm);
	}

	.mockup-footer {
		background: #121212;
		border-top: 1px solid var(--color-border);
		padding: 0.5rem 0.75rem;
	}

	.mockup-footer p {
		color: var(--color-text-muted);
		font-size: 0.8rem;
		line-height: 1.4;
		margin: 0;
	}

	/* Split Columns (Timeline & Competencies) */
	.split-layout {
		display: grid;
		grid-template-columns: 1fr;
		gap: 1rem;
	}

	@media (min-width: 900px) {
		.split-layout {
			grid-template-columns: 1.05fr 0.95fr;
			gap: 1.25rem;
			align-items: start;
		}
	}

	/* Timeline formatting */
	.timeline-body,
	.competencies-body {
		padding: 1rem 1.25rem;
	}

	.compact-timeline {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		border-left: 2px solid var(--color-border);
		padding-left: 1rem;
		margin-left: 0.5rem;
	}

	.timeline-item {
		position: relative;
	}

	.timeline-bullet {
		position: absolute;
		left: -28px;
		top: 2px;
		background: var(--color-border);
		border: 1px solid rgba(212, 168, 83, 0.3);
		color: var(--color-primary);
		width: 20px;
		height: 20px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		box-shadow: 0 0 8px rgba(0,0,0,0.5);
	}

	.timeline-bullet span {
		font-size: 0.65rem;
		font-weight: 700;
		font-family: monospace;
	}

	.timeline-info h4 {
		font-size: 0.95rem;
		color: #ffffff;
		font-weight: 600;
		margin: 0 0 0.25rem;
	}

	.timeline-info p {
		font-size: 0.8rem;
		color: var(--color-text-muted);
		line-height: 1.45;
		margin: 0;
	}

	/* Competencies formatting */
	.comp-list {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	.comp-item {
		display: flex;
		gap: 0.75rem;
		align-items: flex-start;
	}

	.comp-bullet {
		color: var(--color-primary);
		font-size: 0.75rem;
		margin-top: 0.15rem;
	}

	.comp-desc strong {
		font-size: 0.9rem;
		color: #ffffff;
		display: block;
		margin-bottom: 0.15rem;
		line-height: 1.4;
	}

	.comp-desc p {
		font-size: 0.8rem;
		color: var(--color-text-muted);
		line-height: 1.45;
		margin: 0;
	}
</style>
