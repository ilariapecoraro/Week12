import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        self._model.creaGrafo()

        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"{self._model._grafo}"))
        for u, v,data in self._model._grafo.edges(data = True):
            tempo_perc = data["tempo"]
            self._view.lst_result.controls.append(ft.Text(f"{u} -> {v}. Tempo percorrenza: {tempo_perc}"))
        self._view.update_page()


    def handleCercaRaggiungibili(self,e):
        id_staz_partenza = int(self._view.ddStazPartenza.value)
        print(f"{id_staz_partenza}")
        ris = self._model.get_raggiungibili(id_staz_partenza)

        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"Fermate raggiungibili "
                                                      f"da {self._model._dizionario_fermate[id_staz_partenza]}"))
        for v in ris:
            self._view.lst_result.controls.append(ft.Text(f"{v}"))
        self._view.update_page()

    def populate_dropdown(self,dd):
        self._model.getAllFermate()
        #Le fermate le trovo nel model, in _lista_fermate

        for fermata in self._model._lista_fermate:
            dd.options.append(ft.dropdown.Option(key=fermata.id_fermata,
                                                 text=fermata.nome))
