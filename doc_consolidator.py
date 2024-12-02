import os
from pathlib import Path
import re
import shutil
from typing import Dict, List, Set
import logging
import sys
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

class DocConsolidator:
    def __init__(self, root_dir='.'):
        self.root_dir = Path(root_dir)
        self.gitbook_dir = self.root_dir / '.gitbook'
        self.backup_dir = self.root_dir / 'docs_backup'
        
    def backup_docs(self):
        """Create a backup of the docs directory"""
        logging.info("Creating backup of documentation...")
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        shutil.copytree(self.gitbook_dir, self.backup_dir)
        logging.info(f"Backup created at {self.backup_dir}")

    def consolidate_glossary_sections(self):
        """Consolidate all glossary sections into a single file"""
        logging.info("Consolidating glossary sections...")
        
        # Main glossary file
        glossary_file = self.gitbook_dir / 'glossary.md'
        if not glossary_file.exists():
            logging.error("Main glossary file not found!")
            return

        # Read original glossary content
        glossary_content = glossary_file.read_text(encoding='utf-8')
        
        # Find all files with glossary sections
        for file_path in tqdm(self.gitbook_dir.rglob('*.md')):
            if file_path == glossary_file:
                continue
                
            try:
                content = file_path.read_text(encoding='utf-8')
                if "# Glossary" in content:
                    # Extract glossary section
                    glossary_section = re.search(r'# Glossary.*?(?=^#|\Z)', 
                                              content, 
                                              re.MULTILINE | re.DOTALL)
                    if glossary_section:
                        # Remove glossary section from original file
                        new_content = content.replace(glossary_section.group(0), '')
                        file_path.write_text(new_content.strip() + '\n', encoding='utf-8')
                        
                        # Add reference to main glossary
                        with file_path.open('a', encoding='utf-8') as f:
                            f.write('\n\nFor glossary terms, please refer to the [main glossary](/glossary.md).\n')
                        
                        logging.info(f"Consolidated glossary from {file_path}")
            except Exception as e:
                logging.error(f"Error processing {file_path}: {e}")

    def consolidate_upgrade_procedures(self):
        """Consolidate duplicate upgrade procedures"""
        logging.info("Consolidating upgrade procedures...")
        
        upgrade_dir = self.gitbook_dir / 'nodes/validators/mainnet/canonical-chain-upgrades'
        if not upgrade_dir.exists():
            logging.error("Upgrade procedures directory not found!")
            return

        # Create a template upgrade procedure
        template_content = """# Upgrade Procedure

This document provides the standard upgrade procedure for Injective nodes. For version-specific details, see the sections below.

## Standard Upgrade Steps

1. Wait for the chain to reach the upgrade height
2. The chain will halt automatically at the upgrade height
3. Back up your data directory
4. Download and install the new version
5. Restart your node

For specific version upgrade instructions, see the individual upgrade guides below.
"""
        
        template_file = upgrade_dir / 'UPGRADE_TEMPLATE.md'
        template_file.write_text(template_content, encoding='utf-8')
        
        # Update all upgrade procedure files to reference the template
        for file_path in upgrade_dir.glob('*.md'):
            if file_path.name == 'UPGRADE_TEMPLATE.md':
                continue
                
            try:
                content = file_path.read_text(encoding='utf-8')
                if "Upgrade Procedure" in content:
                    new_content = f"""# {file_path.stem} Upgrade

For the standard upgrade procedure, see the [upgrade template](./UPGRADE_TEMPLATE.md).

## Version-Specific Instructions

"""
                    # Extract any version-specific instructions
                    specific_instructions = re.search(r'# Upgrade Procedure.*?(##.*?)(?=##|\Z)', 
                                                   content, 
                                                   re.MULTILINE | re.DOTALL)
                    if specific_instructions:
                        new_content += specific_instructions.group(1).strip() + '\n'
                    
                    file_path.write_text(new_content, encoding='utf-8')
                    logging.info(f"Updated upgrade procedure in {file_path}")
            except Exception as e:
                logging.error(f"Error processing {file_path}: {e}")

    def execute_consolidation(self):
        """Execute all consolidation tasks"""
        try:
            self.backup_docs()
            self.consolidate_glossary_sections()
            self.consolidate_upgrade_procedures()
            logging.info("Documentation consolidation complete!")
        except Exception as e:
            logging.error(f"Error during consolidation: {e}")

def main():
    consolidator = DocConsolidator()
    consolidator.execute_consolidation()

if __name__ == '__main__':
    main() 