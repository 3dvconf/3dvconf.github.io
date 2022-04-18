---
layout: 2021_sidebar_no_news
year: 2021
title: <i class="far fa-newspaper"></i> &nbsp;Latest News</h1>
---

<ul style="list-style-type:none;">

  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">
      	<div>
      	<h4>{{ post.title }}</h4>
      	<b>{{ post.date  | date: "%-d %B %Y"}}</b>

      	</div>
      </a>
    </li>
    <hr>
  {% endfor %}
</ul>
