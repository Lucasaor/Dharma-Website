<script lang="ts">
	import { locale, t } from '$lib/i18n';
	import { base } from '$app/paths';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();

	let scrolled = $state(false);
	let mobileOpen = $state(false);

	function handleScroll() {
		scrolled = window.scrollY > 50;
	}

	function closeMobile() {
		mobileOpen = false;
	}

	const navLinks = ['about', 'services', 'results', 'clients', 'team', 'contact'] as const;
</script>

<svelte:window onscroll={handleScroll} />

<nav class="navbar" class:scrolled>
	<div class="nav-container">
		<a href="#hero" class="nav-logo" onclick={closeMobile}>
			<img src="{base}/media/dharma_logos/dharma_datatech_light.png" alt="Dharma Datatech" />
		</a>

		<div class="nav-links" class:open={mobileOpen}>
			{#each navLinks as link}
				<a href="#{link}" class="nav-link" onclick={closeMobile}>
					{t(currentLocale, `nav.${link}`)}
				</a>
			{/each}
			<button class="lang-toggle" onclick={() => locale.toggle()}>
				{currentLocale === 'pt-BR' ? 'EN' : 'PT'}
			</button>
		</div>

		<button
			class="hamburger"
			class:active={mobileOpen}
			onclick={() => (mobileOpen = !mobileOpen)}
			aria-label="Toggle menu"
		>
			<span></span>
			<span></span>
			<span></span>
		</button>
	</div>
</nav>

{#if mobileOpen}
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="overlay" onclick={closeMobile} onkeydown={() => {}}></div>
{/if}

<style>
	.navbar {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 1000;
		padding: 1rem 1.5rem;
		transition: background-color 0.3s ease, padding 0.3s ease, backdrop-filter 0.3s ease;
	}

	.navbar.scrolled {
		background-color: rgba(13, 13, 13, 0.95);
		backdrop-filter: blur(10px);
		padding: 0.5rem 1.5rem;
		box-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
	}

	.nav-container {
		max-width: var(--max-width);
		margin: 0 auto;
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.nav-logo img {
		height: 40px;
		width: auto;
		transition: height 0.3s ease;
	}

	.navbar.scrolled .nav-logo img {
		height: 32px;
	}

	.nav-links {
		display: flex;
		align-items: center;
		gap: 2rem;
	}

	.nav-link {
		color: var(--color-text);
		font-size: 0.9rem;
		font-weight: 500;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		position: relative;
		transition: color var(--transition);
	}

	.nav-link::after {
		content: '';
		position: absolute;
		bottom: -4px;
		left: 0;
		width: 0;
		height: 2px;
		background: linear-gradient(90deg, var(--color-primary), var(--color-accent-light));
		transition: width var(--transition);
	}

	.nav-link:hover {
		color: var(--color-accent-light);
	}

	.nav-link:hover::after {
		width: 100%;
	}

	.lang-toggle {
		background: transparent;
		border: 1px solid var(--color-primary);
		color: var(--color-text);
		padding: 0.35rem 0.75rem;
		border-radius: 4px;
		font-size: 0.8rem;
		font-weight: 600;
		cursor: pointer;
		transition: all var(--transition);
		font-family: var(--font-body);
		letter-spacing: 0.05em;
	}

	.lang-toggle:hover {
		background: var(--color-primary);
		color: white;
	}

	.hamburger {
		display: none;
		flex-direction: column;
		gap: 5px;
		background: none;
		border: none;
		cursor: pointer;
		padding: 4px;
		z-index: 1001;
	}

	.hamburger span {
		display: block;
		width: 24px;
		height: 2px;
		background: var(--color-text);
		transition: all 0.3s ease;
	}

	.hamburger.active span:nth-child(1) {
		transform: rotate(45deg) translate(5px, 5px);
	}

	.hamburger.active span:nth-child(2) {
		opacity: 0;
	}

	.hamburger.active span:nth-child(3) {
		transform: rotate(-45deg) translate(5px, -5px);
	}

	.overlay {
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.5);
		z-index: 998;
	}

	@media (max-width: 768px) {
		.hamburger {
			display: flex;
		}

		.nav-links {
			position: fixed;
			top: 0;
			right: -100%;
			width: 280px;
			height: 100vh;
			background: var(--color-bg);
			flex-direction: column;
			padding: 5rem 2rem 2rem;
			gap: 1.5rem;
			transition: right 0.3s ease;
			z-index: 999;
			box-shadow: -5px 0 20px rgba(0, 0, 0, 0.3);
		}

		.nav-links.open {
			right: 0;
		}
	}
</style>
