<html>
<body>
<h2> Shopping List </h2>
<hr/>
<table>
%for item in shopping_list:
<tr>
<!--Prof Version - {{str(item["id"])}}-->
<td> {{str(item["description"])}} </td>
<td> {{str(item["quantity"])}} </td>
<td><a href="/delete/{{item["id"]}}"> Delete </a> </td>
<td><a href="/edit/{{item["id"]}}"> Edit </a> </td>
</tr>
%end
</table>
<hr/>
<form action = '/add' method="post">
    <p> Add New Item: <input name = "description"/></p>
    <p> quantity: <input name = "quantity"/></p>
    <p> <button type = "submit"> Submit </button>
</form>
</body>
</html>