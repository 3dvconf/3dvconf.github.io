---
layout: 2021_default
year: 2024
title: Tutorials
---

<br><br>

{% assign tutorials = site.data.tutorials[page.year] | sort: 'order' %}

{% for tutorial in tutorials %}

{%assign session = site.data.schedule[page.year] | where: 'type', "Tutorial" | where: 'index', {{tutorial.order}}  %}
{% assign session = session[0]%}

<table class="table table-striped" id="Tutorial{{tutorial.order}}">
<tr class="bg-dark text-light">
   <th style="text-align:center;"><h3>{{tutorial.title}}</h3></th>
</tr>
	
<!--
<tr>
	<td style="text-align:left;">
		<b>Speakers</b>
		<p>{{tutorial.organisers}}</p>
		<b>Description</b>
		<p>{{tutorial.description}}</p>
	</td>
</tr>
-->	
<tr>
	<td style="text-align:left;">
	<b>Website:</b> <a href="{{tutorial.website}}" target="_blank">{{tutorial.website}}</a><br>
	<b>Date:</b> {{tutorial.date}}<br>
	<b>Room:</b> {{tutorial.room}}<br>
	<br>

		<b>Speakers</b>
		<ul>
    {% assign organisers = tutorial.organisers %}
    
    {% for organiser in organisers %}
    <li><b>{{organiser.name}}</b> ({{organiser.affiliation}})</li>
    {% endfor %}
    </ul>
	<b>Description</b>
	<p>{{tutorial.description}}</p>
	</td>
</tr>	


{% endfor %}
