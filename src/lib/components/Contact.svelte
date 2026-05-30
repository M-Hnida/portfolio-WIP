<script lang="ts">
	import { MapPin, Mail, Link, Code2 } from "@lucide/svelte";

	let message = "";

	function handleSubmit(e: Event) {
		e.preventDefault();

		// Création du lien mailto avec les informations pré-remplies
		const subject = encodeURIComponent("Contact depuis le Portfolio");
		const body = encodeURIComponent(`Message:\n${message}`);

		// Ouvre le client mail par défaut de l'utilisateur
		window.location.href = `mailto:simowgoat@gmail.com?subject=${subject}&body=${body}`;
	}
</script>

<section id="contact" class="section-card">
	<div class="contact-header">
		<h2 class="section-title">Me Contacter</h2>
		<p class="subtitle">
			Disponible pour échanger autour d'un projet, d'un stage ou d'une
			opportunité en développement backend, applications desktop, data
			science ou machine learning.
		</p>
	</div>

		<div class="contact-content">
			<div class="info-card">
				<h3>Informations</h3>
				<ul class="info-list">
					<li>
						<span class="icon"><MapPin size={18} /></span>
						<span>Miramas, France</span>
					</li>
					<li>
						<span class="icon"><Mail size={18} /></span>
						<a href="mailto:simowgoat@gmail.com"
							>simowgoat@gmail.com</a
						>
					</li>
					<li>
						<span class="icon"><Link size={18} /></span>
						<a
							href="https://www.linkedin.com/in/mohammed-h-161110360/"
							target="_blank"
							rel="noopener noreferrer">LinkedIn</a
						>
					</li>
					<li>
						<span class="icon"><Code2 size={18} /></span>
						<a
							href="https://github.com/M-Hnida"
							target="_blank"
							rel="noopener noreferrer">GitHub</a
						>
					</li>
				</ul>
			</div>

			<div class="form-card">
				<form on:submit={handleSubmit} class="contact-form">
					<div class="form-group">
						<label for="message">Message</label>
						<textarea
							id="message"
							bind:value={message}
							required
							rows="4"
							placeholder="Votre message..."
						></textarea>
					</div>

					<button type="submit" class="submit-btn">
						Ouvrir mon application Mail
					</button>
				</form>
			</div>
		</div>
</section>

<style>
	.contact-header {
		margin-bottom: 2rem;
	}

	.section-title {
		font-family: var(--font-heading);
		font-size: 1.75rem;
		color: var(--color-text);
		margin-bottom: 0.5rem;
		font-weight: 600;
	}

	.subtitle {
		color: var(--color-text-muted);
		font-size: 0.95rem;
		line-height: 1.6;
	}

	.contact-content {
		display: grid;
		grid-template-columns: 1fr;
		gap: 1.5rem;
	}

	@media (min-width: 768px) {
		.contact-content {
			grid-template-columns: minmax(260px, 0.9fr) minmax(0, 1.5fr);
		}
	}

	.info-card {
		background: rgba(255, 255, 255, 0.02);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		padding: 1.5rem;
		height: fit-content;
	}

	.info-card h3 {
		font-family: var(--font-heading);
		font-size: 1.25rem;
		color: #c0c0c0;
		margin-bottom: 1rem;
	}

	.info-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.info-list li {
		display: flex;
		align-items: center;
		gap: 1rem;
		color: var(--color-text-muted);
	}

	.icon {
		display: inline-flex;
		align-items: center;
		color: var(--color-primary);
	}

	.info-list a {
		color: var(--color-text);
		text-decoration: none;
		transition: color 0.2s ease;
	}

	.info-list a:hover {
		color: #c0c0c0;
	}

	.form-card {
		background: rgba(255, 255, 255, 0.02);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		padding: 1.5rem;
	}

	.form-group {
		margin-bottom: 1rem;
	}

	label {
		display: block;
		font-size: 0.875rem;
		color: var(--color-text-subtle);
		margin-bottom: 0.5rem;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	textarea {
		width: 100%;
		background: rgba(0, 0, 0, 0.2);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-sm);
		padding: 1rem;
		color: var(--color-text);
		font-family: inherit;
		transition:
			border-color 0.2s ease,
			box-shadow 0.2s ease;
	}

	textarea:focus {
		outline: none;
		border-color: #c0c0c0;
		box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.1);
	}

	textarea {
		resize: vertical;
		min-height: 120px;
	}

	.submit-btn {
		width: 100%;
		padding: 0.875rem 1rem;
		font-weight: 600;
		font-size: 1rem;
		background: var(--color-primary);
		color: #050505;
		border: none;
		border-radius: var(--radius-sm);
		cursor: pointer;
		transition:
			opacity 0.2s ease,
			transform 0.2s ease;
	}

	.submit-btn:hover:not(:disabled) {
		opacity: 0.9;
		transform: translateY(-2px);
	}

	.submit-btn:disabled {
		opacity: 0.7;
		cursor: not-allowed;
	}
</style>
