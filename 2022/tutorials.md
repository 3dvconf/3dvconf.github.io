---
layout: 2021_default
year: 2022
title: Tutorials
---

<br><br>

{% assign tutorials = site.data.tutorials[page.year] | sort: 'order' %}

{% for tutorial in tutorials %}

{%assign session = site.data.schedule[page.year] | where: 'type', "Tutorial" | where: 'index', {{tutorial.order}}  %}
{% assign session = session[0]%}

<table class="table  table-striped" id="Tutorial{{tutorial.order}}">
<tr class="bg-dark text-light">
   <th style="text-align:center;"><h3>{{tutorial.title}}</h3></th>
</tr>
<tr></tr>
<tr>
	{% assign d = session.date | date: "%-d" %}
	{% assign day_ordinalize = ""%}
	{% case d %}
	  {% when "1" or "21" or "31" %}{% assign day_ordinalize = "st"%}
	  {% when "2" or "22" %}{% assign day_ordinalize = "nd"%}
	  {% when "3" or "23" %}{% assign day_ordinalize = "rd"%}
	  {% else %}{% assign day_ordinalize = "th"%}
	{% endcase %}

	<td style="text-align:center;">
		<a href="{{site.url}}/{{page.year}}/schedule/#Day{{session.day}}">	
			{{ session.date | date: "%A %e" }}{{day_ordinalize}} 
      {{  session.date | date: "%B %Y %H:%M (CEST)" }}
		</a> 
    
    <!--
    via 
    {%if session.platform-link %}
      <a href="{{session.platform-link}}" target="_blank">{{session.platform}}</a>
    {% else%}
      {{session.platform}}
    {%endif%}
    -->
	</td>	
</tr>	
	
<tr>
	<td style="text-align:left;">
		<b>Speakers</b>
		<p>{{tutorial.organisers}}</p>
    <!--
		<b>Description</b>
		<p>{{tutorial.description}}</p>
    -->
	</td>
</tr>	

{% endfor %}
