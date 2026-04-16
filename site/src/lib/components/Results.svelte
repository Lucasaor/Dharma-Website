<script lang="ts">
	import { t } from '$lib/i18n';
	import { onMount } from 'svelte';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();

	const stats = [
		{ value: 18, key: 'usa_canada' },
		{ value: 20, key: 'brazil' },
		{ value: 10, key: 'global' }
	];

	const results = ['r1', 'r2', 'r3', 'r4', 'r5'];

	let counterValues = $state<number[]>([0, 0, 0]);
	let statsSection: HTMLElement;
	let animated = false;

	onMount(() => {
		const observer = new IntersectionObserver(
			(entries) => {
				if (entries[0].isIntersecting && !animated) {
					animated = true;
					animateCounters();
				}
			},
			{ threshold: 0.3 }
		);

		if (statsSection) {
			observer.observe(statsSection);
		}

		return () => observer.disconnect();
	});

	function animateCounters() {
		const duration = 1500;
		const start = performance.now();
		function tick(now: number) {
			const progress = Math.min((now - start) / duration, 1);
			const eased = 1 - Math.pow(1 - progress, 3);
			counterValues = stats.map((s) => Math.round(s.value * eased));
			if (progress < 1) requestAnimationFrame(tick);
		}
		requestAnimationFrame(tick);
	}
</script>

<section id="results" class="results">
	<div class="container">
		<h2 class="section-title reveal">{t(currentLocale, 'results.title')}</h2>
		<p class="section-subtitle reveal">{t(currentLocale, 'results.subtitle')}</p>

		<div class="stats-row reveal" bind:this={statsSection}>
			{#each stats as stat, i}
				<div class="stat-card">
					<span class="stat-value">{counterValues[i]}</span>
					<span class="stat-label">{t(currentLocale, `stats.${stat.key}`)}</span>
				</div>
			{/each}
		</div>

		<div class="results-list">
			{#each results as key, i}
				<div class="result-item reveal" style="transition-delay: {i * 0.1}s">
					<div class="result-icon">
						<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
							<polyline points="20 6 9 17 4 12" />
						</svg>
					</div>
					<p>{t(currentLocale, `results.${key}`)}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.results {
		background: var(--color-bg);
	}

	.stats-row {
		display: flex;
		justify-content: center;
		gap: 3rem;
		margin-bottom: 4rem;
	}

	.stat-card {
		text-align: center;
		padding: 2rem;
		background: var(--color-bg-card);
		border: 1px solid var(--color-border);
		border-radius: 12px;
		min-width: 180px;
		transition: all 0.3s ease;
	}

	.stat-card:hover {
		border-color: var(--color-primary);
		transform: translateY(-5px);
		box-shadow: 0 10px 30px rgba(101, 36, 166, 0.15);
	}

	.stat-value {
		display: block;
		font-family: var(--font-heading);
		font-size: 3rem;
		font-weight: 700;
		background: linear-gradient(135deg, var(--color-primary), var(--color-accent-light));
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}

	.stat-label {
		display: block;
		margin-top: 0.5rem;
		color: var(--color-text-muted);
		font-size: 0.95rem;
	}

	.results-list {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		max-width: 900px;
		margin: 0 auto;
	}

	.result-item {
		display: flex;
		align-items: flex-start;
		gap: 1rem;
		padding: 1.25rem 1.5rem;
		background: var(--color-bg-card);
		border: 1px solid var(--color-border);
		border-radius: 10px;
		transition: all 0.3s ease;
	}

	.result-item:hover {
		border-color: var(--color-accent-light);
	}

	.result-icon {
		flex-shrink: 0;
		width: 36px;
		height: 36px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
		border-radius: 50%;
		color: white;
	}

	.result-icon svg {
		width: 18px;
		height: 18px;
	}

	.result-item p {
		color: var(--color-text-muted);
		line-height: 1.6;
		font-size: 1rem;
	}

	@media (max-width: 768px) {
		.stats-row {
			flex-direction: column;
			align-items: center;
			gap: 1rem;
		}

		.stat-card {
			min-width: unset;
			width: 100%;
			max-width: 300px;
		}
	}
</style>
