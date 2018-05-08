from . import plot
from flask import render_template, make_response, send_file, url_for
from ..models import Carpark, Transaction
import matplotlib.pyplot as plt


@plot.route('/test')
def test():
    return render_template('test.html')


@plot.route('/test_plot')
def test_plot():
    # import base64
    # import BytesIO
    from io import BytesIO
    x = [1,2,3,4]
    y = [1,4,9,16]
    plt.plot(x,y)
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    # from matplotlib.figure import Figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x,y)
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.mimetype = 'image/png'
    return response
