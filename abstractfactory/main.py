from abstract import *

def main():
    # Usando la fábrica LCD Azul
    lcd_azul_factory = FactoryLcdAzul()
    color_azul = lcd_azul_factory.create_color()
    tv_lcd = lcd_azul_factory.create_tv()
    color_azul.colorea(tv_lcd)

    # Usando la fábrica Plasma Amarillo
    plasma_amarillo_factory = FactoryPlasmaAmarillo()
    color_amarillo = plasma_amarillo_factory.create_color()
    tv_plasma = plasma_amarillo_factory.create_tv()
    color_amarillo.colorea(tv_plasma)

if __name__ == "__main__":
    main()