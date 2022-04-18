---
layout: 2021_sidebar
title: Area Chairs
year: 2021
---

<div class="row">
{% assign sorted_chairs = site.data.area-chairs[page.year] | sort:'name' %}
{% for chair in  sorted_chairs %}
	<div class="col-md-3 align-self-center profile crop" >
		<img alt="{{chair.name}}" src="{{site.url}}/{{chair.image}}"><br>
		<b>{{chair.name}}</b>
		<p>{{chair.affiliation}}</p>
	</div>
{% endfor %}
</div>


