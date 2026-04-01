<script lang="ts">
	import { t } from '$lib/i18n';
	import { base } from '$app/paths';
	import { onMount } from 'svelte';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();
	let videoEl: HTMLVideoElement;

	onMount(() => {
		if (videoEl) {
			videoEl.play().catch(() => {});
		}
	});
</script>

<section id="hero" class="hero">
	<div class="hero-video-wrapper">
		<video
			bind:this={videoEl}
			autoplay
			muted
			loop
			playsinline
			poster="{base}/media/dharma_logos/dharma_logo_branca.png"
		>
			<source src="{base}/media/background_videos/13814794_1920_1080_100fps.mp4" type="video/mp4" />
		</video>
		<div class="hero-overlay"></div>
	</div>

	<div class="hero-content">
		<img
			src="{base}/media/dharma_logos/dharma_logo_branca.png"
			alt="Dharma Datatech"
			class="hero-logo"
		/>
		<h1 class="hero-tagline">{t(currentLocale, 'hero.tagline')}</h1>
		<p class="hero-subtitle">{t(currentLocale, 'hero.subtitle')}</p>
		<a href="#services" class="hero-cta">
			{t(currentLocale, 'hero.cta')}
			<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<path d="M7 13l5 5 5-5M7 6l5 5 5-5" />
			</svg>
		</a>
	</div>

	<div class="scroll-indicator">
		<div class="scroll-mouse">
			<div class="scroll-wheel"></div>
		</div>
	</div>
</section>

<style>
	.hero {
		position: relative;
		height: 100vh;
		min-height: 600px;
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;
	}

	.hero-video-wrapper {
		position: absolute;
		inset: 0;
		z-index: 0;
	}

	.hero-video-wrapper video {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.hero-overlay {
		position: absolute;
		inset: 0;
		background: linear-gradient(
			180deg,
			rgba(13, 13, 13, 0.7) 0%,
			rgba(13, 13, 13, 0.5) 50%,
			rgba(13, 13, 13, 0.9) 100%
		);
	}

	.hero-content {
		position: relative;
		z-index: 1;
		text-align: center;
		padding: 0 1.5rem;
		max-width: 800px;
	}

	.hero-logo {
		width: 200px;
		margin: 0 auto 2rem;
		filter: drop-shadow(0 4px 20px rgba(101, 36, 166, 0.3));
	}

	.hero-tagline {
		font-size: 3rem;
		font-weight: 700;
		margin-bottom: 1rem;
		background: linear-gradient(135deg, #fff 0%, var(--color-accent-light) 100%);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}

	.hero-subtitle {
		font-size: 1.2rem;
		color: var(--color-text-muted);
		margin-bottom: 2.5rem;
		line-height: 1.7;
	}

	.hero-cta {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
		color: white;
		padding: 0.9rem 2rem;
		border-radius: 8px;
		font-weight: 600;
		font-size: 1rem;
		transition: all 0.3s ease;
		box-shadow: 0 4px 15px rgba(101, 36, 166, 0.3);
	}

	.hero-cta:hover {
		transform: translateY(-2px);
		box-shadow: 0 8px 25px rgba(101, 36, 166, 0.4);
		color: white;
	}

	.scroll-indicator {
		position: absolute;
		bottom: 2rem;
		left: 50%;
		transform: translateX(-50%);
		z-index: 1;
	}

	.scroll-mouse {
		width: 26px;
		height: 40px;
		border: 2px solid rgba(255, 255, 255, 0.3);
		border-radius: 13px;
		display: flex;
		justify-content: center;
		padding-top: 8px;
	}

	.scroll-wheel {
		width: 3px;
		height: 8px;
		background: var(--color-accent-light);
		border-radius: 2px;
		animation: scroll 1.5s ease-in-out infinite;
	}

	@keyframes scroll {
		0% { opacity: 1; transform: translateY(0); }
		100% { opacity: 0; transform: translateY(12px); }
	}

	@media (max-width: 768px) {
		.hero-tagline {
			font-size: 2rem;
		}
		.hero-subtitle {
			font-size: 1rem;
		}
		.hero-logo {
			width: 150px;
		}
	}

	@media (max-width: 480px) {
		.hero-tagline {
			font-size: 1.6rem;
		}
	}
</style>
