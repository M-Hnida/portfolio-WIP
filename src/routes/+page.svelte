<script>
	import Hero from "$lib/components/Hero.svelte";
	import About from "$lib/components/About.svelte";
	import Projects from "$lib/components/Projects.svelte";
	import Skills from "$lib/components/Skills.svelte";
	import Contact from "$lib/components/Contact.svelte";
</script>

<svelte:head>
	<title>Portfolio | Backend, Data Science & Applications</title>
	<meta
		name="description"
		content="Portfolio orienté développement backend, data science, machine learning et applications desktop."
	/>
</svelte:head>

<Hero />
<About />
<Projects />
<Skills />
<Contact />
