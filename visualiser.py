'''
  COMPENG 2DX3 Final Project
  Boran Seckin - seckinb - 400305852

  This code uses the file created by the collector.py and
  creates a 3D visualization using the points.
'''

import numpy as np
import open3d as o3d

SETS = 8
RESOLUTION = 32

def main():
  # Read from xyz data from file
  pcd = o3d.io.read_point_cloud("data.txt", format="xyz")
  
  # Add points for boundry boxes and the midpoints
  for i in range(SETS + 1):
    pcd.points.append([i * 50 - 25, 450, 450])
    pcd.points.append([i * 50 - 25, -450, 450])
    pcd.points.append([i * 50 - 25, -450, -450])
    pcd.points.append([i * 50 - 25, 450, -450])
    pcd.points.append([i * 50 - 25, 0, 0])

  lines = []

  # Boundry boxes
  for set in range(SETS + 1):
    offset = RESOLUTION * SETS + (5 * set)
    lines.append([[offset],     [offset + 1]])
    lines.append([[offset + 1], [offset + 2]])
    lines.append([[offset + 2], [offset + 3]])
    lines.append([[offset + 3], [offset]])

  for set in range(SETS):
    offset = RESOLUTION * SETS + (5 * set)
    lines.append([[offset],     [offset + 5]])
    lines.append([[offset + 1], [offset + 6]])
    lines.append([[offset + 2], [offset + 7]])
    lines.append([[offset + 3], [offset + 8]])

  # Inner-set connections
  for set in range(SETS):
    offset = RESOLUTION * set
    for x in range(RESOLUTION):
      if (x == RESOLUTION - 1):
        lines.append([[x + offset], [x + offset - RESOLUTION + 1]])
      else:
        lines.append([[x + offset], [x + offset + 1]])

  # Inter-set connections
  for set in range(SETS - 1):
    offset = RESOLUTION * set
    for x in range(RESOLUTION):
      lines.append([[x + offset], [x + offset + RESOLUTION]])

  line_set = o3d.geometry.LineSet(
    points=o3d.utility.Vector3dVector(np.asarray(pcd.points)),
    lines=o3d.utility.Vector2iVector(lines)
  )

  o3d.visualization.draw_geometries([line_set])

if __name__ == "__main__":
  main()
