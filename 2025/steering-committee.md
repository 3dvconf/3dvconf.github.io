---
layout: 2025_sidebar
title: Steering Committee
year: 2025
---

<div class="row">
{% assign sorted_chairs = site.data.steering-committee[page.year] | sort:'name' %}
{% for chair in  sorted_chairs %}
	<div class="col-md-5 align-self-center profile crop" >
		<b>{{chair.name}}</b>
		<p>{{chair.affiliation}}</p>
	</div>
{% endfor %}
</div>


