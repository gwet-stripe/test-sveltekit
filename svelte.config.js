import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-netlify';

/** @type {import('@sveltejs/kit').Config} */

const config = {
	css: false,

	compilerOptions: {
		cssHash: ({ hash, css }) => `_${hash(css)}`
	},

	kit: {
		target: '#svelte',
		adapter: adapter({
			split: false
		})
	},

	preprocess: [preprocess({})]
};

export default config;
