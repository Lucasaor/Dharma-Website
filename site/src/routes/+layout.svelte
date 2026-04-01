<script lang="ts">
	import '../app.css';
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { locale, t } from '$lib/i18n';
	import { onMount } from 'svelte';

	let { children } = $props();
	let currentLocale = $state<'pt-BR' | 'en'>('pt-BR');

	onMount(() => {
		const unsub = locale.subscribe((val) => {
			currentLocale = val;
			document.documentElement.lang = val;
		});
		return unsub;
	});
</script>

<Navbar {currentLocale} />
{@render children()}
<Footer {currentLocale} />
