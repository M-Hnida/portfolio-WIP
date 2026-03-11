<section class="hero">
	<div class="hero-bg"></div>
	<div class="vignette"></div>

	<!-- Ambient light effects -->
	<div class="light-ray-container">
		<div class="light-ray ray-1 animate-divine-glow"></div>
		<div class="light-ray ray-2 animate-divine-glow delay-1000"></div>
	</div>

	<div class="container">
		<div class="content">
			<div class="text-box">
				<div class="left">
					<p class="pretitle animate-fade-in-up">
						Étudiant en informatique
					</p>
					<h1 class="title animate-fade-in-up delay-100">
						Mohammed<br /><span class="accent">Hnida</span>
					</h1>
					<p class="subtitle animate-fade-in-up delay-200">
						Backend, data science, machine learning et applications
						desktop
					</p>
					<div class="buttons animate-fade-in-up delay-300">
						<a
							href="/cv.pdf"
							download
							class="btn-primary animate-shine">Télécharger CV</a
						>
						<a
							href="https://www.linkedin.com/in/mohammed-h-161110360/"
							target="_blank"
							rel="noopener noreferrer"
							class="btn-outline">LinkedIn</a
						>
					</div>
				</div>
				<div class="right animate-fade-in-up delay-500">
					<div class="photo-wrapper animate-float">
						<div class="photo-placeholder">
							<span class="photo-text">Photo</span>
						</div>
						<div class="photo-glow animate-divine-glow"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.hero {
		min-height: 100vh;
		display: flex;
		align-items: center;
		position: relative;
		overflow: hidden;
		padding: 6rem 0 4rem;
	}

	.hero-bg {
		position: absolute;
		z-index: 0;
		background-image: url("/image.png");
		background-size: cover;
		background-position: center;
		filter: blur(8px) brightness(0.35);
		will-change: transform;
	}

	.light-ray-container {
		position: absolute;
		inset: 0;
		z-index: 1;
		pointer-events: none;
	}

	.light-ray {
		position: absolute;
		width: 40vw;
		height: 100vh;
		background: linear-gradient(
			to bottom,
			transparent,
			rgba(212, 168, 83, 0.05),
			transparent
		);
		transform: rotate(-25deg);
		filter: blur(60px);
	}

	.ray-1 {
		left: -10%;
		top: -20%;
	}
	.ray-2 {
		right: -10%;
		top: 20%;
	}

	.vignette {
		position: absolute;
		inset: 0;
		z-index: 2;
		background: radial-gradient(
			ellipse at center,
			transparent 20%,
			rgba(0, 0, 0, 0.8) 100%
		);
		pointer-events: none;
	}

	.container {
		position: relative;
		z-index: 10;
		width: 100%;
		max-width: 80rem;
		margin: 0 auto;
		padding: 0 1.5rem;
	}

	.content {
		display: flex;
		flex-direction: column;
		gap: 0;
	}

	.text-box {
		display: flex;
		flex-direction: column;
		gap: 3rem;
		padding: 0;
	}

	@media (min-width: 768px) {
		.text-box {
			flex-direction: row;
			align-items: center;
			justify-content: space-between;
			gap: 4rem;
		}
	}

	.left {
		flex: 1;
		max-width: 650px;
	}

	.right {
		flex-shrink: 0;
	}

	.photo-wrapper {
		position: relative;
		padding: 1rem;
	}

	.photo-placeholder {
		width: 280px;
		height: 350px;
		background: linear-gradient(
			145deg,
			rgba(255, 255, 255, 0.05),
			rgba(255, 255, 255, 0.01)
		);
		border: 1px solid rgba(255, 255, 255, 0.1);
		border-radius: 1rem;
		display: flex;
		align-items: center;
		justify-content: center;
		box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
		position: relative;
		overflow: hidden;
		z-index: 2;
	}

	.photo-glow {
		position: absolute;
		inset: -20%;
		background: radial-gradient(
			circle at center,
			rgba(212, 168, 83, 0.15) 0%,
			transparent 70%
		);
		z-index: 1;
		filter: blur(40px);
	}

	.photo-placeholder::after {
		content: "";
		position: absolute;
		inset: 0;
		background: linear-gradient(
			to bottom right,
			transparent 50%,
			rgba(212, 175, 55, 0.05) 100%
		);
	}

	.photo-text {
		color: rgba(255, 255, 255, 0.4);
		font-size: 0.875rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		z-index: 1;
	}

	.pretitle {
		font-size: 0.875rem;
		text-transform: uppercase;
		letter-spacing: 0.25em;
		color: #d4af37;
		margin-bottom: 1.5rem;
		font-weight: 500;
		opacity: 0; /* Handled by animation */
	}

	.title {
		font-size: clamp(3rem, 7vw, 4.5rem);
		font-weight: 700;
		margin-bottom: 1.5rem;
		line-height: 1.05;
		color: #ffffff;
		letter-spacing: -0.02em;
		opacity: 0;
	}

	.accent {
		display: inline-block;
		color: transparent;
		-webkit-text-stroke: 1px rgba(255, 255, 255, 0.72);
		text-shadow: 0 0 18px rgba(192, 192, 192, 0.08);
	}

	.subtitle {
		color: rgba(255, 255, 255, 0.7);
		font-size: 1.125rem;
		line-height: 1.8;
		margin-bottom: 2rem;
		font-weight: 300;
		opacity: 0;
	}

	.buttons {
		display: flex;
		flex-wrap: wrap;
		gap: 0.75rem;
		opacity: 0;
	}

	.btn-primary {
		display: inline-block;
		padding: 0.75rem 1.5rem;
		font-weight: 500;
		font-size: 0.875rem;
		background: linear-gradient(135deg, #d4af37 0%, #c0c0c0 100%);
		color: #050505;
		border: none;
		cursor: pointer;
		text-decoration: none;
		border-radius: 0.25rem;
		transition:
			transform 0.3s ease,
			box-shadow 0.3s ease;
	}

	.btn-primary:hover {
		transform: translateY(-2px);
		box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
	}

	.btn-outline {
		display: inline-block;
		padding: 0.75rem 1.5rem;
		font-weight: 500;
		font-size: 0.875rem;
		background-color: transparent;
		color: var(--color-text);
		border: 1px solid var(--color-border);
		cursor: pointer;
		text-decoration: none;
		border-radius: 0.25rem;
		transition: all 0.3s ease;
	}

	.btn-outline:hover {
		border-color: #d4af37;
		color: #d4af37;
		background: rgba(212, 175, 55, 0.05);
		transform: translateY(-2px);
	}
</style>
