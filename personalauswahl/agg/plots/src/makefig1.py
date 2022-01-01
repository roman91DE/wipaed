def plotWordCloud(text: str):
  """ generate wordcloud plot from input string"""
  # library imports
  import matplotlib.pyplot as plt
  from wordcloud import WordCloud, STOPWORDS
  import numpy as np

  # init obj
  x, y = np.ogrid[:1000, :1000]
  mask = (x - 500) ** 2 + (y - 500) ** 2 > 400 ** 2
  mask = 255 * mask.astype(int)
  
  wordcloud = WordCloud(
    background_color="white",
    width=1920,
    height=1080,
    mask=mask,
    random_state=1,
    collocations=False,
    stopwords = STOPWORDS.union({
      "abs", "werden", "wird", "bei", "es", "um", "zum" ,"der", "die", "das", "und", "oder", "ist", "soll", "auf", "den", "wegen", "einer", "von", "nicht", "ist", "durch", "sind", "für", "eine", "zu", "nach", "in", "dem", "zur", "nach", "ab", "wenn", "wenn", "sich", "nach", "im", "sowie", "des", "ein", "nur", "dass", "hat", "aufgrund", "mit", "diese", "einen", "vor", "keine", "diese", "auch", "einem", "wurde", "aber", "wie", "bereits", "können", "ohne"
    })
    ).generate(text)
    

  # init pyplot
  plt.figure(figsize=(400, 300))
  plt.imshow(wordcloud) 
  plt.axis("off")
  plt.show()


