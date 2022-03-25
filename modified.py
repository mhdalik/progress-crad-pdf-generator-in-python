from reportlab.pdfgen        import canvas
from reportlab.platypus      import Table
from reportlab.lib.pagesizes import A4
from reportlab.lib 		  import colors
from xlprgrm                 import mrklst,getStdntDtl
from body            import genHdrTest,Pdetails,genHdr

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart

	
def rpt(rawNum):	
		
	
	dt = getStdntDtl(rawNum)
	pdfName = str(dt[2])+" " + str(int(dt[1])) + " (" +str(dt[3])+ ")" + ".pdf"
	pdf = canvas.Canvas( pdfName,
	pagesize      = 'A4')
	width, height = A4
	
	barClr = colors.toColor('rgba (190, 252, 114,0.7)')
	ltBlue = colors.toColor('rgba (135,206,250,0.5)')
	blueClr1= colors.toColor('rgba (0,21,120,1)')#kattaBlue
	
	
	#--------Horizontal Grapgh ----------
	
	def make_drawing(rawNum):
	    
	    drawing = Drawing(400, 200)
	    grp     = mrklst(rawNum)[:-1]
	    grp[2]  = int( grp[2])/2
	    datas   = tuple (grp)
	    data    = [ datas
	         #  (5, 20, 15, 12, 16, 8,20, 12),
	           ]
	
	    names = ["Physics","Chemistry","Mathematics","History","Geography","English","Hindi",'Biology']
	    bc   = HorizontalBarChart()
	    bc.x = 8
	    bc.y = 23
	    bc.bars[0].fillColor   = ltBlue#barClr
	    bc.barWidth     = 6
	    bc.groupSpacing = 3
	    bc.height       = 150
	    bc.width        = 442
	    bc.data         = data
	    bc.strokeColor  = colors.white
	    bc.valueAxis.valueMin  = 0
	    bc.valueAxis.valueMax  = 20
	    bc.valueAxis.valueStep = 2
	    bc.categoryAxis.labels.boxAnchor = 'ne'
	    bc.categoryAxis.labels.dx = -10
	    bc.categoryAxis.labels.dy = 7.5
	    bc.categoryAxis.labels.fontName = 'Helvetica'
	    bc.categoryAxis.categoryNames   = names
	    drawing.add(bc)
	    return drawing
	
	
	#colors
	
	blueClr  = colors.toColor('rgba (135,206,250,0.8)')
	blueClr1 = colors.toColor('rgba (0,21,120,1)')
	
	#_________________________________________________
	
	#--------MainTable Structure---------
	#_________________________________________________
	
	
	mainTable = Table([
	["", genHdr(),""],
	
	["", "First Mid Term Examination 2021",""],
	["", "PROGRESS CARD",""],#position (1,2)
	["", 'Student Details ',""],
	["", Pdetails(rawNum), ""   ],
	["", "Mark Details"   ],
	["", genHdrTest(rawNum),""  ],
	["", make_drawing(rawNum)   ],
	["", '']],
	
	colWidths  = [35,(width-51)],
	rowHeights = [60,38,23,33,94,35,251,200,11])
	
	
	
	#--------mnTable Style----------------
	
	mainTable.setStyle([
	#('GRID',(1,0),(1,-3),0,'red'),
	('LEFTPADDING',  (0,0),(0,2),0),
	('ALIGN',        (0,0),(-1,-1),'CENTER'),
	#personaldetai
	('ALIGN',        (1,3),(1,5),'LEFT'),
	#table
	('ALIGN',        (1,6),(1,6),'LEFT'),
	('VALIGN',       (1,6),(1,6),'TOP'),
	
	('BACKGROUND',   (0,-1),(-1,-1),blueClr1),
	('TEXTCOLOR',    (0,-1),(-1,-1),'white'),
	('BOTTOMPADDING',(0,-1),(-1,-1),20),
	('FONTSIZE',     (0,-1),(-1,-1),20),
	#name..under
	('FONTSIZE',     (1,4),(1,4),11),
	('FONTSIZE',     (1,1),(1,1),20),
	('FONT',         (-1,-1),(-1,-1),'Times-Roman'),
	('LINEBELOW',    (1,0),(1,0),0.7,'black'),
	('LINEBELOW',    (1,2),(1,3),0.7,'black'),#top of mark dtls
	('LINEBELOW',    (1,4),(1,4),0.7,'black'),
	('BOTTOMPADDING',(1,0),(1,2),20),
	#fstmidterm examinnn fontSize
	('FONTSIZE',     (1,2),(1,2),20),
	('FONTSIZE',     (1,3),(1,3),15),
	#mark details
	('FONTSIZE',     (1,5),(1,5),15),
	('VALIGN',       (1,2),(-1,-1),'MIDDLE'),
	('BOTTOMPADDING',(1,4),(1,5),11),
	('BOTTOMPADDING',(1,3),(1,3),11),
	#mark dtl
	('BOTTOMPADDING',(1,5),(1,5),18),
	#marktable
	('BOTTOMPADDING',(1,6),(1,6),0),
	('BOTTOMPADDING',(1,2),(1,2),26),
	])
	
	
	mainTable.wrapOn(pdf,0,0)
	mainTable.drawOn(pdf,0,0)
	pdf.showPage()
	pdf.save()
	
for i in range(2,60):
	rpt(i)
	
