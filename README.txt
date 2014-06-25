A couple of things you should know to edit the site:

1. All of the html files should be placed inside of templates.

2. All images, css, videos, gifs, etc. should go inside of the static folder. If you want to incorporate these into your html, use the template tag {{ STATIC_URL }} as a prefix and then append the name of the file, for instance: {{ STATIC_URL }}/images/kitten.png

3. To view the website in your browser, in your terminal change your directory to the outtermost folder, Makersapace_Website, and type in 'python manage.py runserver'. Then, in your browser, navigate to 'localhost:8000/home'. Replace home with whatever page you'd like to view. Django does not provide live-view in the browser, so you'd have to refresh the page to see any of your changes. 

--Justin