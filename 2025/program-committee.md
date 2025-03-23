---
layout: 2025_sidebar
year: 2025
---


<!-- <h2 style="text-align:center;"> Outstanding Reviewers</h2>
<br>
<div class="row" >
{% for people in site.data.program-committee[page.year] %}
		{% if people.outstanding %}
        <div class="col-md-6 col-sm-12 col-12" style="text-align:center;">
        	{{people.name}}
		</div>
		{% endif%}
{% endfor %}
</div>
<br><br> -->

<h2 style="text-align:center;"> Area Chairs </h2>
<br>
<div class="row" >
{% for people in site.data.program-committee[page.year] %}
		{% if people.ac %}
        <div class="col-md-6 col-sm-12 col-12" style="text-align:center;">
        	{{people.name}}
		</div>
		{% endif%}
{% endfor %}
</div>
<br><br>

<h2 style="text-align:center;"> Reviewers</h2>
<br>
<div class="row" >
{% for people in site.data.program-committee[page.year] %}
        <div class="col-md-6 col-sm-12 col-12" style="text-align:center;">
        	{{people.name}}
		</div>
{% endfor %}
</div>
<br><br>


