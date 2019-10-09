# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:
define circleirisout = ImageDissolve("ilustracion7-4.png", 1.0, 8)
define s = Character("Sara", window_background="gui/textbox.png")
define pm = Character("Mamá", window_background="gui/textbox.png")
define ph = Character("Papá", window_background="gui/textbox.png")

define pg = Character("Padre G.", window_background="gui/textbox.png")

define p = Character("[name]", who_color="#ffffff")
define e = Character("Alumno", who_color="#ffffff")
define g = Character("Gabriela", window_background="gui/textboxRojo.png", who_color="#d40000")
define m = Character("Maestro", window_background="gui/textboxCafe.png", who_color="#ffffff")
define n = Character("Niño", window_background="gui/textboxVerde.png", who_color="#0c6b17")
define ns = Character("Niños", window_background="gui/textboxVerde.png", who_color="#0c6b17")
# El juego comienza aquí.

label start:


    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene fondoejm

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show ext
    play music "sound/intro.mp3"



    # Presenta las líneas del diálogo.

    "Desde q nacemos vivimos con miedo"
    "Pero... {w=2}con miedo aque?"
    "Hay muchas razones pero con el tiempo te enteras que ninguna es la
    correcta y en esa busqueda no nos damos cuenta."
    "En lo que nos estamos convirtiendo."

    scene ventanaejm
    with fade

    "cada mañama parece ser un dia normal"
    "el sol sale, los adultos van al trabajo y los niños a la escuela"
    "Sara siempre se va a su escuela sin sus padres, ya que ellos trabajan mucho
    todo el dia y no tienen casi tiempo para ella."
    "aun asi parece ser que a Sara eso no le molesta, ya que ella siempre estara
    acompañada por mi y aunque soy alguien callado"
    "acompañare a sara y jugare con ella en todo momento."


    python:
        name = renpy.input(_("agrega aqui el nombre de tu personaje y oprima Enter para continuar"))



    show sara1ejm
    with dissolve

    s "Date prisa se va hacer tarde [name]"
    hide sara1ejm
    show sara2ejm
    with dissolve

    p "Ya voy"
    hide sara2ejm
    show sara3ejm
    with dissolve

    p "No importa lo que pase yo estare ahi y cada decicion que tome Sara yo la
    apollare."

    scene colegioejm
    with dissolve


    p "Esa misma mañana en horarios de clase llego un nuevo estudiante una persona
    muy alegre con un cabello corto y una sonrisa en su rostro"
    p " no le causo ningun problema presentarse en el pizarron"
    scene ilustracion1
    show gabriela
    with dissolve

    e "Hola!"
    e "Mucho gusto"

    e "Me llamo Gabriela pero mis amigo me dicen Gabi"
    show ilustracion3
    g "Espero que nos llevemos bien"
    scene ilustracion4
    p "Todos los niños e incluso el maestro quedaron sorprendidos ante tanta
    seguridad"
    scene fondo2
    show ilustracion5
    with dissolve
    p "Sara quedo anonadada por esa alegre presencia"
    hide ilustracion5
    show ilustracion6
    with dissolve
    p "Pero tuvo que voltear su mirada hacia su mesa para no llamar la atencion
    de Gabriela"
    scene ilustracion4
    m "Muy bien Gabriela..!"
    m "puedes sentarte alado de un compañero para asi continuar con la clase"

    scene ilustracion7
    show ilustracion71
    with dissolve
    p "En la hora de recreo todos los estudiantes se acercaron a Gabriela
    empujando a Sara y haciendo caer sus cosas"
    p "como si fuera un accidente.."
    p "empezaron a hacerle preguntas a Gabriela"

    p "Sara se quedo muy atras"
    hide ilustracion71
    show ilustracion8
    with dissolve
    p "asi que levanto sus cosas y salio del aula."

    p "mientras caminabamos me comentaba sobre lo genial que se ve Gabriela"
    p "Todo hiba bien hasta que derepente aparecieron ellos..."
    scene ilustracion10
    show ilustracion101
    with dissolve
    p "los niños al darse cuenta de la precencia de Sara se fueron hacia otro lado
    sin dirigirle la mirada"
    p "Mientras continuamos caminando"
    scene ilustracion11
    show ilustracion111
    with dissolve
    p "De la nada le llego una bolsa de jugo"
    scene ilustracion12
    show ilustracion121
    with dissolve


    p "uno de los niños le habia arrojado eso a sara"

    n "DONDE ESTA TU AMIGO NIÑA RARA!!!..."
    hide ilustracion121
    show ilustracion122
    with dissolve
    p "Sara se agacho tapandose la cabeaza"
    p "tenia unas ganas de llorar pero me puse frente a ella"
    p "Sara levanto la mirada y vio en mi una sonrisa"
    p "una sonrisa como la de Gabriela"
    hide ilustracion122
    show ilustracion3
    with dissolve
    show recuerdo
    with dissolve
    p "esa sonrisa de seguridad de que todo va estar bien"
    hide recuerdo
    scene ilustracion12
    show ilustracion123
    with dissolve
    p "sara se levanto y seco sus lagrimas"
    scene ilustracion7
    p "Despues del receso todos los estudiantes volvieron a sus respectivas aulas"
    show ilustracion13
    with dissolve
    p "Sara volvio a su mesa y al tomar asiento, gabriela noto que el cabello de
    sara estaba manchado con leche"
    p "se levanto preocupada pero ya habia llegado el profesor y comenzo a dar la
    clase"
    scene ilustracion15
    show ilustracion15-1
    p "En la clase se escuchaba murmurar a los alumnos, de una manera burlona"
    show ilustracion15-1
    p "tanto que cada vez se hacia mas fuerte aquellas burlas, hasta que ya era
    mas fasil de entender"
    scene ilustracion14
    show ilustracion14-1
    with dissolve
    p "Gabriela parecia perdida y algo atemorizada de las risas de los estudiantes"
    scene ilustracion7
    show ilustracion7-1
    p "cada segundo era mas doloroso para sara"
    show ilustracion7-1
    p "se sentia pequeña..."
    show ilustracion7-1
    p "excluida..."
    show ilustracion7-4#fondo negro
    p "sola..."
    p "Este momento es realmente triste."
    p "no entiendo porque se rien o porque se burlan"
    p "no encuentro gracia en ello"
    p "talvez..."
    p "la humillacion no es divertida para quien conoce al humillado"
    scene ilustracion17
    p "El bullicio en el aula se ve interrumpida por el profesor y el silencio
    se hizo presente"
    scene ilustracion18
    p "en estos momentos se podia sentir algo de paz"
    p "en horarios de salida despues de aquel momento"
    p "Gabriela se hacerco a sara, dirigiendose hacia nuestro haciento"
    #sara se puso incomoda y nerviosa
    scene ilustracion19
    show ilustracion19-1
    g "hola..!"
    s "..."
    hide ilustracion19-1
    show ilustracion19-2
    with dissolve
    g "como te llamas?"
    s "s..s..Sara"
    hide ilustracion19-2
    show ilustracion19-3
    with dissolve
    g "Me llamo gabriela"
    s "eso.. lose.."
    hide ilustracion19-3
    show ilustracion19-4
    with dissolve
    g "lociento es la costumbre jejeje"
    hide ilustracion19-4
    show ilustracion19-2
    with dissolve
    g "Queria preguntarte porque tienes el cabello manchado"
    s "unos niños.."
    hide ilustracion19-2
    show ilustracion19-5
    with dissolve
    g "mm...?"
    s "no es nada."
    hide ilustracion19-5
    show ilustracion19-6
    with dissolve
    p "Gabriela parecia muy insistente"

    p"Asi que se sento alado de sara pero en ese
    entonses Sara..."
    scene ilustracion20
    show ilustracion20-1
    show ilustracion20-2
    with dissolve
    s "QUE ESTAS HACIENDO!!!!"
    p "Gabriela estaba algo asustada por el grito de Sara"
    p "Pero aun asi gabriela respondio"
    g "solo me estoy sentando"
    s "ahi se sienta [name]"
    g "[name]?... pero no hay nadie aqui"
    s "No hay nadie?"
    s "QUITATE!!"
    hide ilustracion20-2
    scene ilustracion7
    show ilustracion21
    with dissolve
    p "Sara empujo a gabriela de su haciento y se fue molesta"
    hide ilustracion21
    scene ilustracion22
    show ilustracion22-1
    with dissolve
    p "Gabriela ya en el suelo desconcertada y algo asustada de lo ocurrido, veia
    como Sara se alejaba de ella ante la multitud viendola."
    g "Quien esta niña?"


    scene ventanaejm
    with circleirisout

    #cap2
    s "no puedo creer que se haya sentado en tu lugar sin antes preguntarte [name]"
    s "es igual que todos los niños, solo busca burlarse de mi"
    s "pero..."
    s "creo que no debi empujarla de esa manera"
    s "[name] crees que deberia..."
    menu:

        "Pedir disculpas.":

            jump pedir_disculpas

        "Ignorar lo ocurrido.":

            jump ignorar_lo_ocurrido
