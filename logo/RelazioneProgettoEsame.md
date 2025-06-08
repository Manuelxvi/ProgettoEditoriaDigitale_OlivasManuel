---
title: Relazione del progetto d'esame di Editoria Digitale
author: Manuel Olivas 20848A studente
date:  a.a. 2024/2025
institute: Università degli Studi di Milano
course: Editoria Digitale
tags: tag1, tag2, tag3
version: 0.1
kind: Document
bibliography: bibliografia.bib
csl: IEEE.csl
---

![Logo UNIMI](./logo/minerva.jpg){width=100px height=100px}

# Titolo Progetto d'Esame
Legame tra SPORT e SOCIETÀ 


## Introduzione

Il progetto ha avuto come obiettivo la creazione di un compendio digitale dedicato alla storia dello sport nel Novecento, e su come abbia impattato su certi aspetti culturali, sociali e politici. A partire da documenti testuali strutturati, è stato sviluppato un flusso editoriale automatizzato per produrre contenuti in formato HTML, PDF e EPUB.

I contenuti sono stati realizzati in HTML e CSS per garantire una presentazione coerente, mentre JavaScript (integrato nei file .html) è stato utilizzato per l’estrazione automatica dei metadati da Wikipedia, senza uso di linguaggi lato server. La conversione nei diversi formati è avvenuta tramite Pandoc, con il supporto di file di metadati strutturati secondo standard come Dublin Core e Schema.org.

Il flusso di produzione è stato rappresentato con un diagramma BPMN che descrive in modo chiaro le fasi: raccolta, verifica, impaginazione, esportazione e pubblicazione. Il risultato è un prodotto editoriale accessibile, ben organizzato e ricco di contenuti multimediali, capace di raccontare eventi sportivi significativi e il loro impatto nella società. 

## Ideazione 

### Tema
Il tema centrale di questo progetto editoriale è l’evoluzione dello sport nel corso del Novecento, analizzato non solo come attività agonistica, ma come fenomeno sociale, culturale e politico. Il prodotto nasce con l’intento di raccontare eventi sportivi emblematici che hanno avuto un impatto profondo sulla società, mettendo in luce come lo sport abbia spesso rappresentato uno specchio del contesto storico in cui si è sviluppato.

Al centro del lavoro vi sono momenti e figure simboliche: Jesse Owens alle Olimpiadi di Berlino del 1936, Diego Armando Maradona con la celebre “Mano de Dios” ai Mondiali del 1986, e Michael Jordan con la sua visione dello sport come disciplina e resilienza. Attraverso questi casi, si affrontano temi trasversali come il razzismo, la propaganda politica, la rivincita sociale, il mito sportivo e la comunicazione globale.

Il progetto risponde all’esigenza di raccontare lo sport in chiave documentale, fornendo fonti, testimonianze e materiali strutturati, e colma un bisogno informativo spesso trascurato: quello di legare lo sport alla memoria collettiva e alla storia culturale. Le domande più frequenti che guidano il progetto sono: in che modo lo sport ha influito sui cambiamenti sociali? Quali eventi sportivi hanno avuto un impatto oltre il campo di gioco? Come si può raccontare lo sport come patrimonio documentale?

Attraverso un impianto narrativo chiaro e formati digitali accessibili (HTML, EPUB, PDF), il progetto si propone di rispondere a questi interrogativi, offrendo contenuti documentati, navigabili e destinati sia al pubblico generico che al contesto educativo e culturale.

