1. Se crearon cuatro modelos conforme al diseño de la bd, se implemento componentes de serializadores que nos ofrece django restframework lo cual nos permite que las estructuras complejas en y los modelos de nuestro proyecto en django se conviertan a estructuras nativas de python y se conviertan facilmente a formato JSON o XML

2. Se creo una vista diferente para cada clase del modelo donde se realiza el crud completo de las entidades.

3. Se creo un archivo de rutas dentro de la app ventas donde se crean todas las urls para realizar las diferentes consultas.


4. Para la vista de clientes se pueden consultar todos los clientes de la bd, tambien consultar por id, por nombre y por apellido.

CLIENTS
 * METODO GET (ejemplo de consultas)
   * Consulta todos los clientes 
   http://127.0.0.1:8000/api/clients
   * Consulta todos los clientes por id 
   http://127.0.0.1:8000/api/clients/1
   * Consulta los clientes por por nombre especifico
   http://127.0.0.1:8000/api/clients/query/nombre/prueba
   * Consulta los clientes por por apellido 
   http://127.0.0.1:8000/api/clients/query/apellido/prueba2
   
 * METODO POST (ejemplo agregar un client)
    {
	"document": "5025",
	"firts_name": "prueba",
	"last_name": "prueba2",
	"email": "prueba@gmail.com"
    }
    
  * METODO PUT (ejemplo actualizar un client)
   * http://127.0.0.1:8000/api/clients/1
  
  * METODO DELETE (ejemplo eliminar un client)
   * http://127.0.0.1:8000/api/clients/1
   
BILLS
* METODO GET (ejemplo de consultas)
   * Consulta todas las bills 
   http://127.0.0.1:8000/api/bills
   * Consulta las bills por id 
   http://127.0.0.1:8000/api/bills/1
   * Consulta las bills por por nombre de compañia especifico
   http://127.0.0.1:8000/api/bills/query/nombre/fruver
   * Consulta las bills por por nit
   http://127.0.0.1:8000/api/bills/query/nit/123
   
   
 * METODO POST (ejemplo agregar bills)
    {
	"company_name": "jumbo",
	"nit": 123,
	"code": 10,
	"client_id": 1
    }
    
  * METODO PUT (ejemplo actualizar bills)
  * http://127.0.0.1:8000/api/bills/1
  
  * METODO DELETE (ejemplo eliminar bills)
   * http://127.0.0.1:8000/api/clients/1
   
PRODUCTS
* METODO GET (ejemplo de consultas)
   * Consulta todos los products 
   http://127.0.0.1:8000/api/products
   * Consulta products por id 
   http://127.0.0.1:8000/api/products/1
   * Consulta products por por nombre especifico
   http://127.0.0.1:8000/api/products/query/nombre/manzana
   * Consulta products por por precio
   http://127.0.0.1:8000/api/products/query/precio/1600
   
 * METODO POST (ejemplo agregar products) 
    {
	"name": "mora",
	"description": "madura",
	"precio": "1000"
    }
    
 * METODO PUT (ejemplo actualizar products)
  * http://127.0.0.1:8000/api/products/1
  
  * METODO DELETE (ejemplo eliminar products)
   * http://127.0.0.1:8000/api/products/1

BILLSPRODUCTS
* METODO GET (ejemplo de consultas)
   * Consulta todos los billsproducts 
   http://127.0.0.1:8000/api/billsproducts
   * Consulta billsproducts por id 
   http://127.0.0.1:8000/api/billsproducts/1 

 * METODO POST (ejemplo agregar billsproducts) 
   {
	"bill_id": 1,
	"product_id": 1
   }
   
* METODO PUT (ejemplo actualizar billsproducts)
  * http://127.0.0.1:8000/api/products/1

* METODO DELETE (ejemplo eliminar billsproducts)
   * http://127.0.0.1:8000/api/products/1

* Usuario: prueba
* Password: prueba
* correo: prueba@gmail.com
* authtoken 742711b298505d7572346d9c7c0138c2406fc574
   
- Se creao toda la Api REST con el crud.

- Base de datos mysql.
   
   
   
   
   
