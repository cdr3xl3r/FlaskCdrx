ip = "192.168.0.200"

from website import create_app, process as P
app = create_app()
P.printProccess("<trigger>")
trigger = input("Do you want to launch your website? Y/n")
if trigger == "":
    P.printProccess("debug")
    app.run(debug=True,host='localhost', port=80)
    exit()
elif trigger == "y" or trigger == "Y":
    P.printProccess(f"hosting on: debug off {ip}")
    app.run(host=ip, port=80)
    exit()
else:
    P.printProccess("trigger error")
    app.aborter()
        