label pedir_disculpas:
    s "tienes razon [name] cuando llegue al colegio me disculpare con gabriela"
    p "sara se muestra muy confiada espero le vaya bien hoy"
    p "al momento de llegar al colegio sara se dirige hacia gabriela"
    p "pero en el intento Gabriela se dirije hacia otra compañera para hablar"
    s "parece que esta ocupada se lo dire en el recreo"
    p "sara intento disculparse en el receso"
    p "pero Gabriela se fue a donde sus compañeros dejando a Sara atras con las
    palabras en la boca"
    s "amm..."
    s "Gabriela..."
    p "gabriela no hacia caso sobre los intentos de comunicarse de Sara"
    p "pero aun asi intento dar lo mejor de ella, para poder disculparse"
    p "aunque.. en ese momento llegan unos compañeros de curso y se hacercaron a
    Sara de forma intimidante"
    n "porque no mejor te vas a estudiar con tus amigos"
    n "solo estas incomodando con tus balbuceos"
    s "lociento yo solo queria..."
    #le llega a sara bolas de papel
    n "VETE NIÑA RARA!!!"
    ns "SI VETE!!"
    p "sara se fue a su mesa  algo triste y desepcionada"
    s "Nose que estoy haciendo mal"
    s "todos son malos con migo"
    s "creo que tengo que ser como Gabriela para que no me traten tan mal"
    s "Apenas lleva dos dias aqui y ya se lleva bien con todos los compañeros"
    s "sera una buena idea o no sera necesario"
