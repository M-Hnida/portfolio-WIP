<script lang="ts">
	import { onMount } from "svelte";

	let isScrolled = false;
	let isMobileMenuOpen = false;

	onMount(() => {
		const handleScroll = () => {
			isScrolled = window.scrollY > 3;
		};
		window.addEventListener("scroll", handleScroll);
		return () => window.removeEventListener("scroll", handleScroll);
	});

	const navLinks = [
		{ href: "/#about", label: "À propos" },
		{ href: "/#projects", label: "Projets" },
		{ href: "/#skills", label: "Compétences" },
		{ href: "/veille", label: "Veille", isExternal: true },
	];

	function scrollToSection(href: string, isExternal?: boolean) {
		isMobileMenuOpen = false;
		if (isExternal) {
			window.location.href = href;
			return;
		}

		const isHome = window.location.pathname === "/";
		if (!isHome) {
			window.location.href = href;
			return;
		}

		const elementId = href.replace("/", "");
		const element = document.querySelector(elementId);
		if (element) {
			element.scrollIntoView({ behavior: "smooth" });
		}
	}
</script>

<nav class:scrolled={isScrolled}>
	<div class="container">
		<!-- Desktop Navigation -->
		<div class="desktop-nav">
			{#each navLinks as link}
				<button
					on:click={() => scrollToSection(link.href, link.isExternal)}
					class="nav-link"
				>
					{link.label}
				</button>
			{/each}
			<button
				on:click={() => scrollToSection("/#contact")}
				class="btn-contact"
			>
				Contact
			</button>
		</div>

		<!-- Mobile Menu Button -->
		<button
			class="mobile-menu-btn"
			on:click={() => (isMobileMenuOpen = !isMobileMenuOpen)}
			aria-label="Toggle menu"
		>
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
				{#if isMobileMenuOpen}
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="1.5"
						d="M6 18L18 6M6 6l12 12"
					/>
				{:else}
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="1.5"
						d="M4 6h16M4 12h16M4 18h16"
					/>
				{/if}
			</svg>
		</button>
	</div>

	<!-- Mobile Menu -->
	{#if isMobileMenuOpen}
		<div class="mobile-menu">
			<div class="mobile-menu-content">
				{#each navLinks as link}
					<button
						on:click={() =>
							scrollToSection(link.href, link.isExternal)}
						class="mobile-nav-link"
					>
						{link.label}
					</button>
				{/each}
			</div>
		</div>
	{/if}
</nav>

<style>
	nav {
		position: sticky;
		top: 0;
		left: 0;
		right: 0;
		z-index: 50;
		transition: all 0.4s ease;
		padding: 1.5rem 0;
		background: transparent;
	}

	nav.scrolled {
		padding: 1rem 0;
		background: rgba(5, 5, 5, 0.9);
		backdrop-filter: blur(1rem);
	}

	.container {
		width: 100%;
		max-width: 80rem;
		margin: 0 auto;
		padding: 0 1.5rem;
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 2.5rem;
	}

	.desktop-nav {
		display: none;
		align-items: center;
		gap: 2.5rem;
	}

	@media (min-width: 768px) {
		.desktop-nav {
			display: flex;
		}
	}

	.nav-link {
		font-family: var(--font-heading);
		font-size: 0.875rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--color-text-muted);
		background: none;
		border: none;
		cursor: pointer;
		transition: color 0.3s ease;
		position: relative;
	}

	.nav-link::after {
		content: "";
		position: absolute;
		bottom: -0.25rem;
		left: 0;
		width: 0;
		height: 1px;
		background: var(--color-primary);
		transition: width 0.3s ease;
	}

	.nav-link:hover {
		color: var(--color-primary);
	}

	.nav-link:hover::after {
		width: 100%;
	}

	.mobile-menu-btn {
		display: flex;
		position: absolute;
		left: 10%;
		color: var(--color-text);
		background: none;
		border: none;
		cursor: pointer;
		padding: 0.5rem;
	}

	.mobile-menu-btn svg {
		width: 1.5rem;
		height: 1.5rem;
	}

	@media (min-width: 768px) {
		.mobile-menu-btn {
			display: none;
		}
	}

	.mobile-menu {
		position: absolute;
		top: 100%;
		left: 0;
		right: 0;
		background: rgba(5, 5, 5, 0.98);
		backdrop-filter: blur(1rem);
	}

	.mobile-menu-content {
		width: 100%;
		max-width: 80rem;
		margin: 0 auto;
		padding: 2rem 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
	}

	.mobile-nav-link {
		font-family: var(--font-heading);
		font-size: 1.125rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--color-text-muted);
		background: none;
		border: none;
		cursor: pointer;
		text-align: left;
		padding: 0.5rem 0;
		transition: color 0.3s ease;
	}

	.mobile-nav-link:hover {
		color: var(--color-primary);
	}

	.btn-contact {
		display: inline-block;
		padding: 0.75rem 1.5rem;
		font-weight: 500;
		font-size: 0.875rem;
		letter-spacing: 0.15em;
		transition: all 0.3s ease;
		background: linear-gradient(135deg, #d4af37 0%, #c0c0c0 100%);
		color: #050505;
		border: none;
		cursor: pointer;
		border-radius: 0.5cap;
		font-family: var(--font-heading);
	}

	.btn-contact:hover {
		box-shadow: 0 0 1.5rem rgba(212, 175, 55, 0.4);
		transform: translateY(-2px);
	}
</style>
