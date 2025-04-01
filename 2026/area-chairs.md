---
layout: 2026_sidebar
title: Area Chairs
year: 2026
---

<div class="row">
{% assign sorted_chairs = site.data.area-chairs[page.year] | sort:'name' %}
{% for chair in  sorted_chairs %}
	<div class="col-md-5 align-self-center profile crop" >
		<b>{{chair.name}}</b>
		<p>{{chair.affiliation}}</p>
	</div>
{% endfor %}
</div>


