import pygame
import random
import time

colors = (
    (0, 0, 0),  # Preto
    (255, 255, 255),  # Branco
    (0, 0, 255),  # Azul
    (255, 40, 0),  # Vermelho
    (0, 255, 0),  # Verde
    (240, 230, 140)  # Amarelo Khaki
)


class Sort:
    def __init__(self, resolution, display):
        self.resolution = resolution
        self.display = display
        self.frameUnit = 20
        self.array = []
        self.mergesortArray = []
        self.bruteForceSortArray = []

    def drawLine(self, color, initialPosition, endPosition):
        pygame.draw.line(self.display, color, initialPosition, endPosition)

    def mergesort(self, array, startColumn=0):
        if len(array) > 1:
            middleListId = int(len(array)/2)

            self.framesBuilder(1, array, startColumn)
            pygame.display.update()
            time.sleep(0.1)
            firstHalf = array[:middleListId]
            secondHalf = array[middleListId:]

            self.mergesort(firstHalf, startColumn)
            self.mergesort(secondHalf, middleListId+startColumn)

            i, j, k = 0, 0, 0
            while i < len(firstHalf) and j < len(secondHalf):
                if firstHalf[i] < secondHalf[j]:
                    array[k] = firstHalf[i]
                    i += 1
                else:
                    array[k] = secondHalf[j]
                    j += 1
                k += 1

            while i < len(firstHalf):
                array[k] = firstHalf[i]
                i += 1
                k += 1

            while j < len(secondHalf):
                array[k] = secondHalf[j]
                j += 1
                k += 1

    def populateFrames(self, sort_f, startCol, array, x_list, endY, x_1_list):
        print("Apresentando a lista nos quadros...")

        if not sort_f or sort_f == 1:
            j = 0

            for i in self.array:
                pygame.draw.rect(
                    self.display, colors[2],
                    (x_list[j] + 1, endY - i * 20 + 1, 19, (i * 20) - 1)
                )

                if not sort_f:
                    time.sleep(0.05)
                    pygame.display.update()

                pygame.draw.rect(
                    self.display, colors[2],
                    (x_1_list[j] + 1, endY - i * 20 + 1, 19, (i * 20) - 1)
                )

                if not sort_f:
                    time.sleep(0.05)
                    pygame.display.update()

                j = j + 1

        if sort_f == 1:
            j = startCol

            for i in array:
                pygame.draw.rect(
                    self.display, colors[3],
                    (x_list[j] + 1, endY - i * 20 + 1, 19, (i * 20) - 1)
                )

                j = j + 1

            pygame.display.update()
            time.sleep(0.1)

    def framesBuilder(self, sort_f, array=[], startColumn=0):
        self.display.fill(colors[0])

        print("Construindo quadros...")

        y, w = 80, self.frameUnit
        x_list, x_1_list = [], []

        limit_x = int((self.resolution[0] / 2) / self.frameUnit)
        limit_y = int((self.resolution[1] - 60) / self.frameUnit)

        for j in range(1, limit_y - 1):
            x = 20
            x_1 = 560

            for i in range(1, limit_x - 1):
                # Linhas da Esquerda
                self.drawLine(colors[1], (x, y), (x, y + w))
                self.drawLine(colors[1], (x_1, y), (x_1, y + w))

                # Linhas do Topo
                self.drawLine(colors[1], (x, y), (x + w, y))
                self.drawLine(colors[1], (x_1, y), (x_1 + w, y))

                # Linhas de Baixo
                self.drawLine(colors[1], (x, y + w), (x + w, y + w))
                self.drawLine(colors[1], (x_1, y + w), (x_1 + w, y + w))

                # Linhas da Direita
                self.drawLine(colors[1], (x + w, y), (x + w, y + w))
                self.drawLine(colors[1], (x_1 + w, y), (x_1 + w, y + w))

                if y == 80:
                    x_list.append(x)
                    x_1_list.append(x_1)

                if not sort_f:
                    pygame.display.update()

                x = x + self.frameUnit
                x_1 = x_1 + self.frameUnit

            y = y + self.frameUnit

        endY = y

        if not sort_f:
            pygame.display.update()

        self.populateFrames(sort_f, startColumn, array, x_list, endY, x_1_list)

    def sortPage(self):
        print("Criando lista de números aleatórios...")
        options = [i + 1 for i in range(25)]
        self.array = [random.choice(options) for i in range(25)]

        self.mergesortArray = self.array
        self.bruteForceSortArray = self.array

        print("Iniciando construção de quadros de dados...")

        # Primeira construção
        sort_f = 0
        self.framesBuilder(sort_f)

        print("Iniciando mergesort...")
        self.mergesort(self.array)

        while 1:
            a=1

    def principal(self):
        running = True
        showInitialPage = False  # True

        while running:
            self.display.fill(colors[0])

            if showInitialPage:
                print("a")
                # self.initialPage()

            print("Acessando tela de ordenações...")
            self.sortPage()


def main():
    pygame.init()

    print("Iniciando aplicação...")

    resolution = (1080, 600)

    pygame.display.set_caption("Sorte")

    # icon = pygame.image.load("./assets/media/icon.png")
    # pygame.display.set_icon(icon)

    display = pygame.display.set_mode(resolution)
    newSort = Sort(resolution, display)
    newSort.principal()


if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
