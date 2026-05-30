<script lang="ts">
	import { onMount } from "svelte";

	let loading = true;
	let currentJob = "apps";
	let mermaidLoaded = false;

	const tabs = [
		{ id: "apps", label: "Développeur d'applications" },
		{ id: "backend", label: "Développeur Backend" },
		{ id: "desktop", label: "Développeur Desktop" },
		{ id: "data", label: "Data Scientist Junior" },
		{ id: "ml", label: "Ingénieur Machine Learning" }
	];

	const mindmaps: Record<string, string> = {
		apps: `
flowchart LR
    %% Left Side: Child --- Parent --- Root
    Debutant("Débutant : 30k€ - 38k€"):::branch
    Experimente("Expérimenté : 45k€ - 65k€+"):::branch
    ESN("ESN (Services Numériques)"):::branch
    Editeurs("Éditeurs de logiciels"):::branch
    PME("PME, ETI & GE"):::branch
    Freelance("Freelance & Startups"):::branch
    Conception("Conception (UML, Merise)"):::branch
    Codage("Codage (Desktop, Web, API)"):::branch
    Tests("Tests & Intégration"):::branch
    Securite("Maintenance & Sécurité (OWASP)"):::branch

    Salaire(Salaire):::branch
    Entreprise(Entreprise):::branch
    Actions(Actions):::branch

    Root(Développeur d'applications):::root

    %% Right Side: Root --- Parent --- Child
    Formation(Formation):::branch
    Diplomes(Diplômes):::branch
    Competences(Compétences):::branch
    Evolution(Evolution):::branch
    Qualites(Qualités):::branch

    Concepteur("Concepteur-Développeur"):::branch
    Lead("Lead Developer"):::branch
    Architecte("Architecte Logiciel"):::branch
    CTO("Directeur Technique (CTO)"):::branch

    Logique("Logique & Rigueur"):::branch
    Team("Travail d'équipe (Git/GitHub)"):::branch
    Veille("Curiosité & Veille active"):::branch
    Adaptation("Autonomie & Adaptation"):::branch

    BTS("BTS SIO SLAM (CNED)"):::branch
    Licence("Licence Professionnelle"):::branch
    Master("Master / Écoles d'ingénieurs"):::branch

    Langages("C# / Java / PHP / Python"):::branch
    BDD("MySQL / PostgreSQL / MongoDB"):::branch
    Methodes("KISS / DRY / SOLID"):::branch
    Concepts("POO / Sockets / MVC"):::branch

    %% Left Side connections
    Debutant --- Salaire
    Experimente --- Salaire
    ESN --- Entreprise
    Editeurs --- Entreprise
    PME --- Entreprise
    Freelance --- Entreprise
    Conception --- Actions
    Codage --- Actions
    Tests --- Actions
    Securite --- Actions

    Salaire --- Root
    Entreprise --- Root
    Actions --- Root

    %% Right Side connections
    Root --- Formation
    Root --- Evolution
    Root --- Qualites

    Formation --- Diplomes
    Formation --- Competences
    Evolution --- Concepteur
    Evolution --- Lead
    Evolution --- Architecte
    Evolution --- CTO
    Qualites --- Logique
    Qualites --- Team
    Qualites --- Veille
    Qualites --- Adaptation

    Diplomes --- BTS
    Diplomes --- Licence
    Diplomes --- Master

    Competences --- Langages
    Competences --- BDD
    Competences --- Methodes
    Competences --- Concepts

    classDef root fill:#1FA3EC,stroke:#1585c5,stroke-width:1.5px,color:#ffffff;
    classDef branch fill:#eaeaea,stroke:#8e8e8e,stroke-width:1.5px,color:#2c2c2c;
		`,
		backend: `
flowchart LR
    %% Left Side: Child --- Parent --- Root
    Debutant("Débutant : 35k€ - 42k€"):::branch
    Experimente("Expérimenté : 50k€ - 70k€+"):::branch
    ESN("ESN (Services Numériques)"):::branch
    Editeurs("Éditeurs de logiciels"):::branch
    PME("Grands Comptes / E-commerce"):::branch
    Freelance("Startups & PME"):::branch
    Conception("Conception (APIs, BDD)"):::branch
    Codage("Codage (C#, Java, PHP, Node)"):::branch
    Tests("Tests Unitaires & CI/CD"):::branch
    Securite("Sécurité (OWASP, JWT)"):::branch

    Salaire(Salaire):::branch
    Entreprise(Entreprise):::branch
    Actions(Actions):::branch

    Root(Développeur Backend):::root

    %% Right Side: Root --- Parent --- Child
    Formation(Formation):::branch
    Diplomes(Diplômes):::branch
    Competences(Compétences):::branch
    Evolution(Evolution):::branch
    Qualites(Qualités):::branch

    Concepteur("Développeur API / Cloud"):::branch
    Lead("Lead Backend Dev"):::branch
    Architecte("Architecte Logiciel"):::branch
    CTO("Directeur Technique (CTO)"):::branch

    Logique("Logique & Résolution"):::branch
    Team("Méthodes Agiles (Git)"):::branch
    Veille("Veille technologique active"):::branch
    Adaptation("Autonomie & Rigueur"):::branch

    BTS("BTS SIO SLAM (CNED)"):::branch
    Licence("Licence Professionnelle"):::branch
    Master("Master / Écoles d'ingénieurs"):::branch

    Langages("C# / Java / PHP / TypeScript"):::branch
    BDD("PostgreSQL / MySQL / MongoDB"):::branch
    Methodes("REST API / Sockets / OOP"):::branch
    Concepts("KISS / DRY / SOLID"):::branch

    %% Left Side connections
    Debutant --- Salaire
    Experimente --- Salaire
    ESN --- Entreprise
    Editeurs --- Entreprise
    PME --- Entreprise
    Freelance --- Entreprise
    Conception --- Actions
    Codage --- Actions
    Tests --- Actions
    Securite --- Actions

    Salaire --- Root
    Entreprise --- Root
    Actions --- Root

    %% Right Side connections
    Root --- Formation
    Root --- Evolution
    Root --- Qualites

    Formation --- Diplomes
    Formation --- Competences
    Evolution --- Concepteur
    Evolution --- Lead
    Evolution --- Architecte
    Evolution --- CTO
    Qualites --- Logique
    Qualites --- Team
    Qualites --- Veille
    Qualites --- Adaptation

    Diplomes --- BTS
    Diplomes --- Licence
    Diplomes --- Master

    Competences --- Langages
    Competences --- BDD
    Competences --- Methodes
    Competences --- Concepts

    classDef root fill:#1FA3EC,stroke:#1585c5,stroke-width:1.5px,color:#ffffff;
    classDef branch fill:#eaeaea,stroke:#8e8e8e,stroke-width:1.5px,color:#2c2c2c;
		`,
		desktop: `
flowchart LR
    %% Left Side: Child --- Parent --- Root
    Debutant("Débutant : 30k€ - 38k€"):::branch
    Experimente("Expérimenté : 42k€ - 58k€+"):::branch
    Editeurs("Éditeurs de logiciels"):::branch
    ESN("ESN (Services Numériques)"):::branch
    Industriel("Secteur Industriel"):::branch
    GrandsComptes("Grands Comptes"):::branch
    GUI("Interface Graphique (GUI)"):::branch
    Applications("Développement d'apps"):::branch
    Serialization("Sérialisation de données"):::branch
    Performances("Optimisation performances"):::branch

    Salaire(Salaire):::branch
    Entreprise(Entreprise):::branch
    Actions(Actions):::branch

    Root(Développeur Desktop):::root

    %% Right Side: Root --- Parent --- Child
    Formation(Formation):::branch
    Diplomes(Diplômes):::branch
    Competences(Compétences):::branch
    Evolution(Evolution):::branch
    Qualites(Qualités):::branch

    Concepteur("Concepteur-Développeur"):::branch
    Lead("Lead Dev Desktop"):::branch
    Architecte("Architecte Logiciel"):::branch

    Rigueur("Précision & Rigueur"):::branch
    UX("Autonomie & Ergonomie (UX)"):::branch
    Team("Esprit d'équipe (Git)"):::branch

    BTS("BTS SIO SLAM (CNED)"):::branch
    Licence("Licence Professionnelle"):::branch
    Master("Master / Écoles d'ingénieurs"):::branch

    Langages("C# / Java / C++"):::branch
    Frameworks("WPF / WinForms"):::branch
    Swing("Java Swing / JavaFX"):::branch
    OOP("POO / MVC / UML / SOLID"):::branch

    %% Left Side connections
    Debutant --- Salaire
    Experimente --- Salaire
    Editeurs --- Entreprise
    ESN --- Entreprise
    Industriel --- Entreprise
    GrandsComptes --- Entreprise
    GUI --- Actions
    Applications --- Actions
    Serialization --- Actions
    Performances --- Actions

    Salaire --- Root
    Entreprise --- Root
    Actions --- Root

    %% Right Side connections
    Root --- Formation
    Root --- Evolution
    Root --- Qualites

    Formation --- Diplomes
    Formation --- Competences
    Evolution --- Concepteur
    Evolution --- Lead
    Evolution --- Architecte
    Qualites --- Rigueur
    Qualites --- UX
    Qualites --- Team

    Diplomes --- BTS
    Diplomes --- Licence
    Diplomes --- Master

    Competences --- Langages
    Competences --- Frameworks
    Competences --- Swing
    Competences --- OOP

    classDef root fill:#1FA3EC,stroke:#1585c5,stroke-width:1.5px,color:#ffffff;
    classDef branch fill:#eaeaea,stroke:#8e8e8e,stroke-width:1.5px,color:#2c2c2c;
		`,
		data: `
flowchart LR
    %% Left Side: Child --- Parent --- Root
    Debutant("Débutant : 38k€ - 45k€"):::branch
    Experimente("Expérimenté : 50k€ - 75k€+"):::branch
    Conseil("Sociétés de conseil en Data"):::branch
    Finances("Établissements financiers"):::branch
    GrandsGroupes("Grandes entreprises"):::branch
    Startups("Startups Deeptech / IA"):::branch
    EDA("Analyse de données (EDA)"):::branch
    ETL("Préparation de données (ETL)"):::branch
    Simulation("Simulation & Backtesting"):::branch
    Interactive("Visualisation interactive"):::branch

    Salaire(Salaire):::branch
    Entreprise(Entreprise):::branch
    Actions(Actions):::branch

    Root(Data Scientist Junior):::root

    %% Right Side: Root --- Parent --- Child
    Formation(Formation):::branch
    Diplomes(Diplômes):::branch
    Competences(Compétences):::branch
    Evolution(Evolution):::branch
    Qualites(Qualités):::branch

    Senior("Data Scientist Senior"):::branch
    Architect("Data Architect"):::branch
    Consultant("Consultant Data / IA"):::branch

    Analyse("Esprit d'analyse"):::branch
    Maths("Esprit math & rigueur"):::branch
    Recherche("Autonomie & recherche"):::branch

    Licence("Licence Pro Data/Maths"):::branch
    Master("Master Data Science"):::branch
    Ingenieur("Écoles d'ingénieurs"):::branch

    Python("Python / R / SQL"):::branch
    Pandas("Pandas & NumPy"):::branch
    Plotly("Visualisation (Plotly)"):::branch
    Nautilus("Backtest (NautilusTrader)"):::branch
    Stats("Statistiques & Modélisation"):::branch

    %% Left Side connections
    Debutant --- Salaire
    Experimente --- Salaire
    Conseil --- Entreprise
    Finances --- Entreprise
    GrandsGroupes --- Entreprise
    Startups --- Entreprise
    EDA --- Actions
    ETL --- Actions
    Simulation --- Actions
    Interactive --- Actions

    Salaire --- Root
    Entreprise --- Root
    Actions --- Root

    %% Right Side connections
    Root --- Formation
    Root --- Evolution
    Root --- Qualites

    Formation --- Diplomes
    Formation --- Competences
    Evolution --- Senior
    Evolution --- Architect
    Evolution --- Consultant
    Qualites --- Analyse
    Qualites --- Maths
    Qualites --- Recherche

    Diplomes --- Licence
    Diplomes --- Master
    Diplomes --- Ingenieur

    Competences --- Python
    Competences --- Pandas
    Competences --- Plotly
    Competences --- Nautilus
    Competences --- Stats

    classDef root fill:#1FA3EC,stroke:#1585c5,stroke-width:1.5px,color:#ffffff;
    classDef branch fill:#eaeaea,stroke:#8e8e8e,stroke-width:1.5px,color:#2c2c2c;
		`,
		ml: `
flowchart LR
    %% Left Side: Child --- Parent --- Root
    Debutant("Débutant : 40k€ - 48k€"):::branch
    Experimente("Expérimenté : 55k€ - 80k€+"):::branch
    Editeurs("Éditeurs de solutions IA"):::branch
    Labos("Laboratoires de R&D"):::branch
    Tech("Géants de la Tech"):::branch
    Fintech("Fintech / Assurtech"):::branch
    Pipelines("Pipelines de ML"):::branch
    Train("Entraînement de modèles"):::branch
    MLOps("Déploiement (MLOps)"):::branch
    Optim("Optimisation d'algos"):::branch

    Salaire(Salaire):::branch
    Entreprise(Entreprise):::branch
    Actions(Actions):::branch

    Root(Ingénieur ML Junior):::root

    %% Right Side: Root --- Parent --- Child
    Formation(Formation):::branch
    Diplomes(Diplômes):::branch
    Competences(Compétences):::branch
    Evolution(Evolution):::branch
    Qualites(Qualités):::branch

    Senior("Ingénieur ML Senior"):::branch
    Chercheur("Chercheur en IA"):::branch
    CTO("Directeur Technique (CTO)"):::branch

    Maths("Rigueur mathématique"):::branch
    Veille("Veille technologique"):::branch
    CodeOptim("Capacité d'optimisation"):::branch

    Master("Master IA"):::branch
    Ingenieur("Écoles d'ingénieurs"):::branch

    Python("Python / PyTorch / TF"):::branch
    Docker("MLOps (Docker, MLflow)"):::branch
    Algos("Algorithmes & Maths"):::branch
    Models("Optimisation de modèles"):::branch

    %% Left Side connections
    Debutant --- Salaire
    Experimente --- Salaire
    Editeurs --- Entreprise
    Labos --- Entreprise
    Tech --- Entreprise
    Fintech --- Entreprise
    Pipelines --- Actions
    Train --- Actions
    MLOps --- Actions
    Optim --- Actions

    Salaire --- Root
    Entreprise --- Root
    Actions --- Root

    %% Right Side connections
    Root --- Formation
    Root --- Evolution
    Root --- Qualites

    Formation --- Diplomes
    Formation --- Competences
    Evolution --- Senior
    Evolution --- Chercheur
    Evolution --- CTO
    Qualites --- Maths
    Qualites --- Veille
    Qualites --- CodeOptim

    Diplomes --- Master
    Diplomes --- Ingenieur

    Competences --- Python
    Competences --- Docker
    Competences --- Algos
    Competences --- Models

    classDef root fill:#1FA3EC,stroke:#1585c5,stroke-width:1.5px,color:#ffffff;
    classDef branch fill:#eaeaea,stroke:#8e8e8e,stroke-width:1.5px,color:#2c2c2c;
		`
	};

	onMount(() => {
		const urlParams = new URLSearchParams(window.location.search);
		const jobParam = urlParams.get("job");
		if (jobParam && tabs.some((tab) => tab.id === jobParam)) {
			currentJob = jobParam;
		}

		const script = document.createElement("script");
		script.src = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js";
		script.onload = () => {
			// @ts-ignore
			window.mermaid.initialize({
				startOnLoad: false,
				theme: "base",
				securityLevel: "loose",
				themeVariables: {
					primaryColor: "#1FA3EC",
					primaryTextColor: "#ffffff",
					lineColor: "#8e8e8e",
					nodeBorder: "#8e8e8e",
					mainBkg: "#ffffff",
					secondaryColor: "#eaeaea",
					secondaryTextColor: "#2c2c2c",
					secondaryBorderColor: "#8e8e8e",
					tertiaryColor: "#eaeaea",
					tertiaryTextColor: "#2c2c2c",
					tertiaryBorderColor: "#8e8e8e",
				}
			});
			mermaidLoaded = true;
			renderDiagram();
		};
		document.head.appendChild(script);
	});

	function renderDiagram() {
		if (!mermaidLoaded) return;
		loading = true;
		setTimeout(() => {
			try {
				// @ts-ignore
				window.mermaid.init(undefined, document.querySelectorAll(".mermaid"));
			} catch (e) {
				console.error("Mermaid render error:", e);
			}
			loading = false;
		}, 50);
	}

	function switchJob(jobId: string) {
		currentJob = jobId;
		renderDiagram();
	}
