<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
        <script type="text/javascript">
        </script>
    </head>
    <template>
        <h1 style="margin-left: 600px">GENE lIST</h1>
        <h2 style="margin-left: 500px">list of genes and their id</h2>
        <table style="margin-left: 400px;width: 600px;background-color: darkgray;padding: 20px">
            <tr><td><strong>Serial No</strong></td><td><strong>Diesis Name ID</strong></td><td><strong>Diesis Name List</strong></td></tr>
            <tr><td><%=j%></td><td><%=id2%></td><td><%=id1%></td></tr>
            <a href="findprot.jsp" style="margin-left: 400px;size: 30px">Find Your Diesis Category</a>
        </table>
    </template>
</html>
