#!/usr/bin/env python3
'''
Test script for Symbol.from_lib() functionality
'''

# Try to import skip
try:
    from skip.eeschema.schematic import Schematic, Symbol
    print("✓ Successfully imported skip modules")
except ImportError as e:
    print(f"✗ Failed to import skip modules: {e}")
    print("You may need to install the package first")
    exit(1)

# Create a simple test
print("\n--- Testing Symbol.from_lib() ---")
print("Note: This test creates a minimal schematic structure")

# For a real test, we'd need an actual schematic file
# This is just to verify the function exists and has the right signature
print("\nChecking if Symbol.from_lib() method exists...")
if hasattr(Symbol, 'from_lib'):
    print("✓ Symbol.from_lib() method found")
    
    # Check the signature
    import inspect
    sig = inspect.signature(Symbol.from_lib)
    print(f"✓ Method signature: {sig}")
    
    params = list(sig.parameters.keys())
    expected_params = ['schematic', 'lib_id', 'reference', 'at_x', 'at_y', 
                      'unit', 'in_bom', 'on_board', 'dnp']
    
    if all(p in params for p in expected_params):
        print("✓ All expected parameters are present")
    else:
        print(f"⚠ Parameters: {params}")
    
    # Get docstring
    if Symbol.from_lib.__doc__:
        print(f"\n✓ Docstring preview:")
        doc_lines = Symbol.from_lib.__doc__.strip().split('\n')
        for line in doc_lines[:5]:
            print(f"  {line}")
        print("  ...")
else:
    print("✗ Symbol.from_lib() method not found")

print("\n--- Test Complete ---")
print("\nTo fully test this function, you would need to:")
print("1. Load an actual schematic file")
print("2. Call Symbol.from_lib() with a valid lib_id")
print("3. Verify the new symbol is created and added to the schematic")
print("\nExample usage:")
print("  sch = Schematic.load('your_schematic.kicad_sch')")
print("  new_cap = Symbol.from_lib(sch, 'Device:C_Small', 'C1', 100, 100)")
print("  sch.save('output.kicad_sch')")
