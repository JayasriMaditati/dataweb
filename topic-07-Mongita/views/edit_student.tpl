<html>
<body>
<h2> Edit Student's City </h2>
<form action="/edit/{{id}}" method = "post">
    <p> First Name: <input name= "Firstname" value="{{Firstname}}" readonly/></p>
    <p> Last Name: <input name= "Lastname" value="{{Lastname}}" readonly/></p>
    <p><b> Edit City: </b><input name= "City" value="{{City}}"/></p>
    <p> <button type="submit">Submit</button> </p>
</form>
<hr/>
<a href="/list"> Cancel </a>
</body>
</html>