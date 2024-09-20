# import 


# sql = 


# execute(sql)

# commit()





########################### SOL ############################
import conn as ping


sql = ''' CREATE TABLE public.USERS(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_surname VARCHAR(255) NOT NULL,
            user_age BIGINT NOT NULL,
            user_email VARCHAR(255) NOT NULL,                     
)'''


ping.connection.execute(sql)

ping.conn.commit()
