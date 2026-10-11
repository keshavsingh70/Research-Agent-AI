import time
import streamlit as st
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# -----------------------------------------------------------------------------
# Page setup
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Research Agent AI | Intelligent Research Workspace",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------------
# White editorial UI: bold typography, royal blue + tangerine accents
# -----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
  --ink: #14213d;
  --muted: #586780;
  --blue: #2457e6;
  --blue-dark: #173db5;
  --blue-soft: #edf3ff;
  --orange: #f07832;
  --orange-soft: #fff2e9;
  --green: #11845b;
  --green-soft: #eaf8f1;
  --line: #dfe6f1;
  --surface: #ffffff;
  --page: #f6f8fc;
}

html, body, [class*="css"], .stApp {
  font-family: 'DM Sans', sans-serif;
  color: var(--ink);
}
.stApp {
  background: var(--page) !important;
  background-image: radial-gradient(circle at 5% 0%, rgba(36,87,230,.055), transparent 26%),
                    radial-gradient(circle at 100% 18%, rgba(240,120,50,.045), transparent 22%) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 1320px; padding: 1.6rem clamp(1rem, 4vw, 3.4rem) 3.5rem; }

/* Streamlit default text and labels */
.stMarkdown, .stText, p, li { color: var(--ink); }
[data-testid="stCaptionContainer"] p { color: var(--muted) !important; }
[data-testid="stWidgetLabel"] p, .stTextInput label, .stTextArea label {
  color: #33415c !important; font-weight: 800 !important; font-size: .9rem !important;
}

