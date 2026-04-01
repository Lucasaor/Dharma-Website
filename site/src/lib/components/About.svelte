<script lang="ts">
	import { t } from '$lib/i18n';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();

	const highlights = [
		{ key: 'highlight_years', icon: '📅' },
		{ key: 'highlight_countries', icon: '🌎' },
		{ key: 'highlight_phd', icon: '🎓' }
	];
</script>

<section id="about" class="about">
	<div class="container">
		<h2 class="section-title reveal">{t(currentLocale, 'about.title')}</h2>
		<p class="section-subtitle reveal">{t(currentLocale, 'about.subtitle')}</p>

		<div class="about-grid">
			<div class="about-text reveal">
				<p>{t(currentLocale, 'about.p1')}</p>
				<p>{t(currentLocale, 'about.p2')}</p>
			</div>

			<div class="about-highlights reveal">
				{#each highlights as { key, icon }}
					<div class="highlight-card">
						<span class="highlight-icon">{icon}</span>
						<span class="highlight-value">{t(currentLocale, `about.${key}`)}</span>
						<span class="highlight-label">{t(currentLocale, `about.${key}_label`)}</span>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<style>
	.about {
		background: var(--color-bg);
	}

	.about-grid {
		display: grid;
		grid-template-columns: 1.5fr 1fr;
		gap: 4rem;
		align-items: start;
	}

	.about-text p {
		margin-bottom: 1.25rem;
		color: var(--color-text-muted);
		font-size: 1.05rem;
		line-height: 1.8;
	}

	.about-highlights {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
	}

	.highlight-card {
		background: var(--color-bg-card);
		border: 1px solid var(--color-border);
		border-radius: 12px;
		padding: 1.5rem;
		display: flex;
		align-items: center;
		gap: 1rem;
		transition: all 0.3s ease;
	}

	.highlight-card:hover {
		border-color: var(--color-primary);
		transform: translateX(5px);
	}

	.highlight-icon {
		font-size: 1.5rem;
	}

	.highlight-value {
		font-family: var(--font-heading);
		font-size: 1.8rem;
		font-weight: 700;
		background: linear-gradient(135deg, var(--color-primary), var(--color-accent-light));
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}

	.highlight-label {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	@media (max-width: 768px) {
		.about-grid {
			grid-template-columns: 1fr;
			gap: 2rem;
		}

		.about-highlights {
			flex-direction: row;
			flex-wrap: wrap;
		}

		.highlight-card {
			flex: 1 1 calc(50% - 0.75rem);
			min-width: 150px;
		}
	}

	@media (max-width: 480px) {
		.highlight-card {
			flex: 1 1 100%;
			flex-direction: column;
			text-align: center;
		}
	}
</style>
