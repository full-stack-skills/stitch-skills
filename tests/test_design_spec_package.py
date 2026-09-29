"""设计包校验的缺项、覆盖和依赖回归用例。"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / 'skills/stitch-design-spec/scripts/validate_package.py'
spec = importlib.util.spec_from_file_location('validator', MODULE)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('README.md', 'DESIGN-SPEC.md', 'COVERAGE.md', 'MASTER-PLAN.md', 'pages/P1.md'):
            path = self.root / name
            path.parent.mkdir(exist_ok=True)
            path.write_text('具体文档内容', encoding='utf-8')
        (self.root / 'prompts').mkdir()
        self.prompt = self.root / 'prompts/Q1.md'
        self.prompt.write_text('[Context]\nDesktop 工作台\n[Layout]\n1. 内容区\n[Components]\n刷新按钮与失败重试\n')
        self.data = {
            'version': 'stitch-design-spec/v1',
            'sources': [{'id': 'S1', 'ref': 'PRD.md#任务', 'status': 'confirmed'}],
            'pages': [{'id': 'P1', 'file': 'pages/P1.md', 'source_ids': ['S1'], 'states': ['normal', 'error']}],
            'prompts': [{'id': 'Q1', 'file': 'prompts/Q1.md', 'page_id': 'P1', 'states': ['normal', 'error'], 'mode': 'inline'}],
            'deferrals': [],
            'tasks': [{'id': 'T1', 'page_ids': ['P1'], 'prompt_ids': ['Q1'], 'depends_on': [], 'acceptance': '重试成功后显示列表'}],
        }

    def errors(self):
        (self.root / 'manifest.json').write_text(json.dumps(self.data))
        return validator.validate(self.root)

    def test_complete(self):
        self.assertEqual([], self.errors())

    def test_missing_prompt(self):
        self.prompt.unlink()
        self.assertTrue(self.errors())

    def test_uncovered_state(self):
        self.data['prompts'][0]['states'] = ['normal']
        self.assertTrue(self.errors())

    def test_reasoned_deferral(self):
        self.data['prompts'][0]['states'] = ['normal']
        self.data['deferrals'] = [{'page_id': 'P1', 'state': 'error', 'reason': '等待错误码定义'}]
        self.assertEqual([], self.errors())

    def test_invalid_ids(self):
        self.data['tasks'][0]['prompt_ids'] = ['missing']
        self.assertTrue(self.errors())

    def test_cycle(self):
        self.data['tasks'][0]['depends_on'] = ['T1']
        self.assertTrue(self.errors())

    def test_wrong_sections(self):
        self.prompt.write_text('[Layout]\n1. 列表\n[Context]\n目的\n[Components]\n按钮')
        self.assertTrue(self.errors())

    def test_applied_without_evidence(self):
        self.data['prompts'][0]['mode'] = 'applied-system'
        self.assertTrue(self.errors())

    def test_applied_with_color(self):
        self.data['prompts'][0].update(mode='applied-system', system={'project_id': 'demo', 'id': 'demo', 'evidence': 'fixture only'})
        self.prompt.write_text(self.prompt.read_text() + '\n主色 #409EFF')
        self.assertTrue(self.errors())

    def test_applied_clean(self):
        self.data['prompts'][0].update(mode='applied-system', system={'project_id': 'demo', 'id': 'demo', 'evidence': 'fixture only'})
        self.assertEqual([], self.errors())

    def test_targeted_edit_requires_delta(self):
        self.data['prompts'][0]['mode'] = 'targeted-edit'
        self.assertTrue(self.errors())

    def test_targeted_edit_allows_requested_color(self):
        self.data['prompts'][0].update(mode='targeted-edit', target='标题', delta='颜色 #409EFF')
        self.prompt.write_text(self.prompt.read_text() + '\n标题颜色 #409EFF')
        self.assertEqual([], self.errors())

    def test_path_escape(self):
        self.data['pages'][0]['file'] = '../outside.md'
        self.assertTrue(self.errors())

    def test_unresolved_template(self):
        self.prompt.write_text(self.prompt.read_text() + '\n{{PRODUCT_NAME}}')
        self.assertTrue(self.errors())

    def test_duplicate_id(self):
        self.data['pages'].append(self.data['pages'][0].copy())
        self.assertTrue(self.errors())

    def test_malformed_json(self):
        (self.root / 'manifest.json').write_text('{')
        self.assertTrue(validator.validate(self.root))

    def test_malformed_fields(self):
        for field, value in [('file', []), ('page_id', {}), ('states', None)]:
            with self.subTest(field=field):
                previous = self.data['prompts'][0][field]
                self.data['prompts'][0][field] = value
                self.assertTrue(self.errors())
                self.data['prompts'][0][field] = previous

    def test_manifest_registry(self):
        manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        actual = {str(path.relative_to(ROOT)) for path in (ROOT / 'skills').iterdir() if path.is_dir()}
        registered = [name.removeprefix('./') for name in manifest['skills']]
        self.assertEqual(len(registered), len(set(registered)))
        self.assertEqual(actual, set(registered))

    def test_example(self):
        self.assertEqual([], validator.validate(ROOT / 'skills/stitch-design-spec/examples/instance-center'))


if __name__ == '__main__':
    unittest.main()
