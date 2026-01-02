import numpy as np
import rasterio as rio
import os

red_path = r"data\red.tif"
nir_path = r"data\nir.tif"
out_path = r"output\ndvi.tif"

os.makedirs("output", exist_ok=True)

with rio.open(red_path) as rds, rio.open(nir_path) as nds:
    red = rds.read(1).astype("float32")
    nir = nds.read(1).astype("float32")
    profile = rds.profile

nodata = profile.get("nodata", 0)
mask = (red == nodata) | (nir == nodata)

ndvi = (nir - red) / (nir + red + 1e-6)
ndvi = np.where(mask, np.nan, ndvi).astype("float32")

profile.update(
    dtype="float32",
    count=1,
    nodata=-9999,
    compress="deflate"
)

ndvi_out = np.where(np.isnan(ndvi), -9999, ndvi)

with rio.open(out_path, "w", **profile) as dst:
    dst.write(ndvi_out, 1)

print(
    "Wrote", out_path,
    "min/max:",
    float(np.nanmin(ndvi)),
    float(np.nanmax(ndvi))
)
