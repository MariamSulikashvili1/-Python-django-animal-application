< div


class ="update" >

< !-- Create
a
Form -->
< form
method = "POST" >
< !-- Security
token
by
Django -->
{ % csrf_token %}

< !-- form as paragraph -->
{{form.as_p}}

< input
type = "submit"
value = "Update" >
< / form >

< / div >

