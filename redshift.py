def calculate_redshift(observed_wavelength, emitted_wavelength):
    # Calculate redshift using the formula: z = (observed_wavelength - emitted_wavelength) / emitted_wavelength
    redshift = (observed_wavelength - emitted_wavelength) / emitted_wavelength
    return redshift

# Get input from the user
observed_wavelength = float(input("Enter the observed wavelength (in nanometers): "))
emitted_wavelength = float(input("Enter the emitted wavelength (in nanometers): "))

# Calculate redshift
redshift_value = calculate_redshift(observed_wavelength, emitted_wavelength)

# Display the result
print(f"Observed Wavelength: {observed_wavelength} nm")
print(f"Emitted Wavelength: {emitted_wavelength} nm")
print(f"Redshift: {redshift_value}")
