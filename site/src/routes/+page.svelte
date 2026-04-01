<script lang="ts">
	import { locale, t } from '$lib/i18n';
	import Hero from '$lib/components/Hero.svelte';
	import About from '$lib/components/About.svelte';
	import Services from '$lib/components/Services.svelte';
	import Results from '$lib/components/Results.svelte';
	import Clients from '$lib/components/Clients.svelte';
	import Partners from '$lib/components/Partners.svelte';
	import Team from '$lib/components/Team.svelte';
	import Contact from '$lib/components/Contact.svelte';
	import { onMount } from 'svelte';

	let currentLocale = $state<'pt-BR' | 'en'>('pt-BR');

	onMount(() => {
		const unsub = locale.subscribe((val) => {
			currentLocale = val;
		});

		// Scroll reveal observer
		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						entry.target.classList.add('visible');
					}
				});
			},
			{ threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
		);

		document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

		return () => {
			unsub();
			observer.disconnect();
		};
	});
</script>

<svelte:head>
	<title>Dharma Datatech — AI & Analytics para Indústria</title>
	<meta name="description" content="Dharma Datatech — Soluções avançadas de Machine Learning, AI e DataOps para a indústria de bens de consumo." />
</svelte:head>

<main>
	<Hero {currentLocale} />
	<About {currentLocale} />
	<Services {currentLocale} />
	<Results {currentLocale} />
	<Clients {currentLocale} />
	<Partners {currentLocale} />
	<Team {currentLocale} />
	<Contact {currentLocale} />
</main>
