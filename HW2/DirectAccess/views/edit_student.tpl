<html>
<body>
<form action="/edit/{{id}}" method = "post">
    <p> First Name:<input name= "Firstname" value="{{Firstname}}" readonly/></p>
    <p> Last Name:<input name= "Lastname" value="{{Lastname}}" readonly/></p>
    <p> Edit City:<input name= "City" value="{{City}}"/></p>
    <p> <button type="submit">Submit</button> </p>
</form>
<hr/>
<a href="/list"> Cancel </a>
</body>
</html>