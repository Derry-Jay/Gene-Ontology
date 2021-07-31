<template>
  <div class="animsition-overlay">
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
            <li class="line">
              <a class="out animsition-link" href="login.jsp">LOGOUT</a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
    <div class="grid flex16">
      <div class="row">
        <div class="colw_6">
          <h1 id="title-sub1">{{uname}}</h1>
          <h2 id="title-sub2">Filtering Rule</h2>
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
      <h1 style="margin-left: 500px">Your Possible Diseases Medicine</h1>
      <table
        style="
          margin-left: 100px;
          width: 1200px;
          background-color: darkcyan;
          padding: 20px;
          height: 50px;
        "
      >
        <tr>
          <td>
            <center><strong>Gene ID</strong></center>
          </td>
          <td>
            <center><strong>{{gid}}</strong></center>
          </td>
        </tr>
        <tr>
          <td>
            <center><strong>Gene Disease Category</strong></center>
          </td>
          <td>
            <center><strong>{{ge}}</strong></center>
          </td>
        </tr>
      </table>
      <table
        style="
          margin-left: 100px;
          width: 1200px;
          background-color: darkcyan;
          padding: 20px;
          height: 50px;
        "
      >
        <tr>
          <td>
            <center><strong>Disease List</strong></center>
          </td>
        </tr>
      </table>
      <table
        style="
          margin-left: 100px;
          width: 1200px;
          background-color: darkgray;
          padding: 20px;
          height: 200px;
        "
      >
        <tr style="background-color: darkcyan">
          <td><strong>Disease ID</strong></td>
          <td><strong>Disease Name</strong></td>
          <td><strong>Disease Symptoms</strong></td>
          <td><strong>Disease Image</strong></td>
          <td><strong>Cure</strong></td>
          <td><strong>BRT</strong></td>
        </tr>
        <tr>
          <td>{{did}}</td>
          <td>{{d0d}}</td>
          <td>{{rs.getString("molecularbasis")}}</td>
          <td>
            {{lst}}<img src="img" style="width: 300px; height: 200px" />
          </td>
          <td>{{pre}}</td>
          <td>
            <form method="post" action="searchresult1.jsp">
              <input type="text" name="gid" value="{{gid}}" hidden="" />
              <input type="text" name="mfavgs" value="{{mfavgs}}" hidden="" />
              <input type="text" name="bpavgs" value="{{bpavgs}}" hidden="" />
              <input type="text" name="ccavgs" value="{{ccavgs}}" hidden="" />
              <input type="text" name="mf" value="{{mf}}" hidden="" />
              <input type="text" name="cc" value="{{cc}}" hidden="" />
              <input type="text" name="bp" value="{{bp}}" hidden="" />
              <input type="text" name="gl" value="{{ge}}" hidden="" />
              <input type="text" name="did" value="{{did}}" hidden="" />
              <input type="text" name="pdn" value="{{d0d}}" hidden="" />
              <input type="text" name="ds" value="{{sym1}}" hidden="" />
              <input type="text" name="pre" value="{{pre}}" hidden="" />
              <input type="text" name="avg" value="{{avg}}" hidden="" />
              <input
                style="background-color: darkcyan; padding: 20px"
                type="submit"
                value="Bayesian Rose Tree"
              />
            </form>
          </td>
        </tr>
      </table>
      <form method="post" action="searchresult1.jsp">
        <input type="text" name="gid" value="{{gid}}" hidden="" />
        <input type="text" name="mfavgs" value="{{mfavgs}}" hidden="" />
        <input type="text" name="bpavgs" value="{{bpavgs}}" hidden="" />
        <input type="text" name="ccavgs" value="{{ccavgs}}" hidden="" />
        <input type="text" name="mf" value="{{mf}}" hidden="" />
        <input type="text" name="cc" value="{{cc}}" hidden="" />
        <input type="text" name="bp" value="{{bp}}" hidden="" />
        <input type="text" name="gl" value="{{ge}}" hidden="" />
        <input type="text" name="did" value="{{did}}" hidden="" />
        <input type="text" name="pdn" value="{{d0d}}" hidden="" />
        <input type="text" name="ds" value="{{sym1}}" hidden="" />
        <input type="text" name="pre" value="{{pre}}" hidden="" />
        <input type="text" name="avg" value="{{avg}}" hidden="" />
        <input
          style="
            margin-left: 100px;
            width: 1200px;
            background-color: darkcyan;
            padding: 20px;
            font-size: 20px;
          "
          type="submit"
          value="Bayesian Rose Tree"
        />
      </form>
      <div id="chart_div"></div>
    </div>
  </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script type='text/javascript' src='https://www.google.com/jsapi'></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery.matchHeight-min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/animsition.min.js"></script>
<script src="js/functions.js"></script>
<script src="js/you-video.js"></script>