wiki = """Allgemeines Gleichbehandlungsgesetz
Basisdaten
Titel:	Allgemeines Gleichbehandlungsgesetz
Abkürzung: 	AGG
Art: 	Bundesgesetz
Geltungsbereich: 	Bundesrepublik Deutschland
Rechtsmaterie: 	Privatrecht, Arbeitsrecht
Fundstellennachweis: 	402-40
Erlassen am: 	14. August 2006
(BGBl. I S. 1897, 1910)
Inkrafttreten am: 	18. August 2006
Letzte Änderung durch: 	Art. 8 G vom 3. April 2013 (BGBl. I S. 610)
Inkrafttreten der
letzten Änderung: 	21. Dezember 2012
(Art. 10 Satz 2 G vom 3. April 2013)
GESTA: 	D073
Weblink: 	Text des AGG
Bitte den Hinweis zur geltenden Gesetzesfassung beachten.

Das Allgemeine Gleichbehandlungsgesetz (AGG) – umgangssprachlich auch Antidiskriminierungsgesetz genannt – ist ein deutsches Bundesgesetz, das „Benachteiligungen aus Gründen der Rasse oder wegen der ethnischen Herkunft, des Geschlechts, der Religion oder Weltanschauung, einer Behinderung, des Alters oder der sexuellen Identität verhindern und beseitigen soll“. Zur Verwirklichung dieses Ziels erhalten die durch das Gesetz geschützten Personen Rechtsansprüche gegen Arbeitgeber und Private, wenn diese ihnen gegenüber gegen die gesetzlichen Diskriminierungsverbote verstoßen. Mit seinem Inkrafttreten 2006 wurde das Beschäftigtenschutzgesetz abgelöst.
Allgemein

Das Allgemeine Gleichbehandlungsgesetz gilt in seinem arbeitsrechtlichen Teil (§§ 6–18) für Arbeitnehmer und Auszubildende unabhängig von der Rechtsform des Arbeitgebers, also primär in der Privatwirtschaft. Es schließt auch Stellenbewerber ein. Für öffentlich-rechtliche Dienstverhältnisse, also für Beamte und Richter insbesondere des Bundes und der Länder findet es entsprechende Anwendung (§ 24). Für Religionsgemeinschaften und ihnen zugeordneten Einrichtungen gilt es nur eingeschränkt (§ 9). Darüber hinaus gilt es auch für bestimmte Bereiche des privaten Vertragsrechts (§§ 19–21).

Schon bisher galt der in Art. 3 Grundgesetz (GG) normierte Grundsatz der Gleichbehandlung, allerdings nur für das Handeln des Staates. Im Verhältnis der Bürger untereinander ist Art. 3 GG, wie alle Normen des öffentlichen Rechts, grundsätzlich nicht anwendbar. Allerdings hat das Bundesarbeitsgericht in seiner Rechtsprechung schon bisher die Grundrechtsnormen im Verhältnis Arbeitgeber-Arbeitnehmer unmittelbar angewandt.

Die konkreten Diskriminierungsverbote des Art. 3 Abs. 3 GG sind nicht völlig deckungsgleich mit denen des Allgemeinen Gleichbehandlungsgesetzes: So verbietet Art. 3 Abs. 3 GG eine Diskriminierung aufgrund der räumlichen Herkunft eines Menschen, nicht aber das AGG. Nach dem AGG hätte es z. B. keine Konsequenzen, wenn ein Kölner Unternehmer grundsätzlich keine Düsseldorfer einstellen und sich dazu auch bekennen würde; ungeachtet, welcher Ethnie der Kölner Unternehmer und die betroffenen Düsseldorfer angehören. Umgekehrt verbietet das GG keine Diskriminierungen auf der Grundlage der sexuellen Identität eines Menschen, wohl aber das AGG.

Die Besonderheit des Allgemeinen Gleichbehandlungsgesetzes im zivilrechtlichen Teil liegt nun darin, dass es als Schutzgesetz in den Privatrechtsverkehr eingreift und damit die Privatautonomie einschränkt. Nach Ansicht des Gesetzgebers ist dies, da der Grundrechtsschutz vorrangig staatliches Handeln erfasst, notwendig, um den objektiv-rechtlichen Gleichbehandlungsauftrag des Grundgesetzes auch für das Verhalten der Bürger untereinander umzusetzen.
Anwendungsbereiche

Das Allgemeine Gleichbehandlungsgesetz findet nicht in allen gesellschaftlichen und rechtlichen Bereichen Anwendung und verbietet auch nicht jede Form der Ungleichbehandlung. Vielmehr verbietet es Diskriminierungen nur dann, wenn diese auf bestimmten, im Gesetz genannten Merkmalen beruhen. Zweitens sind Ungleichbehandlungen nur in bestimmten gesetzlich genannten Situationen verboten.
Personenbezogene Merkmale

Das Allgemeine Gleichbehandlungsgesetz verbietet Benachteiligungen nur, soweit sie an eines der folgenden personenbezogenen Merkmale anknüpfen:

    Rasse oder ethnische Herkunft,[1]

    Geschlecht

    Religion und Weltanschauung,

    Behinderung

    Alter (jedes Lebensalter)

    sexuelle Identität

Gegenüber der EU-Richtlinie, in der „sexuelle Ausrichtung“ definiert ist, wird hier „sexuelle Identität“ mit einem Verweis auf den schon bestehenden § 75 BetrVG verwendet. Auf jeden Fall sind die sexuelle Selbstdefinition sowie die sexuelle Ausrichtung auf andere Menschen (sexuelle Orientierung) erfasst. Daneben ist auch der Transvestitismus einbezogen. Nach der Gesetzesbegründung sollen Intersexualität und Transsexualität auch hierdurch geschützt sein, nach der Rechtsprechung des EuGH jedoch als Geschlecht.[2]

Nicht geregelt ist hingegen die Benachteiligung aufgrund weiterer Merkmale aus der EU-Charta, wie beispielsweise die Diskriminierung aufgrund des Vermögens und der sozialen Herkunft.
Sachlicher Anwendungsbereich

Sachlich bezieht sich das Gesetz nach § 2 Abs. 1 AGG auf

    die Bedingungen für den Zugang zu Erwerbstätigkeit sowie für den beruflichen Aufstieg, einschließlich Auswahlkriterien und Einstellungsbedingungen,

    die Beschäftigungs- und Arbeitsbedingungen einschließlich Arbeitsentgelt und Entlassungsbedingungen,

    den Zugang zu Berufsberatung, Berufsbildung, Berufsausbildung, beruflicher Weiterbildung sowie Umschulung und praktischer Berufserfahrung,

    Mitgliedschaft und Mitwirkung in Gewerkschaften und Arbeitgebervereinigungen und Vereinigungen, deren Mitglieder einer bestimmten Berufsgruppe angehören,

    den Sozialschutz, einschließlich der sozialen Sicherheit und der Gesundheitsdienste,

    die sozialen Vergünstigungen,

    die Bildung,

    den Zugang zu und die Versorgung mit Gütern und Dienstleistungen, die der Öffentlichkeit zur Verfügung stehen, einschließlich von Wohnraum.

Bei Stellenbesetzungen, zum Beispiel auch im öffentlichen Dienst, bezieht sich das Diskriminierungsverbot lediglich auf ein Verfahren mit Ausschreibung sowie auf den Ausschreibungstext selbst, nicht auf die Auswahl der Bewerber.[3] Da in einigen Bereichen (zum Beispiel Hochschulen) Stellen ohne Ausschreibung vergeben werden, können Arbeitgeber daher weiterhin nach Belieben diskrimieren, ohne dass diese Diskriminierung Gegenstand des Allgemeinen Gleichbehandlungsgesetzes werden könnte.
Formen der Benachteiligung

Folgende Formen der Ungleichbehandlung sind zu unterscheiden:

    unmittelbare Benachteiligung (§ 3 Abs. 1 AGG): weniger günstige Behandlung einer Person gegenüber einer anderen in einer vergleichbaren Situation,

    mittelbare Benachteiligung (§ 3 Abs. 2 AGG): Benachteiligung durch scheinbar neutrale Vorschriften, Maßnahmen, Kriterien oder Verfahren, die sich faktisch diskriminierend auswirken,

    Belästigung (§ 3 Abs. 3 AGG): Verletzung der Würde der Person, insbesondere durch Schaffung eines von Einschüchterungen, Anfeindungen, Erniedrigungen, Entwürdigungen oder Beleidigungen gekennzeichneten Umfelds,

    sexuelle Belästigung (§ 3 Abs. 4 AGG),

    die Anweisung zu einer dieser Verhaltensweisen (§ 3 Abs. 5 AGG).

Für die Frage, was mit der in § 3 Abs. 2 AGG gegebenen Definition der mittelbaren Diskriminierung genau gemeint ist, kann die bisherige Rechtsprechung des Europäischen Gerichtshofs und des Bundesarbeitsgerichts Hilfe geben. Die beiden Gerichte haben zur Klärung des Tatbestands der mittelbaren Diskriminierung weitgehende Vorarbeit geleistet. Das Verbot der mittelbaren Diskriminierung ist ursprünglich an den Gesetzgeber gerichtet und an andere Parteien, soweit sie kollektive Maßnahmen durchführen, d. h. Arbeits- und Lebensbedingungen regeln, bzw. die Durchführung von Schuldverhältnissen durch Maßnahmen mit kollektiver Wirkung konkretisieren. Der Sache nach geht es darum, Verfahren als Diskriminierung zu ahnden, die bestimmte Gruppen von Personen benachteiligen, d. h. weniger günstig behandeln,[4] und dabei zwar eine ausdrückliche Benennung der verbotenen Diskriminierungsmerkmale vermeiden, aber durch die Wahl der scheinbar neutralen Kriterien darauf angelegt sind, gerade solche Personen zu benachteiligen, die eines oder mehrere der vom AGG verbotenen Merkmale aufweisen.

Die mittelbare Diskriminierung verläuft im Ausgangspunkt trotz der komplexen Definition des Gesetzes nach einem einheitlichen Muster:

    Zunächst erfolgt eine Gruppenbildung nach nicht ausdrücklich verbotenen Kriterien. Zum Beispiel unterscheidet der Arbeitgeber bei einer Maßnahme zwischen Teilzeit- und Vollzeitbeschäftigten, oder ein Vermieter unterscheidet zwischen Beschäftigten und Arbeitslosen oder zwischen Selbständigen und Angestellten.

    Anschließend wird die eine Gruppe kollektiv und unmittelbar im Sinne von § 3 Abs. 1 AGG benachteiligt. Das kann dadurch geschehen, dass nur die andere Gruppe Vorteile erhält oder dadurch, dass die fragliche Gruppe direkt schlechter behandelt wird. Zum Beispiel wird Teilzeitbeschäftigten keine Lohnfortzahlung gewährt.

    Falls die Benachteiligung der gebildeten Gruppe nun – statistisch betrachtet – in besonderer Weise diejenigen betrifft, die durch Diskriminierungsverbote geschützt werden sollen – also etwa mehr Ausländer als Inländer betrifft oder mehr Frauen als Männer – weil diese in der gebildeten und benachteiligten Gruppe im Verhältnis zur anderen Gruppe überrepräsentiert sind, liegt der Tatbestand einer mittelbaren Diskriminierung vor.

    Eine mittelbare Diskriminierung ist aber ausnahmsweise zulässig, wenn diese statistische „besondere Betroffenheit“ einer vom AGG geschützten Gruppe nur Nebenprodukt eines erlaubten Ziels ist. Wer also etwa das erlaubte Ziel verfolgt, nur die Betriebstreue unbefristet Beschäftigter durch ein Weihnachtsgeld zu belohnen, darf die befristet Beschäftigten von der Zahlung ausnehmen, auch wenn diese Maßnahme ganz überwiegend Frauen trifft.

Aus dem Wortlaut des Gesetzes lässt sich das indessen nicht entnehmen.
Unerlaubte Diskriminierung im Arbeitsrecht
Rechtfertigung von Ungleichbehandlungen

Im Arbeitsverhältnis sind Vereinbarungen, die gegen Diskriminierungsverbote verstoßen, unwirksam (§ 7 Abs. 2 AGG).

Der Arbeitgeber kann jedoch einwenden, dass die Ungleichbehandlung im Einzelfall gerechtfertigt ist (§§ 5 und 8 bis 10 AGG). So kann eine unterschiedliche Behandlung gerechtfertigt sein, wenn dadurch auf angemessene Weise eine bestehende Diskriminierung beseitigt wird. Ein absoluter Vorrang der geschützten Gruppe ist dabei jedoch ausgeschlossen.

Eine unterschiedliche Behandlung, z. B. wegen des Geschlechts, ist nur zulässig, wenn das Geschlecht wegen der Art der auszuübenden Tätigkeit oder der Bedingungen ihrer Ausübung eine unverzichtbare Voraussetzung für die Tätigkeit ist, z. B. Einstellung einer Balletttänzerin (§ 8 Abs. 1 AGG). Für diesen Einwand trägt der Arbeitgeber im Prozess die Darlegungs- und Beweislast (§ 22 AGG). Er wird also den Prozess verlieren, wenn er unzureichend vorträgt oder der Beweis misslingt. Ergänzend gilt für die Ungleichbehandlung beim Arbeitsentgelt wegen des Geschlechts das Entgelttransparenzgesetz.

Für Beschäftigte von Religionsgemeinschaften sind unterschiedliche Behandlungen wegen der Religion oder Weltanschauung ebenfalls zulässig (§ 9 AGG). So wird es z. B. keine verbotene Diskriminierung darstellen, wenn ein Muslim nicht als Reinigungskraft eines katholischen Kindergartens eingestellt wird. Dies entspricht der bereits bestehenden Rechtslage im Arbeitsrecht, die Religionsgemeinschaften, im Gegensatz zu Tendenzbetrieben, vollständig vom Betriebsverfassungsgesetz ausnimmt. In Privatbetrieben hingegen ist dem Unternehmer nicht gestattet, bei der Auswahl von Stellenbewerbern eine Auswahl aufgrund der eigenen religiösen oder weltanschaulichen Überzeugungen vorzunehmen. Ein Muslim muss also auch Juden einstellen und umgekehrt. Mit dem Urteil (2 AZR 579/12) vom 25. April 2013 bestätigte das Bundesarbeitsgericht auch die Möglichkeit der außerordentlichen Kündigung eines Arbeitnehmers einer kirchlichen Einrichtung, wenn er mit seinem Kirchenaustritt gegen seine arbeitsvertraglichen Pflichten (Arbeitsvertragsrichtlinien (AVR)) verstoße. Der Arbeitnehmer werde dadurch nicht nach dem AGG diskriminiert.[5]

Altersbedingte Ungleichbehandlungen können gerechtfertigt sein, wenn sie objektiv angemessen sind und ein legitimes Ziel verfolgen, z. B. Mindest- oder Höchstalter für eine Einstellung, Mindestalter für die Inanspruchnahme von Ansprüchen aus betrieblichen Alterssicherungssystemen (§ 10 AGG).

Ungleichbehandlungen sind generell dann erlaubt, wenn ein geächtetes Kriterium nicht das Hauptmotiv für die Ungleichbehandlung bildet. So stellte das Arbeitsgericht Berlin fest, dass es zulässig sei, Bewerber wegen mangelnder Deutschkenntnisse nicht einzustellen, obwohl von solchen Praktiken vorwiegend Menschen fremder ethnischer Herkunft betroffen seien.[6]

Auch die tarifvertraglich vorgesehene automatische Beendigung des Arbeitsvertrags aus Altersgründen, wie sie im Rahmentarifvertrag für die gewerblichen Beschäftigten in der Gebäudereinigung vorgesehen ist, ist mit der dem AGG zugrunde liegenden Richtlinie 2000/78 vereinbar.[7][8]
Rechtsfolgen unerlaubter Ungleichbehandlungen

Liegen ungerechtfertigte Ungleichbehandlungen vor, hat der Mitarbeiter ein Beschwerderecht (§ 13 AGG).

Der Arbeitgeber muss dann gegen die Beschäftigten, die gegen das Benachteiligungsverbot verstoßen, die geeigneten, erforderlichen und angemessenen Maßnahmen zur Unterbindung der Benachteiligung ergreifen, z. B. Abmahnung, Versetzung, Kündigung (§ 12 Abs. 3 AGG), bzw. bei einer Benachteiligung durch Dritte Schutzmaßnahmen für die Mitarbeiter (§ 12 Abs. 4 AGG).

Bei Belästigungen kann darüber hinaus ein Leistungsverweigerungsrecht bestehen: Ergreift der Arbeitgeber keine oder ungeeignete Maßnahmen, um eine Belästigung zu beenden, so kann der Arbeitnehmer die Leistung verweigern, wenn und soweit dies zu seinem Schutz erforderlich ist (§ 14 AGG). Der Anspruch auf das Arbeitsentgelt bleibt in diesem Fall bestehen.

Daneben hat der Mitarbeiter einen Schadensersatzanspruch (§ 15 Abs. 1 AGG), der sich auf Ersatz von Vermögensschäden richtet, es sei denn, dass kein dem Arbeitgeber zuzurechnendes Verschulden vorlag. Umstritten ist, ob dieser Anspruch auch den Verdienst umfasst, der dem abgelehnten Bewerber entgeht.

Der Mitarbeiter hat auch einen vom Verschulden des Arbeitgebers unabhängigen Entschädigungsanspruch (§ 15 Abs. 2 AGG), der bei Nichtvermögensschäden einen angemessenen Ausgleich in Geld für die erlittene Ungleichbehandlung vorsieht. Die Höhe des Ausgleichsanspruchs richtet sich u. a. nach der Art und Schwere der Interessensschädigung, dem Anlass und den Beweggründen des Arbeitgebers, der Dauer, dem Grad des Verschuldens des Arbeitgebers sowie danach, ob es sich um einen Wiederholungsfall handelt. Das Bundesarbeitsgericht spricht bei vergleichbaren Fällen einer Ungleichbehandlung (nach dem früheren § 611a BGB) einen Entschädigungsanspruch von mindestens einem Monatsgehalt zu. Das AGG sieht für den Fall einer diskriminierenden Nichteinstellung einen Höchstbetrag von drei Monatsgehältern vor. Diese Begrenzung entfällt aber, wenn der Bewerber ohne die Diskriminierung auf jeden Fall eingestellt worden wäre.

Für die Geltendmachung des Schadensersatz- und des Entschädigungsanspruchs gilt eine Frist von zwei Monaten (§ 15 Abs. 4 AGG). Zuständig sind die Arbeitsgerichte (§ 61b ArbGG).

Bei einem Verstoß gegen das Benachteiligungsverbot (§ 7 AGG) besteht kein Anspruch auf Einstellung, Berufsausbildung oder beruflichen Aufstieg (§ 15 Abs. 6 AGG).

Der Arbeitgeber darf Beschäftigte nicht wegen einer Inanspruchnahme von Rechten nach dem AGG benachteiligen (§ 16 AGG).

Soweit ein Betriebsrat besteht bzw. eine Gewerkschaft im Betrieb vertreten ist, haben diese bei groben Verstößen des Arbeitgebers ein eigenes Klagerecht, und zwar auch ohne Zustimmung des Betroffenen (§ 17 Abs. 2 AGG). Dies gilt nicht für den Personalrat im öffentlichen Dienst.
Reaktionen von Arbeitgebern und Personalverantwortlichen

Arbeitgeber und Personalverantwortliche müssen sich seit Inkrafttreten des AGG mit folgenden Fragen befassen:

    Wer muss wie vor Diskriminierung geschützt werden (z. B. eigene freie Mitarbeiter)?

    Gibt es im Betrieb mittelbare/unmittelbare, bewusste/unbewusste/billigend in Kauf genommene Diskriminierung, bzw. gibt es Situationen, bei denen deren Entstehen vorhersehbar ist?

    Welches sind Belästigungs- oder Benachteiligungsmerkmale?

    Können Benachteiligungen AGG-konform gerechtfertigt werden?

Insbesondere müssen Pflichten, Haftungsrisiken und Entschädigungsansprüche beachtet werden, die das AGG Arbeitgebern neu zuweist: Diese Änderungen betreffen die Schutz-, Organisations- und Maßnahmenpflichten des Arbeitgebers, die Beweislastumkehr zu Lasten des Arbeitgebers, die Entschädigungsansprüche, auch einstweilige Verfügungsverfahren und nicht zuletzt das Beschwerde- und Leistungsverweigerungsrecht der Arbeitnehmer.

Arbeitgeber müssen die neuen Rechte des Betriebsrates (nicht allerdings des Personalrates), die notwendigen Neuregelungen für Stellenausschreibungen, Einstellungs- und Auswahlverfahren, Absagen, neue Maßstäbe auch für Arbeitsverträge, Kündigungen, Sozialauswahl, Arbeitszeugnisse beachten. Die Neuregelungen betreffen Organisation, Zusammenarbeit, Mitarbeiterführung, Gehaltsfragen ebenso wie die Mitbestimmungsmodalitäten von Arbeitnehmer respektive die Zusammenarbeit mit dem Betriebsrat.

In Bewerbungsverfahren ist die Praxis üblich geworden, keinerlei Gründe mehr für die Nicht-Einstellung eines Kandidaten anzuführen. Stattdessen enthalten Anschreiben bei Rücksendungen von Bewerbungsunterlagen oft nur noch Mustertexte wie: „Leider konnte ihre Bewerbung nicht berücksichtigt werden.“[9] Bei dem Entschluss, so zu verfahren, spielt die Hoffnung von Arbeitgebern eine zentrale Rolle, keine Angriffspunkte für den Verdacht zu bieten, es liege ein Fall unzulässiger Diskriminierung des jeweiligen Bewerbers vor.
Versicherbarkeit

Die Versicherungsbranche reagiert inzwischen durch das Angebot spezieller Versicherungspolicen (so genannter englisch Liability Employment Practices). In Anlehnung an US-amerikanische Vorbilder sollen sich Arbeitgeber gegen das Risiko einer Inanspruchnahme durch Mitarbeiter und Bewerber wegen Verletzung des AGG – insbesondere bei Ansprüchen nach § 15 AGG – versichern können.
Unerlaubte Diskriminierung im Zivilrecht

Auch im allgemeinen Zivilrechtsverkehr, d. h. bei der Begründung, Durchführung und Aufhebung von Verträgen, sind Diskriminierungen aus einem der im Gesetz genannten Merkmale grundsätzlich unzulässig (§§ 19 bis 21 AGG). Das betrifft jedoch im Wesentlichen nur

    den Abschluss sogenannter Massengeschäfte (die typischerweise ohne Ansehen der Person abgeschlossen werden)

    und privatrechtliche Versicherungsverträge.

Darüber hinaus ist eine „Benachteiligung aus Gründen der Rasse oder wegen der ethnischen Herkunft“ auch bei der Begründung, Durchführung und Beendigung sonstiger zivilrechtlicher Schuldverhältnisse im Sinne des § 2 Abs. 1 Nr. 5 bis 8 AGG (§ 19 Abs. 2 AGG) unzulässig, wenn sie nicht die nach § 19 Abs. 3 AGG benannten Ausnahmen der ausgewogenen Siedlungsstrukturen oder ausgeglichener wirtschaftlicher, sozialer oder kultureller Strukturen betreffen.[10]

Keine Anwendung finden Diskriminierungsverbote auf

    familien- und erbrechtliche Rechtsverhältnisse (§ 19 Abs. 4 AGG), sowie auf

    Schuldverhältnisse, bei denen ein besonderes Nähe- oder Vertrauensverhältnis der Parteien oder ihrer Angehörigen begründet wird; dies gilt auch für das Mietrecht, und zwar insbesondere dann, wenn die Parteien oder ihre Angehörigen auf demselben Grundstück wohnen (§ 19 Abs. 5 AGG). Die Vermietung von nicht mehr als 50 Wohnungen ist in der Regel kein Massengeschäft im Sinne des Allgemeinen Gleichbehandlungsgesetzes.

Liegt objektiv eine Benachteiligung vor, kann diese im Einzelfall gerechtfertigt, d. h. erlaubt und sanktionslos, sein. Gerechtfertigt sind Ungleichbehandlungen aus sachlichen Gründen, z. B. zur Abwehr von Gefahren (§ 20 AGG).

Bei privatrechtlichen Versicherungsverträgen ist eine Ungleichbehandlung aufgrund des Geschlechts zulässig, wenn das Geschlecht ein bestimmender Faktor bei der versicherungsmathematischen Risikobewertung ist. Das entsprechende Datenmaterial und die Berechnung müssen offengelegt werden. Kosten von Schwangerschaft und Entbindung dürfen nicht zu unterschiedlichen Prämien oder Leistungen führen, sie müssen vielmehr zwingend geschlechtsneutral verteilt werden (§ 20 Absatz 2 AGG).

Bei einer ungerechtfertigten Ungleichbehandlung hat der Benachteiligte Beseitigungs-, Unterlassungs- und materiellen/immateriellen Schadensersatzansprüche, die jeweils innerhalb einer Frist von zwei Monaten geltend gemacht werden müssen (§ 21 AGG).
Steuerrecht

Steuerrechtlich werden Entschädigungen, welche auf Grund des AGG gezahlt werden, als steuerfreie Schmerzensgeldzahlungen gewertet.
Besonderheiten im Prozess
Beweislast

Der Kläger muss zunächst 1. eine weniger günstige Behandlung gegenüber einer anderen Person 2. in einer vergleichbaren Situation 3. unmittelbar oder mittelbar wegen eines in § 1 AGG genannten Grundes darlegen und beweisen. Gem. § 22 AGG hat der Kläger hinsichtlich der dritten Voraussetzung lediglich Indizien zu beweisen, die eine Benachteiligung wegen eines in § 1 AGG genannten Grundes vermuten lassen mit der Folge, dass der Beklagte die Beweislast dafür trägt, dass keine nach dem AGG verbotene Benachteiligung vorliegt. Den Beklagten trifft dann die volle Darlegungs- und Beweislast für das Nichtvorliegen einer verbotenen Benachteiligung.[11]

Die vom Kläger vorgetragenen Tatsachen müssen aus objektiver Sicht nach allgemeiner Lebenserfahrung mit überwiegender Wahrscheinlichkeit darauf schließen lassen, dass eine Benachteiligung aufgrund eines in § 1 AGG genannten Merkmals erfolgt ist.[12] Dann genügt es, dass ein nach § 1 AGG unzulässiges Kriterium auch nur neben anderen Kriterien eine Rolle für eine ungünstigere Behandlung gespielt hat (sog. Motivbündel). Für eine „überwiegende Wahrscheinlichkeit“  genügt es beispielsweise, wenn der Arbeitgeber eine Stellenanzeige nicht geschlechtsneutral formuliert, allgemeine Statistiken etwa über die Unterrepräsentanz von Frauen in Führungspositionen haben hingegen keine ausreichende Indizfunktion.[13]

Im Rahmen der richterlichen Würdigung des Sachverhalts kann u. a. das sog. Testing-Verfahren[14] einen tatsächlichen Anhaltspunkt darstellen. Dabei wird dem Vermieter bzw. Arbeitgeber eine weitere qualitativ vergleichbare Bewerbung einer weiteren (fiktiven) Person um die Wohnung bzw. Arbeitsstelle vorgelegt, auf die das Diskriminierungsmerkmal nicht zutrifft. Für den Rückschluss auf Diskriminierung müssen jedoch andere, nicht diskriminierende Erklärungen für eine Benachteiligung möglichst ausgeschlossen werden können, indem sich die betroffene und die Testperson mit Ausnahme des vermuteten Diskriminierungskriteriums weitestgehend gleichen.[15] Das gilt im Arbeitsrecht insbesondere für die objektive Eignung für die zu besetzende Stelle.[16]

Im Erfolgsfall ist der Anspruch des Klägers auf eine Entschädigung gem. § 15 Abs. 2 AGG begrenzt; Schadensersatz erhält er nicht.[17][18]
Klagefrist

Wenn die Tarifvertragsparteien nichts anderes vereinbart haben, muss ein Schadensersatz- oder Entschädigungsanspruch binnen zwei Monaten nach Ablehnung der Bewerbung bzw. nach Kenntnis von der Benachteiligungshandlung schriftlich beim Arbeitgeber geltend gemacht werden, § 15 Abs. 4 AGG. Für eine Klage zum Arbeitsgericht ist eine weitere Frist von drei Monaten ab schriftlicher Geltendmachung zu beachten, § 61b Abs. 1 ArbGG.
Europarechtlicher Hintergrund

    Hauptartikel: Europarechtliche Vorgaben zum Diskriminierungsverbot

Die Regelungsbereiche der EG-Antidiskriminierungsrichtlinien

Das Allgemeine Gleichbehandlungsgesetz dient der Umsetzung von vier Europäischen Richtlinien aus den Jahren 2000 bis 2004, nämlich um die

    Richtlinie 2000/43/EG des Rates vom 29. Juni 2000 zur Anwendung des Gleichbehandlungsgrundsatzes ohne Unterschied der Rasse oder der ethnischen Herkunft (ABl. EG Nr. L 180 S. 22) – so genannte Antirassismus-Richtlinie –

    Richtlinie 2000/78/EG des Rates vom 27. November 2000 zur Festlegung eines allgemeinen Rahmens für die Verwirklichung der Gleichbehandlung in Beschäftigung und Beruf (ABl. EG Nr. L 303 S. 16) – so genannte Rahmenrichtlinie Beschäftigung –

    Richtlinie 2002/73/EG des Europäischen Parlaments und des Rates vom 23. September 2002 zur Änderung der Richtlinie 76/207/EWG des Rates zur Verwirklichung des Grundsatzes der Gleichbehandlung von Männern und Frauen hinsichtlich des Zugangs zur Beschäftigung, zur Berufsbildung und zum beruflichen Aufstieg sowie in Bezug auf die Arbeitsbedingungen (ABl. EG Nr. L 269 S. 15) – so genannte Gender-Richtlinie –

    Richtlinie 2004/113/EG des Rates vom 13. Dezember 2004 zur Verwirklichung des Grundsatzes der Gleichbehandlung von Männern und Frauen beim Zugang zu und bei der Versorgung mit Gütern und Dienstleistungen (ABl. Nr. L 373 vom 21/12/2004 S. 37–43)

Einige Rechtsexperten vertreten die Auffassung, dass das Allgemeine Gleichbehandlungsgesetz die Vorgaben der vier EG-Richtlinien nur ungenügend umsetze und daher in einigen Punkten europarechtswidrig sei.[19]
Entstehung des Gesetzes

Das Allgemeine Gleichbehandlungsgesetz geht im Kern auf den Entwurf des so genannten Antidiskriminierungsgesetzes (ADG) zurück, der bereits in der 15. Legislaturperiode erarbeitet und beraten,[20] aber infolge der Diskontinuität des Gesetzgebungsprozesses nie verabschiedet  wurde.

Nach den vorgezogenen Bundestagsneuwahlen brachte die Fraktion Bündnis 90/Die Grünen im Dezember den ADG-Entwurf erneut in den Bundestag ein. Dieser Entwurf wurde im Bundestag beraten, fand aber keine parlamentarische Mehrheit.

Anfang Mai 2006 einigten sich SPD, CDU und CSU auf einen neuen Gesetzesentwurf. Dieser Regierungsentwurf erhielt die Bezeichnung Allgemeines Gleichbehandlungsgesetz, war aber inhaltlich in großen Teilen mit dem Entwurf des Antidiskriminierungsgesetzes von 2005 identisch.

Wichtige inhaltliche Änderungen des Allgemeinen Gleichbehandlungsgesetzes zum Entwurf des Antidiskriminierungsgesetzes sind folgende:

    die Kirchenklausel (§ 9 AGG)

    Regelung des Kontrahierungszwangs wurde gestrichen, ohne dass dieser jedoch entfällt

    neue Besonderheiten und Klarstellungen bei der Beweislast und beim Klagerecht der Gewerkschaften

    Einschränkungen des Verbandsklagerechts

    keine mögliche Haftung des Arbeitgebers für Handlungen Dritter

Besonders umstritten ist die Ausklammerung des arbeitsgerichtlichen Kündigungsrechts in § 2 Abs. 4 des Allgemeinen Gleichbehandlungsgesetzes. Dies dürfte der Umsetzung der EG-Richtlinie zuwiderlaufen und einen Verstoß gegen Art. 3 Abs. 1 lit. c der Richtlinie 2000/78/EG darstellen. Danach gelten die Diskriminierungsverbote (u. a. wegen der sexuellen Ausrichtung) auch für „die Entlassungsbedingungen“. Unter den Begriff „Entlassungsbedingungen“ fallen auch Kündigungen.[21]

In einem Grundsatzurteil im November 2008 entscheidet das Bundesarbeitsgericht, dass das Allgemeine Gleichbehandlungsgesetz nicht nur bei Einstellungen und während der Berufsausübung gilt, sondern ebenso bei der Kündigung zu berücksichtigen ist.[22]

Das Gesetz wurde mit den Stimmen der CDU, SPD und der Grünen beschlossen, abgelehnt wurde es von der FDP und der Linkspartei mit jeweils gegensätzlicher Begründung.
Das Gesetz in der politischen Auseinandersetzung
Gegner des Gesetzes

Das Gesetzesvorhaben war und ist scharfer rechtspolitischer Kritik seitens der Wirtschaftsverbände sowie seitens der FDP[23] ausgesetzt, insbesondere zu folgenden Punkten:

    Einschränkung der Privatautonomie für Anbieter von Gütern und Dienstleistungen, da sie – anders als private Verbraucher – ihre Kunden gleich behandeln müssen

    Schaffung eines bürokratischen Aufwandes, da durch die Beweislastumkehr jeder Anbieter von Gütern Beweise dafür vorrätig halten muss, dass er gerade nicht diskriminiert hat

    schwierige Abgrenzungsfragen zwischen erlaubter und verbotener Ungleichbehandlung

    vermutete Mehrbelastung der Justiz mit einer Vielzahl von Prozessen

    Auferlegung des staatlichen Gleichbehandlungsgebots auf alle Privaten und damit eine Reduktion marktwirtschaftlicher, nämlich auch irrationaler, Freiheit. Diese Freiheit unterfällt aber ihrerseits dem Schutz der Werteordnung des Grundgesetzes als Allgemeine Handlungsfreiheit, Freiheit der wirtschaftlichen Betätigung und Schutz der eigenen religiösen Überzeugung

    einseitiger Schutz nur einiger ausgewählter Gruppen unter Ausblendung anderer diskriminierungsanfälliger Gruppen wie Kindern und Familien

Weiterhin befürchten einige Kritiker, dass die Situation von Angehörigen einer Minderheit durch das Allgemeine Gleichbehandlungsgesetz verschlechtert werden könnte. So könnten beispielsweise zukünftig Arbeitgeber davon absehen, Angehörige von Minderheiten zu Vorstellungsgesprächen einzuladen, um falschen oder irrtümlichen Diskriminierungsvorwürfen aus dem Weg zu gehen.

Seit Einführung des Gesetzes berichten Gegner des Gesetzes über Personen, die sich nur zum Zwecke der Erlangung von Schadensersatzansprüchen nach dem AGG bei Unternehmen und Firmen auf Stellenausschreibungen bewerben, die diskriminierende Inhalte haben. Nach Berichten[24] sollen vermeintliche Bewerber Formulierungen wie „junges Team“ (Altersdiskriminierung) oder „Bewerbung mit Lichtbild“ (Diskriminierung wegen der Rasse oder Herkunft) als Zeichen einer möglichen Diskriminierung deuten. Die Bewerber hätten kein Interesse an einer Anstellung, sondern würden nach einer Absage Rechte aus dem AGG geltend machen. Diese Praxis nennen die Kritiker AGG-Hopping nach dem „611a-Hopping“. § 611a des Bürgerlichen Gesetzbuchs (BGB) a.F. regelte die Gleichbehandlung von Männern und Frauen bei Stellenausschreibungen, und dasselbe Phänomen sei bereits bei Einführung des § 611a BGB im Jahr 1980 zu beobachten gewesen. Erst 25 Jahre später prägte das Arbeitsgericht Potsdam den Begriff in einem Urteil.[25] Die Sorge vor derartigen Klagen führe in der Praxis nun dazu, dass bei der Ablehnung einer Bewerbung möglichst wenige Informationen herausgegeben werden würden, um erst gar keinen Anfangsverdacht entstehen zu lassen. Hierdurch würde Bewerbern auch weniger konstruktive Kritik gegeben, die bei zukünftigen Bewerbungen helfen könnte.

Andererseits wird zu bedenken gegeben, dass – im Vergleich etwa zum Grundgesetz und zur EU-Grundrechtecharta – wesentliche Bereiche der Diskriminierung im Allgemeinen Gleichbehandlungsgesetz nicht behandelt werden; so vor allem Diskriminierung aufgrund sozialer Herkunft oder wegen Kinderreichtums. Dies führe zu einer Antidiskriminierungshierarchie, und es bestehe die Gefahr, dass Benachteiligung aufgrund sozialer Herkunft per Definition nicht als Diskriminierung wahrgenommen wird. Eine Einbeziehung der sozialen Herkunft in den Antidiskriminierungsrichtlinien war vorgeschlagen, blieb aber bei der Einigung zu den Amsterdamer Verträgen außer Betracht.

Allerdings baut das Allgemeine Gleichbehandlungsgesetz keinen bestehenden Schutz ab. Ein Gesetzentwurf zur Abschaffung der sozialen Diskriminierung liegt in Deutschland nicht vor, wird aber auf europäischer Ebene diskutiert.

Laut einer im März 2005 veröffentlichten Allensbachumfrage lehnte die Mehrheit der Bevölkerung das damals diskutierte Antidiskriminierungsgesetz am Beispiel einer Klage gegen einen Wohnungsvermieter ab.

Juristen bemängeln auch technische Schwächen des Gesetzes. Neben unnötig komplizierten Satzkonstruktionen fällt etwa auf, dass das Gesetz zwar für den Bereich von Kündigungen keine Anwendung finden soll, andererseits aber ausdrückliche Regelungen gerade für diesen Bereich enthält.
Befürworter des Gesetzes

Befürworter kommen vornehmlich aus dem Bereich der Behinderten- und Frauenverbände, dem Lesben- und Schwulenverband in Deutschland (LSVD), dem DGB, der Partei Die Linke, der Grünen und der Sozialdemokratie.

Sie weisen darauf hin, dass die Beweislasterleichterung – für den Bereich der geschlechtsbezogenen Diskriminierung – bereits seit 25 Jahren im BGB bestehe. Des Weiteren sei es unsinnig, wenn Diskriminierung aufgrund der ethnischen Herkunft verboten werde, nicht aber aufgrund der Behinderung, sexueller Identität oder anderer vom Gesetzgeber in das AGG aufgenommenen Kriterien. Sie fordern stattdessen gleichen Schutz für alle.

Sie verweisen darauf, dass es um eine Einbeziehung aller Kriterien von Artikel 13 des Amsterdamer Vertrages geht. Diese Kriterien sind für das Arbeitsrecht auch verbindlich von der EU vorgeschrieben.

Insbesondere wird mit dem moralischen Anspruch argumentiert, der als Grundgedanke hinter dem Gesetzesvorhaben steht. Dieser Anspruch beruft sich auf den Grundgedanken der christlichen Nächstenliebe, der zu den Fundamenten der deutschen Gesellschaft gehöre.
Folgen des Gesetzes

Zu einer Klageflut, vor der Gegner des Gesetzes gewarnt hatten, ist es nach dem Inkrafttreten des Allgemeinen Gleichbehandlungsgesetzes nicht gekommen.[26] Zwar berichtete das Fernsehmagazin plusminus im Februar 2007 von einem Mann, der bislang mehr als 30 Unternehmen wegen angeblicher Geschlechtsdiskriminierung verklagt hat.[27] Die unberechtigte Ungleichbehandlung wegen des Geschlechts war jedoch bereits vor Inkrafttreten des Allgemeinen Gleichbehandlungsgesetzes gesetzlich verboten.

Ein erster großer Prozess wurde von einer Versicherungsangestellten angestrengt, die, unterstützt von Anwälten der Deutschen Gesellschaft für Antidiskriminierungsrecht, von ihrem Arbeitgeber R+V Versicherung einen Schadensersatz von 500.000 Euro wegen eindeutiger Geschlechtsdiskriminierung und möglicher ethnischer Diskriminierung fordert.[28][29] In 1. Instanz sprach das Gericht für die erfolgte Versetzung der Angestellten ihr einen Entschädigungsanspruch in Höhe von 10.818 Euro zu und erklärte die Versetzung für unwirksam.[30]

Das Landesarbeitsgericht Hamm verurteilte im Jahr 2008 ein Frachtflugunternehmen zu Schadensersatz in Höhe von 6.450 Euro. Das Unternehmen hatte eine Stelle als „Flugkapitän“ ausgeschrieben und die Bewerbung einer Pilotin nicht berücksichtigt. In der Gerichtsverhandlung konnte das Unternehmen den Anschein der Diskriminierung nicht widerlegen.[31]

Die Initiative Neue Soziale Marktwirtschaft (INSM) beauftragte die Studie „Gesetzesfolgekosten des Allgemeinen Gleichbehandlungsgesetzes (AGG)“[32][33] welche zu dem Schluss kam, dass 1,73 Mrd. € Kosten durch das AGG für die deutschen Unternehmen entstanden seien. Diese Studie wurde von der Antidiskriminierungsstelle durch eine einberufene Kommission überprüft. Dabei kommen die Kommissionsmitglieder Birger Priddat und Heinrich Wilms in ihrem Gutachten „Nutzen und Kosten des Allgemeinen Gleichbehandlungsgesetzes (AGG)“[34] zu dem Ergebnis, dass die befürchtete Prozesswelle ausgeblieben ist und die angebliche Kostenschwemme auf einer Fiktion beruhe.[35][36]
Vertragsverletzungsverfahren der Europäischen Union

Die Europäische Kommission hat 2007 Vertragsverletzungsverfahren wegen der unkorrekten Umsetzung zweier EU-Antidiskriminierungs-Rechtsakte (Richtlinie 2000/78/EG sowie Richtlinie 2000/43/EG) eingeleitet. Die Rügen betreffen unter anderem § 2 Abs. 4, § 8 Abs. 1 S. 1, § 9 Abs. 1, § 10 S. 2 Nr. 4 und § 15 Abs. 1, 3 und 4 sowie § 23 Abs. 1 S. 2 AGG.  Nach partiellen Änderungen des AGG wurden 2010 die Vertragsverletzungsverfahren eingestellt.[37][38]
Ausweitung des Allgemeinen Gleichbehandlungsgesetzes

Auf europäischer Ebene steht die Ausweitung der Antidiskriminierungsgesetze vom Bereich des Arbeitsplatzes zusätzlich auf den Zugang zu Waren und Dienstleistungen (wie zum Beispiel Wohnraumvermietung) in der Diskussion.

Einem Konsens der 27 Länder stehen bislang nur die Länder Deutschland und Tschechien entgegen. Die Argumentation gegen diesen Konsens beruft sich darauf, dass auf nationaler Ebene einer Diskriminierung viel besser entgegengetreten werden könne und dass die geplante Ausweitung zu einer „Überregulierung“ führe.[39]
Internationaler Vergleich

Ebenso wie das deutsche Allgemeine Gleichbehandlungsgesetz beruhen ähnliche Gesetze in den anderen EU-Staaten ebenfalls auf den EG-Antidiskriminierungsrichtlinien, sind also ähnlich gestaltet, wenn auch zum Teil weitergehend.

In den USA gibt es ein ähnliches Gesetz seit 1964, den Civil Rights Act. Dieser verbot von Anfang an die Diskriminierung aufgrund von Rasse, Hautfarbe, Religion, Geschlecht oder Herkunft, später kamen noch Alter und Behinderung hinzu. Der Arbeitgeber hat in den USA darauf zu achten, dass keine feindliche Umgebung („hostile work environments“) besteht, in der ein Arbeitnehmer Anfeindungen, Beleidigungen, Erniedrigungen etc. seitens seiner Vorgesetzten oder anderer Mitarbeiter ausgesetzt ist. Der Arbeitgeber ist sogar gehalten, im Rahmen beruflicher Aus- und Fortbildung auf die Unzulässigkeit solcher Benachteiligungen hinzuweisen. Dem Diskriminierten wird eine Klage vor Gericht dadurch erleichtert, dass er nur die Tatsachen glaubhaft machen muss, aus denen sich eine Diskriminierung ergibt. Der Beklagte muss dann beweisen, dass sachliche und nicht diskriminierende Gründe für die unterschiedliche Behandlung vorliegen.[40]

Die UN hat auf internationaler Ebene Erklärungen und Resolutionen der Vereinten Nationen über die sexuelle Orientierung und geschlechtliche Identität verkündet."""


if __name__ == "__main__":
  plotWordCloud(wiki)
