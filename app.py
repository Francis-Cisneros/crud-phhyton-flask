from flask import Flask
from flask import render_template,request,redirect,url_for,flash
from flaskext.mysql import MySQL



app =Flask(__name__)
app.secret_key="Develoteca"

mysql= MySQL()
#CreamoS la base de datos en MySQL
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='productos'
mysql.init_app(app)


@app.route('/')
def index():
    sql="Select *from `producto`;"
    #Establecemos una conexión con MySQL
    conn=mysql.connect()
    #Almacenamiento
    cursor=conn.cursor()
    #Ejecución de consultas
    cursor.execute(sql)
    producto=cursor.fetchall()
    print(producto)
    conn.commit()
    #Retorno a nuestro index productos
    return render_template('productos/index.html',producto=producto)

@app.route('/destroy/<string:id>')
def destroy(id):
    #Establecemos conexión con MySQL
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("delete from producto where codigo in(%s)",(id))
    conn.commit()
    #Retorna al router
    return redirect('/')

@app.route('/edit/<string:id>')
def edit(id):
    #Establecemos conexión con MySQL
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("Select  *from producto where codigo in(%s)",(id))
    producto=cursor.fetchall()
    conn.commit()
    print(producto)
    #Retorno a nuestro index productos
    return render_template('productos/edit.html',producto=producto)

@app.route('/update', methods=['POST'])
def update():
    _codigo=request.form['txtcodigo']
    _descripcion=request.form['txtdescripcion']
    _categoria=request.form['cbocategoria']
    _precio=request.form['txtprecio']
    _stock=request.form['txtcantidad']
    sql="UPDATE `producto` SET `descripcion`=%s,`categoria`=%s,`precio`=%s,`stock`=%s WHERE codigo in(%s)"
    datos=(_descripcion,_categoria,_precio,_stock,_codigo)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    #Retorna al router
    return redirect("/")

@app.route('/create')
def create():
    return render_template('productos/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _codigo=request.form['txtcodigo']
    _descripcion=request.form['txtdescripcion']
    _categoria=request.form['cbocategoria']
    _precio=request.form['txtprecio']
    _stock=request.form['txtcantidad']
    if _codigo=='' or _descripcion=='' or _categoria=='' or _precio=='' or _stock=='' :
       conn=mysql.connect()
       cursor=conn.cursor()
       cursor.execute("SELECT RIGHT(MAX(codigo),1)+1 FROM `producto`")
       codigo=cursor.fetchone()
       codi=int(codigo[0])
       if codi<=9:
         cod='C00'+str(codi)
       elif codi<=99:
         cod='C0'+str(codi)
       elif codi<=999:
         cod='C'+str(codi)
       conn.commit()
       flash('Ingrese los datos :)')
       #Envio al html productos
       return render_template('productos/create.html',cod=cod)

    sql="INSERT INTO `producto`(`codigo`, `descripcion`, `categoria`, `precio`, `stock`) VALUES (%s,%s,%s,%s,%s);"
    #Enviar datos
    datos=(_codigo,_descripcion,_categoria,_precio,_stock)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

@app.route('/generar')
def generar():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT RIGHT(MAX(codigo),1)+1 FROM `producto`")
    codigo=cursor.fetchone()
    codi=int(codigo[0])
    if codi<=9:
        cod='C00'+str(codi)
    elif codi<=99:
        cod='C0'+str(codi)
    elif codi<=999:
        cod='C'+str(codi)
    conn.commit()
    return render_template('productos/create.html',cod=cod)

if __name__== '__main__':
    #Corremos el producto
    app.run(debug=True)
