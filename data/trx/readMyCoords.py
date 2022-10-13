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
    ax.text(np.mean(x), np.mean(y), f"{i+1}", color=col)
    ax.grid(True)

fig.savefig("schleiz-tx-pos.pdf")
