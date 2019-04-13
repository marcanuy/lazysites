# lazysites
Transforms images of a static site into responsive lazy-loading images
thanks to [lazysizes](https://github.com/aFarkas/lazysizes).

Python script that traverses all HTML files of a directory and adds
the `lazyload` class to each HTML `img` element as required by
**lazysizes**, e.g. transforms this:

~~~ html
<img class="mt-3" src="foo.jpg" />
~~~

into

~~~ html
<img class="mt-3 lazyload" src="foo.jpg" data-src="foo.jpg" />
~~~

for all HTML files.

It is specially designed to be run after a static website generator
produces website's files. This way, you can use plain Markdown in
them and just modify the resulting website without interfering with
the generator so it can be applied to Hugo, Jekyll, etc.

## How it works

1. Starting in a directory, visits all its directories and
subdirectories.
2. Visits all `.html` files
3. Checks for `img` tags and
   1. add `lazyload` class
   2. copies `src` attribute content to `data-src`
4. Adds the JS library if not present any `lazysizes.js`:
   
        <script src="https://cdn.jsdelivr.net/npm/lazysizes@4.1.7/lazysizes.min.js"></script>
   
## How to use it

Create a virtual environment

~~~python
python3 -m venv ~/.virtualenvs/lazysite
~~~

Use it `source ~/.virtualenvs/lazysite/bin/activate`.

Install dependencies `pip install -r requirements.txt`

Copy your website files to `./public`.

And run the generator `python3 generator.py`.
   
## License

MIT licensed.
