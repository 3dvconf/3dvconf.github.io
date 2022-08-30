---
layout: 2021_default
year: 2022
title: Schedule
---

<br>

{% assign sessionsByDay = site.data.schedule[page.year] | group_by: 'day' %}

{% for sessions in sessionsByDay %}
<table class="table table-striped" style="width:100%;">

session name {{sessions.name}}

<tbody>
	{% assign day_index = sessions.name| plus: 0 %}
  
  dayindex {{day_index}}
	
  {% assign session-day = site.data.3dv[page.year].program[day_index] %}
  sessionday {{session-day}}
 	
  {% assign d = session-day.date | date: "%-d" %}
  d {{d}}

	{% case d %}
	  {% when "1" or "21" or "31" %}{% assign day_ordinalize = "st"%}
	  {% when "2" or "22" %}{% assign day_ordinalize = "nd"%}
	  {% when "3" or "23" %}{% assign day_ordinalize = "rd"%}
	  {% else %}{% assign day_ordinalize = "th"%}
	{% endcase %}
	{% assign date_str = {{ session-day.date | date: "%A %e" }} | append: {{day_ordinalize}} | append:  {{ session-day.date | date: "%B %Y" }} %}
  {{date_str}}

  <tr class="bg-dark text-light">
		<th colspan="7" style="text-align: center; padding:10px;">
			<h4>{{session-day.name}} - {{ session-day.date | date: "%A %e" }}{{day_ordinalize}} {{ session-day.date | date: "%B %Y" }} 
			</h4> 
		</th>
	</tr>


{% endfor %}
