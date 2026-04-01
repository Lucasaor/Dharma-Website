<script lang="ts">
	import { t } from '$lib/i18n';
	import { base } from '$app/paths';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();

	const partners = [
		{ name: 'Closed-loop Automations', file: 'closed-loop-logo.png' },
		{ name: 'Gaia Tech', file: 'LOGO GAIATECH.png' },
		{ name: 'Bridge-port Data Solutions', file: 'bds_logo.png' }
	];
</script>

<section id="partners" class="partners">
	<div class="container">
		<h2 class="section-title reveal">{t(currentLocale, 'partners.title')}</h2>
		<p class="section-subtitle reveal">{t(currentLocale, 'partners.subtitle')}</p>

		<div class="logo-grid reveal">
			{#each partners as partner}
				<div class="logo-card">
					<img
						src="{base}/media/partners/{partner.file}"
						alt={partner.name}
						loading="lazy"
					/>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.partners {
		background: var(--color-bg);
	}

	.logo-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2rem;
		max-width: 900px;
		margin: 0 auto;
	}

	.logo-card {
		background: var(--color-bg-card);
		border: 1px solid var(--color-border);
		border-radius: 12px;
		padding: 2rem;
		display: flex;
		align-items: center;
		justify-content: center;
		transition: all 0.3s ease;
		min-height: 120px;
	}

	.logo-card:hover {
		border-color: var(--color-accent-light);
		transform: scale(1.03);
		box-shadow: 0 8px 25px rgba(4, 157, 191, 0.1);
	}

	.logo-card img {
		max-height: 60px;
		max-width: 160px;
		object-fit: contain;
		opacity: 0.85;
		transition: opacity 0.3s ease;
	}

	.logo-card:hover img {
		opacity: 1;
	}

	@media (max-width: 768px) {
		.logo-grid {
			grid-template-columns: repeat(2, 1fr);
			gap: 1rem;
		}
	}

	@media (max-width: 480px) {
		.logo-grid {
			grid-template-columns: 1fr;
		}
	}
</style>
