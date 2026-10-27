
import streamlit as st
import streamlit.components.v1 as components
import html

st.set_page_config(
    page_title="Chem Data | Chemistry Virtual Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Visual theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --navy:#102b46;
    --blue:#164e78;
    --cyan:#18b8c8;
    --ice:#effaff;
    --ink:#17324b;
}

html, body, [class*="css"] {
    font-family:'DM Sans',sans-serif;
}

.stApp {
    background:linear-gradient(145deg,#f7fcff 0%,#edf8fc 55%,#f5fbff 100%);
    color:var(--ink);
}

.block-container {
    max-width:1180px;
    padding-top:1.2rem;
    padding-bottom:3rem;
}

header[data-testid="stHeader"] {
    background:rgba(247,252,255,.85);
}

#MainMenu, footer {
    visibility:hidden;
}

.hero {
    background:linear-gradient(115deg,#102b46 0%,#164e78 58%,#087f9b 100%);
    color:white;
    padding:28px 30px;
    border-radius:24px;
    position:relative;
    overflow:hidden;
    box-shadow:0 16px 38px rgba(16,43,70,.15);
}

.hero:after {
    content:"";
    position:absolute;
    width:230px;
    height:230px;
    border:1px solid rgba(255,255,255,.18);
    border-radius:50%;
    right:-60px;
    top:-95px;
    box-shadow:0 0 0 24px rgba(255,255,255,.04),
               0 0 0 50px rgba(255,255,255,.035);
    pointer-events:none;
}

.eyebrow {
    color:#83eff5;
    text-transform:uppercase;
    letter-spacing:2px;
    font-size:11px;
    font-weight:700;
}

.hero h1 {
    font-family:Manrope,sans-serif;
    font-size:clamp(28px,4vw,42px);
    line-height:1.1;
    margin:8px 0 10px;
    color:white;
}

.hero p {
    color:#d8f0f7;
    margin:0;
    max-width:650px;
    font-size:15px;
}

.section-label {
    color:#0e7890;
    text-transform:uppercase;
    font-size:11px;
    letter-spacing:1.8px;
    font-weight:800;
    margin:8px 0 10px;
}

.molecule-card {
    border:1px solid #d9edf5;
    border-radius:18px;
    padding:16px;
    background:rgba(255,255,255,.88);
    box-shadow:0 7px 20px rgba(23,72,99,.05);
    min-height:110px;
}

.molecule-card.active {
    border:1.5px solid #18b8c8;
    box-shadow:0 8px 24px rgba(24,184,200,.13);
    background:#f4feff;
}

.molecule-card h3 {
    font-family:Manrope,sans-serif;
    margin:5px 0 3px;
    font-size:18px;
    color:#123652;
}

.molecule-card p {
    margin:0;
    color:#648095;
    font-size:12px;
}

.pill {
    display:inline-block;
    background:#dff9fb;
    color:#087b8b;
    border-radius:20px;
    padding:4px 9px;
    font-size:11px;
    font-weight:700;
}

.panel {
    background:white;
    border:1px solid #dceef5;
    border-radius:20px;
    padding:18px;
    box-shadow:0 8px 24px rgba(16,67,95,.055);
}

.panel-title {
    color:#123652;
    font-family:Manrope,sans-serif;
    font-weight:800;
    font-size:18px;
    margin-bottom:4px;
}

.muted {
    color:#6b8798;
    font-size:13px;
}

.metric {
    background:#f1fbfe;
    border:1px solid #d9f0f5;
    border-radius:14px;
    padding:12px 14px;
    min-height:76px;
    overflow-wrap:anywhere;
}

.metric-label {
    color:#648095;
    font-size:11px;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing:.7px;
}

.metric-value {
    color:#123652;
    font-family:Manrope,sans-serif;
    font-size:20px;
    font-weight:800;
    margin-top:4px;
    overflow-wrap:anywhere;
}

.smiles-box {
    background:#f4feff;
    border:1px solid #ccecf2;
    border-radius:14px;
    padding:13px 15px;
    margin-top:12px;
}

.smiles-value {
    color:#087b8b;
    font-family:monospace;
    font-size:17px;
    font-weight:700;
    overflow-wrap:anywhere;
    word-break:break-word;
    margin-top:7px;
}

.info-title {
    font-family:Manrope,sans-serif;
    font-size:14px;
    color:#087b8b;
    font-weight:800;
    margin:12px 0 4px;
}

div.stButton > button {
    border-radius:12px;
    border:1px solid #cbe8f0;
    min-height:44px;
    font-weight:700;
}

div.stButton > button[kind="primary"] {
    background:linear-gradient(90deg,#0d829b,#18b8c8);
    color:white;
    border:0;
}

div[data-testid="stRadio"] > div {
    gap:8px;
}

div[data-testid="stRadio"] label {
    background:white;
    border:1px solid #d9edf5;
    border-radius:14px;
    padding:10px 13px;
}

div[data-testid="stRadio"] label p {
    font-weight:700;
}

.viewer-note {
    background:#e8f9fc;
    color:#286477;
    border-radius:10px;
    padding:9px 12px;
    font-size:12px;
    margin-top:8px;
}

.stAlert {
    border-radius:12px;
}

@media (max-width:700px) {
    .block-container {
        padding-left:.8rem;
        padding-right:.8rem;
    }

    .hero {
        padding:22px 20px;
        border-radius:18px;
    }

    .panel {
        padding:13px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------- Molecule database ----------
MOLECULES = {
    "Methane": {
        "cid": 297,
        "formula": "CH₄",
        "mass": "16.04 g/mol",
        "smiles": "C",
        "group": "Alkane (C–H single bonds)",
        "geometry": "Tetrahedral",
        "state": "Gas",
        "color": "#18b8c8",
        "summary": (
            "The simplest alkane, with one carbon atom "
            "bonded to four hydrogen atoms."
        ),
        "properties": [
            "Non-polar molecule with a symmetrical tetrahedral shape.",
            "Highly flammable; complete combustion produces "
            "carbon dioxide and water.",
            "Only weak London dispersion forces act "
            "between methane molecules."
        ],
        "uses": [
            "Main component of natural gas and a common fuel.",
            "Feedstock for hydrogen and industrial chemicals.",
            "Used in controlled laboratory demonstrations "
            "of combustion."
        ],
        "geometry_note": (
            "The H–C–H bond angle is approximately 109.5°."
        )
    },

    "Ethanol": {
        "cid": 702,
        "formula": "C₂H₆O",
        "mass": "46.07 g/mol",
        "smiles": "CCO",
        "group": "Alcohol (hydroxyl, –OH)",
        "geometry": "Tetrahedral around each carbon",
        "state": "Liquid",
        "color": "#1687b5",
        "summary": (
            "A two-carbon alcohol containing a polar "
            "hydroxyl group."
        ),
        "properties": [
            "Polar; its –OH group enables hydrogen bonding.",
            "Miscible with water and volatile at room temperature.",
            "Flammable liquid; keep away from ignition sources."
        ],
        "uses": [
            "Solvent in laboratories, cosmetics and some medicines.",
            "Used in approved disinfectant formulations.",
            "Fuel additive and starting material in "
            "chemical manufacturing."
        ],
        "geometry_note": (
            "Each carbon is approximately tetrahedral; "
            "rotation around the C–C single bond is possible."
        )
    },

    "Benzene": {
        "cid": 241,
        "formula": "C₆H₆",
        "mass": "78.11 g/mol",
        "smiles": "c1ccccc1",
        "group": "Aromatic hydrocarbon (delocalized π system)",
        "geometry": "Planar hexagonal ring",
        "state": "Liquid",
        "color": "#0d6e91",
        "summary": (
            "An aromatic ring of six carbon atoms "
            "with delocalized π electrons."
        ),
        "properties": [
            "Flat, symmetrical ring; all six C–C bonds "
            "are equivalent in the idealized structure.",
            "Non-polar and volatile at room temperature.",
            "Toxic and carcinogenic; avoid exposure and do not "
            "handle outside properly equipped facilities."
        ],
        "uses": [
            "Industrial feedstock for plastics, resins "
            "and synthetic fibers.",
            "Starting material for making other chemicals "
            "in controlled industrial systems.",
            "Not suitable for casual use as a solvent "
            "because of its serious health hazards."
        ],
        "geometry_note": (
            "The ring is planar, with bond angles close to 120°."
        )
    }
}


# ---------- Session state ----------
if "selected_molecule" not in st.session_state:
    st.session_state.selected_molecule = "Methane"


if "page" not in st.session_state:
    st.session_state.page = "Virtual Lab"


# ---------- Header and navigation ----------
nav_left, nav_right = st.columns([1, 2])

with nav_left:
    st.markdown(
        """
        <div style="
            font-family:Manrope,sans-serif;
            font-weight:800;
            font-size:22px;
            color:#123652;
            padding:8px 0;">
            ⚗️ Chem Data
        </div>
        """,
        unsafe_allow_html=True
    )

with nav_right:
    selected_page = st.radio(
        "Main navigation",
        ["Virtual Lab", "About"],
        horizontal=True,
        label_visibility="collapsed",
        key="main_navigation",
    )


# ---------- About page ----------
if selected_page == "About":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">ABOUT THE PROJECT</div>
        <h1>About Chem Data</h1>
        <p>
            An interactive Chemistry Virtual Lab designed to make
            molecular structures and chemical concepts easier to explore.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="panel">
        <div class="panel-title">Project overview</div>
        <p style="font-size:14px;line-height:1.7;color:#6b8798">
            Chem Data is a mobile-friendly educational website for
            exploring Methane, Ethanol and Benzene. It combines
            interactive 3D molecular models with information about
            molecular formula, molar mass, SMILES notation, geometry,
            bonding, physical state, chemical properties and applications.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    about_left, about_right = st.columns(2, gap="large")

    with about_left:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">Developer</div>
            <div style="
                font-family:Manrope,sans-serif;
                font-size:25px;
                font-weight:800;
                color:#087f9b;
                margin:12px 0 5px;">
                LUCKISH
            </div>
            <div class="muted">
                College assignment · Chemistry Virtual Lab
            </div>
            <p style="color:#48697d;line-height:1.7;margin-top:14px">
                Created as a learning project to present chemistry
                concepts through a clear, responsive and interactive interface.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with about_right:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">Technology used</div>
            <p style="color:#48697d;line-height:1.9;margin-top:12px">
                <b>Python & Streamlit</b> — web app and interface<br>
                <b>3Dmol.js</b> — interactive 3D molecule viewer<br>
                <b>PubChem</b> — molecular structure source<br>
                <b>SMILES</b> — text-based molecular notation
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "For educational use. Molecular structures are visual "
        "representations; follow appropriate laboratory safety guidance."
    )

    st.markdown("---")
    st.caption("Chem Data · Developed by Luckish")
    st.stop()


# ---------- Virtual Lab hero ----------
st.markdown("""
<div class="hero">
    <div class="eyebrow">CHEMISTRY • INTERACTIVE LEARNING</div>
    <h1>Chem Data</h1>
    <p>
        A pocket-sized virtual lab to explore molecular shape,
        bonding and real-world chemistry. Select a molecule,
        then rotate and zoom its 3D structure.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------- Molecule selection ----------
st.markdown(
    '<div class="section-label">01 / Choose a molecule</div>',
    unsafe_allow_html=True
)

names = list(MOLECULES.keys())
cols = st.columns(3)

symbols = {
    "Methane": "◇",
    "Ethanol": "◉",
    "Benzene": "⬡"
}

for col, molecule_name in zip(cols, names):

    info = MOLECULES[molecule_name]

    with col:

        active = (
            st.session_state.selected_molecule == molecule_name
        )

        st.markdown(
            f'<div class="molecule-card {"active" if active else ""}">'
            f'<span class="pill">{info["formula"]}</span>'
            f'<h3>{symbols[molecule_name]} &nbsp; {molecule_name}</h3>'
            f'<p>{info["group"]}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "Explore " + molecule_name,
            key="select_" + molecule_name,
            type="primary" if active else "secondary",
            use_container_width=True
        ):
            st.session_state.selected_molecule = molecule_name
            st.rerun()


# ---------- Selected molecule ----------
name = st.session_state.selected_molecule
mol = MOLECULES[name]

st.markdown(
    '<div class="section-label">02 / Molecular workspace</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1.15, 0.85], gap="large")


# ---------- 3D molecular viewer ----------
with left:

    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-title">3D molecular viewer</div>
            <div class="muted">
                {name} · PubChem 3D structure ·
                Drag to rotate, pinch or scroll to zoom
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    viewer_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>

        <style>
            * {{
                box-sizing:border-box;
            }}

            html, body {{
                margin:0;
                padding:0;
                width:100%;
                height:100%;
                overflow:hidden;
                background:transparent;
                font-family:Arial,sans-serif;
            }}

            #wrap {{
                position:relative;
                width:100%;
                height:420px;
                max-height:65vh;
                min-height:300px;
                background:radial-gradient(
                    circle at 50% 42%,
                    #ffffff 0%,
                    #f0fbff 62%,
                    #e4f6fb 100%
                );
                border:1px solid #d4edf4;
                border-radius:18px;
                overflow:hidden;
            }}

            #viewer {{
                position:absolute;
                inset:0;
                width:100%;
                height:100%;
                touch-action:pan-y;
            }}

            #status {{
                position:absolute;
                left:12px;
                right:12px;
                bottom:10px;
                text-align:center;
                font-size:12px;
                color:#547789;
                background:rgba(255,255,255,.82);
                border-radius:8px;
                padding:6px 8px;
                pointer-events:none;
            }}

            #retry {{
                display:none;
                position:absolute;
                top:45%;
                left:50%;
                transform:translate(-50%,-50%);
                border:0;
                border-radius:9px;
                padding:10px 14px;
                background:#087f9b;
                color:white;
                font-weight:bold;
            }}

            @media(max-width:600px) {{
                #wrap {{
                    height:360px;
                    min-height:300px;
                }}
            }}
        </style>
    </head>

    <body>
        <div id="wrap">
            <div id="viewer"></div>
            <div id="status">
                Loading 3D structure from PubChem…
            </div>
            <button id="retry" onclick="loadModel()">
                Retry loading
            </button>
        </div>

        <script>
            const cid = {mol["cid"]};
            let viewer;

            function fail(msg) {{
                document.getElementById('status').textContent = msg;
                document.getElementById('retry').style.display = 'block';
            }}

            async function loadModel() {{

                document.getElementById('retry').style.display = 'none';

                document.getElementById('status').textContent =
                    'Loading 3D structure from PubChem…';

                try {{

                    if (!window.$3Dmol) {{
                        throw new Error(
                            '3D viewer library did not load. Check your internet connection.'
                        );
                    }}

                    const url =
                        `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/${{cid}}/SDF?record_type=3d`;

                    const response = await fetch(url);

                    if (!response.ok) {{
                        throw new Error(
                            'PubChem structure is unavailable right now (HTTP '
                            + response.status + ').'
                        );
                    }}

                    const sdf = await response.text();

                    if (
                        !sdf ||
                        sdf.length < 30 ||
                        sdf.includes('PUGREST.NotFound')
                    ) {{
                        throw new Error(
                            'No 3D structure was returned by PubChem.'
                        );
                    }}

                    document.getElementById('viewer').innerHTML = '';

                    viewer = $3Dmol.createViewer(
                        'viewer',
                        {{
                            backgroundColor:'white',
                            antialias:true
                        }}
                    );

                    viewer.addModel(sdf, 'sdf');

                    viewer.setStyle(
                        {{}},
                        {{
                            stick:{{radius:0.13}},
                            sphere:{{scale:0.24}}
                        }}
                    );

                    viewer.zoomTo();
                    viewer.zoom(0.88);
                    viewer.render();
                    viewer.resize();

                    document.getElementById('status').textContent =
                        'Drag to rotate • Pinch or scroll to zoom';

                    window.addEventListener('resize', () => {{
                        if (viewer) {{
                            viewer.resize();
                            viewer.render();
                        }}
                    }});

                }} catch(e) {{
                    fail(e.message || 'Unable to load the molecular model.');
                }}
            }}

            loadModel();
        </script>
    </body>
    </html>
    """

    components.html(
        viewer_html,
        height=440,
        scrolling=False
    )

    st.markdown(
        """
        <div class="viewer-note">
            Tip: on touchscreens, drag with one finger to rotate
            and pinch to zoom. The model is loaded live from PubChem.
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- Molecular information panel ----------
with right:

    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-title">{name}</div>
            <div class="muted">{mol["summary"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Formula and molar mass
    m1, m2 = st.columns(2)

    with m1:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-label">Formula</div>
                <div class="metric-value">{mol["formula"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m2:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-label">Molar mass</div>
                <div class="metric-value" style="font-size:17px">
                    {mol["mass"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # Geometry and physical state
    m3, m4 = st.columns(2)

    with m3:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-label">Geometry</div>
                <div class="metric-value" style="font-size:15px">
                    {mol["geometry"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m4:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-label">At room temperature</div>
                <div class="metric-value">{mol["state"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------- NEW: SMILES notation ----------
    smiles_safe = html.escape(mol["smiles"])

    st.markdown(
        f"""
        <div class="smiles-box">
            <div class="metric-label">
                SMILES NOTATION
            </div>
            <div class="smiles-value">{smiles_safe}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "SMILES (Simplified Molecular Input Line Entry System) "
        "represents molecular structures as text."
    )

    # Copyable SMILES string
    with st.expander("View and copy SMILES"):

        st.write(f"**{name} — SMILES notation**")

        st.code(mol["smiles"], language=None)

        st.caption(
            "Select the code above to copy the molecular notation."
        )

    # Bonding and functional group
    st.markdown(
        '<div class="info-title">Bonding & functional group</div>',
        unsafe_allow_html=True
    )

    st.write(mol["group"])

    # Chemical properties
    st.markdown(
        '<div class="info-title">Key chemical properties</div>',
        unsafe_allow_html=True
    )

    for item in mol["properties"]:
        st.markdown(f"- {item}")

    # Applications
    st.markdown(
        '<div class="info-title">Applications & uses</div>',
        unsafe_allow_html=True
    )

    for item in mol["uses"]:
        st.markdown(f"- {item}")

    # Geometry explanation
    with st.expander("Geometry note"):
        st.write(mol["geometry_note"])


# ---------- Footer ----------
st.markdown("---")

st.markdown("""
<div style="
    display:flex;
    flex-wrap:wrap;
    justify-content:space-between;
    gap:8px;
    color:#668395;
    font-size:12px;">
    <span>CHEM DATA · COLLEGE VIRTUAL LAB</span>
    <span>Structure source: PubChem · Viewer: 3Dmol.js</span>
</div>
""", unsafe_allow_html=True)

st.caption(
    "Educational reference only. Molecular models are visual "
    "representations and do not show electron density. "
    "SMILES notation is a textual representation of molecular structure."
)
