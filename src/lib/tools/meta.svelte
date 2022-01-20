<script>
	export let title;
	export let description;
	export let image = 'https://svelte.dev/images/thumbnail.png';
</script>

<svelte:head>
	<title>{title}</title>
	<meta name="title" content={title} />
	<meta name="description" content={description} />

	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://svelte.dev/" />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:image" content={image} />

	<meta property="twitter:card" content="summary_large_image" />
	<meta property="twitter:url" content="https://svelte.dev/" />
	<meta property="twitter:title" content={title} />
	<meta property="twitter:description" content={description} />
	<meta property="twitter:image" content={image} />
</svelte:head>
