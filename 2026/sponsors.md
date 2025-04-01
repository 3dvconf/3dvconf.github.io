---
layout: 2021_sidebar_no_sponsors
year: 2025
title: Sponsors
title-logo: <i class="far fa-handshake"></i>
---

<!-- <h3 class="centre">Platinum Partners</h3>

<a href="https://hexagon.com" target="_blank">
<img src="{{site.url}}/img/2024/sponsors/HEXAGON_STANDARD_RGB_LOGO Hires Standard.png" width="90%"></a> -->


<!-- <h3 class="centre">Gold Partners</h3>

<h3 class="centre">Silver Partners</h3>

<h3 class="centre">Bronze Partners</h3>

<h3 class="centre">Startup Partners</h3> -->





{% for section in site.data.sponsors[page.year] %}
<h3 class="centre" style="background-color: #EEEEEE">{{ section.name }}</h3>
<br/>
<div align="center">
	{% assign sorted_company = section.company | sort:'name' %}
	{% for company in sorted_company %}
	<!-- <div class="col-md-12 assia"> -->
	<a href="{{company.url}}" target="_blank">
	<img alt="{{company.name}} Logo" src="{{site.url}}/{{company.logo}}" style="width:{{company.width}}; margin-left: 10px" class="centre">
	</a>
	<!-- </div> -->
	<!-- <br/><br/> -->
	{% endfor %}
</div>
<br><br>

{% endfor %}


