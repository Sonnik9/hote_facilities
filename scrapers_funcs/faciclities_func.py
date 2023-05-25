from bs4 import BeautifulSoup
import re
from . import facilities_data

def page_scraper_facilities(resHtml, hotelid):
    # print('hello faci')
    result_facilities_upz = []
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")     
    except Exception as ex:
        # print(f"str102___{ex}") 
        return None

    try:     
        span_tag = soup1.find('span', attrs={'data-testid': 'facility-group-icon'})
        parent_div = span_tag.find_parent('div')
        parent_class = parent_div['class'][0]
        parent_div_main = parent_div.find_parent('div').find_parent('div').find_parent('div').get('class')[0]
        facilities_list = soup1.find_all('div', class_=parent_div_main)
        for item in facilities_list:

            try:
                try:
                    facilitytype_name = ''                
                    facilitytype_name = item.find('div', class_= parent_class).get_text().strip()
                except Exception as ex:
                    facilitytype_name = '' 
                    # print(f"str129___{ex}")
                try:
                    facilitytype_id = ''
                    for key, value in facilities_data.hotelfacility_gen_en.items():
                        if re.search(f'{value}', facilitytype_name):
                            facilitytype_id = key
                            break
                    if facilitytype_id == '':
                        for key, value in facilities_data.hotelfacility_gen_en.items():
                            if re.search(f'{facilitytype_name}', value):
                                facilitytype_id = key
                                break
                except Exception as ex:
                    facilitytype_id = ''         

                try:
                    name = ''
                    uniq = ''               
                    name_block = item.find_all('li')
                    for i, li in enumerate(name_block):
                        uniq = f"{hotelid}_{i}"
                        try:
                            name = li.get_text(strip=True, separator="\n")   
                        except:
                            pass            
                        try:
                            hotelfacilitytype_id = ''
                            for key, value in facilities_data.hotelfacility_local_en.items():
                                if re.search(f'{value}', name):
                                    hotelfacilitytype_id = key
                                    break
                            
                            if  hotelfacilitytype_id == '':
                                for key, value in facilities_data.hotelfacility_local_en.items():
                                    if re.search(f'{name}', value):
                                        hotelfacilitytype_id = key
                                        break
                            if  hotelfacilitytype_id == '':
                                for key, value in facilities_data.roomfacility.items():
                                    if re.search(f'{value}', name):
                                        hotelfacilitytype_id = key
                                        break
                            if  hotelfacilitytype_id == '':
                                for key, value in facilities_data.roomfacility.items():
                                    if re.search(f'{name}', value):
                                        hotelfacilitytype_id = key
                                        break
                        except:
                            hotelfacilitytype_id = 'not found'
                        
                        result_facilities_upz.append({  
                            "hotelid": int(hotelid),
                            "facilitytype_id": int(facilitytype_id),  
                            'name': name,     
                            "facilitytype_name": facilitytype_name,
                            'hotelfacilitytype_id': int(hotelfacilitytype_id),
                            "uniq": uniq, 
                        })
                except Exception as ex:
                  
                    # print(f"str129___{ex}") 
                    pass
            except:
                continue
           
    except Exception as ex:
        # print(f"str226___{ex}") 
        return None
    try:
        return result_facilities_upz
    except:
        return None




