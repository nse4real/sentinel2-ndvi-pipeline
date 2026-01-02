import rasterio as rio
import numpy as np
import matplotlib.pyplot as plt

with rio.open(r"output\ndvi.tif") as ds:
    ndvi = ds.read(1).astype("float32")
    ndvi = np.where(ndvi == ds.nodata, np.nan, ndvi)

plt.figure(figsize=(6, 6))
plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar(label="NDVI")
plt.title("NDVI preview")
plt.axis("off")
plt.tight_layout()
plt.savefig(r"output\ndvi_preview.png", dpi=150)
plt.close()

print("Wrote output\\ndvi_preview.png")
