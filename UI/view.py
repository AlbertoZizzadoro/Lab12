import flet as ft
from UI.alert import AlertManager


class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab12"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Definisco gli elementi a None per pulizia
        self.txt_anno = None
        self.lista_visualizzazione_1 = None
        self.txt_soglia = None
        self.lista_visualizzazione_2 = None
        self.txt_id_rifugio_partenza = None
        self.txt_id_rifugio_arrivo = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """




        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # Intestazione
        self.txt_titolo = ft.Text(value="Gestione Sentieri di Montagna", size=38, weight=ft.FontWeight.BOLD)

        # Riga 1 (Grafo)
        self.txt_anno = ft.TextField(label="Anno (1950-2024)", width=200)
        pulsante_crea_grafo = ft.ElevatedButton(
            text="Crea Grafo",
            on_click=self.controller.handle_grafo if self.controller else None,
            width=200
        )
        row1 = ft.Row([self.txt_anno, pulsante_crea_grafo], alignment=ft.MainAxisAlignment.CENTER)
        self.lista_visualizzazione_1 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        # Riga 2 (Conta Archi)
        self.txt_soglia = ft.TextField(label="Soglia Peso", width=200)
        self.pulsante_conta_archi = ft.ElevatedButton(
            text="Conta Archi",
            width=200,
            on_click=self.controller.handle_conta_archi if self.controller else None
        )
        row2 = ft.Row([self.txt_soglia, self.pulsante_conta_archi], alignment=ft.MainAxisAlignment.CENTER)
        self.lista_visualizzazione_2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        # Riga 3 (Cammino Minimo - INPUT)
        self.txt_id_rifugio_partenza = ft.TextField(label="ID Partenza", width=150)
        self.txt_id_rifugio_arrivo = ft.TextField(label="ID Arrivo", width=150)

        pulsante_calcola_cammino = ft.ElevatedButton(
            text="Calcola Cammino",
            width=200,
            on_click=self.controller.handle_cammino_minimo if self.controller else None
        )

        row3 = ft.Row(
            [self.txt_id_rifugio_partenza, self.txt_id_rifugio_arrivo, pulsante_calcola_cammino],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # --- 2. LAYOUT PAGINA (UN SOLO PAGE.ADD) ---
        self.page.add(
            self.toggle_cambia_tema,  # Ora esiste!
            self.txt_titolo,
            ft.Divider(),

            # Sezione 1
            row1,
            self.lista_visualizzazione_1,
            ft.Divider(),

            # Sezione 2
            row2,
            self.lista_visualizzazione_2,
            ft.Divider(),

            # Sezione 3
            ft.Text("Ricerca Cammino Minimo", size=20, weight=ft.FontWeight.W_500),
            row3

        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()