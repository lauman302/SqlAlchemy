from datetime import datetime

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, MetaData,
                        Numeric, String, Table, create_engine, insert)

metadata = MetaData()

cookies = Table('cookies', metadata,
 Column('cookie_id', Integer(), primary_key=True),
 Column('cookie_name', String(50), index=True),
 Column('cookie_recipe_url', String(255)),
 Column('cookie_sku', String(55)),
 Column('quantity', Integer()),
 Column('unit_cost', Numeric(12, 2))
)

users = Table('users', metadata,
 Column('user_id', Integer(), primary_key=True),
 Column('customer_number', Integer(), autoincrement=True),
 Column('username', String(15), nullable=False, unique=True),
 Column('email_address', String(255), nullable=False),
 Column('phone', String(20), nullable=False),
 Column('password', String(25), nullable=False),
 Column('created_on', DateTime(), default=datetime.now),
 Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

orders = Table('orders', metadata,
 Column('order_id', Integer(), primary_key=True),
 Column('user_id', ForeignKey('users.user_id'))
)

line_items = Table('line_items', metadata,
 Column('line_items_id', Integer(), primary_key=True),
 Column('order_id', ForeignKey('orders.order_id')),
 Column('cookie_id', ForeignKey('cookies.cookie_id')),
 Column('quantity', Integer()),
 Column('extended_cost', Numeric(12, 2))
)


engine = create_engine('sqlite:///E:\\Dev\\db_test\db.sqlite3')
# metadata.create_all(engine)
connection = engine

ins = insert(cookies).values(
 cookie_name="chocolate chip",
 cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
 cookie_sku="CC01",
 quantity="12",
 unit_cost="0.50"
)

ins = cookies.insert()
result = connection.execute(
 ins,
 cookie_name='dark chocolate chip',
 cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
 cookie_sku='CC02',
  quantity='1',
 unit_cost='0.75'
)
result.inserted_primary_key


engine = create_engine('sqlite:///E:\\Dev\\db_test\db.sqlite3')
# metadata.create_all(engine)
connection = engine

ins = cookies.insert()
inventory_list = [
 {
 'cookie_name': 'peanut butter',
 'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
 'cookie_sku': 'PB01',
 'quantity': '24',
 'unit_cost': '0.25'
 },
 {
 'cookie_name': 'oatmeal raisin',
 'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
 'cookie_sku': 'EWW01',
 'quantity': '100',
 'unit_cost': '1.00'
 }
]
result = connection.execute(ins, inventory_list)
print(str(result))

from sqlalchemy.sql import select

engine = create_engine('sqlite:///E:\\Dev\\db_test\db.sqlite3')
# metadata.create_all(engine)
connection = engine

s = select([cookies])
rp = connection.execute(s)
results = rp.fetchall()
print(results)

from sqlalchemy import desc
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(desc(cookies.c.quantity))


from sqlalchemy.sql import func
s = select([func.sum(cookies.c.quantity)])
rp = connection.execute(s)
print(rp.scalar())

from sqlalchemy.sql.functions import count

s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
rp = connection.execute(s)
record = rp.first()
print(record.keys())
print(record.inventory_count)

s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
rp = connection.execute(s)
record = rp.first()
print(record.items())

s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
s = s.limit(2)
rp = connection.execute(s)
print([result.cookie_name for result in rp])

s = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])
for row in connection.execute(s):
 print(row)

 from sqlalchemy import cast
s = select([cookies.c.cookie_name,
 cast((cookies.c.quantity * cookies.c.unit_cost),
 Numeric(12,2)).label('inv_cost')])
for row in connection.execute(s):
 print('{} - {}'.format(row.cookie_name, row.inv_cost))


from sqlalchemy import and_, or_, not_
s = select([cookies]).where(
 and_(
 cookies.c.quantity > 23,
 cookies.c.unit_cost < 0.40
 )
)
for row in connection.execute(s):
 print(row.cookie_name)

 from sqlalchemy import and_, or_, not_
s = select([cookies]).where(
 or_(
 cookies.c.quantity.between(10, 50),
 cookies.c.cookie_name.contains('chip')
 )
)
for row in connection.execute

from sqlalchemy import update
u = update(cookies).where(cookies.c.cookie_name == "chocolate chip")
u = u.values(quantity=(cookies.c.quantity + 120))
result = connection.execute(u)
print(result.rowcount)
s = select([cookies]).where(cookies.c.cookie_name == "chocolate chip")
result = connection.execute(s).first()
for key in result.keys():
 print('{:>20}: {}'.format(key, result[key]))


 from sqlalchemy import delete
