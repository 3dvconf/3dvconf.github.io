---
layout: 2025_sidebar
year: 2025
title: Keynote Speakers
---

<br>

{% assign keynotes = site.data.keynotes[page.year] | sort: 'index' %}



{% for keynote in keynotes %}

{%assign sessions = site.data.schedule[page.year] | where: 'type', "Keynote" | where: 'index', {{keynote.index}} %}


<table class="table  table-striped" id="{{keynote.name | remove: " "}}">
<tr class="bg-dark text-light">
   <th colspan="2"  style="text-align:center;"><h3>{{keynote.name}}</h3>
   </th>
</tr>
<tr></tr>
<tr>
	<td style="text-align:center; padding:10px;">
		<div style="float:left;">
			{% for round in sessions %}
				{% assign d = round.date | date: "%-d" %}
				{% assign day_ordinalize = ""%}
				{% case d %}
				  {% when "1" or "21" or "31" %}{% assign day_ordinalize = "st"%}
				  {% when "2" or "22" %}{% assign day_ordinalize = "nd"%}
				  {% when "3" or "23" %}{% assign day_ordinalize = "rd"%}
				  {% else %}{% assign day_ordinalize = "th"%}
				{% endcase %}
			
				{% assign html_id = "Day" |append: {{round.day}} | append: "Round" %}
				<div style="float:left;text-align:left;">
				<a href="{{site.url}}/{{page.year}}/schedule/#{{html_id}}">{{round.title}} - {{ round.date | date: "%A %e" }}{{day_ordinalize}} {{  round.date | date: "%B %Y %H:%M (CEST)"}}</a> 

        {{keynote.prez}}
        
        <!--
        via
        {%if round.platform-link %}
          <a href="{{round.platform-link}}" target="_blank">{{round.platform}}</a>
        {% else%}
          {{round.platform}}
        {%endif%}
        -->
      </div>
      <br>
			{% endfor %}
		</div>
	
  <!--
  <div style="float:right; text-align: right;">
			Chaired by<br>
			<b>{{sessions[0].chairs}}</b>
	</div>
  -->
	
  </td>
</tr>
<tr>
	<td>
		<div class="row">
			<div class="col-sm-3">
				<div class="container-fluid">
							<img class="rounded mx-auto d-block" style="margin:auto;" src="{{site.url}}/{{keynote.image}}" alt="{{keynote.name}} - Keynote Speaker at #3DV 2022" style="height:200px;float: right;margin:10px;"/>
				</div>
			</div>
			<div class="col-sm-9">
				<div style="container-fluid;">
					{% if keynote.title %}
					<b>{{keynote.title}}</b>
					<p>{{keynote.abstract}}</p>
					{% endif %}
					{% if keynote.bio %}
					<b>Biography</b>
					<p>{{keynote.bio}}</p>
					{% endif %}
				</div>
			</div>
		</div>
	</td>
</tr>

</table>
{%endfor %}





