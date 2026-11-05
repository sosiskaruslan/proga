import customtkinter as ctk
from tkinter import messagebox, simpledialog
import random

# тема приложения
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# список футбольных клубов
clubs_list = [
    "Реал Мадрид", "Барселона", "Бавария", "Манчестер Юнайтед",
    "Ливерпуль", "Ювентус", "ПСЖ", "Челси", "Арсенал", "Милан", "Интер", "Атлетико"
]

# база футболистов кто за какие клубы играл
players_base = {
    ("Реал Мадрид", "Барселона"): ["Луиш Фигу", "Роналдо", "Микаэль Лаудруп", "Хавьер Савиола", "Рональд Куман"],
    ("Реал Мадрид", "Бавария"): ["Тони Кроос", "Хамес Родригес", "Арьен Роббен"],
    ("Реал Мадрид", "Манчестер Юнайтед"): ["Криштиану Роналду", "Дэвид Бекхэм", "Хуан Мата"],
    ("Реал Мадрид", "Ливерпуль"): ["Хаби Алонсо", "Майкл Оуэн", "Стив Макманаман"],
    ("Реал Мадрид", "Ювентус"): ["Зинедин Зидан", "Гонсало Игуаин", "Альваро Мората", "Фабио Каннаваро"],
    ("Реал Мадрид", "ПСЖ"): ["Килиан Мбаппе", "Анхель Ди Мария", "Николя Анелька"],
    ("Реал Мадрид", "Челси"): ["Тибо Куртуа", "Эден Азар", "Клод Макелеле"],
    ("Реал Мадрид", "Арсенал"): ["Месут Озил", "Дани Себальос", "Николя Анелька"],
    ("Реал Мадрид", "Милан"): ["Кака", "Андрей Шевченко", "Роналдо", "Кларенс Зеедорф"],
    ("Реал Мадрид", "Интер"): ["Уэсли Снейдер", "Роналдо", "Самюэль Это'О"],
    ("Реал Мадрид", "Атлетико"): ["Тибо Куртуа", "Альваро Мората", "Фернандо Торрес"],

    ("Барселона", "Бавария"): ["Роберт Левандовски", "Тьяго Алькантара", "Хавьер Маскерано"],
    ("Барселона", "Манчестер Юнайтед"): ["Златан Ибрагимович", "Хуан Верон", "Жерар Пике"],
    ("Барселона", "Ливерпуль"): ["Луис Суарес", "Фелипе Коутиньо", "Хавьер Маскерано"],
    ("Барселона", "Ювентус"): ["Артур Мело", "Миралем Пьянич", "Тьяго Мотта"],
    ("Барселона", "ПСЖ"): ["Неймар", "Лионель Месси", "Роналдиньо", "Тьяго Мотта"],
    ("Барселона", "Челси"): ["Сеск Фабрегас", "Педро Родригес", "Хуан Верон"],
    ("Барселона", "Арсенал"): ["Алексис Санчес", "Тьерри Анри", "Сеск Фабрегас"],
    ("Барселона", "Милан"): ["Роналдиньо", "Златан Ибрагимович", "Патрик Клюйверт"],
    ("Барселона", "Интер"): ["Роналдо", "Хавьер Дзанетти", "Луиш Фигу"],
    ("Барселона", "Атлетико"): ["Давид Вилья", "Луис Суарес", "Тьяго Алькантара"],

    ("Бавария", "Манчестер Юнайтед"): ["Бастиан Швайнштайгер", "Хуан Мата", "Гордон Стракан"],
    ("Бавария", "Ливерпуль"): ["Тьяго Алькантара", "Дитмар Хаманн", "Штефан Эффенберг"],
    ("Бавария", "Ювентус"): ["Маттейс де Лигт", "Артуро Видаль", "Дуглас Коста"],
    ("Бавария", "ПСЖ"): ["Кингсли Коман", "Эрик Максим Чупо-Мотинг", "Бернд Лено"],
    ("Бавария", "Челси"): ["Михаэль Баллак", "Дидье Дрогба", "Жоржиньо"],
    ("Бавария", "Арсенал"): ["Сердж Гнабри", "Лукас Подольски", "Месут Озил"],
    ("Бавария", "Милан"): ["Андреа Пирло", "Кларенс Зеедорф", "Лука Тони"],
    ("Бавария", "Интер"): ["Луиш Фигу", "Кларенс Зеедорф", "Лотар Маттеус"],
    ("Бавария", "Атлетико"): ["Хуанфран", "Диего Симеоне", "Луис Гарсия"],

    ("Манчестер Юнайтед", "Ливерпуль"): ["Майкл Оуэн", "Стив Макманаман", "Питер Крауч"],
    ("Манчестер Юнайтед", "Ювентус"): ["Криштиану Роналду", "Златан Ибрагимович", "Анхель Ди Мария"],
    ("Манчестер Юнайтед", "ПСЖ"): ["Анхель Ди Мария", "Златан Ибрагимович", "Маркус Рэшфорд"],
    ("Манчестер Юнайтед", "Челси"): ["Хуан Мата", "Неманья Видич", "Дидье Дрогба"],
    ("Манчестер Юнайтед", "Арсенал"): ["Робин ван Перси", "Дэнни Уэлбек", "Сол Кэмпбелл"],
    ("Манчестер Юнайтед", "Милан"): ["Златан Ибрагимович", "Дэвид Бекхэм", "Кларенс Зеедорф"],
    ("Манчестер Юнайтед", "Интер"): ["Златан Ибрагимович", "Ромелу Лукаку", "Алексис Санчес"],
    ("Манчестер Юнайтед", "Атлетико"): ["Хуан Мата", "Диего Форлан", "Радмель Фалькао"],

    ("Ливерпуль", "Ювентус"): ["Фабио Каннаваро", "Джанлука Дзамбротта", "Николя Анелька"],
    ("Ливерпуль", "ПСЖ"): ["Николя Анелька", "Джибриль Сиссе", "Маму Сако"],
    ("Ливерпуль", "Челси"): ["Фернандо Торрес", "Дидье Дрогба", "Стив Макманаман"],
    ("Ливерпуль", "Арсенал"): ["Майкл Оуэн", "Николя Анелька", "Джермейн Пеннант"],
    ("Ливерпуль", "Милан"): ["Андрей Шевченко", "Дидье Дрогба", "Кларенс Зеедорф"],
    ("Ливерпуль", "Интер"): ["Иван Перишич", "Ромелу Лукаку", "Луис Суарес"],
    ("Ливерпуль", "Атлетико"): ["Фернандо Торрес", "Луис Гарсия", "Диего Симеоне"],

    ("Ювентус", "ПСЖ"): ["Анхель Ди Мария", "Гонсало Игуаин", "Мойзе Кин"],
    ("Ювентус", "Челси"): ["Альваро Мората", "Гонсало Игуаин", "Клаудио Маркизио"],
    ("Ювентус", "Арсенал"): ["Аарон Рэмси", "Месут Озил", "Николя Анелька"],
    ("Ювентус", "Милан"): ["Андреа Пирло", "Кларенс Зеедорф", "Джанлуиджи Буффон"],
    ("Ювентус", "Интер"): ["Роналдо", "Андреа Пирло", "Кларенс Зеедорф", "Зинедин Зидан"],
    ("Ювентус", "Атлетико"): ["Альваро Мората", "Фернандо Льоренте", "Диего Симеоне"],

    ("ПСЖ", "Челси"): ["Тьяго Силва", "Давид Луиз", "Николя Анелька"],
    ("ПСЖ", "Арсенал"): ["Николя Анелька", "Тьерри Анри", "Александр Ляказетт"],
    ("ПСЖ", "Милан"): ["Златан Ибрагимович", "Роналдиньо", "Дэвид Бекхэм"],
    ("ПСЖ", "Интер"): ["Златан Ибрагимович", "Роналдо", "Майкон"],
    ("ПСЖ", "Атлетико"): ["Анхель Ди Мария", "Диего Симеоне", "Луис Гарсия"],

    ("Челси", "Арсенал"): ["Сеск Фабрегас", "Оливье Жиру", "Николя Анелька", "Эшли Коул"],
    ("Челси", "Милан"): ["Андрей Шевченко", "Дидье Дрогба", "Кларенс Зеедорф"],
    ("Челси", "Интер"): ["Ромелу Лукаку", "Андреа Пирло", "Кларенс Зеедорф"],
    ("Челси", "Атлетико"): ["Диего Коста", "Фернандо Торрес", "Тибо Куртуа"],

    ("Арсенал", "Милан"): ["Андрей Шевченко", "Тьерри Анри", "Патрик Виейра"],
    ("Арсенал", "Интер"): ["Деннис Бергкамп", "Патрик Виейра", "Кларенс Зеедорф"],
    ("Арсенал", "Атлетико"): ["Тьерри Анри", "Хосе Антонио Рейес", "Месут Озил"],

    ("Милан", "Интер"): ["Роналдо", "Андреа Пирло", "Кларенс Зеедорф", "Златан Ибрагимович", "Лука Модрич"],
    ("Милан", "Атлетико"): ["Фернандо Торрес", "Диего Симеоне", "Луис Гарсия"],

    ("Интер", "Атлетико"): ["Диего Симеоне", "Хавьер Дзанетти", "Луис Гарсия"]
}


