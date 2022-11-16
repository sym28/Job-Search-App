from requests_html import HTMLSession

# FOR REED.CO.UK -- COMPLETE

def getData(session, url):
  r = session.get(url)
  return r.html.find('div.details')


def parse_html(html):
  job = {
    'title': html.find('h3.job-result-heading__title > a')[0].text,
    'link': 'https://www.reed.co.uk' + html.find('h3.job-result-heading__title > a')[0].attrs['href'],
    'posted': html.find('div.job-result-heading__posted-by')[0].text
  }
  # some jobs posts have no salary data
  try:
      job['salary'] = html.find('ul.job-metadata > li')[0].text
  except:
      job['salary'] = ' '

  return job
  

def main(what, where):
  what = what.replace(' ', '-')
  parsedJobs = []
  session = HTMLSession()
  url = f'https://www.reed.co.uk/jobs/{what}-jobs-in-{where}'

  jobs = getData(session, url)
  
  for job in jobs[:6]:
    parsedJobs.append(parse_html(job))

  return parsedJobs
    








