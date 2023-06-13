def db_wrtr(total, n2):
    try:
        import time
        import mysql.connector
        from mysql.connector import connect, Error 
        from . import config_real
        print('hello db_writerr faci')

        config = {
            'user': config_real.user,
            'password': config_real.password,
            'host': config_real.host,
            'port': config_real.port,
            'database': config_real.database,      
        }
        for _ in range(5):
            try:
                conn = mysql.connector.connect(**config)      
                print("Writerr connection established2 facility")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue
            
            try:
                cursor = conn.cursor() 
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue
            break
        try:
            print(len(total))
            resFacilities = []          
            whiteList = []
            n = int(int(n2)/1000)
        except:
            pass
        try:
            for t in total:
                try:
                    resFacilities += t
                except:
                    continue
            resFacilities = list(filter(None, resFacilities))
            if len(resFacilities) == 0:
                try:
                    semaforr(conn, cursor, n)
                except:
                    pass 
                return print('len_=0')
            print(f"before___{len(resFacilities)}")
            resFacilities = remove_repetitions(resFacilities)
            print(f"arter___{len(resFacilities)}")    
        except:
            pass  

        try:
            whiteList = writerr_table(conn, cursor, resFacilities)
        except:
            pass
        try:
            changing_hotelsCritery(cursor, conn, whiteList)   
        except:
            pass 

        # try:
        #    semaforr(conn, cursor, n)
        # except:
        #     pass
 
        try:
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    except:
        pass
    return

def writerr_table(conn, cursor, resFacilities):
    faci_white = []
    faci_white_add = []
    faci_white_set = set()
    faci_white_batch_set = set()

    try:
        query3 = "INSERT INTO upz_hotels_facilityties (hotelid, facilitytype_id, name, facilitytype_name, hotelfacilitytype_id, uniq) VALUES (%s, %s, %s, %s, %s, %s)"

        batch_size = 400
        batch_values = []

        for item in resFacilities:
            try:
                values = (item["hotelid"], item["facilitytype_id"], item["name"], item["facilitytype_name"], item["hotelfacilitytype_id"], item["uniq"])
                batch_values.append(values)
                faci_white_batch_set.add(item["hotelid"])

                if len(batch_values) >= batch_size:
                    try:
                        cursor.executemany(query3, batch_values)
                        conn.commit()
                        faci_white_set.update(faci_white_batch_set)
                        faci_white_batch_set = set()
                        batch_values = []
                    except Exception as ex:
                        print(f"117___{ex}")                        
                        faci_white_add = insert_rows_individually_faci(conn, cursor, query3, batch_values)
                        faci_white += faci_white_add
                        faci_white_batch_set = set()
                        batch_values = []
                        continue 

            except Exception as ex:
                print(ex)
                continue

        if batch_values:
            try:
                cursor.executemany(query3, batch_values)
                conn.commit()
                faci_white_set.update(faci_white_batch_set)
            except Exception as ex:
                print(f"130___{ex}")
                faci_white_add = insert_rows_individually_faci(conn, cursor, query3, batch_values)
                faci_white += faci_white_add
                faci_white_batch_set = set()
    except:
        pass

    try:
        faci_white += list(faci_white_set)
    except:
        pass

    return faci_white


def insert_rows_individually_faci(conn, cursor, query, data):
    faci_white_set = set()
    faci_white = []
    try:
        data = eval(data)
    except:
        data = data
    for item in data:
        try:
            values = item
            cursor.execute(query, values)            
            faci_white_set.add(item[0])
        except Exception as ex:
            # print(f"204___: {ex}")
            continue
    try:
        conn.commit()
    except:
        faci_white = []
        return faci_white
    faci_white = list(faci_white_set)
    return faci_white


def changing_hotelsCritery(cursor, conn, whiteList):
    try:       
        query12 = "UPDATE upz_hotels SET facility = %s WHERE hotel_id = %s"

        for item in whiteList:
            try:
                try:
                    find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"                     
                    cursor.execute(find_query, (item,))                      
                    row = cursor.fetchone()                      
                except Exception as ex:
                    print(f"db_writerr__str87__{ex}")

                if row:
                    try:                      
                        cursor.execute(query12, (1, item))                      
                    except Exception as ex:
                        print(f"db_writerr__str90__{ex}")

            except Exception as ex:
                print(f"db_writerr__str95__{ex}")
                continue
        conn.commit()           

    except Exception as ex:
        print(ex)

    return

def semaforr(conn, cursor, n):
    print(n)
    try:
        select_queryF = "SELECT facility_flag FROM hotels_simafor WHERE id = %s"
        cursor.execute(select_queryF, (n,))
        row = cursor.fetchone()

        if row:
            update_query = "UPDATE hotels_simafor SET facility_flag = %s WHERE id = %s"
            cursor.execute(update_query, (1, n))
            conn.commit()  
            print('hello simafor commit!')      

    except Exception as ex:
        print(ex)

def remove_repetitions(data):
    unique_values = set()
    result = []
    for item in data:
        unil_value = item.get("uniq")
        if unil_value not in unique_values:
            result.append(item)
            unique_values.add(unil_value)
    return result

 

