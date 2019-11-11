from django.db import models
from django.utils import timezone
    
    #- class es una palabra clave que indica que estamos definiendo un objeto.
    #- Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Siempre inicia el nombre de una clase con una letra mayúscula.
    #- models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
    
class Post(models.Model): #esta línea define nuestro modelo (es un objeto).
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #Ahora definimos las propiedades de las que hablábamos: title, text, created_date, published_date y author. Para ello tenemos que definir el tipo de cada campo (¿es texto? ¿un número? ¿una fecha? ¿una relación con otro objeto como un User (usuario)?)
    #-models.CharField, así es como defines un texto con un número limitado de caracteres.
    #-models.TextField, este es para texto largo sin límite. Suena perfecto para el contenido de la entrada del blog, ¿no?
    #-models.DateTimeField, este es fecha y hora.
    #-modelos.ForeignKey, este es una relación (link) con otro modelo.

    def publish(self): #def significa que es una función/método y publish es el nombre del método.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    #Los métodos suelen devolver (return, en inglés) algo. Hay un ejemplo de esto en el método __str__. En este escenario, cuando llamemos a __str__() obtendremos un texto (string) con un título de Post.
