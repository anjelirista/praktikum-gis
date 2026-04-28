# Import library inti QGIS
from qgis.core import QgsRasterLayer, QgsProject
# 1. Tentukan URL dari file Cloud Optimized GeoTIFF (COG)
# (Contoh: Citra Sentinel-2 komposit True Color dari AWS)
cog_url="https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/47/N/QA/2023/8/S2B_47NQA_20230806_0_L2A/TCI.tif"
# 2. Tambahkan prefix /vsicurl/ agar GDAL (engine QGIS) tahu ini adalah streaming HTTP
vsi_url = "/vsicurl/" + cog_url
# 3. Buat objek Raster Layer baru
# Parameter: (path data, Nama Layer di QGIS, provider)
layer = QgsRasterLayer(vsi_url, "Citra Streaming COG", "gdal")
# 4. Validasi dan tambahkan ke kanvas peta
if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print("Berhasil! Layer ditambahkan ke peta.")
else:
    print("Gagal memuat layer. Periksa URL atau koneksi internet.")