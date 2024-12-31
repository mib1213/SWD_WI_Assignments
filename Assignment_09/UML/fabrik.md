### "HAS-A" Beziehung (besteht aus/ besitzt)

#### Fabrik vs Gebäude:
`Fabrik` und `Gebäude` haben eine *"HAS-A"* Beziehung miteinander<br>
Eine `Fabrik` *"besitzt"* ein oder mehrere `Gebäude` (1..\*) <br>
Ein `Gebaude` *"gehört"* zu einer einzigen `Fabrik` (1) <br>
Ein `Gebaude` existiert *"unabhägig"* von der `Fabrik` (Aggregation) <br>
`Gebäude` (1..\*) -> `Fabrik` (1) *Kardinalität (Multiplicities)*<br>

#### Hinweise:
<i>
Die Raute darf nur bei der Klasse sein, die die andere Klasse <b>"besitzt"</b>.
</i>
<br>
<i>
Die Beziehung (Aggregation/Komposition) ist nur relevant für die Klasse, die aus der anderen Klasse besteht <b>(zugehört)</b>. Im Beispiel von `Gebäude` und `Fabrik` fragt man, ob ein `Gebäude` existentiell von der `Fabrik` abhängig ist, wenn die `Fabrik` das `Gebäude` <b>"besitzt"</b>.
</i>

#### Gebäude vs Inventargegenstand:
`Gebäude` und `Inventargegenstand` haben eine *"HAS-A"* Beziehung miteinander<br>
Ein `Gebäude` *"besitzt"* kein oder mehrere `Gegenstände` (0..*)<br>
Ein `Gegenstand` *"gehört"* zu einem einzigen `Gebäude` (1)<br>
Ein `Gegenstand` existiert *"unabhängig"* von dem `Gebäude` (Aggregation)<br>
`Gegenstand` (0..*) -> `Gebäude` (1)<br>


#### Gebäude vs Mitarbeiter:
`Gebäude` und `Mitarbeiter` haben eine *"HAS-A"* beziehung miteinander<br>
Ein `Gebäude` *"besitzt"* keinen oder mehrere `Mitarbeiter` (0..*)<br>
Ein `Mitarbeiter` *"gehört"* zu einem einzigen `Gebäude` (1)<br>
Ein `Mitarbeiter` existiert *"unabhängig"* von dem `Gebäude` (Aggregation)<br>
`Mitarbeiter` (0..*) -> `Gebäude` (1)<br>

### "IS-A" Beziehung (Vererbung)

Die Klassen `Lagerhalle`, `Bürogebäude` und `Produktionshalle` sind die Subklassen(Childklassen) von der *"abstrakten"* Baseklasse (Parentklasse) `Gebäude`. Abstrakt weil sie nicht direkt erzeugt werden kann.

Die Klassen `Möbelstück`, `Maschine`, `Material` und `Roboter` sind die Childklassen von der *"abstrakten"* Parentklasse `Inventargegenstand`.

Die Klasse `Mitarbeiter` hat keine "IS-A" Beziehung mit einer anderen Klasse.