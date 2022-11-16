from flask import Blueprint, render_template, request
from web_scraper import reed_job_scraper, cvLibrary_scraper

views = Blueprint(__name__, 'views')


@views.route('/', methods=['GET', 'POST'])
def homepage():
  if request.method == 'POST':
    what = request.form.get('what')
    where = request.form.get('where')
    jobList1 = cvLibrary_scraper.main(what, where)
    jobList2 = reed_job_scraper.main(what, where)
    return render_template('index.html', jobList1=jobList1, jobList2=jobList2)

  return render_template('index.html' )

@views.route('/jobs')
def jobs():
  return 'job page'


