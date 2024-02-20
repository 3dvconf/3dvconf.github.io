---
layout: 2021_default
year: 2024
title: Schedule
---

<div style="width: 920px; height: 600px; position: relative; margin: auto; display: block">
<div style="background-color: white; position: absolute; top: 0; left: 0; width: 100%; height: 25px"></div>
<div style="background-color: white; position: absolute; top: 0; left: 0; width: 10px; height: 100%"></div>
<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vThkXIBXxf7iZqdZBQw-gX4vFDSf147roBOC1-0AzlRfz8sRmzISyacY0lOQyxdzQOekQJikH5FUOYv/pubhtml?gid=2043701182&amp;single=true&amp;widget=false&amp;headers=false&amp;chrome=false&amp;gridlines=false" width="100%" height="600px"  frameborder="0" style="margin: auto; display:block; width: 100%; height: 100%"></iframe>
</div>

<h1>Papers, Orals and Posters</h1>

<script>
function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i]; // .getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
</script>
<div align="center">
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for papers, authors, ..." size="50">
</div>
<ul id="myUL" style="list-style-type: none;"></ul>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

<script type="module">
	import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

	//$.csv.toArray('asd,asd');
	const csv_file_path = '{{site.url}}/schedule.csv';
	let user_name = document.getElementById("name");
	let ul = document.getElementById("myUL");

	const data = await d3.csv(csv_file_path);

	for(let i=1; i<data.length; i++){
		const li = document.createElement("li");
		li.style.backgroundColor = '#E9E9E9';
		li.style.padding = '15px';
		li.style.margin = '15px';
		li.style.borderRadius = '10px';
		li.style.color = 'black';
		if (data[i]['title'] == ""){continue;}
		li.appendChild(document.createTextNode(data[i]['title']));
		ul.appendChild(li);
	}
</script>
<script src="{{site.url}}/js/jquery.csv.js"></script>


<div>
</div>


{% assign sessionsByDay = site.data.schedule[page.year] | group_by: 'day' %}

{% for sessions in sessionsByDay %}
<table class="table table-striped" style="width:100%;">

<tbody>

	{% assign day_index = sessions.name| plus: 0 %}
	{% assign session-day = site.data.3dv[page.year].program[day_index] %}
	
 	{% assign d = session-day.date | date: "%-d" %}
	{% case d %}
	  {% when "1" or "21" or "31" %}{% assign day_ordinalize = "st"%}
	  {% when "2" or "22" %}{% assign day_ordinalize = "nd"%}
	  {% when "3" or "23" %}{% assign day_ordinalize = "rd"%}
	  {% else %}{% assign day_ordinalize = "th"%}
	{% endcase %}

	{% assign date_str = {{ session-day.date | date: "%A %e" }} | append: {{day_ordinalize}} | append:  {{ session-day.date | date: "%B %Y" }} %}
	
	<tr class="bg-dark text-light">
		<th colspan="7" style="text-align: center; padding:10px;">
			<h4>{{session-day.name}} - {{ session-day.date | date: "%A %e" }}{{day_ordinalize}} {{ session-day.date | date: "%B %Y" }} 
			</h4> 
		</th>
	</tr>

{% assign sessionsByRound = sessions.items | group_by: 'round'  %}
{% assign sessionsByRound = sessionsByRound | sort: 'name'  %}

{% for sesh in sessionsByRound %}

  <tr class="text-light" style="background-color: #888;">
	<td id="Day{{session-day.day}}Round{{sesh.name}}" style="text-align: left; width:50%;">
    	{% if sesh.name != "" %}<b>Round {{sesh.name}}</b>{% endif %}
    </td>
    <td style="text-align: center;">Link</td>
<!--winter-->
<!--
    <td style="text-align: center;">PT<br><b style="font-size:12px;">(UTC-8)</b></td>
    <td style="text-align: center;">ET<br><b style="font-size:12px;">(UTC-5)</b></td>
-->
<!--summer-->
    <td style="text-align: center;">PDT<br><b style="font-size:12px;">(UTC-7)</b></td>
    <td style="text-align: center;">EDT<br><b style="font-size:12px;">(UTC-4)</b></td>

    <td style="text-align: center">GMT<br><b style="font-size:12px;">(UTC)</b></td>
    <td style="text-align: center;">CEST<br><b style="font-size:12px;">(UTC+2)</b></td>
    <td style="text-align: center;">JST<br><b style="font-size:12px;">(UTC+9)</b></td>
  </tr>
  
  

