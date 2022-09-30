a=0
b=0
c=0
d=0
e=0
f=0
print("Escuel de Belleza ")
print("1) ver inf de la empresa")
print("2) hacer una compra ")
print("3) agendar una cita ")
print("4) servicio al cliente ")
menu=int(input("Por favor digite una de las opciones vistas anteriormente "))
if menu==1 :
    print("Somos una empresa dedicada a frecer servicios de cuidado personal y estética, atendiendo a las demandas y necesidades de los clientes")
    print("informacion de contacto  ")
    print("via telefonica 3195199095")
    print("Correo electronico saladebelleza@gmail.com")
    print("Encuentranos en as redes como")
    print("facebook  @saladebelleza")
    print("Instagram  @saladebelleza01")
    print("Encuentranos en la Av. de las Americas Carrera 6 # 8-45 local 102")
elif menu==2:
    print("Tenemos los siguientes productos")
    print("a.) Crema para peinar  $15.000")
    print("b.) Shampoo con Savila  $25.000")
    print("c.) Shampoo Anti caspa   $35.000")
    print("d.) Shampoo Anti caspa   $35.000")
    compras=str(input("Por favor coloque el numero del producto que escogio "))
    if compras==a and compras==b and compras==c and compras==d :
        print("Gracias por su compra ")
        print("Que lo disfrute :)")
elif menu==3:
    print("Que tratamineto se desea hacer")
    print("e.) Keratina ")
    print("f.) corte de cabello ")
    trata=str(input("Por favor escoga un tratamineto"))
    if trata==1 and trata==2:
        print("EScoga la fecha y hora de la cita ")
        print("Citas disponibles ")
        print("1.) lunes 4:00 pm")
        print("2.) martes  6:00 pm")
        print("3.) juves  8:00 am")
        print("4.) sabado  10:00 am")
        cita=int(input("Por favor escoga una de las citas disponibles"))
        if cita==1 and cita==2 and cita==3 and cita==4:
            print("Su cita a sido generada con exito!")
elif menu==4:
    print(" Bienvenido al Aseor al cliente ")
    print("que tramite desea solicitar")
    print("1.) Devolucion")
    print("2.) Reasignar cita")
    print("3.) Cancelar cita ")  
    #aqui falta