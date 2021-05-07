from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=180,
                     rotate=0, blocks_arranged_in_reverse_order=False)

    device.contrast(8)
    msg = " <3 Aswatthaama Here!!"
    while(1):
        show_message(device, msg, fill="red", font=proportional(SINCLAIR_FONT), scroll_delay= 0.09)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

