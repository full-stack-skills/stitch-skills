"""生成器在改名和单技能安装之后仍能产出有效、可继续使用的场景技能。"""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

ROOT = Path(__file__).resolve().parents[1]
CREATOR = ROOT / 'skills/stitch-scenario-skill-creator'


class ScenarioCreatorTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # 独立安装只有当前技能，没有相邻执行技能。
        self.creator = self.root / CREATOR.name
        shutil.copytree(CREATOR, self.creator)
        spec = importlib.util.spec_from_file_location('scenario_creator', self.creator / 'scripts/init_stitch_skill.py')
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def test_generated_contract_uses_canonical_skills(self):
        with redirect_stdout(StringIO()):
            result = self.module.init_skill('music', self.root / 'output')
        self.assertEqual('stitch-ui-music-designer', result.name)
        content = (result / 'SKILL.md').read_text()
        for name in ('stitch-ui-execute', 'stitch-ui-guide', 'stitch-design-spec'):
            self.assertIn(name, content)
        self.assertNotIn('stitch-ui-designer', content)
        self.assertNotIn('stitch-ued-guide', content)
        self.assertTrue((result / 'LICENSE.txt').is_file())
        self.assertTrue((result / 'examples/usage.md').is_file())

    def test_existing_generated_skill_is_preserved(self):
        with redirect_stdout(StringIO()):
            result = self.module.init_skill('music', self.root / 'output')
            marker = result / 'SKILL.md'
            marker.write_text('user content')
            self.assertIsNone(self.module.init_skill('music', self.root / 'output'))
        self.assertEqual('user content', marker.read_text())

    def test_invalid_name_creates_nothing(self):
        destination = self.root / 'output'
        with redirect_stdout(StringIO()):
            self.assertIsNone(self.module.init_skill('../escape', destination))
        self.assertFalse(destination.exists())


if __name__ == '__main__':
    unittest.main()
