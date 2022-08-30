---
layout: 2021_default
year: 2022
title: Demo Session
---

<br>

{% assign demos = site.data.demos[page.year] | sort: 'id' %}
{% assign sessions = site.data.schedule[page.year] | where: 'type', "Demo" | sort: 'round'  %}

<table class="table table-bordered table-striped">
	<thead>
		<tr class="bg-dark text-light">
			<td> 
				<div style="float:left;">
					{% for session in sessions%}
						{% assign d = session.date | date: "%-d" %}
						{% assign day_ordinalize = ""%}
						{% case d %}
					  		{% when "1" or "21" or "31" %}{% assign day_ordinalize = "st"%}
					  		{% when "2" or "22" %}{% assign day_ordinalize = "nd"%}
					  		{% when "3" or "23" %}{% assign day_ordinalize = "rd"%}
					 		 {% else %}{% assign day_ordinalize = "th"%}
						{% endcase %}
					
						{% assign html_id = "Day" |append: {{session.day}} | append: "Round" | append: {{session.round}}  %}
			
						<div style="float:left;text-align:left;">
							<a href="{{site.url}}/schedule/#{{html_id}}">{{session.title}} - {{ session.date | date: "%A %e" }}{{day_ordinalize}} {{  session.date | date: "%B %Y %H:%M (CEST)"}}</a> via {%if session.platform-link %} <a href="{{session.platform-link}}" target="_blank">{{session.platform}}</a> {% else %}{{session.platform}}{%endif%} </div> <br>
			
					{% endfor%}	
				</div>
				<!--<div style="float:right; text-align:right;">
					Chaired by<br><b>{{sessions[0].chairs}}</b>
				</div>-->
			</td>
		</tr>
	</thead>
	<tbody>
		{% for demo in demos %}
			<tr class="">
			   <td style="text-align:center;">
			   		<h3>{{demo.title}}</h3><br>
					<b style="text-align:center;">Authors</b>
					<p style="text-align:center;">{{demo.authors}}</p>
					<b style="text-align:center;">Description</b>
					<p style="text-align:center;">{{demo.abstract}}</p>
			   </td>
			   
			</tr>
		{% endfor %}
	</tbody>
</table>

