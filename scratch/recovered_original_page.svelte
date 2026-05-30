<script lang="ts">
import { onMount } from "svelte";

let loading = true;
let currentJob = "apps";
let mermaidInstance: any = null;

const mindmaps: Record<string, string> = {
apps: `
mindmap
root((Développeur<br/>d'applications))
Entreprise
ESN (Services Numériques)
Éditeurs de logiciels
PME, ETI & GE
Freelance & Startups
Salaire
Débutant : 30k€ - 38k€
Expérimenté : 45k€ - 65k€+
Actions
Conception (UML, Merise)
Codage (Desktop, Web, API)
Tests & Intégration
Maintenance & Sécurité (OWASP)
Qualités
Logique & Rigueur
Travail d'équipe (Git/GitHub)
Curiosité & Veille active
Autonomie & Adaptation
Evolution
Concepteur-Développeur
Lead Developer
Architecte Logiciel
Directeur Technique (CTO)
Formation
Diplomes
BTS SIO SLAM (CNED)
Licence Professionnelle
Master / Écoles d'ingénieurs
Competences
C# / Java / PHP / Python
MySQL / PostgreSQL / MongoDB
KISS / DRY / SOLID
POO / Sockets / MVC
`,
backend: `
mindmap
root((Développeur<br/>Backend))
Entreprise
ESN (Services Numériques)
Éditeurs de logiciels
Grands Comptes / E-commerce
Startups & PME
Salaire
Débutant : 35k€ - 42k€

Formation
Diplomes
BTS SIO SLAM (CNED)
Licence Professionnelle
Master / Écoles d'ingénieurs
Competences
C# / Java / PHP / Python
MySQL / PostgreSQL / MongoDB
KISS / DRY / SOLID
REST API / Sockets / OOP
`,
desktop: `
mindmap
root((Développeur<br/>Desktop))
Entreprise
Éditeurs de logiciels
ESN (Services Numériques)
Secteur industriel / embarqué
Grands comptes (outils internes)
Salaire
Débutant : 30k€ - 38k€
Expérimenté : 42k€ - 58k€+
Actions
Conception d'interfaces (GUI)
Développement d'applications
Sérialisation de données
Optimisation de performances
Qualités
Précision & Rigueur
Autonomie & Ergonomie (UX)
Esprit d'équipe (Git/GitHub)
Evolution
Concepteur-Développeur
Lead Dev Desktop
Architecte Logiciel
Formation
Diplomes
BTS SIO SLAM (CNED)
Licence Professionnelle
Master / Écoles d'ingénieurs
Competences
C# / Java / C++
WPF / Windows Forms
Java Swing / JavaFX
POO / MVC / UML / SOLID
`,
data: `
mindmap
root((Data Scientist<br/>Junior))
Entreprise
Sociétés de conseil en Data
Établissements financiers / trading
Grandes entreprises (pôles Data)
Startups Deeptech / IA
Salaire
Débutant : 38k€ - 45k€
Expérimenté : 50k€ - 75k€+
Actions
Analyse de données (EDA)
Préparation de données (ETL)
Préparation de données (ETL)
Simulation & Backtesting
Visualisation interactive
Qualités
Esprit d'analyse
Esprit mathématique & rigueur
Autonomie & esprit de recherche
Evolution
Data Scientist Senior
Data Architect
Consultant Data / IA
Formation
Diplomes
Licence Pro Data / Mathématiques
Master Data Science
Écoles d'ingénieurs (IA/Data)
Competences
Python / R / SQL
Pandas & NumPy
Visualisation (Plotly)
Backtesting (NautilusTrader)
Statistiques & Modélisation
`,
ml: `
mindmap
root((Ingénieur ML<br/>Junior))
Entreprise
Éditeurs de solutions IA
Laboratoires de R&D
Géants de la Tech
Fintech / Assurtech
Salaire
Débutant : 40k€ - 48k€
Expérimenté : 55k€ - 80k€+
Actions
Pipelines de Machine Learning
Entraînement de modèles (ML/DL)
Déploiement en production (MLOps)
Optimisation d'algorithmes
Qualités
Rigueur mathématique
Veille technologique soutenue
Capacité à optimiser le code
Evolution
Ingénieur ML Senior
Chercheur en IA
Directeur Technique (CTO)
Formation
Diplomes
Master Intelligence Artificielle

script.onload = () => {
// @ts-ignore
mermaidInstance = window.mermaid;
mermaidInstance.initialize({
startOnLoad: false,
theme: "dark",
securityLevel: "loose",
themeVariables: {
primaryColor: "#D4A853",
primaryTextColor: "#F5F0E6",
lineColor: "#8B7355",
nodeBorder: "#1a1815",
mainBkg: "#0a0a0a",
}
});
renderDiagram(currentJob);
};
document.head.appendChild(script);
});
</script>

<svelte:head>
<title>Cartes Heuristiques Métiers | Portfolio</title>
</svelte:head>

<div class="page-container">
<div class="container">
<header class="header">
<a href="/" class="btn-back">← Retour au Portfolio</a>
<h1>Fiches Métiers <span class="accent">& Cartes Heuristiques</span></h1>
<p>Visualisation des compétences et structures de vos futurs métiers (Format SIO)</p>
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
<div class="diagram-card">
{#if loading}
<div class="loader">
<div class="spinner"></div>
<p>Régénération du graphique interactif...</p>
</div>
{/if}

<div id="mermaid-render-area" class="mermaid-wrapper" class:hidden={loading}>
<!-- Mermaid target output will be appended here -->
</div>
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
border
background: rgba(212, 168, 83, 0.02);
}

.tab-btn.active {
border-color: var(--color-primary);
color: var(--color-primary);
background: rgba(212, 168, 83, 0.08);
box-shadow: 0 0 10px rgba(212, 168, 83, 0.05);
}

.diagram-card {
background: rgba(255, 255, 255, 0.01);
border: 1px solid var(--color-border);
border-radius: 1rem;
padding: 2rem;
min-height: 520px;
display: flex;
justify-content: center;
align-items: center;
position: relative;
overflow: hidden;
backdrop-filter: blur(12px);
-webkit-backdrop-filter: blur(12px);
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
</style>

