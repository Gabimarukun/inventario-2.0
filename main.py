from modules.menu import mostrar_menu

def main():
    try:
        mostrar_menu()
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")

if __name__ == '__main__':
    main()
