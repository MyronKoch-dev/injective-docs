import os
from pathlib import Path
import re
from collections import defaultdict
import difflib
import logging
import sys
from typing import Dict, List, Set, Tuple
from tqdm import tqdm  # For progress bars

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout  # Ensure logging goes to stdout
)

class DocRefiner:
    def __init__(self, root_dir='.'):
        self.root_dir = Path(root_dir)
        self.gitbook_dir = self.root_dir / '.gitbook'
        self.external_links = set()
        self.headings_map = defaultdict(list)
        self.code_blocks = []
        self.similar_sections = []

    def find_markdown_files(self) -> List[Path]:
        """Find all markdown files in the repository."""
        try:
            if not self.gitbook_dir.exists():
                logging.error(f"Directory not found: {self.gitbook_dir}")
                return []
            return list(self.gitbook_dir.rglob('*.md'))
        except Exception as e:
            logging.error(f"Error finding markdown files: {e}")
            return []

    def analyze_redundant_sections(self, threshold=0.8):
        """Find potentially redundant sections using text similarity."""
        try:
            files = self.find_markdown_files()
            total_files = len(files)
            if total_files == 0:
                logging.warning("No markdown files found to analyze")
                return

            logging.info(f"Analyzing {total_files} files for redundant sections...")
            sections = []

            # Process files with progress bar
            for file_path in tqdm(files, desc="Reading files"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    section_splits = re.split(r'^#{1,6}\s+(.+)$', content, flags=re.MULTILINE)
                    
                    for i in range(1, len(section_splits), 2):
                        heading = section_splits[i]
                        content = section_splits[i+1] if i+1 < len(section_splits) else ""
                        sections.append((heading, content, file_path))
                except Exception as e:
                    logging.error(f"Error processing file {file_path}: {e}")
                    continue

            # Compare sections with progress bar
            total_comparisons = len(sections) * (len(sections) - 1) // 2
            logging.info(f"Comparing {total_comparisons} section pairs...")
            
            with tqdm(total=total_comparisons, desc="Comparing sections") as pbar:
                for i in range(len(sections)):
                    for j in range(i + 1, len(sections)):
                        try:
                            similarity = difflib.SequenceMatcher(
                                None, 
                                sections[i][1], 
                                sections[j][1]
                            ).ratio()
                            
                            if similarity > threshold:
                                self.similar_sections.append({
                                    'section1': {
                                        'heading': sections[i][0],
                                        'file': sections[i][2]
                                    },
                                    'section2': {
                                        'heading': sections[j][0],
                                        'file': sections[j][2]
                                    },
                                    'similarity': similarity
                                })
                        except Exception as e:
                            logging.error(f"Error comparing sections: {e}")
                        pbar.update(1)

        except Exception as e:
            logging.error(f"Error in analyze_redundant_sections: {e}")

    def extract_code_blocks(self):
        """Extract and analyze code blocks from markdown files."""
        try:
            files = self.find_markdown_files()
            total_files = len(files)
            if total_files == 0:
                logging.warning("No markdown files found to analyze")
                return

            logging.info(f"Analyzing {total_files} files for code blocks...")
            
            for file_path in tqdm(files, desc="Extracting code blocks"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    code_blocks = re.finditer(r'```(\w+)?\n(.*?)```', content, re.DOTALL)
                    
                    for block in code_blocks:
                        lang = block.group(1) or 'text'
                        code = block.group(2)
                        self.code_blocks.append({
                            'file': file_path,
                            'language': lang,
                            'code': code,
                            'has_comments': bool(re.search(r'#|//|/\*|\*/', code))
                        })
                except Exception as e:
                    logging.error(f"Error processing file {file_path}: {e}")
                    continue

        except Exception as e:
            logging.error(f"Error in extract_code_blocks: {e}")

    def find_external_links(self):
        """Find all external links in markdown files."""
        try:
            files = self.find_markdown_files()
            total_files = len(files)
            if total_files == 0:
                logging.warning("No markdown files found to analyze")
                return

            logging.info(f"Analyzing {total_files} files for external links...")
            
            for file_path in tqdm(files, desc="Finding external links"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    links = re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content)
                    
                    for link in links:
                        url = link.group(2)
                        if url.startswith(('http', 'https')):
                            self.external_links.add((url, file_path))
                except Exception as e:
                    logging.error(f"Error processing file {file_path}: {e}")
                    continue

        except Exception as e:
            logging.error(f"Error in find_external_links: {e}")

    def analyze_heading_hierarchy(self):
        """Analyze heading hierarchy in markdown files."""
        try:
            files = self.find_markdown_files()
            total_files = len(files)
            if total_files == 0:
                logging.warning("No markdown files found to analyze")
                return

            logging.info(f"Analyzing {total_files} files for heading hierarchy...")
            
            for file_path in tqdm(files, desc="Analyzing headings"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    headings = re.finditer(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
                    
                    current_level = 0
                    for heading in headings:
                        level = len(heading.group(1))
                        text = heading.group(2)
                        
                        if level - current_level > 1:
                            logging.warning(f"Heading level skip in {file_path}: {text}")
                        
                        self.headings_map[file_path].append({
                            'level': level,
                            'text': text
                        })
                        current_level = level
                except Exception as e:
                    logging.error(f"Error processing file {file_path}: {e}")
                    continue

        except Exception as e:
            logging.error(f"Error in analyze_heading_hierarchy: {e}")

    def generate_report(self):
        """Generate a comprehensive report of findings."""
        try:
            logging.info("Generating analysis report...")
            report = []
            report.append("# Documentation Analysis Report\n")

            # Redundant Sections
            report.append("## Potentially Redundant Sections\n")
            for section in self.similar_sections:
                report.append(f"* Similar sections found:\n")
                report.append(f"  * {section['section1']['file']}: {section['section1']['heading']}\n")
                report.append(f"  * {section['section2']['file']}: {section['section2']['heading']}\n")
                report.append(f"  * Similarity: {section['similarity']:.2%}\n")

            # Code Blocks Analysis
            report.append("\n## Code Blocks Analysis\n")
            blocks_without_comments = [b for b in self.code_blocks if not b['has_comments']]
            report.append(f"* Total code blocks: {len(self.code_blocks)}\n")
            report.append(f"* Code blocks without comments: {len(blocks_without_comments)}\n")
            if blocks_without_comments:
                report.append("* Files with uncommented code blocks:\n")
                for block in blocks_without_comments:
                    report.append(f"  * {block['file']}\n")

            # External Links
            report.append("\n## External Links\n")
            report.append(f"* Total external links found: {len(self.external_links)}\n")
            for url, file in sorted(self.external_links):
                report.append(f"* {url} in {file}\n")

            # Heading Hierarchy Issues
            report.append("\n## Heading Hierarchy Analysis\n")
            for file, headings in sorted(self.headings_map.items()):
                report.append(f"\n### {file}\n")
                for heading in headings:
                    report.append(f"{'  ' * (heading['level']-1)}* {heading['text']}\n")

            # Write report to file
            report_path = self.root_dir / 'doc_analysis_report.md'
            report_path.write_text('\n'.join(report), encoding='utf-8')
            logging.info(f"Report generated successfully at {report_path}")

        except Exception as e:
            logging.error(f"Error generating report: {e}")

def main():
    try:
        refiner = DocRefiner()
        logging.info("Starting documentation analysis...")
        refiner.analyze_redundant_sections()
        refiner.extract_code_blocks()
        refiner.find_external_links()
        refiner.analyze_heading_hierarchy()
        refiner.generate_report()
        logging.info("Analysis complete!")
    except Exception as e:
        logging.error(f"Fatal error in main: {e}")

if __name__ == '__main__':
    main() 