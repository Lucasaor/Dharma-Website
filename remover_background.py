from PIL import Image
import numpy as np
from scipy import ndimage
import os


def remove_white_background(input_path, output_path, threshold=30, fade_range=20):
    """
    Remove white/near-white background from an image with smooth edge transitions.
    Only removes white regions connected to the image border, preserving white
    details inside the logo.

    Args:
        input_path (str): Path to the input image file
        output_path (str): Path to save the output PNG file
        threshold (int): Max distance from white to consider as background (0-441)
        fade_range (int): Range over which alpha fades from 0 to 255 for smooth edges
    """
    img = Image.open(input_path).convert('RGBA')
    pixels = np.array(img, dtype=np.float64)

    # Distance of each pixel's RGB from pure white
    white = np.array([255.0, 255.0, 255.0])
    dist = np.sqrt(np.sum((pixels[:, :, :3] - white) ** 2, axis=2))

    # Mask of all near-white pixels (potential background)
    is_white = dist <= (threshold + fade_range)

    # Flood-fill from edges: only white pixels connected to the border are background
    # Create a seed mask that marks border pixels
    h, w = is_white.shape
    border_seed = np.zeros_like(is_white)
    border_seed[0, :] = True
    border_seed[-1, :] = True
    border_seed[:, 0] = True
    border_seed[:, -1] = True

    # Label connected components of white pixels, then keep only those touching the border
    labeled, num_features = ndimage.label(is_white)
    border_labels = set(np.unique(labeled[border_seed])) - {0}
    background_mask = np.isin(labeled, list(border_labels))

    # Build alpha: background pixels get alpha based on distance, others stay opaque
    alpha = np.full((h, w), 255, dtype=np.uint8)
    bg_alpha = np.clip((dist - threshold) / max(fade_range, 1) * 255, 0, 255).astype(np.uint8)
    alpha[background_mask] = bg_alpha[background_mask]

    pixels[:, :, 3] = alpha
    result = Image.fromarray(pixels.astype(np.uint8))

    # Auto-crop to the non-transparent bounding box
    bbox = result.getbbox()
    if bbox:
        result = result.crop(bbox)

    result.save(output_path, 'PNG')
    print(f"Image saved to {output_path} ({result.size[0]}x{result.size[1]})")


if __name__ == "__main__":
    input_file = "media/clients/Estrela_600x600.jpg"
    output_file = "media/clients/Estrela_600x600.png"

    if os.path.exists(input_file):
        remove_white_background(input_file, output_file)
    else:
        print(f"Error: {input_file} not found")
