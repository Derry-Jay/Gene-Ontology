<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<script type='text/javascript' src='https://www.google.com/jsapi'></script>
    <script type="text/javascript">
    </script>
</head>
<body >

        <script type='text/javascript'>
            google.load('visualization', '1', {packages: ['orgchart']});
            google.setOnLoadCallback(drawChart);
            function drawChart() {
                var data = new google.visualization.DataTable();
                data.addColumn('string', 'Node');
                data.addColumn('string', 'Parent');
                data.addRows([
                    ['<%=gid%>', ''],
                    ['<%=mfavgs%>', '<%=gid%>'],
                    ['<%=ccavgs%>', '<%=gid%>'],
                    ['<%=bpavgs%>', '<%=gid%>'],
                    ['<%=mf%>', '<%=mfavgs%>'],
                    ['<%=cc%>', '<%=ccavgs%>'],
                    ['<%=bp%>', '<%=bpavgs%>'],
                    ['<%=cc%>', '<%=gid%>'],
                    ['<%=avg%>', '<%=mf%>'],
                    ['<%=avg%>', '<%=cc%>'],
                    ['<%=avg%>', '<%=bp%>'],
                    ['<%=ge%>', '<%=avg%>'],
                    ['<%=did%>', '<%=ge%>'],
                    ['<%=d0d%>', '<%=did%>'],
                    ['<%=sym1%>', '<%=d0d%>'],
                    ['<%=pre%>', '<%=sym1%>'],
                ]);
                var chart = new google.visualization.OrgChart(document.getElementById('chart_div'));
                chart.draw(data);
            }
        </script>
        <div id='chart_div'></div>
        <a href="home.jsp">Home</a> <a href="upload?id=<%=gid%>">upload Cloud</a>
       </body>
</html>
