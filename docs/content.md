<!-- -*- coding: utf-8 -*- -->

## Алгоритмы и структуры данных

# От символов к байтам

![](images/vignette-2.svg) <!-- .element: style="width: 400px;" -->

### Луцив Дмитрий Вадимович
### ЗАО «Ланит-Терком», СПбГУ



# А что там у Open Source проектов?

<!--.slide: style="text-align:center;" -->
<!-- [PDF](?print-pdf) -->

= = = = = = = = = = = = =

# Где набрать побольше проектов?
## И получше

И *раз* **два** ***три***

![](images/dilbert-meeting.jpg)<!--.element: style="height:600px;" -->
<!--.slide: style="text-align:center;" -->

- - - - - - - - - - - - -
## Каталоги открытых проектов

* Open Hub (бывший Ohloh) — https://www.openhub.net/
* Прямых аналогов не нашёл

- - - - - - - - - - - - -
## Каталоги крупных компаний и фондов

* https://opensource.microsoft.com/
* https://projects.eclipse.org/
* https://opensource.google.com/
* https://projects.apache.org/

- - - - - - - - - - - - -
## Каталоги для пользователей

В духе «скачать FTP клиент бесплатно без СМС»

* Product Hunt https://www.producthunt.com/ — скорее про продукты
* SOFTPEDIA http://www.softpedia.com/ — тоже

Малопригодно

- - - - - - - - - - - - -
## Хостинги

* GitHub
* GitLab
* BitBucket
* SourceForge
* FossHub

Но там уже первичны репозитории, а не проекты

= = = = = = = = = = = = =
# Немножко по известным компаниям и проектам/фондам

- - - - - - - - - - - - -
## MS

https://opensource.microsoft.com/ хостят на Гитхабе (они его купили)

VS Code, TypeScript, RxJS, CNTK (cognitive learning), PowerShell, .NET, Roslyn, ... F#. Хостят на **GitHub**, на OpenHub многие есть.

## Eclipse

https://eclipse.org/ — много своих и зовут чужие. У них практически свой маленький Open Hub. На сайте Eclipse аннотации проектов. Хостятся часть у них, часть снаружи (на Гитхабе например)

## Linux Kernel

Сами на https://kernel.org/ и **зеркало на GitHub**. На OpenHub есть.

## Питон?

https://www.python.org/ — свой мирок. Хостят у себя на http://svn.python.org/, но есть зеркала на Гитхабе. Релизы сторонних библиотек тоже хостят у себя, чтобы легче ставить, но ссылки идут наружу — на **GitHub** и т.д.

- - - - - - - - - - - - -
## LibreOffice

Xостят у себя

## Oracle

Хостят в разных местах — у себя, на Гитхабе, ... но у них немного

## Apache

http://www.apache.org/index.html#projects-list. Хостят у себя на сайтах проектов внутри их сервера

## Google

https://opensource.google.com/ хостят *преимущественно* на **GitHub**, аннотации у себя

- - - - - - - - - - - - -
## Примеры обзоров

Вот пример, но не ясно, из каких принципов

https://medium.com/@likid.geimfari/the-list-of-interesting-open-source-projects-2daaa2153f7c

Ещё бы, вообще всё хаотично...

= = = = = = = = = = = = =
# API

- - - - - - - - - - - - -
## Определение API из SWEBOK (4.1)

*An application programming interface (API) is the set of signatures that are exported and available to the users of a library or a framework to write their
applications. Besides signatures, an API should always include statements about the program’s effects and/or behaviors (i.e., its semantics).*

API design should try to make the API easy to learn and memorize, lead to readable code, be hard to misuse, be easy to extend, be complete,
and maintain backward compatibility. As the APIs usually outlast their implementations for a widely used library or framework, it is desired
that the API be straightforward and kept stable to facilitate the development and maintenance of the client applications.

API use involves the processes of selecting, learning, testing, integrating, and possibly extending APIs provided by a library or framework (see section 3.6, Construction with Reuse).

= = = = = = = = = = = = =
# Grimoire Lab

Попробовал обёртку из Perceval для StackOverflow; King Arthur не пробовал. ELK пока тоже не пробовал и не понял, что он умеет.

Но похоже, что он создан для количественного анализа, т.е. нам могут помочь Perceval и, м.б., Arthur, а дальше сами

= = = = = = = = = = = = =
# GitHub

![](images/octocat.jpg)<!--.element: style="height:600px;" -->

## Как много в этом слове
<!--.slide: style="text-align:center;" -->

- - - - - - - - - - - - -
## Изначальная идея

Social Coding. Т.е. социальная сеть для OpenSource-разработчиков

- - - - - - - - - - - - -
## Их собственные странички, чтобы быть «в теме»

* Стартовая страничка https://github.com/explore →
  * → Topics — репозитории по тематике (LaTeX, C\#, C++, Blockchain, ...) https://github.com/topics/, каталог редактируется вручную
  * → Events — https://github.com/events — конференции / выставки / митапы
  * → Trending repositories https://github.com/trending
  * → ...

**Trending** — то, что нам надо, т.к. GitHub, всё-таки, хостит в первую очередь не проекты, а именно код

- - - - - - - - - - - - -
## GitHub Trending

Самый длинный доступный период — месяц https://github.com/trending?since=monthly, но для «живых проектов» это нормально

Из языков вверху обычно  JavaScript/TypeScript, Python, C++, Go.
Java вверху нету, ибо она сейчас не модная. Но зато у неё с документацией хорошо. Поэтому с неё и начнём: https://github.com/trending/java?since=monthly

- - - - - - - - - - - - -
## Пример Java: Spring Boot

Известный проект: https://github.com/spring-projects/spring-boot компании [Pivotal](https://en.wikipedia.org/wiki/Pivotal_Software),
которая в своё время откололась от EMC.

Артефакт  | Формат   | Где исходник  | Где конечное представление            | Технология
----------|----------|---------------|---------------------------------------|-----------
Дом. стр. |   ?      |      ?        | http://spring.io/projects/spring-boot | 
Исходники | Java + Kotlin    | GitHub        | n/a                                   | n/a
README    | ASCIIdoc | GitHub        | GitHub                                | GitHub pages
Рук-во    |   ?      |      ?        | https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle/ + PDF + EPUB | ASCIIDoctor
API док-ция | JavaDoc + KDoc | GitHub | https://docs.spring.io/spring-boot/docs/current/api/ | JavaDoc + KDoc

- - - - - - - - - - - - -
## Как и где это взять?

* Как и где?
  * В каждом проекте — читаем его README и метаинформацию на Гитхабе, ищем, если есть, отдельную веб-страничку (которая также может генерироваться из файлов на Гитхабе), шарим по сайту проекта и по репозиторию в поисках отдельной документации. В исходниках ищем встроенную. Всё записываем, результаты сохраняем в табличке.
  * Круто, халявно!
* Ни фига не халявно! <!-- .element: class="fragment" -->
  * Половина активных проектов — **исключительно** китайские
  * В большом проекте ковыряться можно час и больше
  * Касательно API <!-- .element: class="fragment" -->
    * API — это на самом деле очень много что: и интерфейс программной библиотеки, и веб-API, и командная строка, и наборы хранимых процедур и т.д.
    * Часто наличие Reference «освобождает» разработчиков от написания API-документации

= = = = = = = = = = = = =

## СПАСИБО!

![](media/images/qr-edu-dluciv-name.png) <!-- .element: style="width: 600px;" -->

<!--.slide: style="text-align:center;" -->
