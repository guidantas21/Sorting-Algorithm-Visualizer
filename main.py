import pygame
import math

pygame.init()

class DrawInformation:
    "This class contains the global constatnts of the pygame window"

    # == CONSTANTS ==

    # colors
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    GREY = 128, 128, 128
    LIGHT_GREY = 192, 192, 192
    DARK_GREY = 160, 160, 160
    BACKGROUND_COLOR = BLACK

    GRADIENTS = [
        GREY,
        LIGHT_GREY,
        DARK_GREY
    ]

    # fonts
    FONT = pygame.font.SysFont('roboto', 25)
    LARGE_FONT = pygame.font.SysFont('roboto', 30)

    # padding
    SIDE_PADDING = 100
    TOP_PADDING = 150


    def __init__(self, width, height, starting_list):
        self.width = width
        self.height = height
        # set up a pygame window
        self.window = pygame.display.set_mode((width, height))
        # set the name of the window
        pygame.display.set_caption("Sorting Algorithm Visualization")

        self.set_list(starting_list)


    def set_list(self, starting_list):
        self.starting_list = starting_list
        self.min_value = min(starting_list)
        self.max_value = max(starting_list)

        self.rect_width = round((self.width - self.SIDE_PADDING) / len(starting_list))
        self.rect_unit_height = math.floor((self.height - self.TOP_PADDING) / (self.max_value - self.min_value))

        self.starting_x = self.SIDE_PADDING // 2



def create_starting_list(n, min_value, max_value):
    from random import randint
    return [randint(min_value, max_value) for _ in range(n)]


def draw(draw_info, sorting_algorithm_name, ascending):
    # draw the window
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    settings = draw_info.LARGE_FONT.render(
        f"{sorting_algorithm_name} - {'Ascending' if ascending else 'Descending'}",
        1,
        draw_info.BLUE
    )

    draw_info.window.blit(settings, (draw_info.width/2 - settings.get_width()/2, 5))


    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending",
        1,
        draw_info.WHITE
    )

    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 35))


    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort",
        1,
        draw_info.WHITE
    )

    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 65))

    draw_list(draw_info)
    # update the window
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_background=False):
    lst = draw_info.starting_list

    if clear_background:
        clear_rect = (draw_info.SIDE_PADDING // 2, draw_info.TOP_PADDING, # x, y
                    draw_info.width - draw_info.SIDE_PADDING, draw_info.height - draw_info.TOP_PADDING) # width, height
        
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.starting_x + i * draw_info.rect_width
        y = draw_info.height - (val - draw_info.min_value) * draw_info.rect_unit_height

        # [i % 3] = 0 or 1 or 2
        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.rect_width, draw_info.height))

    if clear_background:
        pygame.display.update()


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.starting_list
    n = len(lst)

    for i in range(n):

        for j in range(0, n - i - 1):

            if (ascending and lst[j] > lst[j+1]) or (not ascending and lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]

                draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.starting_list

    for i in range(len(lst)):
        key = lst[i]
        j = i - 1

        while True:
            ascending_sort_cond = j >= 0 and key < lst[j] and ascending
            descending_sort_cond = j >= 0 and key > lst[j] and not ascending

            if not ascending_sort_cond and not descending_sort_cond:
                break

            lst[j+1] = lst[j]
            j -= 1
            lst[j+1] = key

            draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
            yield True

    return lst


def main():
    run = True
    clock = pygame.time.Clock()


    # list settings
    n = 100
    min_value = 0
    max_value = 100

    starting_list = create_starting_list(n, min_value, max_value)

    draw_info = DrawInformation(1100, 800, starting_list)

    print(draw_info.starting_list)


    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None


    # application loop
    while run:
        # set the loop FPS
        clock.tick(120)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algorithm_name, ascending)

        # pygame event loop
        for event in  pygame.event.get():

            # quit the application
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                new_list = create_starting_list(n, min_value, max_value)
                draw_info.set_list(new_list)
                sorting = False

            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algorithm_name = "Insertion Sort"

            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algorithm_name = "Bubble Sort"

    pygame.quit()

if __name__ == "__main__":
    main()
