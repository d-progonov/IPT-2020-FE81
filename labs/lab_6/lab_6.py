import lab_5b as l5b
import in_out_module as iom

def main():
    a, b, c = iom.open_file()
    num = l5b.geom_progression(a, b, c)
    iom.write_file(num)
            

if __name__ == "__main__":
    main()  