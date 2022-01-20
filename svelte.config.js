import adapter from '@sveltejs/adapter-netlify';

/** @type {import('@sveltejs/kit').Config} */

const config = {
	css: false,
	kit: {
		target: '#svelte',
		adapter: adapter({
			split: false
		})
	}
};

export default config;
