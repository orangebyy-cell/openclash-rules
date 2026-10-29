from pathlib import Path
import yaml, json, hashlib, ipaddress, re
root=Path(__file__).resolve().parents[1]
files=[]
for p in sorted((root/'rules').glob('*.yaml')):
 d=yaml.safe_load(p.read_text()); assert set(d)=={'payload'} and d['payload'], p.name
 for s in d['payload']:
  assert isinstance(s,str) and not any(x in s for x in ['://','@','__']), p.name
  if s.startswith(('IP-CIDR,','IP-CIDR6,')): assert ipaddress.ip_network(s.split(',')[1]).is_global, p.name
  assert not re.search(r'192\.168\.|duangmi|orangebyy',s,re.I), p.name
 files.append((p.name,len(d['payload'])))
print('Validated', len(files), 'files and',sum(n for _,n in files),'rules')