/* Top brand bar */
.brandbar {
  display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding: .9rem 1.15rem; background:#fff; border:1px solid var(--line);
  border-radius:16px; box-shadow:0 4px 18px rgba(20,33,61,.035); margin-bottom:1.5rem;
}
.brand-left { display:flex; align-items:center; gap:.75rem; }
.brand-mark {
  width:42px; height:42px; border-radius:12px; display:flex; align-items:center; justify-content:center;
  color:#fff; font-size:1.25rem; font-weight:900;
  background:linear-gradient(135deg, #2457e6, #4e83ff); box-shadow:0 6px 14px rgba(36,87,230,.22);
}
.brand-name { color:var(--ink); font-family:'Manrope',sans-serif; font-size:1.15rem; font-weight:900; letter-spacing:-.04em; }
.brand-tagline { color:#68758b; font-size:.76rem; font-weight:700; margin-top:.1rem; }
.top-pill { color:#1f4bc5; background:#edf3ff; border:1px solid #d7e3ff; padding:.48rem .75rem; border-radius:999px; font-size:.7rem; font-weight:900; letter-spacing:.08em; white-space:nowrap; }

/* Hero */
.hero {
  position:relative; overflow:hidden; background:#fff; border:1px solid var(--line);
  border-radius:24px; padding:clamp(1.6rem, 4vw, 3.1rem); margin-bottom:1.35rem;
  box-shadow:0 12px 36px rgba(20,33,61,.045);
}
.hero:after { content:""; position:absolute; right:-58px; top:-100px; width:270px; height:270px; border-radius:50%; border:36px solid #edf3ff; opacity:.95; pointer-events:none; }
.hero-kicker { display:inline-flex; align-items:center; gap:.5rem; background:var(--orange-soft); color:#b94e12; border:1px solid #ffdcc5; padding:.42rem .72rem; border-radius:7px; font-size:.72rem; font-weight:900; letter-spacing:.1em; text-transform:uppercase; }
.hero h1 { font-family:'Manrope',sans-serif; color:var(--ink); font-size:clamp(2.4rem,5.5vw,4.5rem); line-height:1.02; font-weight:900; letter-spacing:-.065em; margin:.95rem 0 .8rem; position:relative; z-index:1; }
.hero h1 span { color:var(--blue); }
.hero p { color:#53627a; max-width:690px; font-size:1.04rem; line-height:1.7; font-weight:500; margin:0; position:relative; z-index:1; }
.hero-meta { display:flex; flex-wrap:wrap; gap:.55rem; margin-top:1.3rem; position:relative; z-index:1; }
.meta-chip { border:1px solid #e1e7f0; color:#35445f; background:#f8faff; border-radius:8px; padding:.45rem .65rem; font-size:.76rem; font-weight:800; }

/* Main research card and input */
.section-title { font-family:'Manrope',sans-serif; font-size:1.28rem; font-weight:900; letter-spacing:-.035em; color:var(--ink); margin:.25rem 0 .25rem; }
.section-subtitle { color:var(--muted); font-size:.9rem; font-weight:500; margin-bottom:1rem; }
.research-card {
  background:#fff; border:1px solid var(--line); border-radius:20px; padding:1.35rem 1.4rem 1.2rem;
  box-shadow:0 8px 28px rgba(20,33,61,.04); margin-bottom:1.25rem;
}
.stTextInput > div > div > input, .stTextArea textarea {
  background:#fff !important; color:var(--ink) !important; border:1.5px solid #cbd6e6 !important;
  border-radius:12px !important; min-height:3.15rem; font-size:1rem !important; font-weight:600 !important;
  box-shadow:inset 0 1px 2px rgba(20,33,61,.025) !important;
}
.stTextInput > div > div > input:focus, .stTextArea textarea:focus {
  border-color:var(--blue) !important; box-shadow:0 0 0 3px rgba(36,87,230,.12) !important;
}
.stTextInput input::placeholder { color:#8995a8 !important; font-weight:500 !important; }
.stButton > button, .stFormSubmitButton > button, .stDownloadButton > button {
  min-height:3rem; border-radius:11px !important; border:1px solid var(--blue) !important;
  background:var(--blue) !important; color:#fff !important; font-family:'Manrope',sans-serif !important;
  font-size:.92rem !important; font-weight:900 !important; letter-spacing:-.01em;
  box-shadow:0 5px 13px rgba(36,87,230,.16) !important; transition:all .18s ease !important;
}
.stButton > button:hover, .stFormSubmitButton > button:hover, .stDownloadButton > button:hover {
  background:var(--blue-dark) !important; border-color:var(--blue-dark) !important;
  transform:translateY(-1px); box-shadow:0 8px 18px rgba(36,87,230,.22) !important;
}
.stDownloadButton > button { background:#fff !important; color:var(--blue) !important; border:1.5px solid #b9ccff !important; box-shadow:none !important; }
.stDownloadButton > button:hover { background:var(--blue-soft) !important; }

/* Example topic buttons */
div[data-testid="stHorizontalBlock"] .example-wrap { color:var(--muted); }

/* Pipeline */
.pipeline-head { display:flex; align-items:center; justify-content:space-between; gap:1rem; margin:1.8rem 0 .9rem; }
.pipeline-title { font-family:'Manrope',sans-serif; font-size:1.25rem; font-weight:900; letter-spacing:-.035em; color:var(--ink); }
.pipeline-note { font-size:.78rem; font-weight:800; color:#718099; }
.stage-card { height:100%; min-height:136px; padding:1.05rem 1rem; border:1px solid #dfe6f1; border-radius:15px; background:#fff; box-shadow:0 5px 16px rgba(20,33,61,.025); position:relative; overflow:hidden; }
.stage-card:before { content:""; position:absolute; top:0; left:0; right:0; height:4px; background:#dce4f1; }
.stage-card.running { border-color:#8eabff; background:#f4f7ff; box-shadow:0 6px 18px rgba(36,87,230,.08); }
.stage-card.running:before { background:var(--blue); }
.stage-card.done { border-color:#b6e4cf; background:#f3fbf7; }
.stage-card.done:before { background:#159568; }
.stage-number { font-family:'Manrope',sans-serif; font-size:.73rem; font-weight:900; color:#8290a6; letter-spacing:.08em; }
.stage-name { font-family:'Manrope',sans-serif; font-size:.96rem; font-weight:900; color:var(--ink); margin:.45rem 0 .35rem; }
.stage-desc { color:#65738a; font-size:.77rem; line-height:1.45; font-weight:600; }
.stage-status { display:inline-block; margin-top:.7rem; border-radius:6px; padding:.22rem .42rem; background:#f0f3f8; color:#65738a; font-size:.64rem; font-weight:900; letter-spacing:.07em; }
.stage-card.running .stage-status { background:#dfe8ff; color:#1f4bc5; }
.stage-card.done .stage-status { background:#dff5e9; color:#087448; }

/* Results */
.results-head { display:flex; align-items:center; gap:.7rem; margin:2rem 0 1rem; }
.results-title { font-family:'Manrope',sans-serif; color:var(--ink); font-size:1.65rem; font-weight:900; letter-spacing:-.045em; }
.results-badge { background:var(--green-soft); color:#087448; border:1px solid #c7ecd9; border-radius:7px; padding:.32rem .55rem; font-size:.68rem; font-weight:900; letter-spacing:.06em; }
[data-testid="stVerticalBlockBorderWrapper"] { border-color:var(--line) !important; border-radius:16px !important; background:#fff; }
.report-heading { font-family:'Manrope',sans-serif; font-size:1.05rem; font-weight:900; color:var(--blue); margin-bottom:.7rem; padding-bottom:.65rem; border-bottom:1px solid #e4eaf4; }
.critic-heading { font-family:'Manrope',sans-serif; font-size:1.05rem; font-weight:900; color:#087448; margin-bottom:.7rem; padding-bottom:.65rem; border-bottom:1px solid #d9f0e4; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color:var(--ink) !important; font-family:'Manrope',sans-serif !important; font-weight:900 !important; letter-spacing:-.03em !important; }
.stMarkdown h2 { font-size:1.35rem !important; }
.stMarkdown h3 { font-size:1.08rem !important; }
.stMarkdown p, .stMarkdown li { color:#283852; line-height:1.75; }
[data-testid="stExpander"] { border:1px solid var(--line) !important; border-radius:12px !important; background:#fff !important; }
[data-testid="stExpander"] summary p { color:var(--ink) !important; font-weight:800 !important; }
[data-testid="stAlert"] { border-radius:12px !important; }
.stSpinner > div { color:var(--blue) !important; }
.stMarkdown a { color:var(--blue) !important; font-weight:700; }
.footer { text-align:center; margin-top:2.6rem; padding-top:1.2rem; border-top:1px solid #e0e6f0; color:#8793a6; font-size:.75rem; font-weight:700; }

@media (max-width: 768px) {
  .block-container { padding:1rem .8rem 2.5rem; }
  .brandbar { align-items:flex-start; }
  .top-pill { display:none; }
  .hero { padding:1.45rem; border-radius:18px; }
  .hero:after { width:150px; height:150px; right:-80px; top:-50px; border-width:20px; }
  .hero h1 { font-size:2.6rem; }
  .research-card { padding:1rem; }
  .stage-card { min-height:120px; padding:.85rem; }
  .stage-name { font-size:.84rem; }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Session state
# -----------------------------------------------------------------------------
for key, default in (("results", {}), ("running", False), ("done", False), ("pipeline_error", "")):
    if key not in st.session_state:
        st.session_state[key] = default


def set_example_topic(value: str) -> None:
    st.session_state.topic_input = value


def stage_state(step: str) -> str:
    results = st.session_state.results
    steps = ["search", "reader", "writer", "critic"]
    if step in results:
        return "done"
    if st.session_state.running:
        for current in steps:
            if current not in results:
                return "running" if current == step else "waiting"
    return "waiting"


def render_stage(number: str, title: str, description: str, state: str) -> None:
    labels = {"waiting": "UP NEXT", "running": "IN PROGRESS", "done": "✓ COMPLETE"}
    card_class = "running" if state == "running" else ("done" if state == "done" else "")
    st.markdown(f"""
      <div class="stage-card {card_class}">
        <div class="stage-number">STEP {number}</div>
        <div class="stage-name">{title}</div>
        <div class="stage-desc">{description}</div>
        <span class="stage-status">{labels[state]}</span>
      </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Brand bar + hero
# -----------------------------------------------------------------------------
st.markdown("""
<div class="brandbar">
  <div class="brand-left">
    <div class="brand-mark">R</div>
    <div><div class="brand-name">Research Agent AI</div><div class="brand-tagline">INTELLIGENT RESEARCH WORKSPACE</div></div>
  </div>
  <div class="top-pill">MULTI-AGENT INTELLIGENCE</div>
</div>
<div class="hero">
  <div class="hero-kicker">✦ Your AI-powered research team</div>
  <h1>From research question<br>to <span>evidence-backed insight.</span></h1>
  <p>Research Agent AI brings search, source analysis, report writing, and quality review into one streamlined workflow—so you can explore a topic and turn findings into a clear, structured report.</p>
  <div class="hero-meta">
    <span class="meta-chip">01&nbsp; Search</span><span class="meta-chip">02&nbsp; Read</span>
    <span class="meta-chip">03&nbsp; Write</span><span class="meta-chip">04&nbsp; Review</span>
  </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Research input - full-width, primary action
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">What do you want to investigate?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Enter a topic or question. Your AI agents will find relevant sources, extract useful information, and prepare a report for review.</div>', unsafe_allow_html=True)

with st.container(border=True):
    with st.form("research_form", clear_on_submit=False):
        input_col, button_col = st.columns([5, 1.55], vertical_alignment="bottom")
        with input_col:
            st.text_input(
                "Research topic",
                placeholder="e.g. How AI agents are changing software development",
                key="topic_input",
                help="Use a specific topic for more focused research.",
            )
        with button_col:
            run_btn = st.form_submit_button("✦  Run research", use_container_width=True)
    st.caption("Suggested starting points")
    examples = ["AI agents in software", "CRISPR gene editing", "Fusion energy progress"]
    example_cols = st.columns(3)
    for col, example in zip(example_cols, examples):
        with col:
            st.button(example, key=f"example_{example}", on_click=set_example_topic, args=(example,), use_container_width=True)

# -----------------------------------------------------------------------------
# Pipeline tracker - horizontal steps instead of side-by-side input/pipeline
# -----------------------------------------------------------------------------
st.markdown("""
<div class="pipeline-head">
  <div class="pipeline-title">How your report comes together</div>
  <div class="pipeline-note">4-STAGE WORKFLOW</div>
</div>
""", unsafe_allow_html=True)

stage_cols = st.columns(4, gap="medium")
stage_specs = [
    ("01", "Search", "Find relevant web sources", "search"),
    ("02", "Read", "Extract useful page content", "reader"),
    ("03", "Write", "Build the research report", "writer"),
    ("04", "Review", "Score and critique the report", "critic"),
]
for col, (number, title, desc, key) in zip(stage_cols, stage_specs):
    with col:
        render_stage(number, title, desc, stage_state(key))

if st.session_state.pipeline_error:
    st.error(st.session_state.pipeline_error)

# -----------------------------------------------------------------------------
# Run the original research pipeline. Provider/tools are kept in agents.py.
# -----------------------------------------------------------------------------
if run_btn:
    topic_value = st.session_state.get("topic_input", "").strip()
    if not topic_value:
        st.warning("Please enter a research topic first.")
    else:
        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False
        st.session_state.pipeline_error = ""
        st.rerun()

if st.session_state.running and not st.session_state.done:
    results = dict(st.session_state.results)
    topic_value = st.session_state.get("topic_input", "").strip()
    try:
        if "search" not in results:
            with st.spinner("01 / Searching the web for reliable sources…"):
                search_agent = build_search_agent()
                sr = search_agent.invoke(
                    {"messages": [("user", f"Find recent, reliable and detailed information about: {topic_value}")]},
                    config={"recursion_limit": 8},
                )
                results["search"] = sr["messages"][-1].content
                st.session_state.results = dict(results)

        if "reader" not in results:
            with st.spinner("02 / Reading the most relevant sources…"):
                reader_agent = build_reader_agent()
                rr = reader_agent.invoke(
                    {"messages": [("user",
                        f"Based on the following search results about '{topic_value}', "
                        f"pick the most relevant URL and scrape it for deeper content.\n\n"
                        f"Search Results:\n{results['search'][:800]}")]},
                    config={"recursion_limit": 8},
                )
                results["reader"] = rr["messages"][-1].content
                st.session_state.results = dict(results)

        if "writer" not in results:
            with st.spinner("03 / Writing your research report…"):
                research_combined = (
                    f"SEARCH RESULTS:\n{results['search']}\n\n"
                    f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
                )
                results["writer"] = writer_chain.invoke({"topic": topic_value, "research": research_combined})
                st.session_state.results = dict(results)

        if "critic" not in results:
            with st.spinner("04 / Reviewing the report for quality…"):
                results["critic"] = critic_chain.invoke({"report": results["writer"]})
                st.session_state.results = dict(results)

        st.session_state.running = False
        st.session_state.done = True
        st.session_state.pipeline_error = ""
        st.rerun()
    except Exception as exc:
        st.session_state.results = dict(results)
        st.session_state.running = False
        st.session_state.done = False
        error_text = str(exc)
        if "RESOURCE_EXHAUSTED" in error_text or "429" in error_text or "quota" in error_text.lower():
            st.session_state.pipeline_error = (
                "The AI provider quota/rate limit was reached. Your completed steps are saved on this page. "
                "Check your Google AI Studio rate limits and try again when quota is available."
            )
        else:
            st.session_state.pipeline_error = f"The research pipeline stopped: {error_text}"
        st.rerun()

# -----------------------------------------------------------------------------
# Results - report first, review next, raw evidence tucked away
# -----------------------------------------------------------------------------
r = st.session_state.results
if r:
    st.markdown("""
    <div class="results-head"><div class="results-title">Research output</div><div class="results-badge">LIVE WORKSPACE</div></div>
    """, unsafe_allow_html=True)

    if "writer" in r:
        with st.container(border=True):
            st.markdown('<div class="report-heading">▤ &nbsp; FINAL RESEARCH REPORT</div>', unsafe_allow_html=True)
            st.markdown(r["writer"])
            st.download_button(
                label="↓  Download report (.md)",
                data=r["writer"],
                file_name=f"research_report_{int(time.time())}.md",
                mime="text/markdown",
                use_container_width=False,
            )

    if "critic" in r:
        with st.container(border=True):
            st.markdown('<div class="critic-heading">✓ &nbsp; CRITIC REVIEW</div>', unsafe_allow_html=True)
            st.markdown(r["critic"])

    raw_cols = st.columns(2)
    if "search" in r:
        with raw_cols[0]:
            with st.expander("Search agent · raw results", expanded=False):
                st.markdown(r["search"])
    if "reader" in r:
        with raw_cols[1]:
            with st.expander("Reader agent · extracted content", expanded=False):
                st.markdown(r["reader"])

st.markdown("<div class='footer'>Research Agent AI · Multi-agent research workflow · Built with Streamlit</div>", unsafe_allow_html=True)