# python db_writerrr.py




# def db_wrtr(total, n2):
#     try:
#         import time
#         import mysql.connector
#         from mysql.connector import connect, Error 
#         from . import config_real
#         print('hello db_writerr facilities')

#         config = {
#             'user': config_real.user,
#             'password': config_real.password,
#             'host': config_real.host,
#             'port': config_real.port,
#             'database': config_real.database,      
#         }
#         for _ in range(5):
#             try:
#                 conn = mysql.connector.connect(**config)      
#                 print("Writerr connection established2")
#             except Error as e:
#                 print(f"Error connecting to MySQL: {e}")
#                 time.sleep(3)
#                 continue
            
#             try:
#                 cursor = conn.cursor() 
#             except Error as e:
#                 print(f"Error connecting to MySQL: {e}")
#                 time.sleep(3)
#                 continue
#             break
#         try:
#             print(len(total))
#             resFacilities = []
#             whiteList_set = set()
#             whiteList = []
#             n = n2/1000
#         except:
#             pass 

#         try:
#             for t in total:
#                 try:
#                     resFacilities += t
#                 except:
#                     continue
#             resFacilities = list(filter(None, resFacilities))
#             if len(resFacilities) == 0:
#                 try:
#                     semaforr(conn, cursor, n)
#                 except:
#                     pass 
#                 return print('len_=0')
#             print(f"before___{len(resFacilities)}")
#             resFacilities = remove_repetitions(resFacilities)
#             print(f"arter___{len(resFacilities)}")

#             try:
#                 query3 = "INSERT INTO upz_hotels_facilityties (hotelid, facilitytype_id, name, facilitytype_name, hotelfacilitytype_id, uniq) VALUES (%s, %s, %s, %s, %s, %s)"

#                 for item in resFacilities:
#                     try:
#                         values = (item["hotelid"], item["facilitytype_id"], item["name"], item["facilitytype_name"], item["hotelfacilitytype_id"], item["uniq"])
#                         cursor.execute(query3, values)
#                         whiteList_set.add(item["hotelid"])
                        
#                     except Exception as ex:
#                         print(f"83_writerr__{ex}")
#                         continue
#                 conn.commit()
#             except:
#                 pass
#             whiteList = list(whiteList_set)

#             try:
#                 query9 = "UPDATE upz_hotels SET facility = %s WHERE hotel_id = %s"

#                 for item in whiteList:
#                     try:
#                         try:
#                             find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"               
#                             cursor.execute(find_query, (item,))                     
#                             row = cursor.fetchone()                   
#                         except Exception as ex:
#                             print(f"db_writerr__str87__{ex}")

#                         if row:
#                             try:                
#                                 cursor.execute(query9, (1, item))                       
#                             except Exception as ex:
#                                 print(f"db_writerr__str90__{ex}")

#                     except Exception as ex:
#                         print(f"db_writerr__str95__{ex}")
#                         continue

#                 conn.commit()
#             except Exception as ex:
#                 print(ex)  

#             try:
#                 semaforr(conn, cursor, n)
#             except:
#                 pass          

#         except Exception as ex:
#             print(ex)

#         try:
#             cursor.close()
#             conn.close()
#         except Error as e:
#             print(f"Error connecting to MySQL: {e}")
#     except:
#         pass

#     return 

# def semaforr(conn, cursor, n):
#     print(n)
#     try:
#         select_queryF = "SELECT facility_flag FROM hotels_simafor WHERE id = %s"
#         cursor.execute(select_queryF, (n,))
#         row = cursor.fetchone()

#         if row:
#             update_query = "UPDATE hotels_simafor SET facility_flag = %s WHERE id = %s"
#             cursor.execute(update_query, (1, n))
#             conn.commit()  
#             print('hello simafor commit!')      

#     except Exception as ex:
#         print(ex)


# def remove_repetitions(data):
#     unique_values = set()
#     result = []
#     for item in data:
#         unil_value = item.get("uniq")
#         if unil_value not in unique_values:
#             result.append(item)
#             unique_values.add(unil_value)
#     return result




# Полные тексты
# id	
# fotos_flag	
# deskription_flag	
# facility_flag По возрастанию 1	
# otziv_flag	
# room_flag	
# rooms_block_flag

# total = None
# db_opener(total)

# python db_writerrr.py



# resRoomHighlights = []
# with open('result_description__interval_0__1120__Items_982.json', 'r') as f:
#     data_result_descript = json.load(f)
# with open('photos__12_05_2023__16_32__443.json', 'r') as f:
#     resPhoto = json.load(f) 
# with open('facilities__12_05_2023__16_32__1030.json', 'r') as f:
#     resFacilities = json.load(f) 
# with open('room__12_05_2023__16_31__62.json', 'r') as f:
#     resRooms = json.load(f) 
# with open('room_block__12_05_2023__16_31__62.json', 'r') as f:
#     resRoomsBlock = json.load(f)
    # print(resRoomsBlock)


            # query = "UPDATE result_description_test1 SET hotelid = %s, enusname = %s"
