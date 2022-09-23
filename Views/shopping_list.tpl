<html>
<body>
<h2> Shopping List </h2>
<hr/>
<table>
%for item in items:
<tr>
<!--Prof Version - {{str(item["id"])}}-->
<td> {{item["desc"]}} </td>
<td><a href="/delete/{{item["id"]}}"> Delete </a> </td>
<td><a href="/edit/{{item["id"]}}"> Edit </a> </td>
</tr>
%end
</table>
<hr/>
<a href="/add">New Item </a>
</body>
</html>