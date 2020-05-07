import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import requests, base64
from io import BytesIO
import plotly.graph_objects as go
from collections import Counter

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

PLOTLY_LOGO = "https://avatars2.githubusercontent.com/u/37410753?s=460&u=5ff392afec0d036134b5bbe106aab20561fec8b6&v=4"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Profile", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://github.com/rohilzalke1995?tab=repositories",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)







#####App Components#########
#dropdown
def enconde_image(image_url):
    buffered = BytesIO(requests.get(image_url).content)
    image_base64 = base64.b64encode(buffered.getvalue())
    return b'data:image/png;base64,' + image_base64


dropdown_app = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Houston', 'value': 'TX'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC',
        placeholder="Select a city",
    ),
    html.Div(id='output-container')
])

#sq root

slider_sq = app.layout = html.Div([
    html.H1("Square Root Slider Graph"),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(21)},
        max=20,
        value=2,
        step=1,
        updatemode='drag',
    ),
    html.Div(id='updatemode-output-container', style={'margin-top': 20})
])

#word_count

word_count_app = app.layout = html.Div([
    html.H1("Word Count Graph"),
    dcc.Graph(id = 'word-graph', animate = True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Textarea(
        id = 'text-area',
        value = '',
        placeholder='Common words...',
        style={'width':'100%', 'height':'50%'},
    ),

])





'''Cards'''
#card1

card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/dropdown.jfif", top=True),
        dbc.CardBody(
            [
                html.H4("DropDown", className="card-title"),
                html.P(
                    "Select a place of your choice and "
                    "See a image of that place",
                    className="card-text",
                ),
                dbc.Button("Launch", color="primary", id = "open"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(dropdown_app),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close", className="ml-auto")
                        ),
                    ],
            id="modal",
        ),
            ]
        ),
    ],
    style={"width": "18rem"},
)


#
#
# #card2


cardtwo = dbc.Card(
    [
        dbc.CardImg(src="/static/images/sq_root_images.png", top=True),
        dbc.CardBody(
            [
                html.H4("Sq root graph", className="card-title"),
                html.P(
                    "Select a number on the slider and this app will tell the sq of that number ",
                    className="card-text",
                ),
                dbc.Button("Launch", color="primary", id = "opentwo"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(slider_sq),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="closetwo", className="ml-auto")
                        ),
                    ],
            id="modaltwo",
        ),
            ]
        ),
    ],
    style={"width": "18rem"},
)
#
# #card3

card3 = dbc.Card(
    [
        dbc.CardImg(src="/static/images/dropdown.jfif", top=True),
        dbc.CardBody(
            [
                html.H4("Word Count graph", className="card-title"),
                html.P(
                    "Select a number on the slider and this app will tell the sq of that number ",
                    className="card-text",
                ),
                dbc.Button("Launch", color="primary", id = "open3"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(word_count_app),
                        dbc.ModalFooter(
                            dbc.Button("Close3", id="close3", className="ml-auto")
                        ),
                    ],
            id="modal3",
        ),
            ]
        ),
    ],
    style={"width": "18rem"},
)
'''Body'''

body = html.Div(
    dbc.Row([
        dbc.Col(html.Div(card)),
        dbc.Col(html.Div(cardtwo)),
        dbc.Col(html.Div(card3))

    ])
)


#main layout
app.layout = html.Div(
    [navbar, body]
)



#navbar
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

#dropdown call back
@app.callback(
    Output('output-container', 'children'),
    [Input('my-dropdown', 'value')])
def update_output(value):
    NYC_img = enconde_image('https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fcincoveces.files.wordpress.com%2F2011%2F08%2Fnycpan2.jpg&f=1&nofb=1')
    TX_img = enconde_image('https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.sparefoot.com%2Fmoving%2Fwp-content%2Fuploads%2F2015%2F12%2FThinkstockPhotos-480535456-1-1.jpg&f=1&nofb=1')
    SF_img = enconde_image('https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.hotelgsanfrancisco.com%2Fassets%2Fthemes%2Fhotelgsanfrancisco%2Fimg%2FHotelG-map.jpg&f=1&nofb=1')
    if value == 'NYC':
        return html.Div(html.Img(src=NYC_img.decode(), style={'width': '100%', 'height':'400px'}))
    elif value == 'TX':
        return html.Div(html.Img(src=TX_img.decode(), style={'width': '100%', 'height':'400px'}))
    elif value == 'SF':
        return html.Div(html.Img(src=SF_img.decode(), style={'width': '100%', 'height':'400px'}))

#
# #Sq root callback

@app.callback(

    [Output('slider-graph', 'figure'),
    Output('updatemode-output-container', 'children')],
    [Input('slider-updatemode', 'value')]
)
def display_value(value):


    x = []
    for i in range(value):
        x.append(i)

    y = []
    for i in range(value):
        y.append(i*i)

    graph = go.Scatter(
        x=x,
        y=y,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),

    )
    return {'data': [graph], 'layout': layout}, f'Value: {round(value, 1)} Square: {value*value}'

#word count callback
@app.callback(
    Output('word-graph', 'figure'),
    [Input('text-area', 'value')]
)
def display_graph(value):
    word_list = value.split()
    word_dict = Counter(word_list)
    x = list(word_dict.keys())
    y = list(word_dict.values())

    graph = go.Bar(
        x=x,
        y=y,
        name='word-count',
        type='bar',
        marker=dict(color='lightgreen')
    )
    plot_bgcolor='rgba(0,0,0,0)',

    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis = dict(type = 'category'),
        yaxis = dict(range=[min(y), max(y)]),
        font = dict(color='white')
    )

    return {'data':[graph], 'layout':layout}



#modal1
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#modal2
@app.callback(
    Output("modaltwo", "is_open"),
    [Input("opentwo", "n_clicks"), Input("closetwo", "n_clicks")],
    [State("modaltwo", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


#modal3
@app.callback(
    Output("modal3", "is_open"),
    [Input("open3", "n_clicks"), Input("close3", "n_clicks")],
    [State("modal3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open





if __name__=='__main__':
    app.run_server(debug=True, port=8080)