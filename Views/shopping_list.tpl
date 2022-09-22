<html>
<body>
<table>
<tr>
<td>Id</td>
<td>Desc</td>
</tr>
%for item in items:
<tr>
<!--Prof Version - {{str(item["id"])}}-->
<td> {{item["id"]}} </td>
<td> {{item["desc"]}} </td>
<td><a href="/delete/{{item["id"]}}"> Delete </a> </td>
</tr>
%end
</table>
<hr/>
<a href="/add">New Item </a>
</body>
</html>