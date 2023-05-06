from mpi4py import MPI

def worker(rank, size):
    """Fungsi untuk menjalankan tugas pada proses MPI"""
    print('Worker', rank, 'of', size)

if __name__ == '__main__':
    try:
        # Inisialisasi MPI
        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        size = comm.Get_size()

        # Panggil fungsi worker pada setiap proses MPI
        worker(rank, size)

        # Menunggu semua proses selesai
        comm.Barrier()
    except Exception as e:
        print('An error occurred in process', rank, ':', e)
        comm.Abort()