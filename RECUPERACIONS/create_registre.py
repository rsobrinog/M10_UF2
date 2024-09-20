import 

sql_insert = 


executre(sql)

commit()


############################################## SOL ################################################
import conn as ping

sql_insert = ''' INSERT INTO public.users(user_id, user_name, user_surname, user_age, user_email) 
            VALUES ('1', 'Roger', 'Sobrino', '40', 'roger@roger.com') '''


ping.connection.execute(sql_insert)

ping.conn.commit()