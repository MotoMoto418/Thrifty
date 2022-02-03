def page():
    global run

    page_surface = pygame.Surface((WIDTH, HEIGHT))
    
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')

    while run:
        clock.tick(FPS)
        time_delta = clock.tick(FPS)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            manager.process_events(event)

        page_surface.fill(BEIGE)

        manager.update(time_delta)
        SCREEN.blit(page_surface, ORIGIN)
        manager.draw_ui(SCREEN)

        pygame.display.update()
