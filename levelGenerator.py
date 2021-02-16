import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 60

word_data = []
lines = 16
cols = 31

monitor = pygame.display.Info()
screen_width = monitor.current_w
screen_height = monitor.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
object_size = screen_width // 30

for i in range(lines):
    line = []
    for j in range(cols):
        line.append(0)
    word_data.append(line)

object_list = []
grass_image = pygame.image.load("image/grassland.png")
wall_image = pygame.image.load("image/brick_wall.png")
road_image = pygame.image.load("image/road.png")

def __drawWorld():
    object_list = []
    for i in range(lines):
        for j in range(cols):
            if word_data[i][j] == 0:
                img = pygame.transform.scale(grass_image, (object_size, object_size))
                img_rect = img.get_rect()
                img_rect.x = j * object_size
                img_rect.y = i * object_size
                object = (img, img_rect)
                object_list.append(object)
            if word_data[i][j] == 1:
                img = pygame.transform.scale(wall_image, (object_size, object_size))
                img_rect = img.get_rect()
                img_rect.x = j * object_size
                img_rect.y = i * object_size
                object = (img, img_rect)
                object_list.append(object)
            if word_data[i][j] == 2:
                img = pygame.transform.scale(road_image, (object_size, object_size))
                img_rect = img.get_rect()
                img_rect.x = j * object_size
                img_rect.y = i * object_size
                object = (img, img_rect)
                object_list.append(object)

    for object in object_list:
        screen.blit(object[0], object[1])
        pygame.draw.rect(screen, (255, 255, 255), object[1], 1)



delay = 0
clicked = False
run = True
while run:
    clock.tick(fps)
    __drawWorld()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    delay += 1
    if delay > 10:
        clicked = False
        delay = 0
    if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        for i in range(lines):
            for j in range(cols):
                # check mouseover and clicked condition
                rectangle = pygame.Rect(j * object_size, i * object_size, object_size, object_size)

                if rectangle.collidepoint(mouse_position):
                    word_data[i][j] += 1
                    clicked = True
                if word_data[i][j] > 2:
                    word_data[i][j] = 0
                if clicked == True:
                    break
            if clicked == True:
                break

        __drawWorld()

    pygame.display.update()


for i in range(lines):
    for j in range(cols):
        print(word_data[i][j], end=" ")
    print("")

pygame.quit()


