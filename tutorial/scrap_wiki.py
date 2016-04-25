def scrap(wiki):
	from bs4 import BeautifulSoup
	
	import requests
	
	
	response = requests.get(wiki)
	html_data = response.text
	soup2 = BeautifulSoup(html_data)
	
	toc_div = soup2.find('div', id="toc", class_="toc")
	
	soup3=BeautifulSoup(str(toc_div))
	
	soln = soup3.find_all("span",class_="tocnumber")
	soln2 = soup3.find_all("span",class_="toctext")
	
	combined=r""""""
	for i in range(0,len(soln)):
	     combined= combined + (soln[i].text + "  " + soln2[i].text + "\n")
	return combined

        
        