jump opcion1
label ignorar_lo_ocurrido:
    $ menu_flag = False
    s "no tengo el porque pedir disculpas ella empeso"
    s "ademas ya lo debio olvidar no fue tan grave"
    p "Sara esta confundida despues de lo que paso"
    p "Es como si lo que hizo no fuera lo correcto"
    p "ya es de mañana Sara se prepara para ir a la escuela"
    p "Al momento de entrar al aula, Sara ve a Gabriela y nota que ella esta
    esta tranquila hablando con sus compañeros"
    p "Sara se fue a su asiento, como siempre algo apartada de los demas"
    p "Solo podia ver como Gabriela se llevaba bien con los demas"
    s "Gabriela siempre esta sonriendo y se lleva bien con todos"
    s "Apenas lleva unos dias aqui......"
    s "Tal vez deberia ser como Gabriela"
    s "Crees que....... ?"
label opcion1:
    menu:


        "No es necesario.":

            jump no_es_necesario
        "Es una buena idea.":

            jump es_una_buena_idea

label es_una_buena_idea:

    s "decidido!.. desde maña tratare de cambiar y sere igual que Gabriela"
    p "no importa la desicion que tome sara yo la apoyare siempre."
    #al dia siguiente
    p "esta mañana Sara se puso pensativa sobre lo que tendria que cambiar para
    agradarle a todos"
    s "sara siempre esta con una sonrisa"
    s "talvez deberia sonreir mas"
    p "cuando bajamos para desayunar habia una nota que decia"
    #el desayuno esta en el microhondas
    p "en el camino Sara se decia asi misma 'sonrie' "
    s "'Sonrie Sara' 'Sonrie Sara' 'Sonrie Sara'."
    p "Cuando entro al aula Sara salto una sonrisa de oreja a oreja
    aunque se veia muy forzada, Sara intentaba que esto no le molestara"
    p "todos los alumnos se quedaron callados al verla"
    p "como si se vieran incomodados por su sonrisa"
    p "Sara de dirijia hacia su asiento mientras todos se hacian a un lado"
    p "cuando gabriela vio a sara y noto que ella esta sonriendo, ella tambien
    se puso a sonreir"
    p "Al parecer a Gabriela no le incomodaba el echo que Sara este sonriendo"
    p "llego el profesor , todos se sentaron y comenzo la clase"
    p "El profesor en medio de la clase voltea, ve a Sara y le pregunta "
    m "Sara?"
    s "Si profesor?"
    m "Que te hace tan gracioso?"
    s "Nada.."
    m "O mi clase te hace reir?"
    s "No profesor"
    m "Entonces es abubrrida mi clase?"
    s "... no es eso profesor" #bajando la cabeza
    m "Quite esa sonrisa y ponga atencion"
    s "si profesor.."
    p "En el receso se podia escuchar la burlas de los compañeros"
    p "Aunque a Gabriela parecia no gustarle aquellas burlas"
    s "El profesor me llamo la atencion, nose si deberia seguir con esta idea"
    menu:
        "Deberias dejarlo.":

            jump deberias_dejarlo1

        "Continuar con la idea.":

            jump continuar_con_la_idea

