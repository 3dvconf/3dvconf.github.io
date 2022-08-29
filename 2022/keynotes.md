---
layout: 2021_default
year: 2022
title: Keynote Speakers
---

<br>
{% assign keynotes = site.data.keynotes[page.year] | sort: 'index' %}

{% for keynote in keynotes %}

<table class="table  table-striped" id="{{keynote.name | remove: " "}}">
<tr class="bg-dark text-light">
   <th colspan="2"  style="text-align:center;"><h3>{{keynote.name}}</h3>
   </th>
</tr>
<tr></tr>

<tr>
	<td>
		<div class="row">
			<div class="col-sm-3">
				<div class="container-fluid">
              <a href="{{keynote.url}}">
							<img class="rounded mx-auto d-block" style="margin:auto;" src="{{site.url}}/{{keynote.image}}" alt="{{keynote.name}} - Keynote Speaker at #3DV 2022" style="height:200px;float: right;margin:10px;"/>
              </a>
				</div>
			</div>
			<div class="col-sm-9">
				<div style="container-fluid;">
					{% if keynote.title %}
					<b>{{keynote.title}}</b>
					<p>{{keynote.abstract}}</p>
					{% endif %}
					<b>Biography</b>
					<p>{{keynote.bio}}</p>
				</div>
			</div>
		</div>
	</td>
</tr>

</table>
{%endfor %}






