def products_select_safe(category = ""):
    mydb = mysql.connector.connect(
        host="containers-us-west-101.railway.app",
        user="root",
        password="6G74WClR1fVadVdFKqFX",
        database="railway",
        port=7171
    )
    mycursor = mydb.cursor()
    table_name = 'products'
    mycursor.execute("SELECT * FROM %s WHERE category = %%s AND released = 1" % table_name,[category])
    myresult = mycursor.fetchall()
    return myresult


def products_select_sp(category = ""):
    mydb = mysql.connector.connect(
        host="containers-us-west-101.railway.app",
        user="root",
        password="6G74WClR1fVadVdFKqFX",
        database="railway",
        port=7171
    )
    args = (category,)
    cursor = mydb.cursor()
    cursor.callproc('sp_products_by_category', args)
    for result in cursor.stored_results():
        product = result.fetchall()
    json_products = json.dumps(product)
    return json_products