label continuar_con_la_idea:
    s "Tienes razon, no importa si el profesor se molesto
    debo continuar sonriendo."
    p "Sara realmente es alguien fuerte"
    p "no entiendo porque a nadie le cae bien Sara"
    n "Sara!!? porque no quitas esa sonrisa estupida de tu cara"
    ns "JAJAJAJAJAJA...!!"
    s "Hola" #con una sonrisa
    p "al niño no parece haberle gustado esa sonrisa"
    #le echa jugo en la cara
    n "VAMOS!!, SONRIE!!, niña rara!"
    p "mientras Sara se limpiaba la cara"
    p "El niño tiro sus cosas al suelo y se fue"
    p "Gabriela intento ayudar a sara, peros mientras se asercaba aqule niño le dijo
    si te haces amiga de de esa niña rara...
    Seras parte de la burla"
    p "Gabriela se quedo quieta pero despues de un tiempo retrosedio"
    p "terminando las clases sara alisto sus cosas
    y decidio irse lo mas pronto posible"
    p "pero gabriela nos dio alcanse e invito a sara a comer un helado"
    g "Sara! espera aun monento!..."
    g "vamos a comer un helado"
    #"sara con una cara decaida"
    s "yo... mm..."
    #viendo el rostro de grabriela
    s "si vamos"
    p "en el camino Gabriela noto la triste cara de Sara"
    g "no debes dejar que te afecte"
    s "ya estoy acostumbrada"
    s "ademas [name] esta conmigo"
    g "quien es [name]"
    s "[name] es mi mejor amigo"
    g "mm... no lo conosco"
    s "esta aqui conmigo"
    s "el es [name]"
    p "Gabriela parecia algo confundida pero se quedo y me saludo"
    g "hola [name] me alegro de que acompañes a sara en cada momento"
    g "espero que siempre estes con ella"
    p "Sara no se lo podia creer"
    p "pero en ese momento"
    p "llegaron los padres de grabriela y se fue con ellos"
    p "no sin antes depedirse de nosotros"
    g "Adios Sara cuidate"
    g "Adios [name] cuida a Sara"
    #sara sorprendida
    #llega a casa
    s "ella... te saludo..."
    p "Sara se puso a soltar lagrimas, intentaba contenerse pero..."
    s "no debo llorar"
    s "se supone que debo sonreir pero..."
    s "no puedo evitarlo.. esto me pone feliz."
    #cap3
    p "ya es de mañana y sara parece estar mas animada"
    p "creo hoy sera un buen dia."
    s "me acabo de dar cuenta que sonreir cada rato no es bueno"
    s "solo tengo que sonreir cuando realmente me sienta feliz"
    p "Sara tiene mas confianza en si misma, eso me tranquiliza"
    p "hoy toca educacion fisica"
    p "los compañeros se alistan para salir a la cancha"
    p "Sara se acerca a Gabriela y empieza a hablarle"
    p "los demas niños observan a Sara y gabriela algo incomoda intenta evitar
    una conversacion con ella"
    s "Hola Gabriela!"
    g "hola emm... tengo que alistarme"
    m "Para el ejercicio de hoy trabajaremos con un compañero para que nos apolle"
    s "Gabr...."
    s "No!.. si  trabajo con Gabriela are a un lado a [name] "
    s "no puedo hacerle eso"
    p "Sara se encuentra pensativa de lo que va hacer"
    s "mm.. bueno."
    p "Parece ser que ya tomo una decicion."
    s "Gabiela!!!"
    s "se dirije hacia Gabriela de una forma muy alegre y confiada pero.."
    g "No puedo."
    g "ya tengo compañero enverdad lociento"
    p "se podia sentir las miradas y burlas hacia Sara, incluso se podia observar
    lo distante que se ve Sara hacia sus compañeros"
    p "cada segundo parecia estar mas lejos"
    p "en el transcurso del tiempo nos quedamos solos realizando los ejercicios"
    p "Sara me pregunto"
    s "deberia intentar otravez hablar con Gabriela..?"
    menu:

        "Es una buena idea.":

            jump es_una_buena_idea1

        "Sigamos con la clase.":

            jump sigamos_con_la_clase

label sigamos_con_la_clase:
    s "si.. mejor continuemos"
    s "ademas esta cerca de los niños que me molestan"
    p "terminado la clase de Educacion Fisica Sara se alista para la salida y
    en la puerta de la entrada se encontraba Gabriela esperandonos"
    g "perdon por no poder tu compañera en la clase"
    s "no te preocupes.. jeje"
    g "vamos por helado?"
    s "claro vamos!!"
    p "continuaron hablando en el camino de muchas cosas como programas de tv o
    de dibujos nunca vi a Sara tan segura de si misma"
    g "porque te molestan tanto?"
    s "me molestan por [name]"
    g "que tienen con [name]"
    s "me molestan por tener un amigo que ellos no pueden ver"
    g "bueno.. yo pienso que tener un amigo es algo muy bueno"
    g "te ayuda en los malos momentos"
    g "te apolla en tus deciciones y sobre todo nunca te haria sentir sola"
    g "pero... no es el unico"
    g "PUEDES HACER MUCHOS AMIGOS!!!"
    p "sara vio una luz"
    p "se reflejaba en su mirada aquella felicidad que habia perdido"
    #en casa
    s "Aun puedo hacer muchos amigos"
    s "se que puedo."
    #cap 4
    #en la mañana
    p "Sara se alista para ir a la escuela, esta muy animada"
    s "[name] crees que deba cambiar de imagen?"
    menu:
        "NO, estas bien asi.":

            jump estas_bien_asi

        "un cambio daria una nueva imprecion.":

            jump un_cambio_daria_una_nueva_imprecion

