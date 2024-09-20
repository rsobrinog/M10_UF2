# import

# sql_read



# fetchAll()

# for i in result:





############################################## SOL ################################################
import conn as ping

sql_read = ''' SELECT user_id, user_name, user_surname, user_age, user_email
            FROM public.users '''


ping.connection.execute(sql_read)

result = ping.connection.fetchAll()

for i in result:
    print("user id: ", i[0])
    print("name: ", i[1])
    print("surname: ", i[2])
    print("age: ", i[3])
    print("email: ", i[4] + "\n\n")
