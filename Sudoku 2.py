def get_papan_kosong():
  """Membuat papan berukuran 9x9 baru yang kosong (semuanya bernilai 0)"""
  papan = []
  for i in range(9):
    row = []
    for j in range(9):
      row.append(0)
    papan.append(row)
  return papan
def get_papan_default():
  """Membuat papan berukuran 9x9 baru yang beberapa indeks berisi nilai"""
  papan = [
      [7, 8, 0, 4, 0, 0, 1, 2, 0],
      [6, 0, 0, 0, 7, 5, 0, 0, 9],
      [0, 0, 0, 6, 0, 1, 0, 7, 8],
      [0, 0, 7, 0, 4, 0, 2, 6, 0],
      [0, 0, 1, 0, 5, 0, 9, 3, 0],
      [9, 0, 4, 0, 6, 0, 0, 0, 5],
      [0, 7, 0, 3, 0, 0, 0, 1, 2],
      [1, 2, 0, 0, 0, 7, 4, 0, 0],
      [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
  return papan