label estas_bien_asi:
    s "tienes razon"
    s "tengo que ser yo misma si quiero hacer mas amigos"
    p "nos dirigimos a la escuela despues del desayuno"
    p "hoy esta nublado"
    p "en la clase de Manualidades el profesor pidio hacer un grupo para realizar
    una maqueta de cualquier paisaje"
    p "parece ser que todos ya tienen parejas"
    s "bueno parece ser que hoy toca hacer sola.."
    g "Sara!.. no tienes compañero?"
    s "mm.."
    g "hagamos equipo"
    #exprecion de asombro y felizidad
    g "si, resulta que estube distraida y no me dio tiempo de buscar un compañero"
    g "jejeje..."
    p "en el recreo Sara y Gabriela se quedaron en el aula hablando de como seria
    el paisaje para realizar la maqueta"
    g "bueno y donde lo realizamos?"
    s "como?"
    g "que te parece si lo realizamos en tu casa"
    s "bueno..."
    g "no te preocupes jeje."
    s "se lo dire a mis padres"
    p "en medio de la platica uno de los compañeros entro con sus amigos y se nos
    acerco"
    n "Como puedes estar con esa niña RARA!!?"
    n "o se te pego lo rara tambien?"
    g "no es rara y dejanos!"
    n "claro las dejo, pero antes..."
    p "en eso el niño da una señal a sus amigos y agarran a Sara y Gabriela"
    p "el niño empieza a vaciar sus mochilas desparramando sus cosas por el suelo"
    p "todos lo veian pero nadie queria hacer nada"
    n "Sera mejor que empieces a escojer bien tus amistades Gabriela."
    p "cuando las soltaron, Sara corrio por todos lados recojiendo las pertenencias
    de Gabriela"
    s "losiento."
    s "enverdad losiento"#llorando
    s "si no estubieras conmigo esto no te estaria pasando"
    g "porque te disculpas"
    s "...?"
    g "es lo que yo decidi, no te preocupes"
    p "Gabriela recojio las cosas de Sara y se alistaron para la siguiente clase"
    #sara calmo sus lagrimas
    p "en la noche cuando llegaron los padres de Sara"
    p "Sara se dirigio a su padre para decirle que vendra Gabriela el Sabado
    pero su padre le dijo que hablara con su madre"
    s "Mamá mañana vendra una amiga para hacer un trabajo"
    pm "Estabien hija, puedes pasarme la libreta azul de la mesa?"
    p "sara se fue a dormir para recibir el gran dia no podia esperar"
    #esa tarde
    p "tocaron la puerta y Sara fue a recibir a gabriela"
    pg "hola buenas tardes"
    pg "tu debes ser Sara"
    s "..si.. buenas tardes."
    pg "tus padres estan en casa?"
    s "no, salieron a trabajar."
    g "Papá ya dejanos.. puedes irte"
    pg "ok ok cuidate ok hija."
    g "si papá estare bien"
    pg "esta bien, pasare por ti en la noche"
    p "el padre de Gabriela se fue y las dos comenzaron a realizar la maqueta"
    g "tus padres... solo hoy salieron?"
    s "bueno.. salen todo los dias."
    g "espera!"
    g "osea que estas sola todos los dias"
    s "si, pero no me molesta ya estoy acostumbrada"
    g "ya veo"
    g "eres reealmente sorprendente."
    g "pero... no estas sola con [name]"
    s "Quien?"
    s "Ha! si."
    s "siempre esta a mi lado"
    p "fue un arduo trabajo realizar la maqueta pero porfin lo terminaron"
    g "PORFIN!!!..."
    g "parece que quedo bien"
    s "eso parece"
    s "voy por algunos refrigerios"
    p "llegando a ser las 8:00 de la noche el padre de gabriela toco la puerta"
    pg "perdon por la tardanza se me fue la hora"
    g "Aun no llegan tus padres?"
    pg "Enserio? estaras bien sola?"
    s "si, no se preocupe estare bien."
    g "bueno cuidate Sara"
    p "Sara se despide de Gabriela cuando ya esta en el auto"
    s "ahora.."
    s "estoy sola."
    s "No!.. tengo amigos a mi lado"
    #cap 5
    p "ya es de mañana"
    p "Sara se alista y lleva la maqueta a su escuela"
    p "al llegar vemos a gabriela en su asiento y la saludamos
    se ven muy felices"
    s "aqui esta la maqueta"
    g "que bien.. ya solo queda presentarlo"
    m "muy bien Alumnos, los trabajos lo presentaremos al final de la clase
    para que lo vean los otros cursos"
    p "Comenzaron con la clase hasta que toco el timbre de recreo y todos salieron
    al patio"
    s "Crees que quedo bien?"
    g "yo creo q quedo fantastico"
    s "esque..."
    g "Sara, realizamos juntas este trabajo"
    s "si tienes razon"
    p "Cuando regresamos al aula vimos el trabajo de Sara y Gabriela
    partido en dos y destrozado"
    p "al rededor solo se escuchaban burlas"
    p "Sara no podia resistir y callo en lagrimas entre el suelo y todo
    alrededor solo parecia ser burlas y llanto"
    p "Gabriela no molesta se dirigio hacia el niño"
    g "Fuiste tu?"
    n "Y que si fui yo."
    n "no puedes hacer nada al respecto porque todos aqui"
    p "el niño fue empujado tan fuerte que cayo entre los asientos"
    p "entre ellos se ve una pelea pero los estudiantes van a detener a Gabriela
    socorriendo al niño"
    p "el niño molesto viendo a Gabriela vulnerable se le hacerca con furia
    pero en eso se ecucha una voz fragil."
    s "porque?"
    s "porque me odias?"
    s "PORQUE TODOS ME ODIAN TANTO?"
    p "Todos los estudiantes se quedaron en silencio y Gabriela le grito al niño"
    g "SARA SIEMPRE ESTA SOLA!!!"
    g "Sus padres nunca estan con ella"
    g "y tiene que venir aqui solo para soportar a personas como tu"
    g "A ti te hace feliz hacerle esto???"
    n "yo... no lo sabia"
    n "Mis padres se separaron"
    p "todos los niños sintieron culpa por las cosas que le hicieron a Sara"
    p "Gabriela comenzo a recojer los trozos de la maqueta y en ese momento los
    demas comenzaron a ayudar a repararla"
    p "Sara solo estaba en su lugar deprimida"
    g "Sara?"
    g "terminamos la Maqueta."
    p "sara levanto la mirada y vio a todos los niños rodeandola"
    n "P...pe...PERDON!!!"
    ns "Lociento Sara. perdon Sara. yo tambien te pido perdon"
    ns "LO SENTIMOS MUCHO SARA!!!!!"
    p "Sara realmente no lo podia creer."
    p "cuando vio la maqueta, noto que habia muchas cosas en ella"
    p "Fue uno de los momentos mas emotivos en la vida de Sara."
    p "Despues de terminar las Clases todos se fueron a sus casas."
    g "Crees que la maqueta quedo bien?"
    s "Yo creo que quedo..."
    s "Muy bonita"
    #Final bueno de la novela
    return
