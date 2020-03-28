import obd

connection = obd.OBD()

c = obd.commands.RPM

response  = connection.query(c)
print(response.value)

connection.close()