<template>
  <div class="animsition-overlay">
    <div class="horBar2Bxx wow fadeInLeftBig" data-wow-duration="3s"></div>
    <header class="main_h">
      <div class="menufix"> <a class="logo" href="index.html"><img src="images/logo.png" alt="Hello"></a>
        <div class="mobile-toggle"> <span></span> <span></span> <span></span> </div>
        <nav>
          <ul>
            <li><a class="out active animsition-link" href="home.jsp">HOME</a></li>
              <li class="line"><a class="out animsition-link" href="disease.jsp">Category</a></li>
              <li class="line"><a class="out animsition-link" href="asso.jsp">Gene List</a></li>
              <li class="line"><a class="out animsition-link" href="go.jsp">Search Gene</a></li>
              <li class="line"><a class="out animsition-link" href="history.jsp">History</a></li>
              <li class="line"><a class="out animsition-link" href="login.jsp">LOGOUT</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <div class="grid flex16">
      <div class="row">
        <div class="colw_6">
          <h2 id="title-sub2"> clustering</h2>
        </div>
        <div class="col_6">
          <div class="bannerbox">
            <div class="banner">
              <div class="phrase-1">Select Gene</div>
              <div class="phrase-2">Gene Ontology</div>
              <div class="blob-1"></div>
              <div class="blob-2"></div>
              <div class="blob-3"></div>
            </div>
            <a href="home.jsp">Home</a>
          </div>
         </div>
      </div>
    </div>
    <div>
      <h1 style="margin-left: 600px">Associated Genes</h1>
      <form method="post" action="go1.jsp">
        <table style="margin-left: 400px;width: 600px;background-color: darkgray;padding: 20px">
          <tr><td>S.No</td><td><strong>Disease Name ID</strong></td><td><strong>Disease Name List</strong></td><td><strong>Associated Gene</strong></td><td><strong>Enter Your Gene</strong></td></tr>
          <tr><td><center>{{kkk}}</center></td><td>{{did}}</td><td>{{dis}}</td><td>{{ddd}}</td><td> <input type="text" placeholder="Ener Your Gene Id" name="gid" ><input type="submit"  value="Find gene"></td></tr>
        </table>
      </form>
    </div>
  </div>
</template>
<script type="text/javascript">
</script>
<style src="css/animsition.min.css"></style>
<style src="css/grid.min.css"></style>
<style src="css/style.css"></style>
<style src="css/menu.css"></style>
<style src="css/overlay.css"></style>
<style src="css/social.css"></style>
<style src="css/banner.css"></style>
<style src="css/you-video.css"></style>
<style src="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css"></style>
<style src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css"></style>
<style src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome-animation/0.0.8/font-awesome-animation.min.css"></style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="js/jquery.matchHeight-min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/animsition.min.js"></script>
<script src="js/functions.js"></script>
<script src="js/you-video.js"></script>
