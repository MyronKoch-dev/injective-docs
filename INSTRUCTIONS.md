
# Injective Documentation Pre-processing Prompts

## Remove SVGs

**Objective:** Remove all SVG files from the Injective documentation repository while preserving the repository's integrity and providing clear feedback to the user.

**Instructions:**

1. **Locate SVG Files:** Search the entire repository, starting from the root directory (`.`), for files ending in the `.svg` extension.  Prioritize searching within the `.gitbook` directory.

2. **Verify File Type (Magic Number Check):** For each file found, verify it's an SVG by checking its magic number.  The magic number for an SVG file typically starts with `<svg`. Read the first few bytes of the file and compare them to this signature.  If the file doesn't start with `<svg`, skip it and report a warning to the console.

3. **Confirm Removal (Optional):** Before removing each SVG file, print a message to the console indicating the full path to the file and ask for user confirmation (y/n).

4. **Remove File:** If the user confirms removal (or if confirmation is disabled), attempt to delete the SVG file.

5. **Handle Errors:** Implement comprehensive error handling:
    * **`FileNotFoundError`:** If the file is not found, report a warning and continue.
    * **`PermissionError`:** If there are permission issues, report an error and continue.
    * **Other Errors:** Catch and report any other exceptions and continue.

6. **Report Results:** After processing, print a summary to the console indicating:
    * The total number of `.svg` files found.
    * The number of SVG files successfully removed.
    * The number of files skipped due to verification failures or errors.



## Remove PNGs

**Objective:** Remove all PNG files from the Injective documentation repository, extract and store associated alt text, and provide a summary of the operation.

**Instructions:**

1. **Locate PNG Files:** Search the entire repository for files ending in the `.png` extension.  Prioritize searching within the  `.gitbook` directory.

2. **Verify File Type (Magic Number Check):** Verify each file is a PNG by checking the first 8 bytes. These should be `\x89PNG\r\n\x1a\n`. Skip any files that do not match and log a warning.


3. **Extract Alt Text:** Before removing, search for references to the PNG file within markdown files using a regular expression to locate image tags (`![alt_text](image.png)`).  Extract the alt text if a reference is found.

4. **Store Alt Text:**  Store the extracted alt text, associated with the filename, for later use.

5. **Confirm Removal (Optional):** Before removing each PNG, print a message to the console showing the file path and ask for confirmation (y/n).  This helps prevent unintended deletions during testing.

6. **Remove File:** If confirmed (or confirmation is off), delete the PNG.

7. **Handle Errors:** Handle file operation errors:
    * **`FileNotFoundError`:** If the file isn't found, log a warning and continue.
    * **`PermissionError`:** If there are permission problems, report an error and continue with other files.
    * **Other Errors:**  Catch and report other exceptions and continue.

8. **Report Results:** Provide a summary including:
    * Total PNG files found.
    * Number of PNG files removed.
    * Number of files skipped due to issues.



## Generate Diagram Descriptions (Placeholder - Add Specific Prompts Later)

This section will contain prompts for generating descriptions for diagrams. Add these after SVG and PNG removal. Each diagram should have its own prompt.

**Example (for a specific diagram):**

```
**Diagram File (original location):** ./.gitbook/assets/architecture_diagram.svg

**Prompt:** Describe the key components and relationships shown in the architecture diagram, including the flow of information and control.  Be concise but comprehensive.  Explain the purpose of each component and how they interact.
```
```

This expanded prompt eliminates ambiguity and ensures that all the information Claude needs is explicitly provided.  It's now ready for use in Cursor, though, as always, thorough testing on a sample of your data is strongly recommended before applying it to the entire repository.  Continue to be very cautious with file deletion operations and maintain regular backups.



