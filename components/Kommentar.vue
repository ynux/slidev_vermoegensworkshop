<!--
  Persönlicher Kommentar auf einer Folie.
  Verwendung im Markdown:  <Kommentar>Hier mein Gedanke.</Kommentar>
  Leer lassen (<Kommentar></Kommentar>) = nichts wird angezeigt.
  Position: unten rechts. <Kommentar oben>…</Kommentar> = oben rechts,
  <Kommentar inline>…</Kommentar> = im Textfluss an der Stelle, wo es im Markdown steht.
-->
<script setup>
defineProps({ oben: { type: Boolean, default: false }, inline: { type: Boolean, default: false } })
</script>

<template>
  <div v-if="$slots.default" class="kommentar" :class="{ oben, inline }"><slot /></div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:ital,wght@1,500;1,600&display=swap');

.kommentar {
  position: absolute;
  right: 3.5rem;
  bottom: 2.1rem;
  max-width: 36%;
  font-family: 'Nunito', 'Segoe UI', 'Helvetica Neue', sans-serif;
  font-style: italic;
  font-weight: 600;
  font-size: 0.78rem;
  line-height: 1.4;
  color: #1dad86;
  text-align: right;
  z-index: 10;
}
.kommentar.oben {
  bottom: auto;
  top: 1.2rem;
}
.kommentar.inline {
  position: static;
  max-width: none;
  text-align: left;
  margin-top: 0.6rem;
}
.kommentar p { margin: 0; }
</style>
