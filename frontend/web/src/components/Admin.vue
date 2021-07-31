<template>
  <div class="animsition-overlay">
    <div id="section-1">
      <header class="main_h">
        <div class="menufix">
          <router-link to="/welcome"
            ><img src="images/logo.jpg" alt="Hello"
          /></router-link>
          <div class="mobile-toggle">
            <span></span> <span></span> <span></span>
          </div>
          <nav>
            <ul>
              <li>
                <router-link to="/welcome">HOME</router-link>
              </li>
              <li class="line">
                <router-link to="/upload">Add/Update Data</router-link>
              </li>
              <li class="line">
                <router-link to="/login"></router-link>
              </li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="hero">
        <h1 id="title-1">
          WELCOME<em>{{ uname }}</em>
        </h1>
        <div class="fixbottarro">
          <a class="scroll" href="#section-2">Scroll for more</a>
        </div>
      </div>
    </div>
    <center>
      <h1 style="margin-left: 50px">GENE lIST</h1>
      <table
        style="
          margin-left: 100px;
          width: 700px;
          background-color: darkgray;
          padding: 20px;
        "
      >
        <tr>
          <td><strong>Serial No</strong></td>
          <td><strong>Gene Name</strong></td>
          <td><strong>Gene ID</strong></td>
        </tr>
        <tr>
          <td></td>
        </tr>
        <tr>
          <td></td>
        </tr>
      </table>
    </center>
    <div class="colw_6 paddbott100 spec-r"></div>
  </div>
</template>
<script type="text/javascript">
</script>
