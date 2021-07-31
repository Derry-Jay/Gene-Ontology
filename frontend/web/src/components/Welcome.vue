<template>
  <div class="animsition-overlay">
    <icon name></icon>
    <div id="section-1">
      <header class="main_h">
        <div class="menufix">
          <router-link v-bind:to="'/welcome'" class="logo">
            <img
              src="{{ url_for('static',filename='images/logo.jpg') }}"
              alt="Hello"
            />
          </router-link>
          <div class="mobile-toggle">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <nav>
            <ul>
              <li>
                <router-link
                  v-bind:to="'/welcome'"
                  class="out active animsition-link"
                  >HOME</router-link
                >
              </li>
              <li class="line">
                <router-link v-bind:to="'/login'" class="out animsition-link"
                  >SIGNIN</router-link
                >
              </li>
              <li class="line">
                <router-link to="/signup" class="out animsition-link"
                  >SIGNUP</router-link
                >
              </li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="hero">
        <h1 id="title-1">
          GENE
          <em> <span>M</span>iRNA </em>
        </h1>
        <div class="fixbottarro">
          <a class="scroll" href="#section-2">Scroll for more</a>
        </div>
      </div>
    </div>
    <div class="colw_6 paddbott100 spec-r">
      <p class="dolje" id="section-2"></p>
    </div>
  </div>
</template>
<script type="text/javascript">
</script>
