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
        </nav>
      </div>
    </header>
    <div class="grid flex16">
      <div class="row">
        <div class="colw_6">
          <h2 id="title-sub2">clustering</h2>
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
      <center>
        <form method="posgt" action="go2.jsp">
          <input type="text" value="{{id}}" name="id" hidden="" />
          <input
            style="
              margin-left: 100px;
              width: 400px;
              font-size: 20px;
              background-color: #0099ff;
              padding: 20px;
              height: 50px;
            "
            type="submit"
            value="Find your Disease Category"
          />
        </form>
      </center>
      <table
        style="
          margin-left: 100px;
          width: 1200px;
          background-color: #349e1f;
          padding: 20px;
          height: 50px;
        "
      >
        <tr>
          <td><strong>Serial No</strong></td>
          <td><strong>Disease Name ID</strong></td>
          <td><strong>Disease Name List</strong></td>
        </tr>
        <tr>
          <td>{{ kkk }}</td>
          <td>{{ did }}</td>
          <td>{{ dis }}</td>
        </tr>
        <table
          style="
            margin-left: 100px;
            width: 1200px;
            background-color: darkcyan;
            padding: 20px;
          "
        >
          <tr>
            <td>
              <center><strong>Biological Process</strong></center>
            </td>
          </tr>
        </table>
        <table
          style="
            margin-left: 100px;
            width: 1200px;
            background-color: darkgray;
            padding: 20px;
          "
        >
          <tr>
            <td><strong>Name</strong></td>
            <td><strong>Goid</strong></td>
            <td><strong>Score</strong></td>
            <td><strong>Affiliating Genes</strong></td>
          </tr>
          <tr>
            <td>{{ bname }}</td>
            <td>{{ bgoid }}</td>
            <td>{{ bscore }}</td>
            <td>{{ baf }}{{ bpavg }}</td>
          </tr>
        </table>
        <table
          style="
            margin-left: 100px;
            width: 1200px;
            background-color: darkcyan;
            padding: 20px;
          "
        >
          <tr>
            <td>
              <center><strong>Cellular Component</strong></center>
            </td>
          </tr>
        </table>
        <table
          style="
            margin-left: 100px;
            width: 1200px;
            background-color: darkgray;
            padding: 20px;
          "
        >
          <tr>
            <td><strong>Name</strong></td>
            <td><strong>Goid</strong></td>
            <td><strong>Score</strong></td>
            <td><strong>Affiliating Genes</strong></td>
          </tr>
          <tr>
            <td>{{ cname }}</td>
            <td>{{ cgoid }}</td>
            <td>{{ cscore }}</td>
            <td>{{ caf }}</td>
          </tr>
        </table>
        <table
          style="
            margin-left: 100px;
            width: 1200px;
            background-color: darkcyan;
            padding: 20px;
          "
        >
          <tr>
            <td>
              <center><strong>Molecular Function</strong></center>
            </td>
          </tr>
        </table>
        <table
          style="
            margin-left: 100px;
            width: 1200px;
            background-color: darkgray;
            padding: 20px;
          "
        >
          <tr>
            <td><strong>Name</strong></td>
            <td><strong>Goid</strong></td>
            <td><strong>Score</strong></td>
            <td><strong>Affiliating Genes</strong></td>
          </tr>
          <tr>
            <td>{{ mname }}</td>
            <td>{{ mgoid }}</td>
            <td>{{ mscore }}</td>
            <td>{{ maf }}</td>
          </tr>
          <table
            style="
              margin-left: 300px;
              width: 600px;
              background-color: darkcyan;
              padding: 20px;
            "
          >
            <tr style="background-color: darkcyan">
              <td>Name</td>
              <td>Biological Process</td>
              <td>Cellular Component</td>
              <td>Molecular Function</td>
            </tr>
            <tr style="background-color: darkseagreen">
              <td>Total Values</td>
              <td>{{ bpavg }}</td>
              <td>{{ ccavg }}</td>
              <td>{{ mfavg }}</td>
            </tr>
            <tr style="background-color: darkseagreen">
              <td>Avg Values</td>
              <td>{{ bpavgs }}</td>
              <td>{{ ccavgs }}</td>
              <td>{{ mfavgs }}</td>
            </tr>
          </table>
        </table>
      </table>
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
