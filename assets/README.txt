Drop images here.

Reference them from a content file as "assets/<filename>", e.g.

    "visual": {
        "type": "image",
        "path": "assets/copilot-message-box.png",
        "side": "right",
        "tag": "What you will see",
        "caption": "The message box sits at the bottom of the Copilot window.",
        "label": "WHAT TO LOOK AT",
        "points": [
            "The box you type into is at the very bottom.",
            "Anything you paste here leaves your laptop.",
            "The model name sits at the top of the panel.",
        ],
    },

Visual types that take images:
  image          - image one side, explanation the other  (path, side, points)
  image_band     - one wide image across the content area (path, caption)
  image_compare  - two images side by side                (bad_path, good_path)

Images are cropped to fill their box exactly. They are never stretched and
never letterboxed, so any aspect ratio is safe. Use the largest version you
have; 2000px on the long edge or more is ideal.

A referenced file that is missing stops the build with a clear error. The
decks never ship a placeholder box.
