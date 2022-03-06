<script context="module">
    import {browser, dev} from '$app/env';

    // import {Col, Row} from 'sveltestrap/src';

    // we don't need any JS on this page, though we'll load
    // it in dev so that we get hot module replacement...
    export const hydrate = dev;

    // ...but if the client-side router is already loaded
    // (i.e. we came here from elsewhere in the app), use it
    export const router = browser;

    // since there's no dynamic data here, we can prerender
    // it so that it gets served as a static asset in prod
    export const prerender = true;
</script>

<svelte:head>
    <title>About</title>
</svelte:head>

<div class="content">
    <h1>Know is Steve Matos?</h1>
    <p>
        Hi, i'm Steve Matos from Lima, Perú.
        <br>
        I studied software engineering at the Universidad Nacional Mayor de San Marcos, and I am curious about
        gastronomy in
        general.
        <br>
        <br>
        Apart from coding, some other activities that I love to do!
    </p>
    <ul>
        <li>
            Playing Video Games
        </li>
        <li>
            Watch anime, series and movies.
        </li>
        <li>
            Play with my cats
        </li>
    </ul>

    <h1 class="project-heading">Professional <strong class="purple">Skillset </strong></h1>
    <div class="row">
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-python-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-git-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-postgresql-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-amazonwebservices-original"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-docker-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-graphql-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-mysql-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-django-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-svelte-plain"></i>
        </div>
    </div>
    <h1 class="project-heading"><strong class="purple">Tools</strong> I use</h1>
    <div class="row">
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-linux-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-pycharm-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-jupyter-plain"></i>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" role="img" viewBox="0 0 24 24" height="1em"
                 width="1em" xmlns="http://www.w3.org/2000/svg"><title></title>
                <path d="M13.527.099C6.955-.744.942 3.9.099 10.473c-.843 6.572 3.8 12.584 10.373 13.428 6.573.843 12.587-3.801 13.428-10.374C24.744 6.955 20.101.943 13.527.099zm2.471 7.485a.855.855 0 0 0-.593.25l-4.453 4.453-.307-.307-.643-.643c4.389-4.376 5.18-4.418 5.996-3.753zm-4.863 4.861l4.44-4.44a.62.62 0 1 1 .847.903l-4.699 4.125-.588-.588zm.33.694l-1.1.238a.06.06 0 0 1-.067-.032.06.06 0 0 1 .01-.073l.645-.645.512.512zm-2.803-.459l1.172-1.172.879.878-1.979.426a.074.074 0 0 1-.085-.039.072.072 0 0 1 .013-.093zm-3.646 6.058a.076.076 0 0 1-.069-.083.077.077 0 0 1 .022-.046h.002l.946-.946 1.222 1.222-2.123-.147zm2.425-1.256a.228.228 0 0 0-.117.256l.203.865a.125.125 0 0 1-.211.117h-.003l-.934-.934-.294-.295 3.762-3.758 1.82-.393.874.874c-1.255 1.102-2.971 2.201-5.1 3.268zm5.279-3.428h-.002l-.839-.839 4.699-4.125a.952.952 0 0 0 .119-.127c-.148 1.345-2.029 3.245-3.977 5.091zm3.657-6.46l-.003-.002a1.822 1.822 0 0 1 2.459-2.684l-1.61 1.613a.119.119 0 0 0 0 .169l1.247 1.247a1.817 1.817 0 0 1-2.093-.343zm2.578 0a1.714 1.714 0 0 1-.271.218h-.001l-1.207-1.207 1.533-1.533c.661.72.637 1.832-.054 2.522zM18.855 6.05a.143.143 0 0 0-.053.157.416.416 0 0 1-.053.45.14.14 0 0 0 .023.197.141.141 0 0 0 .084.03.14.14 0 0 0 .106-.05.691.691 0 0 0 .087-.751.138.138 0 0 0-.194-.033z"></path>
            </svg>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" role="img" viewBox="0 0 24 24" height="1em"
                 width="1em" xmlns="http://www.w3.org/2000/svg"><title></title>
                <path d="M20.61 0H3.39C2.189 0 1.23.96 1.23 2.16v19.681c0 1.198.959 2.159 2.16 2.159h17.22c1.2 0 2.159-.961 2.159-2.159V2.16C22.77.96 21.811 0 20.61 0zm.96 21.841c0 .539-.421.96-.96.96H3.39c-.54 0-.96-.421-.96-.96V2.16c0-.54.42-.961.96-.961h17.22c.539 0 .96.421.96.961v19.681zM6.63 20.399L9.33 18l-2.7-2.4v4.799zm9.72-9.719c-.479-.48-1.379-1.08-2.879-1.08-1.621 0-3.301.421-4.5.84V3.6h-2.4v10.38l1.68-.78s2.76-1.26 5.16-1.26c1.2 0 1.5.66 1.5 1.26v7.2h2.4v-7.2c.059-.179.059-1.501-.961-2.52zM13.17 7.5h2.4c1.08-1.26 1.62-2.521 1.8-3.9h-2.399c-.241 1.379-.841 2.64-1.801 3.9z"></path>
            </svg>
        </div>
        <div class="tech-icons col-md-3 col-4">
            <i class="devicon-bash-plain"></i>
        </div>

    </div>
</div>

<style>
    .tech-icons {
        font-size: 4.5em !important;
        margin: 15px !important;
        padding: 10px !important;
        opacity: .93 !important;
        border: 1.7px solid rgba(200, 137, 230, .637) !important;
        vertical-align: middle !important;
        text-align: center !important;
        border-radius: 5px !important;
        display: table !important;
        box-shadow: 4px 5px 4px 3px rgba(89, 4, 168, .137) !important;
        overflow: hidden !important;
        transition: all .4s ease 0s !important;
    }
</style>
