import numpy as np
import matplotlib.pyplot as plt
# import pyproj
from glob import glob
from saem.tools import readCoordsFromKML

# utm = pyproj.Proj(proj='utm', zone=32, ellps="WGS84")
fig, ax = plt.subplots()
for i, xmlfile in enumerate(glob("*.kml")):
    x, y, *_ = readCoordsFromKML(xmlfile)
    col = f"C{i}"
    ax.plot(x, y, "x-", color=col)
    ax.set_aspect(1.0)
    if xmlfile.startswith("Tx"):
        ax.text(x[0]-100, y[0]+100, xmlfile[2:-4],
                color=col, ha="right")#, va="center")
    ax.grid(True)

fig.savefig("schleiz-tx-pos.pdf")
