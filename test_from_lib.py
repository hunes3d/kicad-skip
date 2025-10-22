#!/usr/bin/env python3
'''
Test script for Symbol.from_lib() functionality with improvements:
1. Symbol is added to schematic.symbol collection immediately
2. Reference and Value have setter support
'''

import sys
sys.path.insert(0, 'src')

# Try to import skip
try:
    from skip.eeschema.schematic import Schematic, Symbol
    print("✓ Successfully imported skip modules")
except ImportError as e:
    print(f"✗ Failed to import skip modules: {e}")
    print("You may need to install the package first")
    exit(1)

# Create a simple test
print("\n--- Testing Symbol.from_lib() Improvements ---")

# Check if method exists
print("\n1. Checking if Symbol.from_lib() method exists...")
if hasattr(Symbol, 'from_lib'):
    print("   ✓ Symbol.from_lib() method found")
    
    # Check the signature
    import inspect
    sig = inspect.signature(Symbol.from_lib)
    print(f"   ✓ Method signature: {sig}")
else:
    print("   ✗ Symbol.from_lib() method not found")
    exit(1)

# Check for property setters
print("\n2. Checking for Reference and Value property setters...")
has_ref_setter = hasattr(Symbol.Reference, 'fset') and Symbol.Reference.fset is not None
has_val_setter = hasattr(Symbol.Value, 'fset') and Symbol.Value.fset is not None

if has_ref_setter:
    print("   ✓ Reference property has setter")
else:
    print("   ✗ Reference property missing setter")
    
if has_val_setter:
    print("   ✓ Value property has setter")
else:
    print("   ✗ Value property missing setter")

print("\n--- Test Complete ---")
print("\n3. To fully test with a real schematic:")
print("   from skip.eeschema.schematic import Schematic, Symbol")
print("   sch = Schematic('your_schematic.kicad_sch')")
print("   ")
print("   # Get initial count")
print("   initial_count = len(sch.symbol)")
print("   ")
print("   # Create new symbol")
print("   new_cap = Symbol.from_lib(sch, 'Device:C_Small', 'C99', 100, 100)")
print("   ")
print("   # Verify it appears in collection immediately")
print("   assert len(sch.symbol) == initial_count + 1")
print("   assert new_cap in sch.symbol")
print("   assert sch.symbol.C99 == new_cap")
print("   ")
print("   # Test property setters")
print("   new_cap.Reference = 'C100'")
print("   new_cap.Value = '10uF'")
print("   assert new_cap.property.Reference.value == 'C100'")
print("   assert new_cap.property.Value.value == '10uF'")
print("   ")
print("   # Save to verify it writes correctly")
print("   sch.save('output.kicad_sch')")

print("1. Load an actual schematic file")
print("2. Call Symbol.from_lib() with a valid lib_id")
print("3. Verify the new symbol is created and added to the schematic")
print("\nExample usage:")
print("  sch = Schematic.load('your_schematic.kicad_sch')")
print("  new_cap = Symbol.from_lib(sch, 'Device:C_Small', 'C1', 100, 100)")
print("  sch.save('output.kicad_sch')")
