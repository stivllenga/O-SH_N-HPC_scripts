print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
print("§                  Stiv Llenga                   §")
print("§           PhD student of CCC group             §")
print("§  Heidelbeg Institute for Theoretical Sciences  §")
print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
print()
print("Hello User, I can help calculating the Adiabatic and Vertical Ionization Energies and Electron Affinities:")
print()
coef_eV = 27.2114
coef_kJmol = 2625.5
coef_kcalmol = 627.5
coef_inv_cm = 219474.6
while True:
    neutral_energy=input("Enter the energy [hartree] of the neutral compound:\n")
    print()
    opt_anion_energy=input("Enter the energy [Hartree] of the anion after the orbital relaxation:\n")
    print()
    anion_energy=input("Enter the energy [Hartree] of the anion without orbital relaxation:\n")
    print()
    opt_cation_energy=input("Enter the energy [Hartree] of the cation after the orbital relaxation:\n")
    print()
    cation_energy=input("Enter the energy [Hartree] of the cation without orbital relaxation:\n")
    print()
    print("The program is calculating the Adiabatic IE; Vertical IE; Adiabatic EA & Vertical EA...")
    adiabatic_EA=float(neutral_energy)-float(opt_anion_energy)
    vertical_EA=float(neutral_energy)-float(anion_energy)
    adiabatic_IE=-float(neutral_energy)+float(opt_cation_energy)
    vertical_IE=-float(neutral_energy)+float(cation_energy)
    print()
    print("The Adiabatic Ionisation Energy is:\n ")
    print(f"In eV:       {adiabatic_IE*coef_eV}")
    print(f"In kJ/mol:   {adiabatic_IE * coef_kJmol}")
    print(f"In kcal/mol: {adiabatic_IE * coef_kcalmol}")
    print(f"In cm^-1:    {adiabatic_IE * coef_inv_cm}")
    print()
    print("The Vertical Ionisation Energy is:\n ")
    print(f"In eV:       {vertical_IE * coef_eV}")
    print(f"In kJ/mol:   {vertical_IE * coef_kJmol}")
    print(f"In kcal/mol: {vertical_IE * coef_kcalmol}")
    print(f"In cm^-1:    {vertical_IE * coef_inv_cm}")
    print()
    print("The Adiabatic Electron Affinity is:\n ")
    print(f"In eV:       {adiabatic_EA * coef_eV}")
    print(f"In kJ/mol:   {adiabatic_EA * coef_kJmol}")
    print(f"In kcal/mol: {adiabatic_EA * coef_kcalmol}")
    print(f"In cm^-1:    {adiabatic_EA * coef_inv_cm}")
    print()
    print("The Vertical Electron Affinity is:\n ")
    print(f"In eV:       {vertical_EA * coef_eV}")
    print(f"In kJ/mol:   {vertical_EA * coef_kJmol}")
    print(f"In kcal/mol: {vertical_EA * coef_kcalmol}")
    print(f"In cm^-1:    {vertical_EA * coef_inv_cm}")
    print()
    print()
    print("************************************************")
    print("THE IMPORTANT THING IS TO NEVER STOP QUESTIONING")
    print("             -Albert Einstein-")
    print("************************************************")
