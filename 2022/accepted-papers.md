---
layout: 2021_sidebar
year: 2022
title: Accepted Papers
---

The list of accepted 3DV papers is now available!

**[Download list of accepted papers]({{site.url}}/files/2022/papers_accepted.txt)**


<br><br>

{% assign paper_index = 1%}

{% assign session_days = site.papers | group_by: 'day'  | sort: 'name' %}

{% for session_day in session_days %}

	{% assign session_ids = session_day.items | group_by: 'session' | sort: 'name' %}

	{% for session_id in session_ids %}

		{% assign session_types = session_id.items | group_by: 'type' | sort: 'name' %}
		{% for session_type in session_types %}
	
			{% case session_type.name %}
				{% when "Oral"   %}{% assign session_combined_title = 	{{session_type.name}} | append: " Session " 	| append: {{session_id.name}} %}

				{% when "Poster" %}{% assign session_combined_title = 	{{session_type.name}} | append: " Spotlight " 	| append: {{session_id.name}} %}

				{% when "Spotlight" %}
					{% assign poster_id = ""%}
					{% case session_id.name %}
					  {% when "1" or "2" or "31" %}{% assign poster_id = "1"%}
					  {% when "3" or "4" %}{% assign poster_id = "2"%}
					  {% when "5" or "6" %}{% assign poster_id = "3"%}
					  {% else %}{% assign day_ordinalize = "th"%}
					{% endcase %}
        {% assign session_combined_title = 	{{session_type.name}} | append: " " 	| append: {{session_id.name}} | append: " / Poster " | append:{{poster_id}}%}
			{% endcase %}
			{% assign sessions = site.data.schedule[page.year] | where: "type", {{session_type.name}} | where: "index", {{session_id.name}} %}
			{% assign session = sessions[0] %}
			
<table class="table table-striped">
	<thead>
		<tr class="bg-dark text-light" id="{{session_type.name}}{{session_id.name}}">
			<td colspan="2" style="text-align: left;">
		   		<div style="width:100%; text-align: center;">
		   			<h3>{{session_combined_title}}{% if session.subtitle %}: {{session.subtitle}}{% endif %}</h3>
		   		</div>
		   		<br>
		   		<div style="float:left;">
				{% for round in sessions%}
					{% assign date = round.date %}
					{% assign d = date | date: "%-d" %}
					{% assign day_ordinalize = ""%}
					{% case d %}
					  {% when "1" or "21" or "31" %}{% assign day_ordinalize = "st"%}
					  {% when "2" or "22" %}{% assign day_ordinalize = "nd"%}
					  {% when "3" or "23" %}{% assign day_ordinalize = "rd"%}
					  {% else %}{% assign day_ordinalize = "th"%}
					{% endcase %}
					<a href="{{site.url}}/{{page.year}}/schedule/#Day{{round.day}}Round{{round.round}}">
          {{round.title}} - {{ date | date: "%A %e" }}{{day_ordinalize}} {{ date | date: "%B %Y %H:%M (CEST)" }}
          </a>
					
          <!--
          via
          {%if round.platform-link %}
            <a href="{{round.platform-link}}" target="_blank">{{round.platform}}</a>
          {% else%}
            {{round.platform}}
          {%endif%}
          -->
          <br>
				{% endfor %}
				</div>

			   	{% if session.chairs %}
			   	<div style="float:right; text-align: right; font-weight:normal;">Chaired by<br><b>{{session.chairs}}</b></div>
			   	{% endif %}
			</td>
		</tr>
	</thead>
	<tbody>

			{% assign sorted_papers = session_type.items | sort: 'order' %}
			
      {% for paper in  sorted_papers %}
			  <tr>
			    <td style="width:10%; text-align:center;">
            <b style="font-size: 15px;">{{paper.order}}</b>
            <br>
            <!--
            <p style="text-align:center; font-size: 13px; colour:gray;">[{{paper.submission-id }}]</p>
            -->
          </td>

			    <td style="width:90%;"> 
			    	<!--
            <a href="{{site.url}}/papers/{{ paper.submission-id | prepend: '000' | slice: -3, 3 }}.html">
            -->

            <b>{{paper.title}}</b>

            <!--</a>
            -->

            <br/>
			    	
            <p>{{paper.authors}}</p>
            
            <!--
			    	<a href="{{paper.link}}" target="_blank">PDF (protected)</a>
            -->

			    </td>
			  </tr>
	
			{% assign paper_index = paper_index | plus: 1%}	
			{% endfor %}

	</tbody>
</table>

		{% endfor %}
	{% endfor %}
{% endfor %}

<br>
