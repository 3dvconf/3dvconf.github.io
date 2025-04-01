---
layout: 2026_sidebar
year: 2026
title: Papers
---

<script>
function myFunction() {
  var input, filter, ul, li, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = document.getElementsByClassName('paper_li');

  // Loop through all list items, and hide those that don't match the search query
  for (i = 0; i < li.length; i++) {
    txtValue = li[i].textContent || li[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
</script>

<p>
  You will find the schedule for both poster and oral sessions of accepted papers below.
  Poster presenters are free to select their board from those available and are kindly reminded
  to take down their posters following their designated session slot.
</p>

<div style="border: 2px solid #467CFD; padding: 15px; text-align: left">
<i>The proceedings will be available on IEEE Xplore. This material is presented here to ensure timely dissemination of scholarly and technical work. Copyright and all rights therein are retained by authors or by other copyright holders. All persons copying this information are expected to adhere to the terms and constraints invoked by each author's copyright.
</i>
</div>
<br><br>


<div align="center">
  <input type="text" id="myInput" onkeyup="myFunction()" 
         placeholder="Search for papers, authors, ..." class="paper_search">
</div>

<div id="myUL" style="list-style-type: none;"></div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

<script type="module">
  import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

  // Adjust path to your actual CSV containing 'PDF Link' and 'Supplementary'
  const csv_file_path = '{{site.url}}/2026/schedule_updated2.csv';
  const ul = document.getElementById("myUL");

  const data = await d3.csv(csv_file_path);

  for (let i = 0; i < data.length; i++) {
    // Skip rows with no title
    if (!data[i]['Title'] || data[i]['Title'].trim() === "") continue;

    // Each paper entry as a <div>
    const paperDiv = document.createElement("div");
    paperDiv.classList.add("paper_li");

    // Poster badge
    const posterBadge = document.createElement("p");
    posterBadge.classList.add("paper_badge");
    // Pad the Poster ID if numeric
    const posterId = data[i]['Poster ID'] 
      ? data[i]['Poster ID'].toString().padStart(2, '0') 
      : "N/A";
    posterBadge.appendChild(
      document.createTextNode("Poster " + (data[i]['Poster Session'] || "") + "-" + posterId)
    );
    paperDiv.appendChild(posterBadge);

    // Oral badge (if any)
    if (data[i]['Oral Session'] && data[i]['Oral Session'].trim() !== "") {
      const oralBadge = document.createElement("p");
      oralBadge.classList.add("paper_badge");
      oralBadge.appendChild(
        document.createTextNode("Oral " + data[i]['Oral Session'])
      );
      paperDiv.appendChild(oralBadge);
    }

    // Title
    const titleElem = document.createElement("span");
    titleElem.classList.add("paper_title");
    titleElem.textContent = data[i]['Title'];
    paperDiv.appendChild(titleElem);

    // Authors
    const authorsElem = document.createElement("div");
    authorsElem.classList.add("paper_authors");
    authorsElem.textContent = data[i]['Authors'] || '';
    paperDiv.appendChild(authorsElem);

    // Links: PDF / Supplementary / Abstract
    const linksDiv = document.createElement("div");
    linksDiv.classList.add("paper_links");

    // PDF link (if present)
    if (data[i]['PDF Link'] && data[i]['PDF Link'].trim() !== "") {
      const pdfLink = document.createElement("a");
      pdfLink.href = data[i]['PDF Link'].trim();
      pdfLink.target = "_blank";
      pdfLink.textContent = "PDF";
      pdfLink.classList.add("paper_pdf_link");
      linksDiv.appendChild(pdfLink);
    }

    // Supplementary link (if present)
    if (data[i]['Supplementary Link'] && data[i]['Supplementary Link'].trim() !== "") {
      // Add separator if PDF link was already added
      if (linksDiv.childNodes.length > 0) {
        linksDiv.appendChild(document.createTextNode(" | "));
      }
      const suppLink = document.createElement("a");
      suppLink.href = data[i]['Supplementary Link'].trim();
      suppLink.target = "_blank";
      suppLink.textContent = "Supp. Mat.";
      suppLink.classList.add("paper_supp_link");
      linksDiv.appendChild(suppLink);
    }

    // Abstract link: toggle the abstract collapse
    {
      // Add separator if there are already any links
      if (linksDiv.childNodes.length > 0) {
        linksDiv.appendChild(document.createTextNode(" | "));
      }
      const abstractToggle = document.createElement("a");
      abstractToggle.href = "#abstract_" + i;
      abstractToggle.setAttribute("data-toggle", "collapse");
      // If you're using Bootstrap's collapse, you might also want
      // `role="button" aria-expanded="false" aria-controls="abstract_i"`
      abstractToggle.setAttribute("role", "button");
      abstractToggle.setAttribute("aria-expanded", "false");
      abstractToggle.setAttribute("aria-controls", "abstract_" + i);

      abstractToggle.textContent = "Abstract";
      abstractToggle.classList.add("paper_abstract_link");
      linksDiv.appendChild(abstractToggle);
    }

    // Append the links row
    paperDiv.appendChild(linksDiv);

    // Abstract container (collapsed by default)
    const abstractDiv = document.createElement("div");
    abstractDiv.classList.add("paper_abstract", "collapse");
    abstractDiv.setAttribute("id", "abstract_" + i);
    abstractDiv.textContent = data[i]['Abstract'] || '';
    paperDiv.appendChild(abstractDiv);

    // Finally, append the entire paper entry to #myUL
    ul.appendChild(paperDiv);
  }

  // Handle ?search= in the URL
  const $_GET = {};
  window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(a, name, value) {$_GET[name] = value;});
  if ($_GET['search']) {
    const searchVal = $_GET['search'].replace('%20', ' ');
    document.getElementById("myInput").value = searchVal;
    myFunction();
  }
</script>

<!-- If needed, keep jQuery CSV script, though not used in this version -->
<script src="{{site.url}}/js/jquery.csv.js"></script>

<div></div>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br>
