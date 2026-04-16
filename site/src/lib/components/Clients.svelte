<script lang="ts">
	import { t } from '$lib/i18n';
	import { base } from '$app/paths';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();

	const clients = [
		{ name: 'Thingz Inc.', file: 'thingz-logo.png', url: 'https://thingz.ai' },
		{ name: 'Diageo', file: 'Diageo-Logo.wine.png', url: 'https://www.diageo.com/' },
		{ name: 'Unilever', file: 'Unilever-Logo.png', url: 'https://www.unilever.com/' },
		{ name: 'Wesco', file: 'wesco-brandpreferred.png', url: 'https://www.wesco.com/us/en.html' },
		{ name: 'Kraft-Heinz', file: 'heinz logo.png', url: 'https://www.kraftheinz.com/' },
		{ name: 'Quimica Estrela', file: 'Estrela_600x600.png', url: 'https://quimicaestrela.com.br/' },
		{ name: 'Namastex', file: 'nmstxvectorwhite.svg', url: 'https://namastex.ai/' },
		{ name: 'CSM Media', url: 'https://www.instagram.com/csm.digital/' }
	];
</script>

<section id="clients" class="clients">
	<div class="container">
		<h2 class="section-title reveal">{t(currentLocale, 'clients.title')}</h2>
		<p class="section-subtitle reveal">{t(currentLocale, 'clients.subtitle')}</p>

		<div class="logo-grid reveal">
			{#each clients as client}
				<a href={client.url} target="_blank" rel="noopener noreferrer" class="logo-card">
					{#if client.file}
						<img
							src="{base}/media/clients/{client.file}"
							alt={client.name}
							loading="lazy"
						/>
					{:else}
						<span class="logo-fallback">{client.name}</span>
					{/if}
				</a>
			{/each}
		</div>
	</div>
</section>

<style>
	.clients {
		background: var(--color-bg-light);
	}

	.logo-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 2rem;
		max-width: 1100px;
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
		cursor: pointer;
	}

	.logo-card:hover {
		border-color: var(--color-primary);
		transform: scale(1.03);
		box-shadow: 0 8px 25px rgba(101, 36, 166, 0.1);
	}

	.logo-card img {
		max-height: 60px;
		max-width: 160px;
		object-fit: contain;
		opacity: 0.85;
		transition: opacity 0.3s ease;
	}

	.logo-fallback {
		font-size: 1rem;
		font-weight: 600;
		text-align: center;
		color: var(--color-text);
	}

	.logo-card:hover img {
		opacity: 1;
	}

	@media (max-width: 768px) {
		.logo-grid {
			grid-template-columns: repeat(2, minmax(0, 1fr));
			gap: 1rem;
		}
	}

	@media (max-width: 480px) {
		.logo-grid {
			grid-template-columns: 1fr;
		}
	}
</style>
