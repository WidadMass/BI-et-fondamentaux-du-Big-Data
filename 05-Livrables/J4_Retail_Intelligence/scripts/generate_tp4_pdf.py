from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    Image, KeepTogether
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "TP4_Retail_Intelligence.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

TEMP = Path(r"C:\Users\r5\AppData\Local\Temp")
SCREENSHOTS = [
    (TEMP / "codex-clipboard-3a8ff748-c589-4646-a1d0-a1cfbd48d00d.png", "Groupe de ressources Azure en francecentral"),
    (TEMP / "codex-clipboard-74e05985-816d-4e39-ac75-d1af7609f4cb.png", "Compte ADLS Gen2 avec HNS active"),
    (TEMP / "codex-clipboard-59d63e11-0972-4b4f-9ac4-4f2776e0d075.png", "Arborescence ADLS Bronze, Silver et Gold"),
    (TEMP / "codex-clipboard-b07f0f17-cd62-420b-886e-965a8d8b4693.png", "Fichier Bronze promotion.dat depose"),
    (TEMP / "codex-clipboard-753ae839-4e2b-4784-a66a-e860f8beb7d2.png", "Role RBAC Storage Blob Data Contributor"),
    (TEMP / "codex-clipboard-61c9a673-dbd7-4a57-9d6f-66633e624276.png", "ACL ADLS verifiee sur Bronze"),
    (TEMP / "codex-clipboard-156b8940-0952-4488-b379-f8397c09c9ce.png", "Execution Spark UC08 et indicateurs"),
    (TEMP / "codex-clipboard-35a3bc07-bab5-48a4-823a-731114e69bf1.png", "Notebook TP4 execute"),
    (ROOT / "analytics" / "visualizations" / "promotions_par_categorie.png", "Visualisation des promotions par categorie"),
    (ROOT / "analytics" / "visualizations" / "distribution_field_05.png", "Distribution de field_05"),
]

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleTP", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=23, leading=28, alignment=TA_CENTER, textColor=colors.HexColor("#17324D"), spaceAfter=14))
styles.add(ParagraphStyle(name="SubTitleTP", parent=styles["Normal"], fontName="Helvetica", fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor("#40566B"), spaceAfter=18))
styles.add(ParagraphStyle(name="H1TP", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#17324D"), spaceBefore=8, spaceAfter=9))
styles.add(ParagraphStyle(name="H2TP", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=colors.HexColor("#2B6784"), spaceBefore=7, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyTP", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13, spaceAfter=6))
styles.add(ParagraphStyle(name="SmallTP", parent=styles["BodyText"], fontName="Helvetica", fontSize=8, leading=10, textColor=colors.HexColor("#52616B")))
styles.add(ParagraphStyle(name="CaptionTP", parent=styles["BodyText"], fontName="Helvetica-Oblique", fontSize=8, leading=10, alignment=TA_CENTER, textColor=colors.HexColor("#52616B"), spaceAfter=8))

def P(text, style="BodyTP"):
    return Paragraph(text, styles[style])

def table(data, widths=None):
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#6E8FA0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("LEADING", (0, 0), (-1, -1), 10),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C7CF")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F5F7")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t

def img(path, max_w=16.8*cm, max_h=9.8*cm):
    im = Image(str(path))
    scale = min(max_w / im.imageWidth, max_h / im.imageHeight)
    im.drawWidth = im.imageWidth * scale
    im.drawHeight = im.imageHeight * scale
    return im

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D3DDE2"))
    canvas.line(1.5*cm, 1.35*cm, A4[0]-1.5*cm, 1.35*cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#63737D"))
    canvas.drawString(1.5*cm, 0.85*cm, "TP4 - Retail Intelligence - Azure / Spark")
    canvas.drawRightString(A4[0]-1.5*cm, 0.85*cm, f"Page {doc.page}")
    canvas.restoreState()

story = []
story += [Spacer(1, 2.1*cm), P("TP4 - Retail Intelligence", "TitleTP"), P("UC07 Azure Data Lake Gen2 et UC08 analyse decisionnelle", "SubTitleTP")]
story += [P("Ce dossier rassemble la mise en oeuvre realisee, les resultats Spark et les preuves techniques. L'environnement Azure utilise est Azure for Students, avec une execution reproductible depuis Docker.", "BodyTP"), Spacer(1, 0.3*cm)]
story += [table([["Element", "Valeur"], ["Abonnement", "Azure for Students"], ["Groupe de ressources", "rg-retail-intelligence"], ["Region", "francecentral"], ["Compte ADLS Gen2", "retailtp4widad2026"], ["Filesystem", "retail-intelligence"], ["HNS / TLS", "Active / TLS 1.2"], ["SKU", "Standard_LRS"]], [5.2*cm, 10.8*cm])]
story += [Spacer(1, 0.4*cm), P("Perimetre", "H2TP"), P("Le parcours Azure et le transfert des zones Bronze, Silver et Gold sont realises. Azure Data Factory, Synapse Analytics et Power BI sont documentes comme extensions cibles mais ne sont pas deployes dans cette etape. L'analyse et les graphiques sont produits localement avec Spark, Jupyter et Matplotlib dans Docker.")]
story += [PageBreak(), P("1. Architecture et organisation des donnees", "H1TP"), P("Le flux suit une organisation medallion : la source brute est deposee en Bronze, les donnees nettoyees sont conservees en Silver, puis les agregats analytiques sont publies en Gold.")]
story += [table([["Zone", "Chemin ADLS", "Contenu"], ["Bronze", "bronze/tpcxbb/", "promotion.dat - source brute - 46 396 octets"], ["Silver", "silver/promotion/", "Parquet Snappy - 300 lignes - 19 colonnes"], ["Gold", "gold/promotion_summary/", "Parquet Snappy - 9 lignes agregees"], ["Qualite", "quality/", "Emplacement reserve aux controles"], ["Documentation", "documentation/", "Emplacement reserve aux documents"]], [3*cm, 5.2*cm, 7.8*cm])]
story += [Spacer(1, 0.4*cm), P("Correspondance des composants", "H2TP"), P("ADLS Gen2 assure le stockage et la hierarchie. Les scripts Spark executent localement les transformations qui pourraient etre portees dans Synapse Spark. Les sorties Parquet servent de contrat de donnees pour une consommation future dans Synapse SQL ou Power BI.")]
story += [PageBreak(), P("2. Resultats UC08", "H1TP"), P("Le script tp4_uc08.py et le notebook TP4_Retail_Intelligence.ipynb ont ete executes sur les donnees Silver et Gold produites dans l'UC06.")]
story += [table([["Controle", "Resultat"], ["Lignes Silver", "300"], ["Colonnes Silver", "19"], ["Lignes Gold", "9"], ["Categories Gold", "9"], ["Valeurs nulles controlees", "0"], ["Doublons de field_00 controles", "0"], ["Moyenne field_05", "521,23"], ["Min / max field_05", "12,63 / 995,16"], ["Mediane field_05", "559,51"]], [7.2*cm, 8.8*cm])]
story += [Spacer(1, 0.35*cm), P("KPI par categorie", "H2TP"), table([["Categorie", "Promotions", "Moyenne field_05"], ["able", "37", "446,43"], ["anti", "36", "564,18"], ["ation", "36", "530,95"], ["pri", "35", "577,82"], ["bar", "33", "517,13"], ["cally", "33", "545,79"], ["ought", "32", "597,34"], ["eing", "31", "514,89"], ["ese", "27", "372,26"]], [5*cm, 4*cm, 7*cm])]
story += [PageBreak(), P("3. Analyse metier et limites", "H1TP"), P("La categorie technique la plus frequente est able avec 37 observations. Les categories anti et ation suivent avec 36 observations. La categorie ese est la moins representee avec 27 observations. Les ecarts sont moderes, mais field_07 reste un nom technique : aucune conclusion commerciale ne doit etre tiree sans dictionnaire metier.")]
story += [P("La mesure field_05 varie de 12,63 a 995,16. Sa moyenne est 521,23 et sa mediane 559,51. La mediane superieure a la moyenne suggere une influence de valeurs plus faibles, sans permettre d'expliquer la cause. L'unite de field_05 n'etant pas connue, il ne faut pas l'appeler prix, cout ou montant de vente.")]
story += [P("Recommandations", "H2TP"), P("Qualifier field_07 et field_05 avec le metier, documenter les unites et les regles de calcul, puis ajouter des indicateurs de qualite et des KPI commerciaux seulement lorsque les champs necessaires sont identifies.")]
story += [PageBreak(), P("4. Securite et preuves Azure", "H1TP"), P("Le compte utilisateur w.masghar@ecole-ipssi.net dispose du role Storage Blob Data Contributor a la portee du compte de stockage, sans elargir le role a tout l'abonnement. Les zones Bronze, Silver et Gold utilisent l'ACL user::rwx,group::r-x,other::---.")]
story += [table([["Zone", "Proprietaire", "Groupe", "Autres"], ["Bronze", "rwx", "r-x", "aucun acces"], ["Silver", "rwx", "r-x", "aucun acces"], ["Gold", "rwx", "r-x", "aucun acces"]], [4*cm, 3.7*cm, 3.7*cm, 4.1*cm])]
story += [Spacer(1, 0.3*cm), P("Matrice fonctionnelle cible", "H2TP"), table([["Profil", "Bronze", "Silver", "Gold"], ["Equipe ingestion", "Ecriture controlee", "Lecture limitee", "Aucun acces par defaut"], ["Data engineering", "Lecture/ecriture", "Lecture/ecriture", "Ecriture controlee"], ["Analyste metier", "Aucun acces", "Lecture selon besoin", "Lecture"], ["Administrateur", "Gestion habilitee", "Gestion habilitee", "Gestion habilitee"]], [4*cm, 3.7*cm, 3.7*cm, 4.1*cm])]
story += [PageBreak(), P("5. Captures de preuve Azure", "H1TP")]
for path, caption in SCREENSHOTS[:6]:
    if path.exists():
        story += [KeepTogether([img(path, max_w=16.8*cm, max_h=8.4*cm), P(caption, "CaptionTP")]), Spacer(1, 0.15*cm)]
story += [PageBreak(), P("6. Captures de preuve Spark et visualisations", "H1TP")]
for path, caption in SCREENSHOTS[6:]:
    if path.exists():
        story += [KeepTogether([img(path, max_w=16.8*cm, max_h=8.2*cm), P(caption, "CaptionTP")]), Spacer(1, 0.15*cm)]
story += [PageBreak(), P("7. Reproduction", "H1TP"), P("Depuis le dossier du projet, lancer le conteneur Spark puis le script UC08 :")]
story += [P("docker compose -f .\\docker-compose.tp3.yml up -d spark-uc06", "SmallTP"), P("docker exec retail-uc06-spark /opt/spark/bin/spark-submit --master local[2] /opt/project/tp4/scripts/tp4_uc08.py", "SmallTP")]
story += [P("Les fichiers de sortie sont conserves dans analytics/outputs et les graphiques dans analytics/visualizations. Le notebook est disponible dans notebooks/TP4_Retail_Intelligence.ipynb. Les avertissements PyArrow observes pendant l'execution n'empechent pas le calcul : Spark utilise le mode de repli non optimise et les resultats sont produits correctement.")]
story += [P("Conclusion", "H2TP"), P("Le TP4 est documente avec les ressources Azure effectivement creees, les donnees transferees, les droits d'acces, les controles de qualite, les resultats analytiques et les limites de l'environnement etudiant.")]

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.45*cm, bottomMargin=1.7*cm, title="TP4 Retail Intelligence")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
