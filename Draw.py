from rdkit import Chem
from rdkit.Chem import rdChemReactions, AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D
import io
from PIL import Image, ImageDraw, ImageFont

# Reaction SMILES
smile_reaction = 'CCO.CC(O)=O>>O=C(OCC)C'

# convert the reaction to a RDKit reaction object
rxn = rdChemReactions.ReactionFromSmarts(smile_reaction, useSmiles=True)

# Calculate coordinates for all molecules
for mol in list(rxn.GetReactants()) + list(rxn.GetProducts()):
    AllChem.Compute2DCoords(mol)

# Draw the reaction via RDKit
drawer = rdMolDraw2D.MolDraw2DCairo(800, 300)
drawer.DrawReaction(rxn)
drawer.FinishDrawing()
png = drawer.GetDrawingText()

# Convert to PIL Image
img = Image.open(io.BytesIO(png))
draw = ImageDraw.Draw(img)

# Font settings support for Unicode
try:
    font = ImageFont.truetype("DejaVuSans.ttf", 16)
except:
    font = ImageFont.load_default()

# Text to add to the image
text = "Conc.H₂SO₄"

# Position to place the text
x, y = 395, 129
draw.text((x, y), text, fill="black", font=font)

# Save the image with high quality
img.save("reaction_with_text.png", "PNG", quality=600)
# Display the image
img
