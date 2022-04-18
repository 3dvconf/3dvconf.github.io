---
layout: 2021_sidebar_no_sponsors
year: 2021
title: <i class="far fa-handshake"></i> &nbsp; Sponsors
---

{% for section in site.data.sponsors[page.year] %}
<h3 class="centre">{{ section.name }}</h3>
<br/>
<div >
	{% assign sorted_company = section.company | sort:'name' %}
	{% for company in sorted_company %}
	<div class="col-md-12 align-self-center sponsor-logo" >
		<a href="{{company.url}}" target="_blank"><img alt="{{company.name}} Logo" src="{{site.url}}/{{company.logo}}" style="max-height:{{company.height}};"></a>
	</div>
	<br/><br/><br/>
	{% endfor %}
	
</div>
<br><br>

{% endfor %}