label no_es_necesario:
    s "si, no veo el porque tenfria q ser como gabriela"
    s "Ella tiene su forma de ser con los demas"
    s "continuare con mi forma de ser"
jump deberias_dejarlo
label deberias_dejarlo1:
    s "todo esto es inutil"
label deberias_dejarlo:
    p "y asi surgio hasta que termino la clase"
    p "tras recojer sus cosas se topo con sus compañeros de curso"
    n "Sara... sigues sola"
    s "No estoy sola"
    s "Estoy con [name]"
    n "Sigues con ese jueguito niña rara?"
    p "El niño da una señal y los otros compañeros sujetaron a Sara"
    p "Mientras el otro niño buscaba todo el dinero que tenia Sara"
    p "Tomo su mochila y removio entre su cosas"
    n "tch...... , Solo eso?"
    n "Bueno para algo servira"
    s "Porfavor... devuelveme mi dinero"
    s "Lo necesito para volver a mi casa"
    #llorando
    p "Los niños con la sonria marcada en sus caras se van del aula"
    n "Dile a tu amigo que te preste
    Jajaja..."
    p "Sara se veia humillada despues de lo ocurrido"
    s "[name]?"
    s "Por que nos tratan tan mal?"
    #aguantando las lagrimas
    g "Nos?"
    p "Sara levanto la mirada y vio Gabriela delante de ella"
    g "Por que te tratan tan mal tus compañeros?"
    s "Es por que no pueden ver a [name]"
    g "[name]?"
    s "Si, el es mi amigo"
    g "Bueno, pues [name] no deberia dejarte sola"
    s "No estoy sola."
    g "Bueno, quieres ir a tomar un helado?"
    s "Mmmm.. Lo siento me quitaron mi dinero"
    #mirando su mochila
    s "No tengo para volver a mi casa"
    g "......... Toma!"
    g "Supongo que el helado sera para otro rato"
    #sara se pone feliz por el gesto de gabriela
    s "Gracias!!"
    g "No te preocupes"
    g "Ya me tengo que ir, nos vemos mañana"
    p "Sara se fue a su casa, parece estar mejor de lo ocurrido"
    p "Realmente esos son los gestos que pueden cambiar
    el estado de animo de la gente"
    p "Sara se fue a dormir mas tranquila"
    #a la mañana siguiente
    p "Ya es de dia y Sara se pone su uniforme de educacion fisica para salir"
    s "Vamos!! [name]"
    #en clases
    p "Todos salimos al patio para empezar la clase"
    m "Bien, para el ejercicio de hoy trabajaremos con un compañero
    para que nos apolle"
    s "[name] debo hablar para el ejercicio de hoy, crees que sea.."
    menu:
        "Es una buena idea.":
            jump es_una_buena_idea1

        "No creo necesario.":
            jump no_creo_necesario


