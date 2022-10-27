<html>
   <head>
      <style>
         table, th, td {
            border: 1.5px solid white;
         }
      </style>
   </head>
<body>
<h2> Student Registration </h2>
<hr/>
<table>
<th>FirstName </th>
<th>LastName </th>
<th>City </th>
<th>Action </th>
%for item in items:
<tr>
<td style="padding-left:5px;"> {{item["Firstname"]}} </td>
<td style="padding-left:5px;"> {{item["Lastname"]}} </td>
<td style="padding-left:5px;"> {{item["City"]}} </td>
<td><a href="/delete/{{item["id"]}}"> Delete </a> </td>
<td><a href="/edit/{{item["id"]}}"> Edit </a> </td>
</tr>
%end
</table>
<hr/>
<a href="/add">Add New Student </a>
</body>
</html>