u = delete(cookies).where(cookies.c.cookie_name == "dark chocolate chip")
result = connection.execute(u)
print(result.rowcount)
s = select([cookies]).where(cookies.c.cookie_name == "dark chocolate chip")
result = connection.execute(s).fetchall()
print(len(result))


from datetime import datetime
from sqlalchemy import (Column, DateTime, ForeignKey, Integer, MetaData,
                        Numeric, String, Table, create_engine, insert)
metadata = MetaData()

engine = create_engine('sqlite:///E:\\Dev\\db_test\db.sqlite3')
# metadata.create_all(engine)
connection = engine

users = Table('users', metadata,
 Column('user_id', Integer(), primary_key=True),
 Column('customer_number', Integer(), autoincrement=True),
 Column('username', String(15), nullable=False, unique=True),
 Column('email_address', String(255), nullable=False),
 Column('phone', String(20), nullable=False),
 Column('password', String(25), nullable=False),
 Column('created_on', DateTime(), default=datetime.now),
 Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

orders = Table('orders', metadata,
 Column('order_id', Integer(), primary_key=True),
 Column('user_id', ForeignKey('users.user_id'))
)

line_items = Table('line_items', metadata,
 Column('line_items_id', Integer(), primary_key=True),
 Column('order_id', ForeignKey('orders.order_id')),
 Column('cookie_id', ForeignKey('cookies.cookie_id')),
 Column('quantity', Integer()),
 Column('extended_cost', Numeric(12, 2))
)


customer_list = [
 {
 'username': 'cookiemon',
 'email_address': 'mon@cookie.com',
 'phone': '111-111-1111',
 'password': 'password'
},
 {
 'username': 'cakeeater',
 'email_address': 'cakeeater@cake.com',
 'phone': '222-222-2222',
 'password': 'password'
 },
 {
 'username': 'pieguy',
 'email_address': 'guy@pie.com',
 'phone': '333-333-3333',
 'password': 'password'
 }
]
#ins = users.insert()
# result = connection.execute(ins, customer_list)


ins = insert(orders).values(user_id=1, order_id=1)
result = connection.execute(ins)
ins = insert(line_items)
order_items = [
 {
 'order_id': 1,
 'cookie_id': 1,
 'quantity': 2,
 'extended_cost': 1.00
 },
 {
 'order_id': 1,
 'cookie_id': 3,
 'quantity': 12,
 'extended_cost': 3.00
 }
]
result = connection.execute(ins, order_items)
ins = insert(orders).values(user_id=2, order_id=2)
result = connection.execute(ins)
ins = insert(line_items)
order_items = [
 {
 'order_id': 2,
 'cookie_id': 1,
 'quantity': 24,
 'extended_cost': 12.00
 },
 {
 'order_id': 2,
 'cookie_id': 4,
 'quantity': 6,
 'extended_cost': 6.00
 }
]
result = connection.execute(ins, order_items)

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders))
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()
for row in result:
 print(row)


columns = [orders.c.order_id, users.c.username, users.c.phone,
cookies.c.cookie_name, line_items.c.quantity,
line_items.c.extended_cost]
cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(orders.join(users).join(
line_items).join(cookies)).where(users.c.username ==
'cookiemon')
result = connection.execute(cookiemon_orders).fetchall()
for row in result:
    print(row)

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders))
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()
for row in result:
    print(row)

 def get_orders_by_customer(cust_name):
    columns = [orders.c.order_id, users.c.username, users.c.phone,
    cookies.c.cookie_name, line_items.c.quantity,
    line_items.c.extended_cost]
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(
    users.join(orders).join(line_items).join(cookies))
    cust_orders = cust_orders.where(users.c.username == cust_name)
    result = connection.execute(cust_orders).fetchall()
    return result
get_orders_by_customer('cakeeater')

def get_orders_by_customer(cust_name, shipped=None, details=False):
    columns = [orders.c.order_id, users.c.username, users.c.phone]
    joins = users.join(orders)
    if details:
    columns.extend([cookies.c.cookie_name, line_items.c.quantity,
    line_items.c.extended_cost])
    joins = joins.join(line_items).join(cookies)
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(joins)
    cust_orders = cust_orders.where(users.c.username == cust_name)
    if shipped is not None:
        cust_orders = cust_orders.where(orders.c.shipped == shipped)
        result = connection.execute(cust_orders).fetchall()
    return result

get_orders_by_customer('cakeeater')


