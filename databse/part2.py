import mysql.connector

class DatabaseException(Exception):
    pass
def connect_db():
     try:
         conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="jassmof7",
         database="business_management"
         )
         print("✔ Connexion réussie")
         return conn
     except Exception as e:
         print("Erreur :", e)
     return None

conn = connect_db()

class ProductDAO:
    def __init__(self, id, name, category, price, quantity_in_stock):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def save(self, conn):
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO products (name,category,price,quantity_in_stock) VALUES(%s,%s,%s,%s)",
                (self.name, self.category,self.price,self.quantity_in_stock))
            conn.commit()
            print("Product saved")
        except:
            conn.rollback()
            print("Erreur ")
        finally:
            conn.close()

    def update(self,conn):
        cur = conn.cursor()
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE products SET name=%s,category=%s,price=%s,quantity_in_stock=%s WHERE id=%s",
                (self.name, self.category, self.price, self.quantity_in_stock, self.id))
            conn.commit()
            print("Product updated")
        except :
            conn.rollback()
            print("Erreur ")
        finally:
            conn.close()

    def delete(self,conn):
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM products WHERE id=%s", (id,))
            conn.commit()
        except Exception as e:
            conn.rollback(); raise DatabaseException("delete product", str(e))
        finally:
            conn.close()

    def find_by_id(self, conn, id):
        cursor = conn.cursor
        try:
            cursor.execute("SELECT * FROM Products WHERE product_id=%s ", (id,))
            row = cursor.fetchall()
            print(row)
        except:
            conn.rollback()
            print("Erreur — ID non trouvée!")

    class CustomerDAO:
        def __init__(self, id, name, email):
            self.id = id
            self.name = name
            self.email = email

        def save(self, conn):
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO Customer (customer_id,last_name,email) VALUES (%s, %s, %s) ",
                               (self.id, self.name, self.email))
                conn.commit()
                print("Customer saved")
            except:
                conn.rollback()
                print("Erreur, no modification applied")

        def update(self, conn):
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE Customer SET name=%s, email=%s WHERE customer_id=%s",
                               (self.name, self.email, self.id))
                conn.commit()
                print("Customer updated ")
            except:
                conn.rollback()
                print("Erreur, no modification applied")

        def delete(self, conn):
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE * FROM Customer WHERE customer_id=%s", (self.id,))
                conn.commit()
                print("Customer deleted ")
            except:
                conn.rollback()
                print("Erreur, no modification applied")

        def find_by_id(self, conn, id):
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM Customer WHERE customer_id=%s ", (id,))
                row = cursor.fetchall()
                print(row)
            except:
                conn.rollback()
                print("Erreur — ID non trouvée!")

    class OrderDAO:
        def __init__(self, id, customer_id, order_date, orderitem_id):
            self.id = id
            self.customer_id = customer_id
            self.order_date = order_date
            self.orderitem_id = orderitem_id

        def save(self, conn):
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO Order (order_id,customer_id,order_date,orderitem_id) VALUES (%s, %s, %s,%s) ",
                    (self.id, self.customer_id, self.order_date, self.orderitem_id))
                conn.commit()
                print("Order saved ")
            except:
                conn.rollback()
                print("Error,no modification applied")

        def update(self, conn):
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE Order SET customer_id=%s, order_date=%s, orderitem_id=%s WHERE order_id=%s",
                               (self.customer_id, self.order_date, self.orderitem_id, self.id))
                conn.commit()
                print("Order updated ")
            except:
                conn.rollback()
                print("Error, no modification applied ")

        def delete(self, conn):
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE * FROM Order WHERE order_id=%s", (self.id,))
                conn.commit()
                print("Order deleted ")
            except:
                conn.rollback()
                print("Error, no modification applied ")

        def find_by_id(self, conn, id):
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM Order WHERE order_id=%s ", (id,))
                row = cursor.fetchall()
                print(row)
            except:
                conn.rollback()
                print("Error, no modification applied")