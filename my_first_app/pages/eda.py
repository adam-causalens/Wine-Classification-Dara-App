from bokeh.plotting import figure
from dara.components import Bokeh, Card, Select, Stack, Text
from dara.components.plotting.palettes import CategoricalLight3
from dara.core import py_component, Variable

from my_first_app.data import data, features


@py_component()
def scatter_plot(x: Variable[str], y: Variable[str]):
    plot_data = data.copy()
    plot_data['color'] = plot_data['species_names'].map(
        {x: CategoricalLight3[i] for i, x in enumerate(data['species_names'].unique())}
    )

    p = figure(title=f"{x} vs {y}", sizing_mode='stretch_both', toolbar_location=None)
    p.circle(
        x,
        y,
        color='color',
        source=plot_data,
        fill_alpha=0.4,
        size=10,
        legend_group='species_names'
    )
    return Bokeh(p)


def eda_page():
    x_var = Variable('alcohol')
    y_var = Variable('color_intensity')

    return Card(
        Stack(
            Text('X:'),
            Select(items=features, value=x_var),
            Text('Y:'),
            Select(items=features, value=y_var),
            direction='horizontal',
            align='center',
            hug=True,
        ),
        scatter_plot(x_var, y_var),
        title='Exploratory Data Analysis',
        subtitle="Scatter Plot"
    )
