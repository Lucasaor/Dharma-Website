<script lang="ts">
	import { t } from '$lib/i18n';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();

	const services = [
		{ key: 's1', icon: '🤖' },
		{ key: 's2', icon: '🔄' },
		{ key: 's3', icon: '🔒' },
		{ key: 's4', icon: '🧠' },
		{ key: 's5', icon: '⚙️' },
		{ key: 's6', icon: '📊' },
		{ key: 's7', icon: '🎯' },
		{ key: 's8', icon: '🌱' }
	];
</script>

<section id="services" class="services">
	<div class="container">
		<h2 class="section-title reveal">{t(currentLocale, 'services.title')}</h2>
		<p class="section-subtitle reveal">{t(currentLocale, 'services.subtitle')}</p>

		<div class="services-grid">
			{#each services as { key, icon }, i}
				<div class="service-card reveal" style="transition-delay: {i * 0.05}s">
					<span class="service-icon">{icon}</span>
					<h3>{t(currentLocale, `services.${key}_title`)}</h3>
					<p>{t(currentLocale, `services.${key}_desc`)}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.services {
		background: var(--color-bg-light);
	}

	.services-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 1.5rem;
	}

	.service-card {
		background: var(--color-bg-card);
		border: 1px solid var(--color-border);
		border-radius: 12px;
		padding: 2rem 1.5rem;
		transition: all 0.3s ease;
		position: relative;
		overflow: hidden;
	}

	.service-card::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		height: 3px;
		background: linear-gradient(90deg, var(--color-primary), var(--color-accent-light));
		transform: scaleX(0);
		transform-origin: left;
		transition: transform 0.3s ease;
	}

	.service-card:hover::before {
		transform: scaleX(1);
	}

	.service-card:hover {
		border-color: var(--color-primary);
		transform: translateY(-5px);
		box-shadow: 0 10px 30px rgba(101, 36, 166, 0.15);
	}

	.service-icon {
		font-size: 2rem;
		display: block;
		margin-bottom: 1rem;
	}

	.service-card h3 {
		font-size: 1.1rem;
		margin-bottom: 0.75rem;
		color: var(--color-text);
	}

	.service-card p {
		font-size: 0.9rem;
		color: var(--color-text-muted);
		line-height: 1.6;
	}

	@media (max-width: 1024px) {
		.services-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 480px) {
		.services-grid {
			grid-template-columns: 1fr;
		}
	}
</style>
