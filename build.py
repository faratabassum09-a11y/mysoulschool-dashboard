import pandas as pd, json, re
d=pd.read_excel('/mnt/user-data/uploads/Students_Records.xlsx',sheet_name='Dashboard')
d=d[d['First Name'].notna() & d['First Name'].astype(str).str.strip().ne('')]
fn=d['First Name'].astype(str).str.strip().str.lower(); em=d['Email'].astype(str).str.lower().str.strip()
d=d[~(fn.str.match(r'^test( ?[0-9]+)?$')|em.str.match(r'^test[0-9]*@'))]
d=d[d['Blocklist'].isna()|d['Blocklist'].astype(str).str.strip().isin(['','0','FALSE'])]
d=d[d['Enrolled On Date'].notna()]
k=d['Duplicate Email'].where(d['Duplicate Email'].notna(),d['Duplicate Phone']).astype(str)+'|'+d['Program'].astype(str)
d=d[~k.duplicated()]
num=lambda c:pd.to_numeric(d[c],errors='coerce').fillna(0)
cb=d['Closed By'].where(d['Closed By'].notna()&(d['Closed By']!='#REF!'),'Not Tagged')
rows=[[t.strftime('%Y-%m-%d'),p if isinstance(p,str) else 'No Program Found',float(f),float(b),float(a),float(u),s,c]
 for t,p,f,b,a,u,s,c in zip(d['Enrolled On Date'],d['Program'],num('Program Fee'),num('Booking Amount'),num('Amount Received'),num('Amount Due'),d['Pymt Status'],cb)]
print(len(rows))
h=open('t.html',encoding='utf8').read().replace('/*DATA*/',json.dumps(rows,separators=(',',':'),ensure_ascii=False)).replace('/*ASOF*/',pd.Timestamp.now().strftime('%d %b %Y'))
open('/mnt/user-data/outputs/mysoulschool_sales_dashboard.html','w',encoding='utf8').write(h)
