<template>
  <div class="animsition-overlay">
    <div class="horBar2Bxx wow fadeInLeftBig" data-wow-duration="3s"></div>
    <header class="main_h">
      <div class="menufix"> <a class="logo" href="index.html"><img src="images/logo.png" alt="Hello"></a>
        <div class="mobile-toggle"> <span></span> <span></span> <span></span> </div>
        <nav>
          <ul>
              <li class="line"><a class="out animsition-link" href="login.jsp">LOGOUT</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <div class="grid flex16">
      <div class="row">
        <div class="colw_6">
          <h1 id="title-sub1"></h1>
          <h2 id="title-sub2">Filtering   Rule</h2>
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
       <h1 style="margin-left: 500px">Your Possible Diseases Symptoms</h1>
          <form method="post" action="fie">
              <table style="margin-left: 200px;width: 1000px;background-color: darkcyan;padding: 20px;height: 50px">
                  <tr><td><center><strong>Gene ID</strong></center></td><td><center><strong></strong></center></td></tr>
                  <tr><td><center><strong>Gene Disease Category</strong></center></td><td><center><strong></strong></center></td></tr>
              </table>
              <table style="margin-left: 200px;width: 1000px;background-color: darkcyan;padding: 20px;height: 50px">
                  <tr><td><center><strong>Disease List</strong></center></td></tr></table>
              <table style="margin-left: 200px;width: 1000px;background-color: darkgray;padding: 20px;height: 200px">
                  <tr style="background-color: darkcyan;"><td><strong>Disease ID</strong></td><td><strong>Disease Name</strong></td><td><strong>Disease Symptoms</strong></td><td><strong>Disease Image</strong></td><td><strong>View Cure</strong></td></tr>
                  <tr><td></td><td></td><td></td><td><img src="" style="width:300px;height:200px;"></td><td><a href="">View cure</a></td></tr>
              </table>
          </form>
      </div>
    </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="js/jquery.matchHeight-min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/animsition.min.js"></script>
<script src="js/functions.js"></script>
<script src="js/you-video.js"></script>
<script type="text/javascript">
</script>
