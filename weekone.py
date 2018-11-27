import requests
from bs4 import BeautifulSoup

# Returns a list of lists containing the job title, job company, and link for more information.
def get_webpage(url):
    # Returns a response object.
    res = requests.get(url)

    # Raise Exception if unable to download file.
    try:
        res.raise_for_status()
    except Exception as e:
    	print(e)

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())

    job_info = []
    jobs = soup.find_all("div", attrs={'class': 'job_content'})

    for job in jobs:
        j = []
        job_title = job.find_all("span")[0].contents
        j.extend(job_title)
        job_company = job.find_all("a")[1].contents
        j.extend(job_company)
        job_link = job.find_all('a')[0]['href']
        j.append(job_link)

        job_info.append(j)

    return job_info

if __name__ == '__main__':
    get_webpage('https://www.ziprecruiter.com/candidate/search?location=Berkeley%2C%20California&search=Software')