class TicTacToeFootball(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Футбольные крестики-нолики")
        self.geometry("800x900")

        # переменные игры
        self.rows_clubs = []
        self.cols_clubs = []
        self.field = [[None for _ in range(3)] for _ in range(3)]
        self.cells = [[None for _ in range(3)] for _ in range(3)]
        self.current = 1

        self.build_ui()
        self.new_game()

    # создаем интерфейс
    def build_ui(self):
        self.lbl_title = ctk.CTkLabel(self, text="Футбольные крестики-нолики",
                                      font=ctk.CTkFont(size=28, weight="bold"))
        self.lbl_title.pack(pady=(20, 10))

        self.lbl_turn = ctk.CTkLabel(self, text="Ходит: Игрок 1",
                                     font=ctk.CTkFont(size=22, weight="bold"),
                                     text_color="red")
        self.lbl_turn.pack(pady=5)

        self.lbl_info = ctk.CTkLabel(self, text="Выберите клетку на поле",
                                     font=ctk.CTkFont(size=16), text_color="gray")
        self.lbl_info.pack(pady=10)

        self.frame = ctk.CTkFrame(self, fg_color="gray25", corner_radius=15)
        self.frame.pack(pady=20)

        self.btn_new = ctk.CTkButton(self, text="Новая игра",
                                     command=self.new_game,
                                     font=ctk.CTkFont(size=18, weight="bold"),
                                     width=200, height=40,
                                     fg_color="green", hover_color="darkgreen")
        self.btn_new.pack(pady=20)

    # новая игра
    def new_game(self):
        chosen = random.sample(clubs_list, 6)
        self.rows_clubs = chosen[:3]
        self.cols_clubs = chosen[3:]

        self.field = [[None for _ in range(3)] for _ in range(3)]
        self.current = 1
        self.show_turn()
        self.lbl_info.configure(text="Выберите клетку на поле")

        # удаляем старые виджеты
        for w in self.frame.winfo_children():
            w.destroy()

        # пустой угол
        ctk.CTkLabel(self.frame, text="", width=120, height=60).grid(row=0, column=0, padx=10, pady=10)

        # клубы сверху
        for c in range(3):
            ctk.CTkLabel(self.frame, text=self.cols_clubs[c],
                         font=ctk.CTkFont(size=14, weight="bold"),
                         width=120, height=60,
                         fg_color="gray40", corner_radius=10,
                         text_color="white").grid(row=0, column=c + 1, padx=10, pady=10)

        # клубы слева и клетки
        for r in range(3):
            ctk.CTkLabel(self.frame, text=self.rows_clubs[r],
                         font=ctk.CTkFont(size=14, weight="bold"),
                         width=120, height=60,
                         fg_color="gray40", corner_radius=10,
                         text_color="white").grid(row=r + 1, column=0, padx=10, pady=10)

            for c in range(3):
                btn = ctk.CTkButton(
                    self.frame, text="",
                    width=120, height=120,
                    font=ctk.CTkFont(size=40, weight="bold"),
                    fg_color="gray50", hover_color="gray60",
                    corner_radius=10, border_width=0,
                    command=lambda r=r, c=c: self.click_cell(r, c)
                )
                btn.grid(row=r + 1, column=c + 1, padx=10, pady=10)
                self.cells[r][c] = btn

    # клик по клетке
    def click_cell(self, r, c):
        if self.field[r][c] is not None:
            messagebox.showinfo("Ошибка", "Эта клетка уже занята!")
            return

        rc = self.rows_clubs[r]
        cc = self.cols_clubs[c]
        self.lbl_info.configure(text=f"Клетка: {rc}  {cc}")

        name = simpledialog.askstring(
            "Назовите футболиста",
            f"Игрок {self.current}, назовите футболиста,\n"
            f"который играл за «{rc}» и «{cc}»:",
            parent=self
        )

        if not name or not name.strip():
            messagebox.showwarning("Пропуск хода", "Вы не назвали футболиста. Ход переходит сопернику.")
            self.next_turn()
            return

        name = name.strip()

        if self.check_answer(r, c, name):
            self.field[r][c] = self.current
            self.draw_cell(r, c)
            self.lbl_info.configure(text=f"Верно! {name} играл за оба клуба.")

            if self.check_win():
                self.light_win()
                messagebox.showinfo("Победа!", f"Игрок {self.current} победил!")
                self.lock_all()
            elif self.check_draw():
                messagebox.showinfo("Ничья", "Все клетки заполнены. Ничья!")
                self.lock_all()
            else:
                self.next_turn()
        else:
            hints = self.get_hints(r, c)
            h_text = ", ".join(hints[:3]) if hints else "Нет данных"

            messagebox.showerror(
                "Неверный ответ",
                f"Футболист «{name}» не играл за оба клуба!\n\n"
                f"Правельные варианты:\n{h_text}\n\n"
                f"Ход переходит к Игроку {3 - self.current}."
            )
            self.next_turn()

    # нормализация текста
    def norm(self, text):
        return text.lower().replace('ё', 'е').strip()

    # проверка ответа
    def check_answer(self, r, c, name):
        rc = self.rows_clubs[r]
        cc = self.cols_clubs[c]

        k1 = (rc, cc)
        k2 = (cc, rc)

        plist = players_base.get(k1) or players_base.get(k2)
        if not plist:
            return False

        in_words = set(self.norm(name).split())
        for p in plist:
            p_words = set(self.norm(p).split())
            if in_words & p_words:
                return True
        return False

    # подсказки
    def get_hints(self, r, c):
        rc = self.rows_clubs[r]
        cc = self.cols_clubs[c]

        k1 = (rc, cc)
        k2 = (cc, rc)

        if k1 in players_base:
            return players_base[k1]
        elif k2 in players_base:
            return players_base[k2]
        return []

    # отрисовка клетки
    def draw_cell(self, r, c):
        for row in self.cells:
            for btn in row:
                if btn.cget("state") == "normal":
                    btn.configure(border_width=0)

        btn = self.cells[r][c]
        if self.field[r][c] == 1:
            btn.configure(fg_color="red", hover_color="darkred",
                          text="X", text_color="white",
                          border_width=3, border_color="yellow")
        elif self.field[r][c] == 2:
            btn.configure(fg_color="blue", hover_color="darkblue",
                          text="O", text_color="white",
                          border_width=3, border_color="yellow")
        btn.configure(state="disabled")

    # подсветка победной линии
    def light_win(self):
        b = self.field
        wc = []

        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] and b[i][0] is not None:
                wc = [(i, 0), (i, 1), (i, 2)]
                break
            if b[0][i] == b[1][i] == b[2][i] and b[0][i] is not None:
                wc = [(0, i), (1, i), (2, i)]
                break

        if not wc:
            if b[0][0] == b[1][1] == b[2][2] and b[0][0] is not None:
                wc = [(0, 0), (1, 1), (2, 2)]
            elif b[0][2] == b[1][1] == b[2][0] and b[0][2] is not None:
                wc = [(0, 2), (1, 1), (2, 0)]

        for r, c in wc:
            self.cells[r][c].configure(fg_color="green", border_width=3, border_color="white")

    # следущий ход
    def next_turn(self):
        self.current = 3 - self.current
        self.show_turn()
        self.lbl_info.configure(text="Выберите клетку на поле")

    # показать кто ходит
    def show_turn(self):
        color = "red" if self.current == 1 else "blue"
        self.lbl_turn.configure(text=f"Ходит: Игрок {self.current}", text_color=color)

    # проверка победы
    def check_win(self):
        b = self.field
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] and b[i][0] is not None: return True
            if b[0][i] == b[1][i] == b[2][i] and b[0][i] is not None: return True
        if b[0][0] == b[1][1] == b[2][2] and b[0][0] is not None: return True
        if b[0][2] == b[1][1] == b[2][0] and b[0][2] is not None: return True
        return False

    # проверка ничьей
    def check_draw(self):
        for r in range(3):
            for c in range(3):
                if self.field[r][c] is None: return False
        return True

    # заблокировать поле
    def lock_all(self):
        for r in range(3):
            for c in range(3):
                self.cells[r][c].configure(state="disabled")


if __name__ == "__main__":
    app = TicTacToeFootball()
    app.mainloop()

