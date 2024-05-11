---
layout: 2021_sidebar
year: 2025
---


{% for section in site.data.organisers[page.year] %}
<h2 class="centre">{{section.name}}</h2>
<div class="row justify-content-center" >
{% if section.mail %}
<h6 class="centre">Contact: {{section.mail}}</h6>
{% endif %}
</div>
<br>

<div class="row justify-content-center" >
	

	{% for people in section.people %}
	<div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 col-12" >
		
		{% if people.image %}
		<div class="profile crop">
			{% if people.url %}<a href="{{people.url}}" target="_blank">{% endif %}
				<img alt=" {{people.name}}" src="{{site.url}}/{{people.image}}">
			{% if people.url %}</a>{% endif %}
		</div>
		{% endif %}
		<div class="centre">
			<b>{{people.name}}</b>
			<p class="centre small">{{people.affiliation}}</p>
		</div>
	</div>
   {% endfor %}
</div>
<br>
{% endfor %}