![UNIMI](https://www.erasmusmilan.com/wp-content/uploads/2016/02/Statale-e1478865636847.jpg)

### Destinatari
Per identificare il pubblico di riferimento del compendio digitale “La Storia nello Sport”, sono state individuate tre personas, che rappresentano in modo sintetico i principali tipi di utenti a cui il prodotto è destinato. Ognuna riflette bisogni, interessi e modalità diverse di fruizione.

Personas 1:
Una prima figura a cui il prodotto si rivolge è quella di uno studente universitario, ad esempio Luca, 22 anni, iscritto a Scienze motorie. Luca è appassionato di sport, ma anche curioso di comprendere il legame tra eventi sportivi e dinamiche storiche e sociali. Per lui, un compendio ben organizzato, con fonti attendibili e disponibili in formati digitali versatili, rappresenta uno strumento utile per le ricerche, le tesine e lo studio. Luca può leggere i contenuti dal computer, dal tablet o su un lettore EPUB, prendere appunti, inserire citazioni e approfondire eventi come le Olimpiadi del 1936 con uno sguardo critico e documentato.

Personas 2: 
Un secondo scenario coinvolge Giulia, 40 anni, insegnante di storia e educazione civica in una scuola secondaria di secondo grado. Giulia cerca strumenti innovativi e coinvolgenti per trattare in classe tematiche sociali attuali attraverso esempi storici. Grazie al compendio, può mostrare agli studenti pagine in HTML, proiettare immagini, leggere brani di interviste o visualizzare video, utilizzando lo sport come chiave per affrontare questioni come l’inclusione, la discriminazione, la propaganda o l’identità culturale. Il compendio diventa così uno strumento didattico trasversale, utile per stimolare riflessioni e dibattiti in aula.

Personas 3: 
Infine, il progetto si rivolge anche a lettori adulti e appassionati di storia dello sport, come Marco, 65 anni, un ex bibliotecario in pensione con una forte passione per le biografie sportive e i racconti legati alla memoria collettiva. Marco predilige la lettura su dispositivi e-reader, e apprezza contenuti curati, ricchi di contesto, ma anche accessibili e gradevoli nella forma. Il compendio, nella sua versione EPUB, gli permette di ripercorrere episodi come la “Mano de Dios” o le imprese di Michael Jordan, non solo come episodi sportivi, ma come momenti che hanno segnato l’immaginario collettivo di intere generazioni.

Attraverso queste figure immaginarie ma rappresentative, il prodotto si dimostra in grado di soddisfare esigenze differenti: supporto allo studio, strumento didattico, lettura culturale e memoria storica. La struttura digitale e multiformato consente una fruizione ampia, inclusiva e trasversale, adattandosi alle modalità e ai tempi di ogni utente.

### Modello di fruizione
Il prodotto editoriale deve essere accessibile, navigabile e fruibile da dispositivi diversi, mantenendo coerenza tra HTML, PDF ed EPUB. Il modello di lettura adottato è tematico e modulare, adatto sia alla consultazione scolastica che alla lettura personale. I contenuti devono essere chiari, ben organizzati e corredati da immagini e fonti affidabili. Si fa riferimento agli standard EPUB 3.0, HTML5, Dublin Core e Schema.org per garantire compatibilità e archiviazione. L’innovazione risiede nell’uso di JavaScript per l’aggiornamento automatico dei metadati da Wikipedia e nella conversione multiformato con Pandoc. La qualità è garantita da un equilibrio tra contenuto informativo e impatto culturale.

### Canali di distribuzione
Il prodotto editoriale sarà distribuito attraverso più canali per garantire ampia accessibilità e adattabilità ai diversi contesti d’uso. Il canale principale sarà il Web, tramite una versione HTML navigabile pubblicabile su siti personali, piattaforme didattiche o repository culturali. In parallelo, sarà prodotta una versione EPUB 3.0 per la lettura su e-reader e dispositivi mobili, utile per studenti e appassionati. La versione PDF sarà pensata per la stampa o la consultazione offline, con impaginazione curata e aderenza agli standard tipografici tradizionali.

Per i social media, saranno previsti estratti testuali o visivi (immagini, frasi iconiche, brevi video), collegati al contenuto principale. È ipotizzabile anche una distribuzione in ambito didattico o istituzionale tramite Intranet scolastiche o accademiche.

L’identità visiva seguirà uno stile colorato e vivace, titoli in maiuscolo e colori contrastanti fra loro per garantirne la visibilità. Verranno evitate soluzioni grafiche troppo complesse per garantire leggibilità. Il tono sarà prevalentemente formale, ma accessibile, con l’obiettivo di mantenere un equilibrio tra rigore informativo e coinvolgimento del lettore. Si intende così trasmettere una sensazione di affidabilità e cura editoriale, aderendo ai modelli classici della divulgazione culturale ma proponendo al tempo stesso un’esperienza di fruizione aggiornata e multiformato.

## Processo di Produzione

### Acquisizione dei contenuti
I contenuti del prodotto editoriale sono stati acquisiti principalmente da fonti libere e accessibili, in particolare Wikipedia, utilizzata tramite la sua API ufficiale REST. Questa scelta ha permesso di integrare automaticamente metadati aggiornati, descrizioni sintetiche e immagini senza costi di licenza. L’uso di API pubbliche ha ridotto i tempi di redazione, garantendo al contempo l’affidabilità e la verificabilità delle informazioni.

Oltre ai dati estratti automaticamente, alcune sezioni sono state inserite manualmente per contestualizzare gli eventi storici o per sviluppare introduzioni e riflessioni tematiche. Le immagini e i video inclusi nel progetto provengono da fonti con licenza libera (es. Wikimedia Commons o YouTube).

### Gestione documentale
Il flusso di gestione documentale del progetto è stato strutturato in modo chiaro e sequenziale, per garantire coerenza e tracciabilità in ogni fase della produzione editoriale. La prima fase ha riguardato la raccolta e produzione dei contenuti, avvenuta sia attraverso l’acquisizione automatica di dati da fonti aperte (come Wikipedia, tramite API REST), sia mediante la redazione manuale di introduzioni, descrizioni e approfondimenti. Questa combinazione ha permesso di coniugare accuratezza e originalità, mantenendo basso il costo di produzione.

Successivamente è stata effettuata una valutazione dei diritti, selezionando esclusivamente materiali testuali e visivi disponibili con licenza libera (es. CC BY-SA), per assicurare una piena libertà di distribuzione nei diversi formati. I contenuti raccolti sono stati poi strutturati tematicamente, suddivisi in file HTML indipendenti ma coerenti tra loro, organizzati secondo logiche cronologiche o per argomento.

La fase di applicazione dello stile grafico ha previsto l’utilizzo di un foglio di stile CSS unico, per garantire uniformità visiva e tipografica in tutte le versioni del prodotto. L’impaginazione è stata progettata per essere chiara, accessibile e coerente con il tono divulgativo del progetto.

Successivamente si è proceduto alla generazione e gestione dei metadati, utilizzando schemi standard (Dublin Core, Schema.org e ONIX), sia in forma dichiarativa (YAML) sia tramite estrazione dinamica. Questa fase è stata fondamentale per garantire la futura archiviazione e interoperabilità dei contenuti. I contenuti sono stati poi trasformati automaticamente in formato PDF ed EPUB tramite Pandoc, consentendo una diffusione multiformato senza dover duplicare il lavoro redazionale.

Infine, la fase di distribuzione ha incluso la pubblicazione su web e la preparazione di file scaricabili (PDF/EPUB), con la possibilità di diffondere estratti sui social. Ogni fase del processo è stata accompagnata da momenti di revisione e controllo, sia dei testi che della resa grafica, per assicurare la qualità e la coerenza complessiva del prodotto editoriale.

```mermaid
graph LR
A[Raccolta contenuti] --> B((Verifica fonti))
A --> C[Strutturazione contenuti]
B --> D{Contenuti validi?}
C --> D
D -->|Sì| E[Applicazione stile grafico]
D -->|No| F[Revisione/redazione]
E --> G[Generazione metadati]
G --> H[Conversione PDF/EPUB/HTML]
H --> I[Distribuzione multicanale]
```
```mermaid
flowchart LR
    A[Acquisizione automatica via API Wikipedia] --> B[Controllo e integrazione manuale]
    B --> C{Licenza libera?}
    C -->|Sì| D[Strutturazione HTML per sezioni]
    C -->|No| E[Esclusione o sostituzione]
    D --> F[Applicazione stile CSS]
    F --> G[Generazione metadati YAML / Schema.org]
    G --> H[Conversione PDF / EPUB con Pandoc]
    H --> I[Distribuzione su Web e piattaforme]
```

### Tecnologie adottate

Per realizzare questo progetto sono state utilizzate diverse tecnologie, selezionate per facilitare la produzione, la conversione e la distribuzione del contenuto in formato digitale. Il punto di partenza è stato l’utilizzo di Markdown, ideale per scrivere testi strutturati in modo ordinato e convertibile in vari formati. Successivamente, i contenuti sono stati trasformati in HTML, linguaggio utilizzato per costruire le pagine web, con il supporto di CSS per la definizione dello stile grafico e della formattazione visiva.

Per rendere il progetto più interattivo e dinamico, è stato integrato anche JavaScript, impiegato in particolare per estrarre automaticamente i metadati dalle API di Wikipedia, in modo da popolare le pagine HTML con contenuti sempre aggiornati senza dover intervenire manualmente. Uno dei formati finali previsti è l’EPUB, standard internazionale per la pubblicazione di eBook, generato a partire dagli HTML e Markdown grazie all’utilizzo di Pandoc.

Oltre a linguaggi e strumenti di formattazione, sono state utilizzate anche fonti e piattaforme online gratuite. In particolare, Wikipedia è stata usata come principale fonte informativa tramite il suo sistema di API, mentre per il supporto audio-visivo si sono utilizzati servizi di video hosting come YouTube e, in alcuni casi, strumenti online per la generazione vocale o l’adattamento dei contenuti multimediali.

| Tecnologia     | Scenario 1 – Studente universitario            | Scenario 2 – Docente in classe                    |
|----------------|------------------------------------------------|---------------------------------------------------|
| **HTML5/CSS3** | Visualizza il compendio online da browser     | Proietta sezioni in aula con struttura chiara     |
| **JavaScript** | Estrae dinamicamente i metadati da Wikipedia  | Garantisce contenuti sempre aggiornati            |
| **Pandoc**     | Converte i contenuti per stampa/tesi (PDF)    | Esporta EPUB per lettura offline su e-reader      |
| **Markdown**   | Facilita la scrittura dei testi modulari      | Permette aggiornamenti rapidi senza formattazione |
| **YAML**       | Definisce i metadati per ogni sezione         | Compatibile con standard educativi e archivi      |

### Esecuzione del flusso

I file utilizzati per la realizzazione del progetto sono disponibili nella repository documentale 

## Valutazione dei risultati raggiunti

### Valutazione del flusso di produzione

Il flusso di produzione adottato ha permesso di ridurre sensibilmente i tempi di gestione documentale grazie all’automazione dell’estrazione dei metadati e alla conversione automatica dei formati con Pandoc. L’uso di fonti affidabili e strutture standard ha ridotto gli errori e migliorato la coerenza dei contenuti. L’organizzazione modulare e l’impaginazione coerente hanno aumentato la qualità percepita dei documenti. Le tecnologie semplici e accessibili utilizzate hanno favorito l’accettazione da parte degli utenti. Infine, la possibilità di esportare in HTML, EPUB e PDF ha esteso i canali di distribuzione e ha reso il compendio adatto a diversi scenari d’uso, sia educativi che personali.
 
### Confronto con lo stato dell'arte

È possibile confrontare ASIS e TOBE analizzando i due flussi di gestione docu-mentale. Infatti il flusso di gestione documentale realizzato con mermaid analizza e descrive il flusso di gestione che implementa nuove tecnologie, permettendo di eliminare o comprimere alcuni passaggi che prima era necessario svolgere senza l'aiuto delle tecnologie. Il flusso di gestione documentale realizzato con uno schema .svg descrive l'intero procedimento di realizzazione di un documento, dove sono presenti vari passaggi intermedi che devono essere rispettati e realizzati in maniera separata rispetto al flusso di gestione proposto in questo progetto
dove vengono uniti alcuni passaggi in un unico solo.

### Limiti emersi

Sono emersi alcuni limiti con la conversione dei file in formato ePub, siccome durante la conversione non era possibile convertire alcuni caratteri specifici come " ' " o "". Non è stato possibile aggiungere la riproduzione dell'audio nei formati .docx e .epub del documento. Non è stato possibile aggiungere il font Open Dyslexia al formato ePub per via della generazione di errori durante la conversione da formato .md a formato .ePub. Inoltre non è stato possibile aggiungere media all'interno del file in formato .ePub per via di errori nella conversione da .yaml a .ePub.  

## Conclusioni

I risultati ottenuti dimostrano che gli obiettivi definiti nei casi d’uso sono stati in larga parte raggiunti. Il prodotto editoriale multiformato è stato realizzato con successo in HTML, PDF ed EPUB, e reso disponibile attraverso diversi canali di distribuzione, adattandosi così a molteplici scenari d’uso: dalla consultazione individuale alla didattica in aula. L’automazione del flusso tramite JavaScript e Pandoc ha permesso una notevole riduzione dei tempi di produzione, garantendo al tempo stesso coerenza nei contenuti e nella struttura.

Particolarmente soddisfacenti sono stati i risultati ottenuti nella qualità visiva e organizzativa dei documenti HTML e PDF, così come nell’integrazione dei metadati e nell’accessibilità dei contenuti. Le limitazioni principali sono emerse nella gestione dei contenuti multimediali all’interno del formato EPUB, dove problemi tecnici legati alla conversione dei metadati hanno impedito l’inserimento di video o immagini dinamiche. Nonostante ciò, il progetto ha mostrato una forte adattabilità e un buon grado di scalabilità, confermando la validità del flusso di produzione adottato.

## Bibliografia e sitografia
	•	Voce “Jesse Owens” – Wikipedia
	•	Voce “Diego Armando Maradona” – Wikipedia
	•	Voce “Mano de Dios” – Wikipedia
	•	Voce “Michael Jordan” – Wikipedia
	•	Voce “Giochi della XI Olimpiade” – Wikipedia
	•	Articolo “Jesse Owens, l’afroamericano che batté Hitler alle Olimpiadi” – Storicang.it
	•	Video “Mano de Dios – Diego Maradona” – YouTube
	•	Articolo “La Mano de Dios di Maradona” – Il Post
	•	Articolo “Maradona e la Mano de Dios” – La Repubblica
	•	Articolo “La Mano de Dios spiegata” – Fanpage
	•	Articolo “Michael Jordan e la frase sui novemila tiri sbagliati” – Sportface.it
