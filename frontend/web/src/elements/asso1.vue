<template>
  <div class="animsition-overlay">
    <div id="section-1">
      <header class="main_h">
        <div class="menufix"> <a class="logo" href="index.html"><img src="images/logo.png" alt="Hello"></a>
          <div class="mobile-toggle"> <span></span> <span></span> <span></span> </div>
          <nav>
            <ul>
              <li><a class="out active animsition-link" href="admin.jsp">HOME</a></li>
              <li class="line"><a class="out animsition-link" href="asso1.jsp">Gene Disease List</a></li>
              <li class="line"><a class="out animsition-link" href="adminupload.jsp">Update Gene</a></li>
              <li class="line"><a class="out animsition-link" href="login.jsp">LOGOUT</a></li>
            </ul>
          </nav>
        </div>
      </header>
      <div class="hero">
        <h1 id="title-1">WELCOME<em>{{uname}}</em></h1>
        <div class="fixbottarro"> <a class="scroll" href="#section-2">Scroll for more</a> </div>
      </div>
    </div>
    <center>
      <h1 style="margin-left: 50px">GENE lIST</h1>
      <table style="margin-left: 100px;width: 1000px;background-color: darkgray;padding: 20px">
          <tr><td><strong>Disease ID</strong></td><td><strong>Disease Name</strong></td><td><strong>Symptoms</strong></td><td><strong>Precaution</strong></td></tr>
          <tr><td>{{did}}</td><td>{{d0d}}</td><td>{{ddd}}</td><td>{{dd}}</td></tr>
        </table>
      </center>
      <div class="colw_6 paddbott100 spec-r"></div>
    </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
<script src="{{ url_for('static',filename='js/jquery.matchHeight-min.js') }}"></script>
<script src="{{ url_for('static',filename='js/wow.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/animsition.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/jquery.parallax-scroll.js') }}"></script>
<script src="{{ url_for('static',filename='js/owl.carousel.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/jquery.cbpQTRotator.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/functions.js') }}"></script>
<script src="{{ url_for('static',filename='js/particle.js') }}"></script>
