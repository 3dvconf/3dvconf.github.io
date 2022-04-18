---
layout: 2021_sidebar_no_news
year: 2022
title: <i class="far fa-newspaper"></i> &nbsp;Latest News</h1>
---

<ul style="list-style-type:none;">

  {% for post in site.posts %}
    {% if post.year == page.year %}
    <li>
      <a href="{{site.url}}/{{ post.url }}">
      	<div>
      	<h4>{{ post.title }}</h4>
      	<b>{{ post.date  | date: "%-d %B %Y"}}</b>

      	</div>
      </a>
    </li>
    <hr>
	  {% endif %}
  {% endfor %}
</ul>
