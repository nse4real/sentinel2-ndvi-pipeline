# Sentinel-2 NDVI Mini-Pipeline (GDAL + GeoPandas + Rasterio)

A small end-to-end Earth Observation project that:
- downloads Sentinel-2 L2A bands via GDAL from public Cloud-Optimized GeoTIFFs (COGs),
- clips to an AOI polygon,
- computes NDVI,
- exports an analysis-ready GeoTIFF and a quick PNG preview.

## What this project demonstrates
- GDAL-based remote raster access + warping
- AOI-driven clipping (GeoJSON)
- Raster index computation (NDVI)
- Reproducible, script-based workflow
- Outputs ready for GIS or downstream ML

## Repo structure
- `aoi/` AOI polygon (GeoJSON)
- `scripts/` pipeline scripts
- `data/` local clipped bands (ignored by git)
- `output/` results (ignored by git)

## Run the pipeline (Windows + conda)

### 1) Create environment
```bash
conda create -n ndvi python=3.12 -y
conda activate ndvi
conda install -c conda-forge gdal rasterio geopandas shapely pyproj fiona numpy matplotlib -y
