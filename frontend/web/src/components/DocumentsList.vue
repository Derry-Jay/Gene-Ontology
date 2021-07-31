<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gene Ontology</title>
<meta property="og:url" content="http://www.valeron.net/index.html" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Free responsive web template Istria - Realize Your Business Goals" />
<meta property="og:description" content="Free responsive web template Istria by Valeron design studio - Realize Your Business Goals" />
<meta property="og:image" content="http://www.valeron.net/img/valeron-artist.jpg" />
<meta name="description" content="Free responsive web template Istria by Valeron design studio - Realize Your Business Goals" />
<meta name="msapplication-tap-highlight" content="no" />
<meta name="robots" content="index,follow,all" />
<meta name="keywords" content="Izrada web stranica, web studio Istra" />
<meta name="author" content="Valeron design studio" />
<link rel="apple-touch-icon" sizes="57x57" href="img/apple-touch-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="img/apple-touch-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="img/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="img/apple-touch-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="img/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="img/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="img/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="img/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="img/apple-touch-icon-180x180.png">
<link rel="icon" type="image/png" href="img/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="img/android-chrome-192x192.png" sizes="192x192">
<link rel="icon" type="image/png" href="img/favicon-96x96.png" sizes="96x96">
<link rel="icon" type="image/png" href="img/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="img/manifest.json">
<meta name="msapplication-TileColor" content="#da532c">
<meta name="msapplication-TileImage" content="img/mstile-144x144.png">
<meta name="theme-color" content="#ffffff">
<link rel="stylesheet" href="css/animsition.min.css">
<link rel="stylesheet" type="text/css" href="css/grid.min.css" />
<link rel="stylesheet" type="text/css" href="css/style.css" />
<link rel="stylesheet" type="text/css" href="css/menu.css" />
<link rel="stylesheet" type="text/css" href="css/overlay.css" />
<link rel="stylesheet" href="css/social.css">
<link rel="stylesheet" href="css/banner.css">
<link rel="stylesheet" href="css/you-video.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome-animation/0.0.8/font-awesome-animation.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="js/jquery.matchHeight-min.js"></script>
<script src="js/wow.min.js"></script>
<script src="js/animsition.min.js"></script>
<script src="js/functions.js"></script>
<script src="js/you-video.js"></script>
<script type="text/javascript">
</script>
</head>
<body>
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
          <h1 id="title-sub1"><%=uname%></h1>
          <h1 id="title-sub2">Regulatory</h1>
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
        <h1 style="margin-left: 500px">Regulatory Modules</h1>
        <table style="margin-left: 400px;width: 600px;background-color: darkgray;padding: 20px;height: 50;">
           <tr style="background-color: darkcyan;" ><td><strong>Serial No</strong></td><td><strong>Gene ID</strong></td><td><strong>MiRNA</strong></td><td><strong>Transaction Factor</strong></td><td><strong>Cross Ontology Value</strong></td><td><strong>Multiplicative Update Algorithm</strong></td></tr>
           <form method="post" action="mides.jsp">
               <tr><td><center><%=kkk%></center></td><td><%=id%></td><td><center><%=img%></center></td><td><center><%=tf%></center></td><td><center><%=avg%></center></td><td> <input type="text" value="<%=id%>" name="id" hidden=""><input type="text" name="bp" value="<%=avg%>" hidden=""> <input type="submit"  value="Process"></td></tr>
           </form>
        </table>
      </div>
   </div>
   <script type="text/javascript">
   $(".enticlick").click(function() {
     window.location = $(this).find("a").attr("href");
     return false;
   });
     var _gaq = _gaq || [];
     _gaq.push(['_setAccount', 'UA-15815880-3']);
     _gaq.push(['_trackPageview']);
     (function() {
       var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
       ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
       var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
     })();
   </script>
  </body>
</html>
