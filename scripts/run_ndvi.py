import argparse
import os
import numpy as np
import rasterio as rio


def compute_ndvi(red_path: str, nir_path: str, out_path: str, nodata_out: float) -> tuple[float, float]:
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    with rio.open(red_path) as rds, rio.open(nir_path) as nds:
        red = rds.read(1).astype("float32")
        nir = nds.read(1).astype("float32")
        profile = rds.profile
        nodata_in = profile.get("nodata", 0)

    mask = (red == nodata_in) | (nir == nodata_in)

    ndvi = (nir - red) / (nir + red + 1e-6)
    ndvi = np.where(mask, np.nan, ndvi).astype("float32")

    profile.update(dtype="float32", count=1, nodata=nodata_out, compress="deflate")
    ndvi_out_arr = np.where(np.isnan(ndvi), nodata_out, ndvi).astype("float32")

    with rio.open(out_path, "w", **profile) as dst:
        dst.write(ndvi_out_arr, 1)

    return float(np.nanmin(ndvi)), float(np.nanmax(ndvi))


def main():
    p = argparse.ArgumentParser(description="Compute NDVI from red and NIR GeoTIFFs.")
    p.add_argument("--red", default=r"data\red.tif", help="Path to red band GeoTIFF (default: data\\red.tif)")
    p.add_argument("--nir", default=r"data\nir.tif", help="Path to NIR band GeoTIFF (default: data\\nir.tif)")
    p.add_argument("--out", default=r"output\ndvi.tif", help="Output NDVI GeoTIFF path (default: output\\ndvi.tif)")
    p.add_argument("--nodata", type=float, default=-9999, help="Nodata value for output (default: -9999)")
    args = p.parse_args()

    mn, mx = compute_ndvi(args.red, args.nir, args.out, args.nodata)
    print(f"Wrote {args.out} min/max: {mn} {mx}")


if __name__ == "__main__":
    main()