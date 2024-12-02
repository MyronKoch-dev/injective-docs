# Injective Documentation Textual Refinement Prompts


## Consolidate Redundant Information

**Objective:** Identify and consolidate redundant information within the Injective documentation to create a single, authoritative source for each topic, improving clarity and conciseness for both human readers and LLMs.

**Instructions:**

1. **Identify Redundant Sections:** Scan the documentation for sections that cover the same concepts, explanations, examples, or tutorials using different wording or structure. Use a combination of techniques:
    * **Text Similarity Comparison:** Use a text similarity algorithm (e.g., cosine similarity, Jaccard index) to compare different sections of text and identify near-duplicates.
    * **Heading/Subheading Analysis:** Analyze the headings and subheadings to identify sections that cover the same topics.
    * **Manual Review (Important):** Manually review potential duplicates identified by automated methods to confirm redundancy and account for nuances in meaning or context.

2. **Merge Redundant Sections:** Merge the identified redundant sections into a single, comprehensive section. Combine the best parts of each version, ensuring accuracy, clarity, and completeness.

3. **Maintain Structure:** Use clear and consistent headings (H1-H6) and subheadings to maintain a well-organized structure within the consolidated sections.

4. **Rewrite and Refine:** After merging, rewrite the combined section to ensure a smooth, consistent flow and avoid abrupt transitions or conflicting information.  Prioritize conciseness and clarity.

5. **Example (Conceptual):**
    * **Redundant Sections:**
        * "Getting Started with Wallets"
        * "Creating an Injective Wallet"
        * "How to Set Up a Wallet"
    * **Consolidated Section:**  "Setting Up Your Injective Wallet" (combining the information from the redundant sections)


## Contextualize Code Examples

**Objective:** Provide clear and comprehensive explanations and comments for all code examples in the documentation to enhance understanding for both human readers and LLMs.

**Instructions:**

1. **Identify Code Examples:**  Locate all code blocks within the documentation.

2. **Add Explanations (Before/After):** Add a textual explanation *before or after* each code example, describing:
    * The purpose of the code.
    * What it does.
    * The expected input and output.
    * How it connects to the surrounding concepts or tutorials.  Refer to specific sections or concepts in the documentation.
    * Any important caveats, limitations, or assumptions.

3. **Add Comments (Within Code):** Add comments *within* the code blocks themselves to clarify the purpose of individual lines, sections, or functions. Use a consistent commenting style appropriate for the programming language used.

4. **Example:**

    ```markdown
    # Sending Tokens with `injectived`

    The following code example demonstrates how to send INJ tokens from one account to another using the `injectived` command-line interface.  This assumes you have already set up your keyring and have sufficient INJ in your account.  See the [Keyring Management](/nodes/getting-started/running-a-node/1.-setting-up-the-keyring.md) section for details on setting up your keyring.

    ```bash
    # Send 100 INJ from sender-address to recipient-address
    injectived tx bank send sender-address recipient-address 100inj --from my_key --chain-id injective-1 --keyring-backend file --gas-prices 500000000inj --gas auto --yes
    ```

    This command generates, signs, and broadcasts a `MsgSend` transaction to the Injective Chain. The `--from` flag specifies the key to use for signing, the `--chain-id` flag specifies the network, and the `--gas-prices` and `--gas` flags set the transaction fees.  The `--yes` flag automatically confirms the transaction without prompting.  After the transaction is included in a block, the recipient account will have 100 more INJ.  You can query the recipient's balance using the following command: `injectived query bank balances recipient-address --node ...`


## Simplify Language and Terminology


**Objective:**  Make the language and terminology in the Injective documentation more accessible and consistent for both human readers and LLMs.

**Instructions:**

1. **Identify Complex Language:**  Review the documentation and locate sentences, paragraphs, or sections that use overly complex or technical language.

2. **Rewrite for Clarity:** Rewrite these sections using simpler, more direct language.  Break down complex sentences into shorter, more manageable ones.  Avoid jargon or technical terms where simpler alternatives exist.

3. **Create Glossary (Recommended):** Create a glossary of key Injective-specific terms and definitions. Link to this glossary from the documentation's introduction or a dedicated "Terminology" section.

4. **Enforce Consistency:** Use the defined glossary terms consistently throughout the documentation. Avoid using synonyms or variations that might confuse an LLM.


## Internalize External Content

**Objective:** Minimize reliance on external links by incorporating essential information directly within the documentation, making it readily available to LLMs.

**Instructions:**

1. **Review External Links:**  Identify all external links within the documentation.

2. **Determine Importance:**  For each link, determine if the linked content is *essential* for understanding the current topic.  Prioritize links to tutorials, critical explanations, or reference materials.

3. **Summarize and Incorporate:** If the linked content is essential, summarize the key information and incorporate it directly into the documentation. Attribute the source if appropriate.

4. **Remove Unnecessary Links:** After internalizing the essential content, remove the external link itself.

5. **Example:**
    * **Original:** "For a detailed tutorial on setting up a validator node, see [this blog post](https://example.com/validator_tutorial)."
    * **Revised:** "Setting Up a Validator Node:  (Summary of key steps from the blog post, with attribution).  For further details, refer to the original blog post (link removed)."



## Ensure Structural Consistency


**Objective:** Enforce a clear and logical structure within the Injective documentation to aid both human comprehension and LLM processing.

**Instructions:**

1. **Heading Hierarchy:** Use headings (H1-H6) to create a hierarchical structure that reflects the logical organization of the content. Ensure that headings are nested correctly (e.g., an H2 should be followed by another H2 or an H3, but not an H4).

2. **Consistent Formatting:** Use a consistent formatting style for headings, lists, code examples, and other elements.

3. **Logical Grouping:** Group related concepts and information under appropriate headings. Ensure that each section focuses on a single, well-defined topic.