label no_creo_necesario:
    s "Sierto, lo que paso hayer solo fue porque me tenia lastima
    mejor trabajo con [name]"
    p "Empesamos a trabajar toda la clase solos, fue algo cansador"
    p "despues de la clase fuimos a comprarnos algo en la salida
    pero nos topamos otravez con los niños"
    n "Hola.."
    p "Sara sentia otravez aquel miedo de lo que pueda ocurrir otravez"
    n "donde vas sara?"
    s "yo... mm... ya me hiva."
    p "el niño lanzo travez una señal y los otros sujetaron nuevamente a sara"
    n "vaya!"
    n "parece que ahora tienes mas"
    s "devuelvemelo porfavor!"
    n "Claro! toma!.."
    p "El niñ arrojo sus monedas a los aires y se va con sus amigos"
    #"Sara recojio sus monedas"
    s "No debo llorar"
    s "asi sera siempre"
    s "solo debo ser mas fuerte"
    s "tengo que empesar a valerme por mi misma"
    p "Parece que Sara hacepto lo que le deparara el futuro
    no crei que llegaria a olvidarme de esta forma"
    p "Espero que le vaya bien en toda su vida"
    "FINAL NEUTRAL"
    #final neutral de la novela
    return
label es_una_buena_idea1:
    s "Si, tienes razon creo que es un buen momento para intentar
    llevarme bien con ella"
    p "Sara esta decidida  en preguntar a Gabriela para formar equipo"
    p "quiza esto sea algo bueno para ella, pero tengo el presentimiento que
    algo malo va a pasar"
    s "Gabriela."
    s "Yo... mm..."
    g "Si?"
    s "queria saber si quieres ser mi compañera de educacion fisica"
    p "ese momento se convirtio en un ambiente silencioso"
    g "Emm... bueno..."
    n "que haces aqui niña rara!"
    n "quieres seguir incomodando?"
    s "yo.. no."
    g "Oye..! no la molestes."
    n "Ella es la rara, no tiene por que estar con nosotros"
    n "Vamos muevete, vete con tu amigo raro."
    p "Gabriela se ve molesta por el mal trato que recive Sara"
    p "Pero a Sara solo la puedo ver sumisa"
    s "Lociento por molestar"
    n "Gabriela."
    n "Si lo que quieres es tener amigos"
    n "te recomiendo que escojas bien tus amistades"
    p "No entiendo poque hay tanta indiferencia hacia sara"
    p "Ella no es una mala persona, solo quiere ser como los demas"
    g "SARA!!!.."#CORRIENDO
    p "Se hoyo un grito en la multitud"
    g "aun te falta compañero?"
    p "Sara no lo podia creer pues ella ya se estaba resignando a continuar sola
    pero ese grito pudo despertarla de su pesar."
    #al dia siguiente
    p "despues de lo ocurrido Sara se ve mas confiada de lo normal"
    p "Parece que ahora tendra un amigo con quien hablar"
    s "Aun no puedo creer lo que paso ayer"
    s "yo.. nose que hacer."
    s "tengo que irme"
jump final_malo
label un_cambio_daria_una_nueva_imprecion:
    s "si, talvez cambie de corte de cabello."
    s "Ya se hace tarde tengo que irme!!"
