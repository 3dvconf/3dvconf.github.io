
## How to run
Assuming Ruby and Jekyll are already installed 
```
git clone git@github.com:3dvconf/3dvconf.github.io.git
cd 3dvconf.github.io

# Serve the website
bundle exec jekyll serve

# Visit the webiste
# Open your browser and type the address output by the previous command
```

## File organization

### Content related
- `assets/`: image and paper templates, various data
- <year> (e.g. `2022/`): website pages for that year 
- `data/`: various instance data such as sponsors, jobs, keynotes ...
- `papers/`: accepted papers (title, abstract)
- `posts/`: for short communications to appear in the 'news' section
- `files/`: to store files to download from the website (e.g. paper template,
  call for paper)
- `img/`: to store website images (e.g. people's pictures)

### Style related
- `includes/`: various html file for the website blocks
- `layouts/`: various html to define the page layouts using the html files in the `includes/`
- `css/`: website style


## How to update

- Create a new directory for the new year (See `2022/` for an example)
- Add new entries in the `_data/` files for the new year.
- Add a new directory for the images in `img/`
- Add a new directory for the images in `files/`
- Update the `_papers/` directory with the new papers 

### Special note on the papers update

The papers and schedule page are automatically generated based on the
information in:
- the `_papers/` directory, with one file per paper. The paper's information
  are stored in a map. 
- `_data/schedule.yml`
- `<year>/schedule.md`
- `<year>/accepted_papers.md` 

Depending on the conference's organisation, you may want to add entries in the
paper's files and the schedule. You can then use update `<year>/schedule.md`
and `<year>/accepted_papers.md` to change these pages' layout. 

You will probably get the list of accepted papers in a tabular form. Parsing
scripts are provided in `assets/<year>/data/` to format the tabular data into
yaml files.

**To improve**: All papers's data are stored in `_papers` with a year prefix.
This is not a sustainable setup but I could not find a way to have the `.md`
files parse a subdirectory. If you know of a better way, please update the
`_papers/` organisation to have the papers in separate directories based on
years.


### Special note on the website assets

Editable files to create the logo and website images are available in
`assets/website`. Feel free to use them as a template and edit them to your
taste.

### Command to create the 3dv.ico

```convert 3dv-256.png 3dv-128.png 3dv-64.png 3dv-48.png 3dv-32.png 3dv-16.png 3dv.ico'''

## Dependencies

### Ruby

Install Ruby
```
sudo apt-get install ruby-full build-essential zlib1g-dev
```

Create a writable directory in your home to store your gems (I feel like like
writing a video game instructions ...)
```
cd
mkdir gems
```

Update your .bashrc to point to this directory
```
# Ruby
export GEM_HOME=""$HOME"/gems"
export PATH="$HOME"/gems/bin:"$PATH"
```

Install jekyll following [these instructions](https://jekyllrb.com/docs/)

## Troubleshooting

### 'no bundle command'
```
Command 'bundle' not found, but can be installed with:
```

Install bundle with `gem install bundle`


#### Pb2: github-pages not installed

`gem install github-pages` outputs a version error so run 
`bundle install` as suggested by the error message, it should automatically solve
the missing dependencies


## Resources

- A conference website with a similar structure: https://github.com/cvmp/cvmp.github.io 
- Jekyll: https://jekyllrb.com/
