try:
    import helper
except ImportError:
    print("Module 'helper' tidak ditemukan!")
else:
    helper.print_message()