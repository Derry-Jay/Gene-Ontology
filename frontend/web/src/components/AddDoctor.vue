<template>
  <div class="animsition-overlay">
    <div id="section-1">
      <header class="main_h">
        <div class="menufix">
          <a class="logo" href="index.html"
            ><img src="images/logo.jpg" alt="Hello"
          /></a>
          <div class="mobile-toggle">
            <span></span> <span></span> <span></span>
          </div>
          <nav>
            <ul>
              <li>
                <a class="out active animsition-link" href="admin.jsp">HOME</a>
              </li>
              <li class="line">
                <a class="out animsition-link" href="asso1.jsp"
                  >Gene Disease List</a
                >
              </li>
              <li class="line">
                <a class="out animsition-link" href="adminupload.jsp"
                  >Update Gene</a
                >
              </li>
              <li class="line">
                <a class="out animsition-link" href="login.jsp">LOGOUT</a>
              </li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="hero">
        <h1 id="title-1">WELCOME<em>{{uname}}</em></h1>
        <div class="fixbottarro">
          <a class="scroll" href="#section-2">Scroll for more</a>
        </div>
      </div>
    </div>
    <center>
      <form action="upload1" method="post">
        <h1 style="margin-left: 50px">UPDATE GENE</h1>
        <table
          style="
            margin-left: 100px;
            width: 700px;
            background-color: darkgray;
            padding: 20px;
          "
        >
          <tr>
            <td><strong>Disease ID</strong></td>
            <td><input type="text" name="did" /></td>
          </tr>
          <tr>
            <td><strong>Disease Name</strong></td>
            <td><input type="text" name="dn" /></td>
          </tr>
          <tr>
            <td><strong>Associated Genes</strong></td>
            <td><input type="text" name="as" /></td>
          </tr>
          <tr>
            <td><strong>Disease Type</strong></td>
            <td>
              <Select name="dt"
                ><option value="intrinsic">intrinsic</option>
                <option value="extrinsic">extrinsic</option></Select
              >
            </td>
          </tr>
          <tr>
            <td><strong>Symptoms</strong></td>
            <td><input type="text" name="sym" /></td>
          </tr>
          <tr>
            <td><strong>Precaution</strong></td>
            <td><input type="text" name="pre" /></td>
          </tr>
          <tr>
            <td><strong>PPI</strong></td>
            <td><input type="text" name="ppi" /></td>
          </tr>
          <tr>
            <td><strong></strong></td>
            <td><input type="submit" name="Upload" /></td>
          </tr>
        </table>
      </form>
    </center>
    <div class="colw_6 paddbott100 spec-r"></div>
  </div>
</template>
<script type="text/javascript">
$(document).ready(function () {
  $('#owl-partners').owlCarousel({
    autoPlay: 4000,
    stopOnHover: true,
    pagination: false,
    items: 5,
    itemsDesktop: [1199, 4],
    itemsDesktopSmall: [959, 3]
  })
})
$(function () {
  $('#cbp-qtrotator').cbpQTRotator()
})
var _gaq = _gaq || []
_gaq.push(['_setAccount', 'UA-15815880-3'])
_gaq.push(['_trackPageview']);
(function () {
  var ga = document.createElement('script')
  ga.type = 'text/javascript'
  ga.async = true
  ga.src =
    (document.location.protocol == 'https:' ? 'https://ssl' : 'http://www') +
    '.google-analytics.com/ga.js'
  var s = document.getElementsByTagName('script')[0]
  s.parentNode.insertBefore(ga, s)
})()
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
<script src="js/jquery.matchHeight-min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/animsition.min.js"></script>
<script src="js/jquery.parallax-scroll.js"></script>
<script src="js/owl.carousel.min.js"></script>
<script src="js/jquery.cbpQTRotator.min.js"></script>
<script src="js/functions.js"></script>
<script src="js/particle.js"></script>
