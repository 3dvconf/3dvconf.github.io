---
layout: 2021_sidebar
year: 2022
title: Jobs Board
---

If you would like to advertise positions related to 3D computer vision, please
reach us at
<br><b>3dv22-jobs [ at ] googlegroups [ dot ] com</b>

with the following information:
- Company name
- Job position title
- Location
- Full job description:
  - Either a link to the full job description
  - Or a text description of the job with a mail to contact


<!-- Marco 2021: NOT GOOD Need to check versions - temp solution-->
<!--Assia 2022: Why not good?-->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
 
<input class="form-control" id="myInput" type="text" placeholder="Search..">

<table class="table table-striped" id="myInput">
    <thead>
	<tr class="bg-dark text-light">
    	<th onclick="sortTable(0)">Company</th>
    	<th onclick="sortTable(1)">Job Title</th>
    	<th onclick="sortTable(2)">Location</th>
  	</tr>
    </thead>
    <tbody id="myTable">
  	{% assign sorted_companies = site.data.jobs[page.year] | sort:'name' %}
	{% for company in  sorted_companies %}
		{% for job in  company.jobs %}
	  	<tr>
	    	<td>{{company.name}}</td>
	   		<td><a href="{%if job.local%}{{site.url}}/{%endif%}{{job.url}}" target="_blank">{{job.title}}</a></td>
	    	<td>{{job.location}}</td>
	    </tr>
		{% endfor %}
	{% endfor %}
	</tbody>
	
</table>


<script>
$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
</script>

