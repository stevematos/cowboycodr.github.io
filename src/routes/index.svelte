<script context="module" lang="ts">
    export const prerender = true;
</script>

<script lang="ts">
    import Typewriter from 'svelte-typewriter'
</script>

<svelte:head>
    <title>Website Steve Matos</title>
    <meta name="description" content="Steve Matos Portfolio Site"/>
</svelte:head>

<section>
    <div class="profile">

        Hi
        <span class="wave">
            <img src="hi_hand.gif" width="35px" />
        </span>
        <br/>
        I'm Steve Matos

        <div class="welcome">
            <picture>
                <source srcset="cat.webp" type="image/webp"/>
                <img src="cat.gif" alt="Welcome"/>
            </picture>
        </div>



        <Typewriter loop>
            I'm
            <span>🐍 Developer</span>
            <span>Backend Developer</span>
            <span>Software Developer</span>
        </Typewriter>

    </div>

</section>

<style>
    .profile {
        text-align: center;
        font-size: 250% ;
    }

    .welcome {
        margin: 2rem 0;
    }

</style>
