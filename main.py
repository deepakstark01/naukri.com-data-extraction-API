

import requests, pandas as pd
def getDataBank(page):
  
  cookies = {
      'test': 'naukri.com',
      '_t_ds': '416583c1691493247-65416583c-0416583c',
      '_t_us': '64D2237F',
      '_t_s': 'direct',
      '_t_r': '1091%2F%2F',
      'persona': 'default',
      '_abck': 'FF1BCB0C8EB19436DDF0C6544A39D85F~0~YAAQN2/ZF2vaZtCJAQAAhnPd1ApL80nZEf49zoNEKHqgHcYQ3xXOQq5IxeqSzsaJb6JvZcTRGZGozmPhe7yitDU2G1mEdwHIaTgWPuT1XrAjPtBdFqdpkI5Q+mZElpJLOXTQIMwy4CmIKpumB0y6Qil1xRD99s+ZUjNSzI617WjtI3/XhPRgelrbaEckmiyxRhj4uJ4exYlyrcHmnb1DkZM9mrtix2dQVDUGf16zfEW1N+s/TNmHQEQ2Ot8vSNVgK0iEPyHk9BZjSnMO8EVAcfAoISt4ldaV3BRiOcWPVxuDknuYS5RxVx6NzCQNWl69b0zLfBw5m1zYUtS13nc1pCdgUEUCPjkY9jPxZ12GQs0fo8umtcFyztBXyyLzrG3qkmdnjGlUw9SdCpT5yoGinaxnkU4iJ+t0Lw==~-1~-1~-1',
      'ak_bmsc': '77BA0150D76EDA805313C7FA3136FC92~000000000000000000000000000000~YAAQN2/ZF7XaZtCJAQAAlX3d1BQbkjF6zMF6xMyYa987uEUX6gnTo4Eq/n7LB2YL+HczRU8Gv5OuLHiOA3JbIouQDfgmmLlk0c2+4mTQu2KG/aNUTS4vn7Dwmlvr3ZYl5E2uWd/lZj9pPG14B4GVS8WvPbwO7F3P2Pzd/auoFlhE3ZkAvEsv2dnalLBr8thKVZ/8GAQinznYOlUGTh57zV0RHjSy08VQ7vQuTSgv16c/kWyFky5ZPrIUv87VdYXPMNMfpS+7NCeDGLpnzmo8RGno7xXidY9yGCW90p9wDznhg0oaZyTAL7PLSFQna3DLFod6aiSCuskgeOxS2U+dZofSxIsrS4jIyl+bJouiuakl0nLNaa35mgFA2JtjWlUkxEVlGRBedO5hS2kICGF3TpIlTbzvBgtT80ml0s/D1NrqbofBjctInKqzpYhTfYrerWrlaYDPCojm9hAONQl6TfhhC6p3z6++HiCIuXaGBtBTIETMv3AxwNTWYBBmOMawX/xscGZahoO68WtyDUxQfZYspXEtFucZeyUuKxWDHE2MLju0pRDwqJshQycJAA==',
      'bm_sz': '9F02FAB7566E9EB9A992F08AE51412B4~YAAQN2/ZFy+QZtCJAQAAYaza1BSqan2TYlf5pARx6F5nQ4WYPRA0+nhPldoSDsTL0PRqPNpf735Cw5i5jOHy+VvihNjN5w3MOtDb6JIQ81K9bwHtzuv5veXR9MFskMgfOSnPO/kPLVRfj7+cFt46+obl0V2DACWXw+4jnbfv/oj4N8GcFmEWPQR8XWk3qfdaoRTV9LxtaeFypIkqRTx0RwDlp8XQQwpq6hr0WEvnoL6HVf+s+u26eLv0A/ZS68hkHrDhIOP45DOgXLLcHc1VOQXnJNWoiWXaFauGlC4duKpI/DU=~3490103~4538672',
      'bm_sv': '2F197ACAF1C5574F57C0B1E0DA927057~YAAQN2/ZF+XaZtCJAQAAroXd1BRICt30Vqd5KkQSFDwXLJCwQ8LpCFkC3ul0PZHOrsItfhXNy3THJnCBLB1kDcx7sY3LC4rXI+4XHNm1TiszADEOHe1IMQIbEOLjNnIa98d5bA6zBIX81lglgSInW0YgPKy3xUFUbSDgaGldxW+IRhFXX5zARtCYNVdaeows3abusr9hgGDioII251CT9Y2Cbib7QjWluSCTO49BjDCoWkNfhJ7+HjN3huUAMKP/Ng==~1',
      '_gcl_au': '1.1.1315628660.1691493253',
      '_ga_K2YBNZVRLL': 'GS1.1.1691493253.1.1.1691493456.60.0.0',
      '_ga': 'GA1.1.1216478544.1691493253',
      'HOWTORT': 'cl=1691493346023&r=https%3A%2F%2Fwww.naukri.com%2Ficici-bank-jobs%3Fk%3Dicici%2520bank%26nignbevent_src%3DjobsearchDeskGNB&nu=https%3A%2F%2Flogin.naukri.com%2FnLogin%2FLogin.php&ul=1691493427780&hd=1691493428272',
      'nauk_at': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJkZXZpY2VUeXBlIjoiZDNza3QwcCIsInVkX3Jlc0lkIjoyNDUxNDEzNTUsInN1YiI6IjI1ODYxMDgwNyIsInVkX3VzZXJuYW1lIjoicnQxODE4NTBAZ21haWwuY29tIiwidWRfaXNFbWFpbCI6dHJ1ZSwiaXNzIjoiSW5mb0VkZ2UgSW5kaWEgUHZ0LiBMdGQuIiwidXNlckFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTA5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTE2LjAiLCJpcEFkcmVzcyI6IjEwLjI0My4xOTcuMTkyIiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjI1ODYxMDgwNywidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVkX2VtYWlsVmVyaWZpZWQiOmZhbHNlLCJ1c2VyVHlwZSI6ImpvYnNlZWtlciIsInNlc3Npb25TdGF0VGltZSI6IjIwMjMtMDgtMDhUMTY6NDY6MzkiLCJ1ZF9lbWFpbCI6InJ0MTgxODUwQGdtYWlsLmNvbSIsInVzZXJSb2xlIjoidXNlciIsImV4cCI6MTY5MTQ5Njk5OSwidG9rZW5UeXBlIjoiYWNjZXNzVG9rZW4iLCJpYXQiOjE2OTE0OTMzOTksImp0aSI6IjgxZDlhNTM5YzA4YjQ0YTdiNTA1ZTM0YTliNGFlYjZhIn0.HJbacS_EW_yB2xPEeIMtM2g4QkvXDRC6aE1JksYSoMCg0JHV4AMv5DZhLj3Rf6VmQIuj3DlJ5bgLmmijOdQYLh-VzweWqWXqaoc5VPoet7KhG9jFyRoPLPW5Y_p1vjX-v6fUgD_GZrZVAZUDcMBjyZ3ZVHWig1Nx1uzepr5eSD5-m-YByphnq1SEYbQyUhcSr4sBHpeqCiMS1LfOPXx5jUYC94U0Vyo1XkqwjehsL5Aq1OVUpI58qazoIxQ-qPRLfNJ9LKc3S80QEDhJSlIfRWIROaSsiCxlKzR_Z3zuzi0gGNOixzbo8Y-yVV5IZtagxl3ZTvDOpHcnOPxws-RIBQ',
      'nauk_rt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJkZXZpY2VUeXBlIjoiZDNza3QwcCIsInVkX3Jlc0lkIjoyNDUxNDEzNTUsInN1YiI6IjI1ODYxMDgwNyIsInVkX3VzZXJuYW1lIjoicnQxODE4NTBAZ21haWwuY29tIiwidWRfaXNFbWFpbCI6dHJ1ZSwiaXNzIjoiSW5mb0VkZ2UgSW5kaWEgUHZ0LiBMdGQuIiwidXNlckFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTA5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTE2LjAiLCJpcEFkcmVzcyI6IjEwLjI0My4xOTcuMTkyIiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjI1ODYxMDgwNywidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVkX2VtYWlsVmVyaWZpZWQiOmZhbHNlLCJ1c2VyVHlwZSI6ImpvYnNlZWtlciIsInNlc3Npb25TdGF0VGltZSI6IjIwMjMtMDgtMDhUMTY6NDY6MzkiLCJ1ZF9lbWFpbCI6InJ0MTgxODUwQGdtYWlsLmNvbSIsInVzZXJSb2xlIjoidXNlciIsImV4cCI6MTcyMzAyOTM5OSwidG9rZW5UeXBlIjoicmVmcmVzaFRva2VuIiwiaWF0IjoxNjkxNDkzMzk5LCJqdGkiOiI4MWQ5YTUzOWMwOGI0NGE3YjUwNWUzNGE5YjRhZWI2YSJ9.j9CwGwzMwbnk5wTDj8ZWoU1BaSXnNdtXMqCckUimXnwOSV064hfOZbVsMyUx1qDjjvwVdWnYydxqbKa89H0t2TzzmFp3imASgoYWdPAaUCesmgMGHG48uKrfSBkbriysiiaKNkSPjUk5EKWwxAtlEIP1CcX3qBIbXugkuGRMhcH9ukGGACDUe5uFzAG2zU_FlZYXrkaEqMBtPJ1kf4o9BmkYVi8LYti06u8bU7H_WXggOOpDSyMuVyErN8tU9HjRipxlH4HG6968cXLSMNjkxc1lJIHrbCmnT3nG1cKijJd-DHR60Skzpl85yYPxIFv28fqjjedrslePNlRG84N8Wg',
      'is_login': '1',
      'nauk_sid': '81d9a539c08b44a7b505e34a9b4aeb6a',
      'nauk_otl': '81d9a539c08b44a7b505e34a9b4aeb6a',
      'NKWAP': 'bdbc4d59124cbcecd557176669927dff7f5f95251a959faeff003c62a2e1a36431b890266d0ecd01~bdbc4d59124cbcecd557176669927dff7f5f95251a959faeff003c62a2e1a36431b890266d0ecd01~1~0',
      'MYNAUKRI[UNID]': '6edc228c19f443daa57826bdf59fec47',
      'PS': 'bdbc4d59124cbcecd557176669927dff7f5f95251a959faeff003c62a2e1a36431b890266d0ecd01',
  }
  
  headers = {
      'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
      'Accept': 'application/json',
      'Accept-Language': 'en-GB,en;q=0.5',
      # 'Accept-Encoding': 'gzip, deflate, br',
      'Referer': 'https://www.naukri.com/icici-bank-jobs?k=icici%20bank&nignbevent_src=jobsearchDeskGNB',
      'clientid': 'm0b5',
      'appid': '135',
      'systemid': '135',
      'Content-Type': 'application/json',
      'Cache-Control': 'no-cache, no-store, must-revalidate',
      'Pragma': 'no-cache',
      'Expires': '0',
      'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
      'DNT': '1',
      'Connection': 'keep-alive',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      # Requests doesn't support trailers
      # 'TE': 'trailers',
  }
  
  
  
  
  
  url = 'https://www.naukri.com/jobapi/v3/search'
  
  params = {
      'noOfResults': 20,
      'keyword': 'icici bank',
      'searchType': 'adv_1',
      'urlType': 'search_by_keyword',
      'k': 'icici bank',
      'nignbevent_src': 'jobsearchDeskGNB',
      'l': '',
      'sort': 'r',
      'seoKey': 'icici-bank-jobs',
      'pageNo': page,
      'src': 'loadmore-jobsearchMob',
      'sid': '16914934283128755',
      'clusters': 'wfhType,citiesGid,experience,topGroupId,industryTypeGid,salaryRange,freshness,roleGid,employement,functionalAreaGid,ugCourseGid,jobType,sortBy,employmentType,stipend,internshipDuration'
  }

  response = requests.get(url, params=params, cookies=cookies, headers=headers)
  #response = requests.get(url, params=params,  headers=headers)
  return response.json()
  

# Data=getDataBank(9)
# print(len(Data['jobDetails']))
# print(Data['jobDetails'][11]['title'])

# title: title
#footerplaceholderlabel
# jobdescription
job_details_list = []

for page in range(1, 10):
  Data=getDataBank(page)
  print("Page : ",page)
  for jobresult in range(0,len(Data['jobDetails'])):
    JobTitle=Data['jobDetails'][jobresult]['title']
    JobPosted=Data['jobDetails'][jobresult]['footerPlaceholderLabel']
    JobDescription=Data['jobDetails'][jobresult]['jobDescription']
    print(f"{jobresult} Index : Jobtitle {JobTitle}  JobPosted {JobPosted} " )
    
    job_details_list.append({
            'JobTitle': JobTitle,
            'JobPosted': JobPosted,
            'JobDescription': JobDescription
        })
  df = pd.DataFrame(job_details_list)

  # Save the DataFrame to an Excel file after each iteration
  excel_filename = 'Data.xlsx'
  df.to_excel(excel_filename, index=False)
#   job_details_list.clear()