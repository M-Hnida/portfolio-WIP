<script lang="ts">
	const education = [
		{
			year: "2025-2027",
			title: "BTS SIO - Option SLAM",
			subtitle: "Solutions Logicielles et Applications Métier",
			place: "CNED (Centre National d'Enseignement à Distance)",
			description:
				"Le BTS SIO option SLAM est une formation formant aux métiers du développement. Elle couvre la conception et le développement d'applications, les bases de données, la sécurité (OWASP), ainsi que la qualité logicielle et les méthodes de gestion de projet.",
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

<div id="parcours">
	<h2 class="section-title">Parcours & <span class="accent">Formation</span></h2>
	
	<div class="parcours-content">
		<div class="timeline-section">
			<h3 class="sub-title">Historique</h3>
			<div class="timeline">
				{#each education as e}
					<article class="timeline-item">
						<div class="timeline-marker"></div>
						<div class="timeline-content">
							<span class="year">{e.year}</span>
							<h4 class="item-title">{e.title}</h4>
							<p class="item-subtitle">{e.subtitle}</p>
							<p class="item-place">{e.place}</p>
							<p class="item-desc">{e.description}</p>
						</div>
					</article>
				{/each}
			</div>
		</div>

		<div class="divider"></div>

		<div class="internship-section">
			<h3 class="sub-title">Stage en entreprise</h3>
			<div class="internship-card">
				<div class="internship-header">
					<span class="badge badge-planned">Planifié (Non réalisé)</span>
					<span class="date-badge">Mai - Juin 2026</span>
				</div>
				<h4 class="internship-title">Stage de 1ère année - BTS SIO SLAM</h4>
				<p class="desc-text-internship">
					Stage d'immersion professionnelle d'une durée de 5 à 6 semaines. Ce stage servira de support pour l'épreuve E4 (Conception et développement d'applications) et permettra de mettre en pratique les compétences de développement et de gestion du patrimoine informatique.
				</p>
			</div>
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

	.parcours-content {
		display: flex;
		flex-direction: column;
		gap: 2rem;
	}

	.sub-title {
		font-family: var(--font-heading);
		font-size: 1.25rem;
		color: var(--color-primary);
		margin-bottom: 1rem;
		font-weight: 600;
	}

	.divider {
		height: 1px;
		background: var(--color-border);
		margin: 0.5rem 0;
	}

	.timeline {
		position: relative;
		padding-left: 1.25rem;
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
		padding-bottom: 1.5rem;
	}

	.timeline-item:last-child {
		padding-bottom: 0;
	}

	.timeline-marker {
		position: absolute;
		left: -23px;
		top: 0.25rem;
		width: 7px;
		height: 7px;
		background: var(--color-primary);
		border-radius: 50%;
	}

	.year {
		font-family: var(--font-heading);
		font-size: 0.8rem;
		color: var(--color-primary);
		letter-spacing: 0.05em;
		margin-bottom: 0.25rem;
		display: block;
		font-weight: 500;
	}

	.item-title {
		font-family: var(--font-heading);
		font-size: 1.05rem;
		color: var(--color-text);
		margin-bottom: 0.25rem;
		font-weight: 600;
	}

	.item-subtitle {
		font-size: 0.875rem;
		color: var(--color-text-muted);
		margin-bottom: 0.25rem;
	}

	.item-place {
		font-size: 0.8rem;
		color: var(--color-text-subtle);
		margin-bottom: 0.5rem;
	}

	.item-desc {
		color: var(--color-text-muted);
		font-size: 0.85rem;
		line-height: 1.5;
		margin: 0;
	}

	.internship-card {
		background: rgba(255, 255, 255, 0.02);
		border: 1px dashed rgba(212, 168, 83, 0.25);
		border-radius: var(--radius-md);
		padding: 1.25rem;
		position: relative;
	}

	.internship-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 0.75rem;
	}

	.badge {
		font-size: 0.75rem;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		padding: 0.2rem 0.5rem;
		border-radius: var(--radius-sm);
		font-weight: 500;
	}

	.badge-planned {
		background: rgba(212, 168, 83, 0.1);
		color: var(--color-primary);
		border: 1px solid rgba(212, 168, 83, 0.2);
	}

	.date-badge {
		font-size: 0.8rem;
		color: var(--color-text-muted);
	}

	.internship-title {
		font-family: var(--font-heading);
		font-size: 1.05rem;
		color: var(--color-text);
		margin-bottom: 0.5rem;
		font-weight: 600;
	}

	.desc-text-internship {
		color: var(--color-text-muted);
		font-size: 0.85rem;
		line-height: 1.5;
		margin: 0;
	}
</style>
