<template>
  <div class="animsition-overlay">
    <section id="section-6">
      <div class="horBar2Bxx wow fadeInLeftBig" data-wow-duration="3s"></div>
      <header class="main_h">
        <div class="menufix">
          <a class="logo" href="index.html"
            ><img src="images/logo.png" alt="Hello"
          /></a>
          <div class="mobile-toggle">
            <span></span> <span></span> <span></span>
          </div>
          <nav>
            <ul>
              <ul>
                <li>
                  <a class="out active animsition-link" href="home.jsp">HOME</a>
                </li>
                <li class="line">
                  <a class="out animsition-link" href="disease.jsp">Category</a>
                </li>
                <li class="line">
                  <a class="out animsition-link" href="asso.jsp">Gene List</a>
                </li>
                <li class="line">
                  <a class="out animsition-link" href="go.jsp">Search Gene</a>
                </li>
                <li class="line">
                  <a class="out animsition-link" href="history.jsp">History</a>
                </li>
                <li class="line">
                  <a class="out animsition-link" href="login.jsp">LOGOUT</a>
                </li>
              </ul>
            </ul>
          </nav>
        </div>
      </header>
      <div class="grid flex">
        <div class="row">
          <div class="colw_6">
            <h1 id="title-sub1">{{ uname }}</h1>
            <h2 id="title-sub2">Association Rule</h2>
          </div>
          <div class="colw_6 wow zoomIn">
            <div class="box-fix">
              <h3 class="centered">Find your Disease on Ontology</h3>
              <div class="social"></div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="colw_6 beta wow column zoomIn">
            <div class="wrapimg hack960">
              <div class="pic">
                <img
                  src="images/1.jpg"
                  class="pic-image full-width"
                  alt="Pic"
                />
                <div class="pic-caption top-to-bottom">
                  <h4 class="pic-title">GENE ONTOLOGY</h4>
                </div>
              </div>
            </div>
          </div>
          <div class="colw_6 beta column reladiv">
            <h1 style="margin-left: 200px">GENE CATEGORY</h1>
            <table
              style="
                margin-left: 100px;
                width: 400px;
                background-color: darkgray;
                padding: 20px;
              "
            >
              <tr>
                <td><strong>Gene Name</strong></td>
                <td><strong>Gene ID</strong></td>
                <td><strong>CATEGORY</strong></td>
              </tr>
              <form method="post" action="go1.jsp">
                <input type="text" name="gid" value="gid" hidden="" />
                <tr>
                  <td>{{ gn }}</td>
                  <td>{{ gid }}</td>
                  <td><input type="submit" value="Category" /></td>
                </tr>
              </form>
            </table>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery.matchHeight-min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/animsition.min.js"></script>
<script src="js/lightgallery-all.min.js"></script>
<script src="js/functions.js"></script>