label final_malo:
    p "Sara llegando al colegio noto la mirada de los estudiantes
    algo escalofriante e intimidante"
    g "Sara que tal estas"
    g "buenos dias"
    s "Buenos dias"
    g "toma asiento"
    g "ya va a comenzar la clase"
    m "muy bien niños... para el lunes necesito que hagan una maqueta sobre
    algun paisaje"
    m "puede ser en grupos de ados"
    s "mm... parese que..."
    g "hacemos equipo?"
    s "Si!"
    p "Sara estaba algo nerviosa"
    p "no sabia que hacer o que decir"
    g "Que tipo de paisaje deberiamos poner"
    g "y tambien en que casa lo deberiamos realizar"
    g "Sara donde vives?"
    s "yo... vivo en Ticti Norte"
    g "mas o menos por donde"
    s "casi llegando a la entrada del parque Tunari"
    g "ENSERIO!!"
    g "Podemos hacer de eso la aqueta"
    s "Bueno... yo creo que si"
    g "Bien! quedamos en tu casa verdad"
    s "Si! se lo dire a mis padres"
    #en casa
    s "Papá?"
    ph "ahora no hija"
    s "Mamá?"
    pm "Si?"
    s "Mañana..."
    pm "Cariño pudes pasrme ese folder azul?"
    s "Mañana vendra una amiga a realizar una maqueta"
    pm "Si amor los amigos q quieras"
    ph "Amor se hace tarde"
    pm "Ya voy!.."
    pm "te calientas la cena, esta en el microondas"
    pm "Te quiero."
    p "Los padres de Sara se fueron y Sara se volvio a quedar sola pero anciosa
    por lo de mañana."
    ####
    #esa tarde
    p "tocaron la puerta y Sara fue a recibir a gabriela"
    pg "hola buenas tardes"
    pg "tu debes ser Sara"
    s "..si.. buenas tardes."
    pg "tus padres estan en casa?"
    s "no, salieron a trabajar."
    g "Papá ya dejanos.. puedes irte"
    pg "ok ok cuidate ok hija."
    g "si papá estare bien"
    pg "esta bien, pasare por ti en la noche"
    p "el padre de Gabriela se fue y las dos comenzaron a realizar la maqueta"
    g "tus padres... solo hoy salieron?"
    s "bueno.. salen todo los dias."
    g "espera!"
    g "osea que estas sola todos los dias"
    s "si, pero no me molesta ya estoy acostumbrada"
    g "ya veo"
    g "eres reealmente sorprendente."
    g "pero... no estas sola con [name]"
    s "Quien?"
    s "Ha! si."
    s "siempre esta a mi lado"
    p "fue un arduo trabajo realizar la maqueta pero porfin lo terminaron"
    g "PORFIN!!!..."
    g "parece que quedo bien"
    s "eso parece"
    s "voy por algunos refrigerios"
    p "llegando a ser las 8:00 de la noche el padre de gabriela toco la puerta"
    pg "perdon por la tardanza se me fue la hora"
    g "Aun no llegan tus padres?"
    pg "Enserio? estaras bien sola?"
    s "si, no se preocupe estare bien."
    g "bueno cuidate Sara"
    p "Sara se despide de Gabriela cuando ya esta en el auto"
    s "ahora.."
    s "estoy sola."
    s "No!.. tengo amigos a mi lado"
    #domingo
    p "Al dia siguienate Sara se pone pensativa de como cambiar su cabello"
    p "Asi que ella va áa buscar a su madre pero ella se encontraba ocupada"
    s "Mamá...?"
    pm "Ahora no hija, yengo que preparar estos documentos para mañana"
    p "Sara no tenia opcion que hacerlo ella sola"
    p "Aunque le tomo mucho tiempo se veia muy bonita"
    #el lunes
    p "Cuando Sara llego a la escuela, todos los niños vieron
    el Gran cambio de Sara e incluso Gabriela quedo sorprendida"
    s "Hola"
    g "Hola sara!, te ves diferente"
    s "Queria cambiar un poco"
    g "Te ves bien"
    p "Esto llamo mucho la atencion de lo niños"
    p "Ya despues de haber presentado los trabajos alistaron sus cosas
    para irse pero en ese momento"
    n "Que bien te ves Sara"#da la orden
    p "Sara y Gabriela son inmovilizadas por los niños y en el acto
    vacian sus mochilas y del suelo levantan una tijera"
    n "Dejame arreglarte el cabello!"
    p "Agarra a Sara y le corta el cabello
    mechon por mechon."
    p "Sara no podia hacer nada estaba totalmente en shock"
    p "Todos veian como se le caia el cabello"
    n "LIsto ahora te ves bien"
    p "Todos se rieron y Sara quedo humillada"
    p "Entre todas las risas Sara se fue lentamente y tomo su mobilidad"
    p "Pero no fue a su casa, llego a la parada y subio lo mas alto
    del Parque tunari"
    p "Camino hasta que oscurecio"
    p "Cuando se dio cuenta de la luz de la luna
    comenzo a llorar."
    s "Porque, porque, porque, porque, poeque, porque."
    s "Yo no hice nada malo"
    s "Yo no quiero esto"
    p "Me quedare con Sara, estare con ella siempre"
    s "[name]?"
    p "Sara me vio y corrio hacia mi."
    #Final malo
    return
    # Finaliza el juego:
    return
