---
layout: 2025_sidebar
year: 2025
title: Award Candidates
---

<script>
function myFunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = document.getElementsByClassName('paper_li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i];
    txtValue = a.innerHTML || a.textContent;
	if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
</script>
The final awards go to:

- <strong style="color:red">Best Paper Award</strong>:<br>
<strong>An Object is Worth 64x64 Pixels: Generating 3D Object via Image Diffusion<br></strong>
Xingguang Yan, Han-Hung Lee, Ziyu Wan, Angel X. Chang

- <strong style="color:red">Best Student Paper Award</strong>:<br>
<strong>MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion<br></strong>
Bardienus Pieter Duisterhof, Lojze Zust, Philippe Weinzaepfel, Vincent Leroy, Yohann Cabon, Jerome Revaud

- <strong style="color:red">Best Paper Honorable Mention Award</strong>:<br>
<strong>MeshUp: Multi-Target Mesh Deformation via Blended Score Distillation<br></strong>
Hyunwoo Kim, Itai Lang, Thibault Groueix, Noam Aigerman, Vladimir Kim, Rana Hanocka

The following papers are selected as <b>award candidates</b>.
<div align="center">
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for papers, authors, ..." class="paper_search">
</div>

<div id="myUL" style="list-style-type: none;"></div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

<script type="module">
	import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";
	const csv_file_path = '{{site.url}}/2025/award_candidates.csv';
	let user_name = document.getElementById("name");
	let ul = document.getElementById("myUL");

	const data = await d3.csv(csv_file_path);

	for(let i=0; i<data.length; i++){
		const li_a = document.createElement("a");
		li_a.classList.add("paper_a");
		li_a.setAttribute("data-toggle", "collapse");
		li_a.setAttribute("href", "#abstract_"+i.toString());
		li_a.setAttribute("role", "button");
		li_a.setAttribute("aria-expanded", "false");
		li_a.setAttribute("aria-controls", "abstract_"+i.toString());

		const li = document.createElement("div");
		li.classList.add("paper_li");
		const badge = document.createElement("p");
		badge.classList.add("paper_badge");
		const poster_badge = document.createElement("p");
		poster_badge.classList.add("paper_badge");
		const authors = document.createElement("div");
		authors.classList.add("paper_authors");
		const title = document.createElement("span");
		title.classList.add("paper_title");
		title.appendChild(document.createTextNode(data[i]['Title']));

		const paper_abstract = document.createElement("div");
		paper_abstract.classList.add("paper_abstract");
		paper_abstract.classList.add("collapse");
		paper_abstract.setAttribute("id", "abstract_"+i.toString());
		paper_abstract.appendChild(document.createTextNode(data[i]['Abstract']));

		// if (data[i]['title'] == ""){continue;}
		// poster_badge.appendChild(document.createTextNode("Poster " + data[i]['Poster Session']));
		// li.appendChild(poster_badge);
		badge.appendChild(document.createTextNode("Award Candidate"));
		li.appendChild(badge);
		li.appendChild(title);
		authors.appendChild(document.createTextNode(data[i]['Authors']));
		li.appendChild(authors);
		li.appendChild(paper_abstract);
		li_a.appendChild(li);
		ul.appendChild(li_a);

	}

	var $_GET=[];
	window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,function(a,name,value){$_GET[name]=value;});
	if ($_GET['search']){
		const search = $_GET['search'].replace('%20', ' ');
		document.getElementById("myInput").value = search;
		myFunction();
	}
</script>
<script src="{{site.url}}/js/jquery.csv.js"></script>

<div>
</div>

<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
