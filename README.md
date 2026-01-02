\# Sentinel-2 NDVI Mini-Pipeline (GDAL + GeoPandas + Rasterio)



A small end-to-end Earth Observation project that:

\- downloads Sentinel-2 L2A bands via GDAL from public COGs,

\- clips to an AOI polygon,

\- computes NDVI,

\- exports analysis-ready GeoTIFF and a quick PNG preview.



\## What this project demonstrates

\- GDAL-based raster access and warping

\- AOI-driven clipping (GeoJSON)

\- Raster index computation (NDVI)

\- Reproducible, script-based workflow

\- Clean outputs ready for GIS / further ML



\## Quickstart (Windows + conda)

1\. Create environment

2\. Run scripts

3\. Generate outputs



> Note: Large rasters are not committed to git. Outputs are created locally.



\## Outputs

\- `output/ndvi.tif`

\- `output/ndvi\_preview.png`



\## Repo structure

\- `aoi/` AOI polygon (GeoJSON)

\- `scripts/` pipeline scripts

\- `data/` local clipped bands (ignored by git)

\- `output/` results (ignored by git)



\## Next improvements

\- Add cloud masking using SCL band

\- Parameterise AOI + date range

\- Add unit tests and CI



