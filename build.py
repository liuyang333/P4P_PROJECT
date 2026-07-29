import json
data = json.load(open('/sessions/pensive-friendly-keller/mnt/outputs/data.json'))
data_js = json.dumps(data, ensure_ascii=False)

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>P4P Conference 2026 — Schedule</title>
<style>
:root{
  --bg:#eef1f6; --card:#ffffff; --ink:#1a2230; --muted:#6b7690;
  --line:#e4e8f0; --navy:#0c0c48; --navy2:#1a1a63; --brand:#0c0c48;
  --brand2:#2b5fd0; --accent:#eaf0fc;
  --s1:#2b5fd0;--s2:#0a9d5a;--s3:#d3223b;--s4:#e59a00;--s5:#7d3cff;--s6:#00a0ad;
  --shadow:0 1px 2px rgba(12,12,72,.06),0 6px 20px rgba(12,12,72,.06);
  --shadow-lg:0 10px 34px rgba(12,12,72,.14);
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.5;-webkit-font-smoothing:antialiased}
header{background:var(--navy);color:#fff;padding:26px 20px 0;border-bottom:3px solid transparent;border-image:linear-gradient(90deg,var(--s1),var(--s6) 55%,var(--s2)) 1}
.wrap{max-width:1260px;margin:0 auto;padding:0 20px}
header h1{margin:0;font-size:25px;font-weight:700;letter-spacing:.2px}
header .sub{opacity:.82;margin-top:5px;font-size:13.5px}
.brandrow{display:flex;align-items:center;gap:22px;flex-wrap:wrap}
.logo-slot{flex:0 0 auto;display:flex;align-items:center}
.logo-slot img{height:68px;width:auto;display:block}
.logo-fallback{display:flex;flex-direction:column;line-height:1.15;background:#fff;color:var(--navy);padding:8px 13px;border-radius:8px;font-weight:700}
.logo-fallback .lf1{font-size:11px;letter-spacing:.5px;text-transform:uppercase;opacity:.75}
.logo-fallback .lf2{font-size:17px}
.htext{min-width:0;padding:6px 0}
.hdiv{width:1px;align-self:stretch;background:rgba(255,255,255,.18);margin:14px 0}
.tabs{display:flex;gap:6px;margin-top:20px}
.tab{background:rgba(255,255,255,.12);color:#fff;border:none;padding:10px 20px;border-radius:9px 9px 0 0;font-size:14px;font-weight:600;cursor:pointer;transition:.18s}
.tab:hover{background:rgba(255,255,255,.22)}
.tab.active{background:var(--bg);color:var(--navy)}
main{padding:22px 0 60px}
.toolbar{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;box-shadow:var(--shadow);margin-bottom:18px}
.search-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.search-box{flex:1;min-width:240px;position:relative}
.search-box input{width:100%;padding:12px 14px 12px 40px;border:1px solid var(--line);border-radius:9px;font-size:15px;outline:none;transition:.15s}
.search-box input:focus{border-color:var(--brand2);box-shadow:0 0 0 3px var(--accent)}
.search-box svg{position:absolute;left:13px;top:13px;width:18px;height:18px;fill:var(--muted)}
select{padding:11px 12px;border:1px solid var(--line);border-radius:9px;font-size:14px;background:#fff;cursor:pointer;color:var(--ink)}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;align-items:center}
.count{color:var(--muted);font-size:13px;margin-left:auto}
.btn-clear{background:#fff;border:1px solid var(--line);color:var(--muted);padding:6px 12px;border-radius:7px;font-size:13px;cursor:pointer}
.btn-clear:hover{border-color:var(--brand2);color:var(--brand)}
.grid-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--brand2);border-radius:12px;padding:15px 17px;box-shadow:var(--shadow);transition:transform .16s,box-shadow .16s}
.card:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg)}
.card .meta{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin-bottom:9px;align-items:center}
.pill{padding:2px 9px;border-radius:20px;font-weight:600;font-size:11px;color:#fff;white-space:nowrap}
.pill.time{background:var(--ink)}
.pill.room{background:#5b6b85}
.card h3{margin:0 0 10px;font-size:15px;line-height:1.4;font-weight:650}
.flag{display:inline-block;background:#fff4d6;color:#8a6100;border:1px solid #f2d98a;font-size:10px;padding:1px 6px;border-radius:5px;font-weight:700;margin-right:5px;vertical-align:middle}
.card .row{font-size:13px;margin:3px 0;color:var(--ink)}
.card .row b{color:var(--muted);font-weight:600;display:inline-block;min-width:78px}
.card .stream-tag{font-size:11px;font-weight:700;padding:2px 8px;border-radius:6px;color:#fff}
.s1{background:var(--s1)}.s2{background:var(--s2)}.s3{background:var(--s3)}.s4{background:var(--s4);color:#3a2c00}.s5{background:var(--s5)}.s6{background:var(--s6)}
mark{background:#fff2a8;color:inherit;padding:0 1px;border-radius:2px}
.empty{text-align:center;padding:60px 20px;color:var(--muted)}
/* grid view */
.session-block{margin-bottom:28px}
.session-title{font-size:16px;font-weight:700;color:var(--brand);margin:0 0 4px}
.event-bar{background:var(--accent);border:1px dashed #b9d4ee;color:var(--brand);padding:9px 14px;border-radius:8px;font-size:13px;font-weight:600;margin:10px 0;text-align:center}
.table-scroll{overflow-x:auto;border:1px solid var(--line);border-radius:11px;box-shadow:var(--shadow);background:#fff}
table{border-collapse:collapse;width:100%;min-width:1100px}
th,td{border:1px solid var(--line);padding:8px 9px;vertical-align:top;text-align:left;font-size:12.5px}
thead th{position:sticky;top:0;background:var(--brand);color:#fff;font-size:12px;z-index:2}
thead th.tcol{width:58px}
th .rm{display:block;font-weight:400;font-size:10.5px;opacity:.85;margin-top:2px}
td.tcell{font-weight:700;background:#f7f9fc;text-align:center;white-space:nowrap;color:var(--brand)}
td .gt{font-weight:650;margin-bottom:4px;display:block;font-size:12px}
td .gs{color:var(--muted);font-size:11px;display:block}
td.talk:hover{background:#f4f9ff}
.chair-row td{background:#eef3f9;font-size:11px;color:var(--muted);font-style:italic}
.legend{display:flex;gap:12px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin-bottom:14px;align-items:center}
.legend span{display:inline-flex;align-items:center;gap:5px}
.dot{width:11px;height:11px;border-radius:3px;display:inline-block}
.infobar{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px;box-shadow:var(--shadow);margin-bottom:20px;display:flex;gap:20px;flex-wrap:wrap;align-items:stretch;position:relative;overflow:hidden}
.infobar::before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;background:linear-gradient(var(--s1),var(--s6))}
.infobar .lead{flex:1;min-width:230px;padding-left:6px}
.infobar .dept{font-size:11.5px;color:var(--muted);font-weight:600;letter-spacing:.2px}
.infobar .evt{font-size:18px;font-weight:750;color:var(--navy);margin:3px 0}
.infobar .when{font-size:14px;color:var(--ink);font-weight:600}
.infobar .ib{min-width:190px;padding-left:20px;border-left:1px solid var(--line);display:flex;flex-direction:column;justify-content:center}
.infobar .ib .k{font-size:10.5px;text-transform:uppercase;letter-spacing:.6px;color:var(--brand2);font-weight:700;margin-bottom:3px}
.infobar .ib .v{font-size:13px;color:var(--ink)}
footer{text-align:center;color:var(--muted);font-size:12px;padding:24px}
@media(max-width:600px){header h1{font-size:20px}.card .row b{min-width:70px}}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <div class="brandrow">
      <div class="logo-slot">
        <img src="logo.png" alt="Waipapa Taumata Rau · University of Auckland"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
        <div class="logo-fallback" style="display:none">
          <span class="lf1">Waipapa Taumata Rau</span><span class="lf2">University of Auckland</span>
        </div>
      </div>
      <div class="hdiv"></div>
      <div class="htext">
        <h1>P4P Conference 2026 — Presentation Schedule</h1>
        <div class="sub" id="hsub">Part IV Research Project Conference · 6 parallel streams</div>
      </div>
    </div>
    <div class="tabs">
      <button class="tab active" data-view="list" onclick="switchView('list')">🔍 Search &amp; Browse</button>
      <button class="tab" data-view="grid" onclick="switchView('grid')">🗓 Timetable Grid</button>
    </div>
  </div>
</header>
<main class="wrap">
  <div class="infobar" id="infobar"></div>
  <!-- LIST VIEW -->
  <section id="view-list">
    <div class="toolbar">
      <div class="search-row">
        <div class="search-box">
          <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 10-.7.7l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0A4.5 4.5 0 1114 9.5 4.5 4.5 0 019.5 14z"/></svg>
          <input id="q" type="text" placeholder="Search title, student, supervisor, assessor, room…" oninput="render()">
        </div>
        <select id="field" onchange="render()">
          <option value="all">All fields</option>
          <option value="title">Title only</option>
          <option value="student">Student</option>
          <option value="supervisor">Supervisor / Co-sup</option>
          <option value="assessor">Assessor</option>
        </select>
      </div>
      <div class="filters">
        <select id="fStream" onchange="render()"><option value="">All streams</option></select>
        <select id="fRoom" onchange="render()"><option value="">All rooms</option></select>
        <select id="fSession" onchange="render()"><option value="">All sessions</option></select>
        <button class="btn-clear" onclick="clearAll()">Clear</button>
        <span class="count" id="count"></span>
      </div>
    </div>
    <div id="cards" class="grid-cards"></div>
    <div id="empty" class="empty" style="display:none">No presentations match your search.</div>
  </section>
  <!-- GRID VIEW -->
  <section id="view-grid" style="display:none">
    <div class="legend" id="legend"></div>
    <div id="gridContent"></div>
  </section>
</main>
<footer>P4P Conference 2026 · Static schedule viewer · Times are indicative (draft v1.1)</footer>
<script>
const DATA = ''' + data_js + r''';

// event info bar
(function(){
  const i=DATA.info; if(!i)return;
  document.getElementById('hsub').textContent=i.department+' · '+i.faculty;
  document.getElementById('infobar').innerHTML=
    `<div class="lead"><div class="dept">${i.department}</div>`+
    `<div class="evt">${i.event}</div>`+
    `<div class="when">📅 ${i.date} · ⏰ ${i.time}</div></div>`+
    `<div class="ib"><div class="k">📍 Venue</div><div class="v">${i.venue}</div></div>`+
    `<div class="ib"><div class="k">🅿 Parking</div><div class="v">${i.parking}</div></div>`;
  document.querySelector('footer').textContent=`${i.event} · ${i.date} · ${i.venue} · Draft schedule v1.1 (times indicative)`;
})();

const streamClass = n => 's'+(n||1);
const streamShort = s => s.replace(/^Stream\s*\d+:\s*/,'');

// populate filters
(function(){
  const streams=[...new Set(DATA.presentations.map(p=>p.stream))].filter(Boolean).sort((a,b)=>a.localeCompare(b));
  const fs=document.getElementById('fStream');
  streams.forEach(s=>{const o=document.createElement('option');o.value=s;o.textContent=streamShort(s);fs.appendChild(o)});
  const fr=document.getElementById('fRoom');
  [...new Set(DATA.presentations.map(p=>p.room))].filter(Boolean).sort().forEach(r=>{const o=document.createElement('option');o.value=r;o.textContent=r;fr.appendChild(o)});
  const fss=document.getElementById('fSession');
  [...new Set(DATA.presentations.map(p=>p.session))].filter(Boolean).forEach(s=>{const o=document.createElement('option');o.value=s;o.textContent=s;fss.appendChild(o)});
})();

function esc(s){return (s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function hl(text,q){text=esc(text);if(!q)return text;const t=q.trim().split(/\s+/).filter(Boolean).map(x=>x.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'));if(!t.length)return text;return text.replace(new RegExp('('+t.join('|')+')','ig'),'<mark>$1</mark>')}

function matchField(p,q,field){
  const qs=q.toLowerCase();
  const S={
    title:p.title,
    student:p.students.join(' '),
    supervisor:p.supervisor+' '+p.cosupervisor,
    assessor:p.assessor,
    all:[p.title,p.students.join(' '),p.supervisor,p.cosupervisor,p.assessor,p.room,p.stream,p.chair,p.time].join(' ')
  };
  return (S[field]||'').toLowerCase().includes(qs);
}

function render(){
  const q=document.getElementById('q').value.trim();
  const field=document.getElementById('field').value;
  const fS=document.getElementById('fStream').value;
  const fR=document.getElementById('fRoom').value;
  const fSe=document.getElementById('fSession').value;
  let list=DATA.presentations.filter(p=>p.type==='talk');
  if(fS)list=list.filter(p=>p.stream===fS);
  if(fR)list=list.filter(p=>p.room===fR);
  if(fSe)list=list.filter(p=>p.session===fSe);
  if(q)list=list.filter(p=>matchField(p,q,field));
  const box=document.getElementById('cards');
  document.getElementById('count').textContent=list.length+' of '+DATA.presentations.filter(p=>p.type==='talk').length+' talks';
  document.getElementById('empty').style.display=list.length?'none':'block';
  box.innerHTML=list.map(p=>{
    const flag=p.flags?`<span class="flag">${esc(p.flags)}</span>`:'';
    const co=p.cosupervisor?`<div class="row"><b>Co-sup:</b> ${hl(p.cosupervisor,field==='supervisor'||field==='all'?q:'')}</div>`:'';
    return `<div class="card" style="border-left-color:var(--${streamClass(p.streamNum)})">
      <div class="meta">
        <span class="pill time">${p.time}</span>
        <span class="pill room">${esc(p.room)}</span>
        <span class="stream-tag ${streamClass(p.streamNum)}">${esc(streamShort(p.stream))}</span>
      </div>
      <h3>${flag}${hl(p.title,field==='title'||field==='all'?q:'')}</h3>
      <div class="row"><b>Students:</b> ${hl(p.students.join(', '),field==='student'||field==='all'?q:'')}</div>
      <div class="row"><b>Supervisor:</b> ${hl(p.supervisor,field==='supervisor'||field==='all'?q:'')}</div>
      ${co}
      <div class="row"><b>Assessor:</b> ${hl(p.assessor,field==='assessor'||field==='all'?q:'')}</div>
    </div>`;
  }).join('');
}

function clearAll(){document.getElementById('q').value='';document.getElementById('field').value='all';document.getElementById('fStream').value='';document.getElementById('fRoom').value='';document.getElementById('fSession').value='';render()}

function switchView(v){
  document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('active',t.dataset.view===v));
  document.getElementById('view-list').style.display=v==='list'?'':'none';
  document.getElementById('view-grid').style.display=v==='grid'?'':'none';
  if(v==='grid')buildGrid();
}

function buildGrid(){
  const g=document.getElementById('gridContent');
  if(g.dataset.built)return;
  // legend
  const streams=DATA.presentations.filter(p=>p.streamNum).reduce((m,p)=>{m[p.streamNum]=streamShort(p.stream);return m},{});
  document.getElementById('legend').innerHTML=Object.keys(streams).sort().map(n=>`<span><span class="dot ${streamClass(n)}"></span>${esc('Stream '+n+': '+streams[n])}</span>`).join('');
  // build chronological rows merging events and talk time-slots per session
  const rooms=DATA.rooms;
  // group talks by session
  const sessions=[...new Set(DATA.presentations.map(p=>p.session))].filter(Boolean);
  // build a global timeline: interleave events and session time slots by time
  let html='';
  // opening events (before first session) handled inline by time order across whole day:
  // We'll render session tables and place events between them by time.
  const allEvents=DATA.events.slice();
  function eventsBetween(lo,hi){
    return allEvents.filter(e=>e.time>=lo && e.time<hi).map(e=>`<div class="event-bar">🍽 ${e.time} — ${esc(e.label)}</div>`).join('');
  }
  // pre-session events (registration/welcome)
  const firstTalkTime=Math.min(...DATA.presentations.filter(p=>p.session===sessions[0]).map(p=>p.time)).toString();
  html+=allEvents.filter(e=>e.time< (DATA.presentations.filter(p=>p.session===sessions[0]).map(p=>p.time).sort()[0])).map(e=>`<div class="event-bar">📋 ${e.time} — ${esc(e.label)}</div>`).join('');
  const usedEventTimes=new Set();
  sessions.forEach((sess,si)=>{
    const items=DATA.presentations.filter(p=>p.session===sess);
    const times=[...new Set(items.map(p=>p.time))].sort();
    // chairs per stream for this session
    const chairs={};
    items.forEach(p=>{if(p.chair)chairs[p.streamNum]=p.chair});
    html+=`<div class="session-block"><h2 class="session-title">${esc(sess)}</h2>`;
    html+=`<div class="table-scroll"><table><thead><tr><th class="tcol">Time</th>`;
    rooms.forEach((rm,i)=>{html+=`<th><span class="dot ${streamClass(i+1)}"></span> Stream ${i+1}<span class="rm">${esc(rm)}</span></th>`});
    html+=`</tr></thead><tbody>`;
    // chair row
    html+=`<tr class="chair-row"><td>Chair</td>`;
    rooms.forEach((rm,i)=>{html+=`<td>${chairs[i+1]?'Chair: '+esc(chairs[i+1]):''}</td>`});
    html+=`</tr>`;
    times.forEach(t=>{
      html+=`<tr><td class="tcell">${t}</td>`;
      for(let i=1;i<=6;i++){
        const p=items.find(x=>x.time===t && x.streamNum===i);
        if(!p){html+='<td></td>';continue}
        if(p.type==='info'){html+=`<td class="info"><span class="gt">${esc(p.title)}</span></td>`;continue}
        const flag=p.flags?`<span class="flag">${esc(p.flags)}</span>`:'';
        html+=`<td class="talk"><span class="gt">${flag}${esc(p.title)}</span><span class="gs">👥 ${esc(p.students.join(', '))}</span><span class="gs">🎓 ${esc(p.supervisor)}${p.cosupervisor?' / '+esc(p.cosupervisor):''}</span><span class="gs">✔ ${esc(p.assessor)}</span></td>`;
      }
      html+='</tr>';
    });
    html+='</tbody></table></div>';
    // events after this session's last time and before next session
    const lastT=times[times.length-1];
    const nextFirst = si<sessions.length-1 ? DATA.presentations.filter(p=>p.session===sessions[si+1]).map(p=>p.time).sort()[0] : '99:99';
    allEvents.forEach(e=>{if(!usedEventTimes.has(e.time) && e.time>lastT && e.time<=nextFirst){usedEventTimes.add(e.time);html+=`<div class="event-bar">🍽 ${e.time} — ${esc(e.label)}</div>`}});
    html+='</div>';
  });
  // trailing events (closing)
  const lastSessLast=DATA.presentations.filter(p=>p.session===sessions[sessions.length-1]).map(p=>p.time).sort().pop();
  allEvents.forEach(e=>{if(!usedEventTimes.has(e.time) && e.time>lastSessLast){usedEventTimes.add(e.time);html+=`<div class="event-bar">🎉 ${e.time} — ${esc(e.label)}</div>`}});
  g.innerHTML=html;g.dataset.built='1';
}
render();
</script>
</body>
</html>'''

open('/sessions/pensive-friendly-keller/mnt/outputs/index.html','w').write(html)
print('written', len(html), 'bytes')
