<html>
<body>
<h2> Student List </h2>
<hr/>
<table>
%for item in items:
<tr>
<td> {{item["Firstname"]}} </td>
<td> {{item["Lastname"]}} </td>
<td> {{item["City"]}} </td>
<td><a href="/delete/{{item["id"]}}"> Delete </a> </td>
<td><a href="/edit/{{item["id"]}}"> Edit </a> </td>
</tr>
%end
</table>
<hr/>
<a href="/add">New Student </a>
</body>
</html>