</script>

<svelte:head>
	<title>Cartes Heuristiques Métiers | Portfolio</title>
</svelte:head>

<div class="page-container">
	<div class="container">
		<header class="header">
			<a href="/" class="btn-back">← Retour au Portfolio</a>
			<h1>Cartes Heuristiques <span class="accent">Métiers & Tech</span></h1>
			<p>Organisation visuelle des métiers visés, des compétences et des technologies associées (Format SIO)</p>
		</header>

		<!-- Tabs navigation -->
		<div class="tabs-nav">
			{#each tabs as tab}
				<button
					class="tab-btn"
					class:active={currentJob === tab.id}
					on:click={() => switchJob(tab.id)}
				>
					{tab.label}
				</button>
			{/each}
		</div>

		<!-- Mindmap diagram card -->
		<div class="diagram-card" class:loading-active={loading}>
			{#if loading}
				<div class="loader">
					<div class="spinner"></div>
					<p>Régénération du graphique interactif...</p>
				</div>
			{/if}

			<div class="mermaid-wrapper" class:hidden={loading}>
				{#key currentJob}
					<div class="mermaid">
						{mindmaps[currentJob]}
					</div>
				{/key}
			</div>
		</div>
	</div>
</div>

<style>
	.page-container {
		min-height: 100vh;
		background-color: var(--color-background);
		padding: 4rem 0;
		color: var(--color-text);
	}

	.container {
		max-width: 80rem;
		margin: 0 auto;
		padding: 0 1.5rem;
	}

	.header {
		text-align: center;
		margin-bottom: 2.5rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
	}

	.btn-back {
		color: var(--color-primary);
		text-decoration: none;
		font-size: 0.9rem;
		font-family: var(--font-heading);
		text-transform: uppercase;
		letter-spacing: 0.1em;
		border: 1px solid var(--color-border);
		padding: 0.5rem 1rem;
		border-radius: 0.25rem;
		transition: all 0.3s ease;
		background: rgba(255, 255, 255, 0.02);
	}

	.btn-back:hover {
		border-color: var(--color-primary);
		background: rgba(212, 168, 83, 0.05);
		transform: translateY(-2px);
	}

	.header h1 {
		font-family: var(--font-heading);
		font-size: clamp(1.75rem, 5vw, 2.5rem);
		margin: 0;
		line-height: 1.2;
	}

	.accent {
		color: #c0c0c0;
	}

	.header p {
		color: var(--color-text-muted);
		margin: 0;
		font-size: 1.05rem;
	}

	.tabs-nav {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
		gap: 0.75rem;
		margin-bottom: 2rem;
	}

	.tab-btn {
		background: var(--color-surface);
		border: 1px solid var(--color-border);
		color: var(--color-text-muted);
		padding: 0.6rem 1.2rem;
		font-size: 0.95rem;
		cursor: pointer;
		border-radius: 0.375rem;
		transition: all 0.3s ease;
	}

	.tab-btn:hover {
		border-color: var(--color-primary);
		color: var(--color-text);
	}

	.tab-btn.active {
		border-color: var(--color-primary);
		color: var(--color-primary);
		background: rgba(212, 168, 83, 0.08);
		box-shadow: 0 0 10px rgba(212, 168, 83, 0.05);
	}

	.diagram-card {
		background: #ffffff;
		border: 1px solid #e0e0e0;
		border-radius: 1rem;
		padding: 2.5rem;
		min-height: 650px;
		display: flex;
		justify-content: center;
		align-items: center;
		position: relative;
		overflow: auto;
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
	}

	.loading-active {
		background: rgba(255, 255, 255, 0.02);
	}

	.loader {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1.5rem;
		color: var(--color-text-muted);
	}

	.spinner {
		width: 40px;
		height: 40px;
		border: 2px solid rgba(212, 168, 83, 0.1);
		border-top-color: var(--color-primary);
		border-radius: 50%;
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	.mermaid-wrapper {
		width: 100%;
		display: flex;
		justify-content: center;
		overflow-x: auto;
		opacity: 1;
		transition: opacity 0.3s ease;
	}

	.hidden {
		opacity: 0;
		pointer-events: none;
		position: absolute;
	}

	:global(.mermaid) {
		width: 100%;
		display: flex;
		justify-content: center;
		background: transparent !important;
	}

	/* Target rendered Mermaid elements inside Svelte */
	:global(.mermaid svg) {
		max-width: 100%;
		height: auto;
		background: transparent !important;
	}

	/* Style central/root node */
	:global(.mermaid .node.root rect),
	:global(.mermaid .node.root circle),
	:global(.mermaid .node.root polygon),
	:global(.mermaid .node.root path) {
		fill: #1FA3EC !important;   /* Blue background matching image.png */
		stroke: #1585c5 !important;  /* Blue border */
		stroke-width: 1.5px !important;
	}

	:global(.mermaid .node.root .label),
	:global(.mermaid .node.root text) {
		color: #ffffff !important;   /* White text */
		fill: #ffffff !important;
		font-weight: 600 !important;
	}

	/* Style all branch nodes to have the same light grey styling */
	:global(.mermaid .node.branch rect),
	:global(.mermaid .node.branch circle),
	:global(.mermaid .node.branch polygon),
	:global(.mermaid .node.branch path) {
		fill: #eaeaea !important;    /* Light grey background */
		stroke: #8e8e8e !important;  /* Grey border */
		stroke-width: 1.5px !important;
	}

	:global(.mermaid .node.branch .label),
	:global(.mermaid .node.branch text) {
		color: #2c2c2c !important;   /* Dark grey text */
		fill: #2c2c2c !important;
	}

	/* Style connecting lines */
	:global(.mermaid .edgePath .path) {
		stroke: #8e8e8e !important;  /* Grey connecting lines */
		stroke-width: 2px !important;
	}
</style>