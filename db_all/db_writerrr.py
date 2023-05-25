def db_wrtr(total, n2):
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    print('hello db_writerr facilities')

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Writerr connection established2")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    print(len(total))
    resFacilities = []
    whiteList_set = set()
    whiteList = []
    n = n2/1000

    try:
        for t in total:
            try:
                resFacilities += t
            except:
                continue
        resFacilities = list(filter(None, resFacilities))
        if len(resFacilities) == 0:
            return

        try:
            query3 = "INSERT INTO upz_hotels_facilityties_test1 (hotelid, facilitytype_id, name, facilitytype_name, hotelfacilitytype_id, uniq) VALUES (%s, %s, %s, %s, %s, %s)"

            for item in resFacilities:
                try:
                    values = (item["hotelid"], item["facilitytype_id"], item["name"], item["facilitytype_name"], item["hotelfacilitytype_id"], item["uniq"])
                    cursor.execute(query3, values)
                    whiteList_set.add(item["hotelid"])
                    
                except Exception as ex:
                    print(ex)
                    continue
            conn.commit()
        except:
            pass
        try:
            query3 = "INSERT INTO upz_hotels_facilityties (hotelid, facilitytype_id, name, facilitytype_name, hotelfacilitytype_id, uniq) VALUES (%s, %s, %s, %s, %s, %s)"

            for item in resFacilities:
                try:
                    values = (item["hotelid"], item["facilitytype_id"], item["name"], item["facilitytype_name"], item["hotelfacilitytype_id"], item["uniq"])
                    cursor.execute(query3, values)
                    whiteList_set.add(item["hotelid"])
                    
                except Exception as ex:
                    print(ex)
                    continue
            conn.commit()
        except:
            pass
        whiteList = list(whiteList_set)

        try:
            query9 = "UPDATE upz_hotels SET facility = %s WHERE hotel_id = %s"

            for item in whiteList:
                try:
                    try:
                        find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"
                        # print("true1")
                        cursor.execute(find_query, (item,))
                        # print("true2")
                        row = cursor.fetchone()
                        # print("true3")
                    except Exception as ex:
                        print(f"db_writerr__str87__{ex}")

                    if row:
                        try:
                        #    print('true4')
                           cursor.execute(query9, (1, item))
                        #    print('true5')
                        except Exception as ex:
                            print(f"db_writerr__str90__{ex}")

                except Exception as ex:
                    print(f"db_writerr__str95__{ex}")
                    continue

            conn.commit()
        except Exception as ex:
            print(ex)
        
        try:
            select_queryF = "SELECT facility_flag FROM hotels_simafor WHERE id = %s"
            cursor.execute(select_queryF, (n,))
            row = cursor.fetchone()

            if row:
                update_query = "UPDATE hotels_simafor SET facility_flag = %s WHERE id = %s"
                cursor.execute(update_query, (1, n))
                conn.commit()        

        except Exception as ex:
            print(ex)
    except Exception as ex:
        print(ex)


    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return 



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
