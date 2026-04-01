import { writable } from 'svelte/store';
import ptBR from './pt-BR.json';
import en from './en.json';

type Locale = 'pt-BR' | 'en';

const translations: Record<Locale, Record<string, any>> = {
	'pt-BR': ptBR,
	en: en
};

function createI18n() {
	const stored = typeof window !== 'undefined' ? localStorage.getItem('locale') : null;
	const initial: Locale = (stored === 'en' ? 'en' : 'pt-BR');

	const { subscribe, set, update } = writable<Locale>(initial);

	return {
		subscribe,
		setLocale: (locale: Locale) => {
			if (typeof window !== 'undefined') {
				localStorage.setItem('locale', locale);
			}
			set(locale);
		},
		toggle: () => {
			update((current) => {
				const next: Locale = current === 'pt-BR' ? 'en' : 'pt-BR';
				if (typeof window !== 'undefined') {
					localStorage.setItem('locale', next);
				}
				return next;
			});
		}
	};
}

export const locale = createI18n();

export function t(locale: Locale, path: string): string {
	const keys = path.split('.');
	let result: any = translations[locale];
	for (const key of keys) {
		if (result && typeof result === 'object' && key in result) {
			result = result[key];
		} else {
			return path;
		}
	}
	return typeof result === 'string' ? result : path;
}
