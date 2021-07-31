<template>
  <div class="animsition-overlay">
    <div class="horBar2Bxx wow fadeInLeftBig" data-wow-duration="3s"></div>
    <header class="main_h">
      <div class="menufix"> <a class="logo" href="index.html"><img src="images/logo.png" alt="Hello"></a>
        <div class="mobile-toggle"> <span></span> <span></span> <span></span> </div>
        <nav>
          <ul>
              <li><a class="out active animsition-link" href="home.jsp">HOME</a></li>
              <li class="line"><a class="out animsition-link" href="asso.jsp">ASSOCIATION RULE</a></li>
              <li class="line"><a class="out animsition-link" href="login.jsp">LOGOUT</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <div class="grid flex16">
      <div class="row">
        <div class="colw_6">
          <h2 id="title-sub2">MOAL Rule</h2>
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
       <h1 style="margin-left: 600px">GENE DISEASE LIST</h1>
       <table style="margin-left: 300px;width: 800px;background-color: darkgray;padding: 20px">
          <tr><td><strong>Serial No</strong></td><td><strong>User Name</strong></td><td><strong>Gene ID</strong></td><td><strong>Gene Category</strong></td></tr>
          <tr><td>{{rs.getString("sid")}}</td><td>{{rs.getString("uid")}}</td><td>{{rs.getString("gid")}}</td><td>{{rs.getString("gtype")}}</td><td><a href="">Download Result</a></td></tr>
       </table>
    </div>
  </div>
</template>
<script type="text/javascript">
</script>
