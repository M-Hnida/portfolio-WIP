<script lang="ts">
	import { reveal } from "$lib/actions/reveal";

	const skills = [
		{
			category: "LANGAGES",
			items: [
				{ name: "Python", level: 5 },
				{ name: "C#", level: 3 },
				{ name: "C++", level: 4 },
				{ name: "PHP", level: 3 },
				{ name: "HTML", level: 4 },
				{ name: "CSS", level: 2 },
				{ name: "JavaScript", level: 3 },
				{ name: "Java", level: 3 },
			],
		},
		{
			category: "IDE",
			items: [
				{ name: "VS Code", level: 5 },
				{ name: "Visual Studio", level: 4 },
				{ name: "Zed", level: 3 },
				{ name: "Netbeans", level: 2 },
				{ name: "Eclipse", level: 2 },
				{ name: "PyCharm", level: 3 },
			],
		},
		{
			category: "SGBD",
			items: [
				{ name: "MySQL", level: 4 },
				{ name: "PostgreSQL", level: 3 },
				{ name: "MongoDB", level: 3 },
			],
		},
		{
			category: "CMS",
			items: [{ name: "WordPress", level: 4 }],
		},
		{
			category: "QUALITÉ LOGICIELLE",
			items: [
				{ name: "Normes (KISS, DRY, SOLID)", level: 4 },
				{ name: "Tests unitaires", level: 3 },
				{ name: "Tests fonctionnels", level: 3 },
				{ name: "Analyse de code (Sonarlint)", level: 4 },
			],
		},
		{
			category: "MÉTHODES DE CONCEPTION",
			items: [
				{ name: "Merise/2", level: 4 },
				{ name: "UML", level: 3 },
			],
		},
		{
			category: "TRAVAIL COLLABORATIF",
			items: [{ name: "GitHub (push, pull request...)", level: 4 }],
		},
	].map((cat) => ({
		...cat,
		items: cat.items.sort((a, b) => b.level - a.level),
	}));
</script>

<section id="skills" class="skills">
	<div class="container">
		<h2 class="title" use:reveal>
			Compétences & <span class="accent">Technologies</span>
		</h2>
		<div class="skills-grid">
			{#each skills as cat, i}
				<article class="skill-card" use:reveal={{ delay: i * 90 }}>
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
</section>

<style>
	.skills {
		padding: 6rem 0;
		background-color: var(--color-surface);
		position: relative;
	}

	.container {
		max-width: 80rem;
		margin: 0 auto;
		padding: 0 1.5rem;
		position: relative;
		z-index: 1;
	}

	.title {
		font-family: var(--font-heading);
		font-size: clamp(2rem, 5vw, 3rem);
		text-align: center;
		margin-bottom: 4rem;
		color: var(--color-text);
		letter-spacing: -0.02em;
		visibility: hidden;
	}

	.accent {
		color: #d4af37;
		background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 100%);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}

	.skills-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
		gap: 2rem;
		align-items: start;
	}

	.skill-card {
		background: rgba(255, 255, 255, 0.02);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		border: 1px solid rgba(255, 255, 255, 0.06);
		border-radius: 1rem;
		padding: 2rem;
		transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
		visibility: hidden;
		height: 100%;
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
		transform: translateY(-5px);
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
		background: rgba(255, 255, 255, 0.03);
	}

	.skill-card:hover::before {
		opacity: 1;
	}

	.card-header {
		display: flex;
		align-items: center;
		gap: 1rem;
		margin-bottom: 1.5rem;
	}

	.cat-title {
		font-family: var(--font-heading);
		font-size: 1.1rem;
		color: #e0e0e0;
		letter-spacing: 0.1em;
		margin: 0;
		font-weight: 600;
	}

	.cat-line {
		flex: 1;
		height: 1px;
		background: linear-gradient(
			90deg,
			rgba(212, 168, 83, 0.3),
			transparent
		);
	}

	.tags {
		display: flex;
		flex-wrap: wrap;
		gap: 0.6rem;
	}

	.tag {
		display: flex;
		align-items: center;
		gap: 0.6rem;
		font-size: 0.85rem;
		color: #a0a0a0;
		border: 1px solid rgba(255, 255, 255, 0.1);
		padding: 0.35rem 0.85rem;
		border-radius: 2rem;
		transition: all 0.3s ease;
		background: rgba(0, 0, 0, 0.2);
		letter-spacing: 0.02em;
		cursor: default;
	}

	.tag:hover {
		border-color: #d4af37;
		color: #ffffff;
		background: rgba(212, 168, 83, 0.15);
		transform: translateY(-2px);
		box-shadow: 0 4px 12px rgba(212, 168, 83, 0.1);
	}

	.level-indicator {
		display: flex;
		gap: 3px;
		margin-top: 1px;
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
		box-shadow: 0 0 4px rgba(212, 168, 83, 0.4);
	}

	.tag:hover .dot.active {
		background: #d4af37;
		box-shadow: 0 0 6px rgba(212, 168, 83, 0.8);
	}

	@media (max-width: 768px) {
		.skills-grid {
			grid-template-columns: 1fr;
		}

		.skills {
			padding: 4rem 0;
		}
	}
</style>
