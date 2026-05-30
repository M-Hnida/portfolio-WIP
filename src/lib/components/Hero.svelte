<script lang="ts">
	// Aucun import requis
</script>

<section id="hero" class="section-card animate-fade-in">
	<div class="hero-content">
		<p class="pretitle animate-fade-in-up">
			Étudiant en informatique
		</p>
		<h1 class="title animate-fade-in-up delay-100">
			Mohammed <span class="accent">Hnida</span>
		</h1>
		<p class="subtitle animate-fade-in-up delay-200">
			Développement d'applications, backend & data science.
			Conception de solutions robustes, de la modélisation de bases de données à l'implémentation de la logique métier et d'outils analytiques.
		</p>
		<div class="buttons animate-fade-in-up delay-300">
			<a
				href="/cv/CV_Hnida_Mohammed.pdf"
				download
				class="btn-primary animate-shine">Télécharger mon CV (PDF)</a
			>
			<a
				href="#contact"
				class="btn-outline">Me contacter</a
			>
		</div>
	</div>
</section>

<style>
	.hero-content {
		max-width: 800px;
	}

	.pretitle {
		font-size: 0.875rem;
		text-transform: uppercase;
		letter-spacing: 0.25em;
		color: var(--color-primary);
		margin-bottom: 1rem;
		font-weight: 600;
	}

	.title {
		font-family: var(--font-heading);
		font-size: clamp(2.5rem, 6vw, 4rem);
		font-weight: 700;
		margin-bottom: 1.5rem;
		line-height: 1.1;
		color: #ffffff;
		letter-spacing: -0.02em;
	}

	.accent {
		color: transparent;
		-webkit-text-stroke: 1px rgba(255, 255, 255, 0.85);
		text-shadow: 0 0 15px rgba(212, 168, 83, 0.2);
	}

	.subtitle {
		color: var(--color-text-muted);
		font-size: 1.125rem;
		line-height: 1.8;
		margin-bottom: 2.5rem;
		font-weight: 400;
	}

	.buttons {
		display: flex;
		flex-wrap: wrap;
		gap: 1rem;
	}

	@media (max-width: 640px) {
		.buttons {
			flex-direction: column;
			align-items: stretch;
		}
		
		.buttons :global(a) {
			text-align: center;
		}
	}
</style>
