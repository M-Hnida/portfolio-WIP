<script lang="ts">
	import { onMount } from "svelte";
	import { User, Briefcase, Zap, Globe, Mail, Menu, X, Link, Code2 } from "@lucide/svelte";

	let isMobileMenuOpen = false;

	const navLinks = [
		{ href: "/#about", label: "À propos", icon: User },
		{ href: "/#projects", label: "Projets", icon: Briefcase },
		{ href: "/#skills", label: "Compétences", icon: Zap },
		{ href: "/veille", label: "Veille", icon: Globe, isExternal: true },
		{ href: "/mediatek86", label: "MediaTek86", icon: Code2, isExternal: true },
		{ href: "/#contact", label: "Contact", icon: Mail }
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

<!-- Mobile Top Header -->
<header class="mobile-header">
	<span class="logo">Mohammed Hnida</span>
	<button
		class="mobile-menu-btn"
		on:click={() => (isMobileMenuOpen = !isMobileMenuOpen)}
		aria-label="Toggle menu"
	>
		{#if isMobileMenuOpen}
			<X size={24} />
		{:else}
			<Menu size={24} />
		{/if}
	</button>
</header>

<!-- Mobile Sidebar Backdrop Drawer Overlay -->
{#if isMobileMenuOpen}
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div class="mobile-overlay" on:click={() => (isMobileMenuOpen = false)}></div>
{/if}

<!-- Sidebar Container -->
<aside class="sidebar-aside" class:open={isMobileMenuOpen}>
	<div class="sidebar-header">
		<div class="avatar-container">
			<img src="/photo.png" alt="Mohammed Hnida" class="avatar" />
		</div>
		<h2 class="name">Mohammed Hnida</h2>
		<span class="title">Étudiant en informatique</span>
		<span class="subtitle-option">Option SLAM</span>
	</div>

	<nav class="sidebar-nav">
		<div class="nav-section-title">Navigation</div>
		{#each navLinks as link}
			<button
				on:click={() => scrollToSection(link.href, link.isExternal)}
				class="nav-link-btn"
			>
				<span class="icon">
					<svelte:component this={link.icon} size={18} />
				</span>
				<span class="label">{link.label}</span>
			</button>
		{/each}
	</nav>

	<div class="sidebar-divider"></div>

	<div class="sidebar-socials">
		<div class="nav-section-title">Liens utiles</div>
		<a
			href="https://www.linkedin.com/in/mohammed-h-161110360/"
			target="_blank"
			rel="noopener noreferrer"
			class="social-link"
		>
			<span class="icon">
				<Link size={18} />
			</span>
			<span>LinkedIn</span>
		</a>
		<a
			href="https://github.com/M-Hnida"
			target="_blank"
			rel="noopener noreferrer"
			class="social-link"
		>
			<span class="icon">
				<Code2 size={18} />
			</span>
			<span>GitHub</span>
		</a>
	</div>
</aside>

<style>
	/* Desktop and General Sidebar styling */
	.sidebar-aside {
		position: fixed;
		top: 0;
		left: 0;
		bottom: 0;
		width: 280px;
		background: rgba(10, 10, 10, 0.65);
		backdrop-filter: blur(20px);
		-webkit-backdrop-filter: blur(20px);
		border-right: 1px solid var(--color-border);
		padding: 2.5rem 1.75rem;
		display: flex;
		flex-direction: column;
		z-index: 100;
		transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
		overflow-y: auto;
	}
	
	.sidebar-header {
		text-align: center;
		margin-bottom: 2rem;
	}

	.avatar-container {
		width: 90px;
		height: 90px;
		border-radius: 50%;
		overflow: hidden;
		margin: 0 auto 1.25rem;
		border: 2px solid var(--color-primary);
		box-shadow: 0 0 15px rgba(212, 168, 83, 0.25);
	}

	.avatar {
		width: 100%;
		height: 100%;
		object-fit: cover;
		scale: 1.15;
	}

	.name {
		font-family: var(--font-heading);
		font-size: 1.25rem;
		font-weight: 600;
		color: #ffffff;
		margin-bottom: 0.25rem;
	}

	.title {
		display: block;
		font-size: 0.8rem;
		color: var(--color-text-muted);
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.subtitle-option {
		display: block;
		font-size: 0.75rem;
		color: var(--color-primary);
		font-weight: 500;
		margin-top: 0.25rem;
	}

	.nav-section-title {
		font-size: 0.7rem;
		text-transform: uppercase;
		letter-spacing: 0.15em;
		color: var(--color-text-subtle);
		margin-bottom: 0.75rem;
		font-weight: 600;
	}

	.sidebar-nav {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		margin-bottom: 2rem;
	}

	.nav-link-btn {
		display: flex;
		align-items: center;
		gap: 1rem;
		width: 100%;
		padding: 0.65rem 1rem;
		background: none;
		border: none;
		border-radius: 0.5rem;
		color: var(--color-text-muted);
		cursor: pointer;
		text-align: left;
		font-size: 0.95rem;
		transition: all 0.2s ease;
	}

	.nav-link-btn:hover {
		background: rgba(255, 255, 255, 0.03);
		color: var(--color-primary);
		transform: translateX(3px);
	}

	.nav-link-btn .icon {
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--color-text-muted);
	}

	.nav-link-btn:hover .icon {
		color: var(--color-primary);
	}

	.sidebar-divider {
		height: 1px;
		background: var(--color-border);
		margin: 0 0 2rem;
	}

	.sidebar-socials {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		margin-bottom: 2rem;
	}

	.social-link {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 0.65rem 1rem;
		border-radius: 0.5rem;
		color: var(--color-text-muted);
		text-decoration: none;
		font-size: 0.95rem;
		transition: all 0.2s ease;
	}

	.social-link:hover {
		background: rgba(255, 255, 255, 0.03);
		color: var(--color-primary);
		transform: translateX(3px);
	}

	.social-link .icon {
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--color-text-muted);
	}

	.social-link:hover .icon {
		color: var(--color-primary);
	}

	/* Mobile styles */
	.mobile-header {
		display: none;
	}

	@media (max-width: 1023px) {
		.mobile-header {
			display: flex;
			position: fixed;
			top: 0;
			left: 0;
			right: 0;
			height: 60px;
			background: rgba(10, 10, 10, 0.85);
			backdrop-filter: blur(10px);
			-webkit-backdrop-filter: blur(10px);
			border-bottom: 1px solid var(--color-border);
			align-items: center;
			justify-content: space-between;
			padding: 0 1.5rem;
			z-index: 90;
		}

		.logo {
			font-family: var(--font-heading);
			font-size: 1.1rem;
			font-weight: 600;
			color: #ffffff;
		}

		.mobile-menu-btn {
			display: flex;
			background: none;
			border: none;
			color: var(--color-text);
			cursor: pointer;
			padding: 0.25rem;
		}

		.mobile-menu-btn :global(svg) {
			width: 1.5rem;
			height: 1.5rem;
		}

		.sidebar-aside {
			transform: translateX(-100%);
			z-index: 120;
			background: rgba(5, 5, 5, 0.98);
			box-shadow: 10px 0 30px rgba(0, 0, 0, 0.8);
		}

		.sidebar-aside.open {
			transform: translateX(0);
		}

		.mobile-overlay {
			position: fixed;
			inset: 0;
			background: rgba(0, 0, 0, 0.7);
			z-index: 110;
		}
	}
</style>
