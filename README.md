# Migaku-Syntax Furigana Filter

Converts Migaku syntax to HTML ruby tags for furigana display in Anki.

Only extracts readings for now.

## Usage

Use `{{migakuFurigana:FieldName}}` in your card templates.

**Example:**

Input: `ほうれん草[ほうれんそう;n3]も 好[す;o]き です[;a]{。}`

Output: `<ruby>ほうれん草<rt>ほうれんそう</rt></ruby>も <ruby>好<rt>す</rt></ruby>き <ruby>です<rt></rt></ruby>。`

## Installation

Copy this folder to your Anki add-ons directory and restart Anki.

## Reference

[Migaku Syntax Guide](https://magenta-dirigible-0d8.notion.site/Syntax-reference-guide-2a55f4eb6327491ca80792e3a935d07a)