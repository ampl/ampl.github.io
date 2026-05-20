"""
Generate a GitHub-style release activity chart for releases/index.md.

Usage as a module:
    from generate_activity_chart import activity_chart_block
    block = activity_chart_block(released_on)   # released_on: {YYYYMMDD: [items...]}

Usage as a script:
    python generate_activity_chart.py source/releases/index.md
    # reads ## YYYYMMDD headers from the file and prints the block
"""

import json
import re
import sys


_MONTHS_JS = "['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']"

_TEMPLATE = """\
## Release Activity

```{{raw}} html
<div id="rac-root">
<style>
#rac-root{{font-size:12px;margin:1em 0 2em}}
.rac-controls{{display:flex;align-items:center;gap:6px;margin-bottom:8px}}
.rac-controls button{{background:none;border:1px solid #ccc;border-radius:4px;cursor:pointer;padding:2px 10px;font-size:12px;color:inherit;line-height:1.4}}
.rac-controls button:hover{{background:#f0f0f0}}
.rac-controls button:disabled{{opacity:.4;cursor:default}}
.rac-year-label{{font-weight:bold;min-width:3em;text-align:center}}
.rac-scroll{{overflow-x:auto}}
.rac-inner{{display:inline-flex;gap:4px}}
.rac-day-col{{display:flex;flex-direction:column;gap:2px;padding-top:18px}}
.rac-day-col span{{height:11px;line-height:11px;font-size:10px;color:#767676;white-space:nowrap;padding-right:4px}}
.rac-chart-col{{display:flex;flex-direction:column}}
.rac-months{{position:relative;height:18px}}
.rac-months span{{position:absolute;font-size:10px;color:#767676;line-height:1}}
.rac-grid{{display:grid;grid-template-rows:repeat(7,11px);grid-auto-columns:11px;grid-auto-flow:column;gap:2px}}
.rac-cell{{width:11px;height:11px;border-radius:2px;cursor:default}}
.rac-l0{{background:#ebedf0}}
.rac-l1{{background:#9be9a8}}
.rac-l2{{background:#40c463}}
.rac-l3{{background:#30a14e}}
.rac-l4{{background:#216e39}}
.rac-lx{{background:#ebedf0;opacity:.25}}
.rac-legend{{display:flex;align-items:center;gap:4px;margin-top:8px;font-size:11px;color:#767676}}
</style>
<div class="rac-controls">
  <button id="rac-prev" onclick="racNav(-1)">&#9664; Prev</button>
  <span class="rac-year-label" id="rac-year"></span>
  <button id="rac-next" onclick="racNav(1)">Next &#9654;</button>
</div>
<div class="rac-scroll">
  <div class="rac-inner">
    <div class="rac-day-col">
      <span>&nbsp;</span><span>Mon</span><span>&nbsp;</span>
      <span>Wed</span><span>&nbsp;</span><span>Fri</span><span>&nbsp;</span>
    </div>
    <div class="rac-chart-col">
      <div class="rac-months" id="rac-months"></div>
      <div class="rac-grid" id="rac-grid"></div>
    </div>
  </div>
</div>
<div class="rac-legend">
  <span>Less&nbsp;</span>
  <div class="rac-cell rac-l0" title="No releases"></div>
  <div class="rac-cell rac-l1" title="1–2 releases"></div>
  <div class="rac-cell rac-l2" title="3–5 releases"></div>
  <div class="rac-cell rac-l3" title="6–8 releases"></div>
  <div class="rac-cell rac-l4" title="9+ releases"></div>
  <span>&nbsp;More</span>
</div>
<script>
(function(){{
var D={data};
var MIN_Y={min_year},MAX_Y={max_year},year=MAX_Y;
var MONTHS={months};
function p2(n){{return String(n).padStart(2,'0')}}
function ds(d){{return d.getFullYear()+'-'+p2(d.getMonth()+1)+'-'+p2(d.getDate())}}
function level(c){{return !c?0:c<=2?1:c<=5?2:c<=8?3:4}}
function render(){{
  document.getElementById('rac-year').textContent=year;
  document.getElementById('rac-prev').disabled=year<=MIN_Y;
  document.getElementById('rac-next').disabled=year>=MAX_Y;
  var grid=document.getElementById('rac-grid');
  var mrow=document.getElementById('rac-months');
  grid.innerHTML=''; mrow.innerHTML='';
  var start=new Date(year,0,1);
  start.setDate(start.getDate()-start.getDay());
  var end=new Date(year,11,31);
  end.setDate(end.getDate()+(6-end.getDay()));
  var mpos={{}},wi=0,d=new Date(start);
  while(d<=end){{
    var iny=d.getFullYear()===year;
    var s=ds(d),c=D[s]||0,lv=iny?level(c):'x';
    if(iny&&d.getDate()===1&&mpos[d.getMonth()]===undefined)mpos[d.getMonth()]=wi;
    var cell=document.createElement('div');
    cell.className='rac-cell rac-l'+lv;
    if(iny){{var lbl=c===0?'No releases':c+' release'+(c>1?'s':'');cell.title=s+': '+lbl;}}
    grid.appendChild(cell);
    d.setDate(d.getDate()+1);
    if(d.getDay()===0)wi++;
  }}
  MONTHS.forEach(function(m,i){{
    if(mpos[i]!==undefined){{
      var sp=document.createElement('span');
      sp.textContent=m;
      sp.style.left=(mpos[i]*13)+'px';
      mrow.appendChild(sp);
    }}
  }});
}}
window.racNav=function(delta){{
  var ny=year+delta;
  if(ny>=MIN_Y&&ny<=MAX_Y){{year=ny;render();}}
}};
render();
}})();
</script>
</div>
```

"""


def activity_chart_block(released_on: dict) -> str:
    """Return the '## Release Activity' markdown block.

    Args:
        released_on: mapping of YYYYMMDD date strings to lists of release items.
    """
    # Build YYYY-MM-DD -> count mapping
    counts = {
        f"{d[:4]}-{d[4:6]}-{d[6:]}": len(set(items))
        for d, items in released_on.items()
    }
    data_json = json.dumps(counts, separators=(",", ":"))

    years = [int(d[:4]) for d in released_on]
    min_year = min(years)
    max_year = max(years)

    return _TEMPLATE.format(
        data=data_json,
        min_year=min_year,
        max_year=max_year,
        months=_MONTHS_JS,
    )


def _parse_index(path: str) -> dict:
    """Parse released_on from an existing index.md."""
    released_on = {}
    current = None
    with open(path) as f:
        for line in f:
            m = re.match(r"^## (\d{8})$", line.rstrip())
            if m:
                current = m.group(1)
                released_on[current] = []
            elif current and line.startswith("- ["):
                released_on[current].append(line.strip())
    return released_on


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path/to/index.md>", file=sys.stderr)
        sys.exit(1)
    released_on = _parse_index(sys.argv[1])
    print(activity_chart_block(released_on), end="")
