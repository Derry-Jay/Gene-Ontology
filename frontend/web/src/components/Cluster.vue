<html>
  <head>
  <a style="font-size: 30px" href="home.jsp">Home</a>&nbsp;&nbsp;&nbsp;&nbsp;<a style="font-size: 30px" href="genedisease.jsp">Back</a>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <center><h1>GRAPH CLUSTERING</h1>
    <script type="text/javascript">
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart(){
      var data = google.visualization.arrayToDataTable([
        ['Protin', 'Value'],
        ['AVG MF',  <%=mfavgs%>],
        ['',  0.0],
        ['MF',  <%=mf%>],
        ['',  0.0],
        ['',  0.0],
        ['AVG BP',  <%=bpavgs%>],
        ['',  0.0],
        ['BP',  <%=bp%>],
       ['',  0.0],['',  0.0],
        ['AVG CC',  <%=ccavgs%>],
        ['',  0.0],
         ['CC',  <%=cc%>],
      ]);
      var options = {
        tooltip: { isHtml: true },    // CSS styling affects only HTML tooltips.
        legend: { position: 'none' },
        bar: { groupWidth: '90%' },
        colors: ['#A61D4C']
      };
      var chart = new google.visualization.ColumnChart(document.getElementById('tooltip_rotated'));
      chart.draw(data, options);
    }
  </script>
</center>
</head>
<template>
  <style>div.google-visualization-tooltip { transform: rotate(30deg); }</style>
  <div id="tooltip_rotated" style="width: 1000px; height: 600px;"></div>
</template>
</html>
