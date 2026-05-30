<script lang="ts">
	import { reveal } from "$lib/actions/reveal";

	const skills = [
		{
			category: "LANGAGES",
			items: [
				{ name: "Python", level: 5 },
				{ name: "C#", level: 3 },
				{ name: "C++", level: 3 },
				{ name: "PHP", level: 3 },
				{ name: "HTML", level: 4 },
				{ name: "CSS", level: 2 },
				{ name: "JavaScript", level: 3 },
				{ name: "Java", level: 3 },
			],
		},
		{
			category: "IDE & OUTILS",
			items: [
				{ name: "VS Code", level: 5 },
				{ name: "Visual Studio", level: 4 },
				{ name: "Zed", level: 2 },
				{ name: "PyCharm", level: 3 },
				{ name: "Netbeans", level: 2 },
				{ name: "Eclipse", level: 2 },
			],
		},
		{
			category: "SGBD",
			items: [
				{ name: "MySQL", level: 4 },
				{ name: "PostgreSQL", level: 4 },
				{ name: "MongoDB", level: 3 },
				{ name: "Redis", level: 2 }
			],
		},
		{
			category: "CMS",
			items: [{ name: "WordPress", level: 4 },
				{ name: "Directus", level: 2 }
			],
		},
		{
			category: "QUALITÉ LOGICIELLE",
			items: [
				{ name: "Normes (KISS, DRY, SOLID)", level: 5 },
				{ name: "Tests unitaires", level: 5 },
				{ name: "Tests fonctionnels", level: 5 },
				{ name: "Analyse (Sonarlint)", level: 4 },
			],
		},
		{
			category: "CONCEPTION",
			items: [
				{ name: "Merise/2", level: 4 },
				{ name: "UML", level: 3 },
			],
		},
		{
			category: "TRAVAIL COLLABORATIF",
			items: [{ name: "GitHub", level: 4 }],
		},
	];

	const col1 = [
		skills.find((s) => s.category === "LANGAGES"),
		skills.find((s) => s.category === "SGBD"),
		skills.find((s) => s.category === "QUALITÉ LOGICIELLE"),
	].filter(Boolean) as typeof skills;

	const col2 = [
		skills.find((s) => s.category === "IDE & OUTILS"),
		skills.find((s) => s.category === "CMS"),
		skills.find((s) => s.category === "CONCEPTION"),
		skills.find((s) => s.category === "TRAVAIL COLLABORATIF"),
	].filter(Boolean) as typeof skills;
</script>

<div id="skills">
	<h2 class="section-title" use:reveal>
		Compétences & <span class="accent">Technologies</span>
	</h2>
	<div class="skills-columns">
		<div class="skills-col">
			{#each col1 as cat, i}
				<article class="skill-card" use:reveal={{ delay: i * 80 }}>
					<div class="card-header">
						<h3 class="cat-title">{cat.category}</h3>
						<div class="cat-line"></div>
					</div>
					<div class="tags">
						{#each cat.items as item}
							<div class="tag" title="Niveau: {item.level}/5">
								<span>{item.name}</span>
								<div class="level-indicator">
									{#each Array.from({ length: 5 }) as _, i}
										<div
											class="dot"
											class:active={i < item.level}
										></div>
									{/each}
								</div>
							</div>
						{/each}
					</div>
				</article>
			{/each}
		</div>
		<div class="skills-col">
			{#each col2 as cat, i}
				<article class="skill-card" use:reveal={{ delay: (i + 3) * 80 }}>
					<div class="card-header">
						<h3 class="cat-title">{cat.category}</h3>
						<div class="cat-line"></div>
					</div>
					<div class="tags">
						{#each cat.items as item}
							<div class="tag" title="Niveau: {item.level}/5">
								<span>{item.name}</span>
								<div class="level-indicator">
									{#each Array.from({ length: 5 }) as _, i}
										<div
											class="dot"
											class:active={i < item.level}
										></div>
									{/each}
								</div>
							</div>
						{/each}
					</div>
				</article>
			{/each}
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

	.skills-columns {
		display: grid;
		grid-template-columns: 1fr;
		gap: 1.5rem;
	}

	@media (min-width: 640px) {
		.skills-columns {
			grid-template-columns: 1fr 1fr;
		}
	}

	.skills-col {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
	}

	.skill-card {
		background: rgba(255, 255, 255, 0.02);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		padding: 1.5rem;
		transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
		display: flex;
		flex-direction: column;
		position: relative;
		overflow: hidden;
	}

	.skill-card::before {
		content: "";
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		height: 2px;
		background: linear-gradient(
			90deg,
			transparent,
			rgba(212, 168, 83, 0.5),
			transparent
		);
		opacity: 0;
		transition: opacity 0.4s ease;
	}

	.skill-card:hover {
		border-color: rgba(212, 168, 83, 0.3);
		transform: translateY(-3px);
		box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
		background: rgba(255, 255, 255, 0.03);
	}

	.skill-card:hover::before {
		opacity: 1;
	}

	.card-header {
		display: flex;
		align-items: center;
		gap: 0.75rem;
		margin-bottom: 1.25rem;
	}

	.cat-title {
		font-family: var(--font-heading);
		font-size: 0.95rem;
		color: #e0e0e0;
		letter-spacing: 0.08em;
		margin: 0;
		font-weight: 600;
	}

	.cat-line {
		flex: 1;
		height: 1px;
		background: linear-gradient(
			90deg,
			rgba(212, 168, 83, 0.25),
			transparent
		);
	}

	.tags {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
	}

	.tag {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		font-size: 0.8rem;
		color: #a0a0a0;
		border: 1px solid rgba(255, 255, 255, 0.08);
		padding: 0.3rem 0.75rem;
		border-radius: var(--radius-sm);
		transition: all 0.3s ease;
		background: rgba(0, 0, 0, 0.25);
		cursor: default;
	}

	.tag:hover {
		border-color: var(--color-primary);
		color: #ffffff;
		background: rgba(212, 168, 83, 0.12);
		transform: translateY(-1px);
	}

	.level-indicator {
		display: flex;
		gap: 2px;
	}

	.dot {
		width: 4px;
		height: 4px;
		border-radius: 50%;
		background: rgba(255, 255, 255, 0.15);
		transition: all 0.3s ease;
	}

	.dot.active {
		background: rgba(212, 168, 83, 0.7);
		box-shadow: 0 0 3px rgba(212, 168, 83, 0.4);
	}

	.tag:hover .dot.active {
		background: var(--color-primary);
		box-shadow: 0 0 5px rgba(212, 168, 83, 0.8);
	}
</style>
