from requests_html import HTMLSession

# FOR cv-library.CO.UK - COMPLETE

def getData(session, url):
  r = session.get(url)
  # r.html.render()
  return r.html.find('div.job__main')

def parse_html(html):
  job = {
    'title': html.find('h2 > a')[0].text,
    'link': 'https://www.cv-library.co.uk' + html.find('h2 > a')[0].attrs['href'],
    'posted': html.find('p.job__posted-by')[0].text
  }
  # some jobs posts have no salary data
  try:
      job['salary'] = html.find('dd.job__details-value')[0].text
  except:
      job['salary'] = ' '

  return job


def main(what, where):
  what = what.replace(' ', '-')
  parsedJobs = []
  session = HTMLSession()
  url = f'https://www.cv-library.co.uk/{what}-jobs-in-{where}'
  jobs = getData(session, url)

  for job in jobs[:6]:
    parsedJobs.append(parse_html(job))
  
  # print('cvLibrary: ')
  # print(parsedJobs)
  return parsedJobs
    


# if __name__ == '__main__':
#   main()





