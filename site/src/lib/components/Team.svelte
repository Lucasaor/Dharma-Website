<script lang="ts">
	import { t } from '$lib/i18n';
	import { base } from '$app/paths';

	let { currentLocale }: { currentLocale: 'pt-BR' | 'en' } = $props();

	const team = [
		{
			name: 'Lucas Rodrigues',
			key: 'lucas',
			file: 'lucas.jpg',
			phd: true,
			linkedin: 'https://www.linkedin.com/in/lucasaor/'
		},
		{
			name: 'Leticia Magnino',
			key: 'leticia',
			file: 'leticia.jpg',
			phd: false,
			linkedin: 'https://www.linkedin.com/in/leticiamagninof/'
		},
		{
			name: 'Beatriz Granado',
			key: 'beatriz',
			file: 'beatriz.jpg',
			phd: true,
			linkedin: 'https://www.linkedin.com/in/beatrizgmarangoni/'
		},
		{
			name: 'Mariana Milani',
			key: 'mariana',
			file: 'mariana.jpg',
			phd: false,
			new: true,
			linkedin: 'https://www.linkedin.com/in/mariana-milanii/'
		}
	];
</script>

<section id="team" class="team">
	<div class="container">
		<h2 class="section-title reveal">{t(currentLocale, 'team.title')}</h2>
		<p class="section-subtitle reveal">{t(currentLocale, 'team.subtitle')}</p>

		<div class="team-grid">
			{#each team as member, i}
				<a
					href={member.linkedin}
					target="_blank"
					rel="noopener noreferrer"
					class="team-card reveal"
					style="transition-delay: {i * 0.1}s"
				>
					<div class="avatar">
						<img src="{base}/media/people/{member.file}" alt={member.name} loading="lazy" />
					</div>
					<h3>
						{member.name}
						{#if member.new}
							<span class="badge badge-new">{t(currentLocale, 'team.new')}</span>
						{/if}
						{#if member.phd}
							<span class="badge">{t(currentLocale, 'team.phd')}</span>
						{/if}
					</h3>
					<p class="role">{t(currentLocale, `team.${member.key}_role`)}</p>
				</a>
			{/each}
		</div>
	</div>
</section>

<style>
	.team {
		background: var(--color-bg-light);
	}

	.team-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 2rem;
		max-width: 1100px;
		margin: 0 auto;
	}

	.team-card {
		background: var(--color-bg-card);
		border: 1px solid var(--color-border);
		border-radius: 16px;
		padding: 2.5rem 2rem;
		text-align: center;
		transition: all 0.3s ease;
		cursor: pointer;
		color: var(--color-text);
	}

	.team-card:hover {
		border-color: var(--color-primary);
		transform: translateY(-5px);
		box-shadow: 0 10px 30px rgba(101, 36, 166, 0.15);
	}

	.avatar {
		width: 80px;
		height: 80px;
		border-radius: 50%;
		margin: 0 auto 1.5rem;
		overflow: hidden;
		border: 2px solid var(--color-border);
	}

	.avatar img {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.team-card h3 {
		font-size: 1.2rem;
		margin-bottom: 0.5rem;
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 0.5rem;
		flex-wrap: wrap;
	}

	.badge {
		font-size: 0.65rem;
		font-weight: 600;
		background: linear-gradient(135deg, var(--color-primary), var(--color-accent-light));
		padding: 0.2rem 0.5rem;
		border-radius: 4px;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.badge-new {
		background: linear-gradient(135deg, var(--color-accent-light), var(--color-accent));
	}

	.role {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	@media (max-width: 768px) {
		.team-grid {
			grid-template-columns: repeat(2, minmax(0, 1fr));
			max-width: 700px;
		}
	}

	@media (max-width: 480px) {
		.team-grid {
			grid-template-columns: 1fr;
			max-width: 400px;
		}
	}
</style>
