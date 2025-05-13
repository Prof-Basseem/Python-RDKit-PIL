# Python-RDKit-PIL

A Python tool for visualizing chemical reactions using RDKit and adding custom text annotations with PIL (Python Imaging Library).

## Description

This project demonstrates how to:
1. Convert SMILES reaction notation to RDKit reaction objects
2. Generate 2D coordinates for chemical structures
3. Draw chemical reactions using RDKit's drawing capabilities
4. Modify the resulting images with PIL to add custom text (including Unicode chemical symbols)

The example reaction shows the esterification of ethanol with acetic acid to form ethyl acetate, catalyzed by concentrated sulfuric acid (H₂SO₄).

## Requirements

- Python 3.6+
- RDKit
- Pillow (PIL)
- io (standard library)

## Installation

```bash
# Install RDKit using conda (recommended approach)
conda install -c conda-forge rdkit

# Install Pillow
pip install Pillow
```

## Usage

Run the script with Python:

```bash
python Draw.py
```

The script will:
1. Create a visual representation of the esterification reaction
2. Add "Conc.H₂SO₄" text at the specified coordinates
3. Save the result as "reaction_with_text.png" in the current directory

## Code Explanation

- The reaction is defined in SMILES notation: `CCO.CC(O)=O>>O=C(OCC)C`
  - CCO: Ethanol
  - CC(O)=O: Acetic acid
  - O=C(OCC)C: Ethyl acetate
- The script converts the SMILES to an RDKit reaction object
- 2D coordinates are computed for all molecules
- The reaction is drawn using RDKit's MolDraw2DCairo
- The resulting image is loaded into PIL
- Custom text with Unicode subscripts (H₂SO₄) is added at specific coordinates
- The final image is saved as a high-quality PNG file

## Customization

To draw different reactions, modify the `smile_reaction` variable with your desired SMILES reaction string.

To change text annotations, modify the `text` variable and the `x, y` coordinates.

## Sample Output

When you run the script, it will generate an image file called "reaction_with_text.png" showing the chemical reaction with the catalyst text labeled.
