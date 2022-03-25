
	
from reportlab.pdfgen   import canvas
from reportlab.platypus import Table, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib     import colors
from xlprgrm import getMark,getStdntDtl, mrklst,getPercent
	
blueClr  = colors.toColor('rgba (135,206,250,0.3)')
blueClr1 = colors.toColor('rgba (0,21,120,1)')
width, height = A4
# images ---------------------------------------
ImgPath1 ='insLogo.png'
img      = Image(ImgPath1,703,703,kind ='proportional')
img2     = Image(ImgPath1,0,0,kind ='proportional')
	
	
#_______________________________________________	
	
	
	
	
#_______________________________________________
	
def genHdr():
		mTable     = Table([['',img]],
		colWidths  = [13,200,200],
		rowHeights = [58])
		
		mTable.setStyle([	
		('BACKGROUND', (0,1),(0,1),'blue'),
	    ('ALIGN',      (1,0),(1,0),'CENTER'),
	    ('LEFTPADDING',(0,0),(0,2),0),
		('VALIGN',     (0,0),(-1,-1),'MIDDLE')])
		return mTable
		
#_______________________________________________
	
def Pdetails(rawNum):
		dt     = getStdntDtl(rawNum)
		mTable = Table([
		
		["Name ",    ':',  dt[2]],
		['Class',    ':',  'X'],
		['Division', ':',  dt[3]],
		['Ad.Number',':',  int(dt[1])]],
		
		colWidths  = [86,15,70],
		rowHeights = [18,18,18,18])
		mTable.setStyle([
		('ALIGN',   (0,2),(0,2),'LEFT'),
		('VALIGN',  (0,0),(0,2),'MIDDLE'),
		('FONTSIZE',(0,0),(-1,-1),14)
		])
		
		return mTable

#_______________________________________________
	
	
	
def genHdrTest(rawNum):
	
	pt  = getPercent(rawNum)
	m   = getMark(rawNum)	
	grp = mrklst(rawNum)[:-1]
	
	
		
	mTable = Table([
	['SI.NO','SUBJECT',"MARKS AWARDED","MAX.MARKS","%"],
	["1","Physics",    m[0] ,"20", (str(pt[0])+"%")],
	["2","Chemistry",  m[1] ,"20", (str(pt[1])+"%")],
	["3","Mathematics",m[2] ,"40", 
	(( str(  (int(int(grp[2])*2.5)))  ) + "%" )],
	
	["4","History",    m[3] ,"20", (str(pt[3])+"%")],
	["5","Geography",  m[4] ,"20", (str(pt[4])+"%")],
	["6","English",    m[5] ,"20", (str(pt[5])+"%")],
	["7","Hindi",  	m[6] ,"20", (str(pt[6])+"%")],
	["8","Biology",	m[7] ,"20", (str(pt[7])+"%")],
	["", "TOTAL",	  m[8] ,"180",
		(str(int(pt[8]))+"%")]
		
		],colWidths = [60,120,125,125,100],
		rowHeights = [36,25,25,25,25,25,25,25,25,25])
		
		
	mTable.setStyle([
		('GRID',      (0,0),(-1,-1),2,'white'),
		('BACKGROUND',(0,2),(4,2),blueClr),
		('BACKGROUND',(0,4),(4,4),blueClr),
		('BACKGROUND',(0,6),(4,6),blueClr),
		('BACKGROUND',(0,8),(4,8),blueClr),
		('TEXTCOLOR', (0,0),(4,0),'white'),
	    ('FONTSIZE',  (0,0),(-1,-1),13),
		('BACKGROUND',(0,0),(4,0),blueClr1),
	    ('ALIGN',     (0,0),(4,0),'CENTER'),
	    ('ALIGN',     (2,1),(-1,-1),'CENTER'),
	    ('ALIGN',     (0,0),(0,8),'CENTER'),
		('VALIGN',    (0,0),(-1,-1),'MIDDLE'),
		('BOTTOMPADDING',(0,1),(-1,-2),8.6),
		])
	return mTable
	