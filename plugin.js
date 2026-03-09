import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const skillDir = path.join(__dirname, 'unique-design');

export async function handleSkill(skillName, input) {
  if (skillName !== 'unique-design') {
    throw new Error(`Unknown skill: ${skillName}`);
  }

  // Load the skill documentation
  const skillPath = path.join(skillDir, 'SKILL.md');
  const skillContent = fs.readFileSync(skillPath, 'utf-8');

  // Load references
  const references = {};
  const refsDir = path.join(skillDir, 'references');

  for (const file of fs.readdirSync(refsDir)) {
    if (file.endsWith('.md')) {
      const name = file.replace('.md', '');
      references[name] = fs.readFileSync(
        path.join(refsDir, file),
        'utf-8'
      );
    }
  }

  return {
    skill: skillName,
    documentation: skillContent,
    references: references,
    input: input
  };
}

export const config = {
  skills: ['unique-design']
};