{% for talk in sesh.items %}
  <!--The next two lines are a trick to use CEST as reference because the
  decoding of talk.date seems to do some second counting with respect to GMT by
  default and I was too lazy to look for where this happens (sorry).-->
	{% assign cest_time_start = talk.date | date: "%s"   %}
  <!--It seems that this I need this locally but not when I deploy ... This
  kind of time trick is better left alone ...-->

	{% assign gmt_time_start = cest_time_start | minus:  7200 %}
	{% assign jst_time_start = gmt_time_start  | plus:  32400 %}

<!--winter-->
<!--{% assign pst_time_start = gmt_time_start  | minus: 28800 %}-->

<!--summer-->
  {% assign pst_time_start = gmt_time_start  | minus: 25200 %}

<!--winter-->
<!--{% assign est_time_start = gmt_time_start  | minus: 18000 %}-->

<!--summer-->
	{% assign est_time_start = gmt_time_start  | minus: 14400 %}
	<!--{% assign cet_time_start = gmt_time_start  | plus:  3600  %}-->
	
	
	{% assign duration_str = talk.duration | split: ":" %}
	{% assign duration_hour = duration_str[0]  | times: 3600 %}
	{% assign duration_min =  duration_str[1]  | times: 60 %}
	{% assign duration_sec =  duration_str[2]  %}
	{% assign duration_secs =  duration_hour | plus: duration_min | plus: duration_sec %}
	
	{% assign cest_time_end = cest_time_start  | plus: {{duration_secs}} %}
	{% assign gmt_time_end = gmt_time_start  | plus: {{duration_secs}} %}
	{% assign jst_time_end = jst_time_start  | plus: {{duration_secs}} %}
	{% assign pst_time_end = pst_time_start  | plus: {{duration_secs}} %}	
	{% assign est_time_end = est_time_start  | plus: {{duration_secs}} %}
	<!--{% assign cet_time_end = cet_time_start  | plus: {{duration_secs}} %}-->
	
	{% assign html_id = talk.title | remove: " " | append: talk.subtitle | remove: " "  %}

  <tr id="{{html_id}}" style="margin:10px;">

    <td>{%if talk.title-link %} 
    		<a href="{{site.url}}/{{talk.title-link}}">{{talk.title}}{%if talk.subtitle%} - {{talk.subtitle}}{%endif%}</a>{%else%}{{talk.title}}
    		{%if talk.subtitle%} - {{talk.subtitle}}{%endif%}
    	{%endif%}
    	{%if talk.chairs %}<br><div style="font-size: 12px;">Chaired by: {{talk.chairs}}</div>{%endif%}
    </td>
    <td style="text-align: center;">
    	{%if talk.platform-link %} 
    		<a href="{{talk.platform-link}}" target="_blank">{{talk.platform}}</a>
    	{% else %}
    		{{talk.platform}}
    	{% endif%}
    </td>
    <td style="text-align: center; font-size: 12px;">{{pst_time_start | date: "%H:%M" }}{% if talk.duration %}-<br>{{pst_time_end | date: "%H:%M" }}{% endif%}</td>
    <td style="text-align: center; font-size: 12px;">{{est_time_start | date: "%H:%M" }}{% if talk.duration %}-<br>{{est_time_end | date: "%H:%M" }}{% endif%}</td>
    <td style="text-align: center; font-size: 12px;">{{gmt_time_start | date: "%H:%M" }}{% if talk.duration %}-<br>{{gmt_time_end | date: "%H:%M" }}{% endif%}</td>
    <td style="text-align: center; font-size: 12px;">{{cest_time_start | date: "%H:%M" }}{% if talk.duration %}-<br>{{cest_time_end | date: "%H:%M" }}{% endif%}</td>
    <td style="text-align: center; font-size: 12px;">{{jst_time_start | date: "%H:%M" }}{% if talk.duration %}-<br>{{jst_time_end | date: "%H:%M" }}{% endif%}</td>
    </tr>

{% endfor %}
{% endfor %}

</tbody>
</table>
<br/>
<br/>


{% endfor %}
