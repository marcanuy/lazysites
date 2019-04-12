# lazysites
Transforms images of a static site into responsive images thanks to [lazysizes](https://github.com/aFarkas/lazysizes).

Python script that traverses all HTML files of a directory and adds
the `lazyload` class to each HTML `img` element, e.g. transforms this:

~~~ html
<img class="mt-3" src="foo.jpg" />
~~~

into

~~~ html
<img class="mt-3 lazyload" src="foo.jpg" data-src="foo.jpg" />
~~~
