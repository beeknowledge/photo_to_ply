from PIL import Image
import numpy as np
import open3d

points = []
colors = []
normals = []

rowimage=Image.open('logo.jpg')
maxcol , maxrow = rowimage.size
print(maxcol , maxrow)
im = np.array(rowimage)
pcd = open3d.geometry.PointCloud()

for i in range(maxrow):
    for j in range(maxcol):
      a = im[i,j][0] #R
      b = im[i,j][1] #G
      c = im[i,j][2] #B
      if a != 0:
        a = a/255.0
      if b != 0:
        b = b/255.0
      if c != 0:
        c = c/255.0

      points.append([ float(i),float(j), 0.0])
      colors.append([a,b,c])

rgb_t = np.transpose(colors)
pcd.points = open3d.utility.Vector3dVector(points)
pcd.colors = open3d.utility.Vector3dVector(colors)

downpcd = pcd.uniform_down_sample(every_k_points=5)

print(im.size)
# ランダムに打った点を可視化
open3d.visualization.draw_geometries(
  [downpcd],
  width=1000,
  height=2000,
  point_show_normal = True
  )

open3d.io.write_point_cloud("test.ply", downpcd)