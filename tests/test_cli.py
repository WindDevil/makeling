import os
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["NO_COLOR"] = "1"
    return subprocess.run(
        ["./makefiling", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=environment,
        check=False,
    )


class RunnerCliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.progress = ROOT / ".makefiling" / "progress.json"
        cls.progress_bytes = cls.progress.read_bytes() if cls.progress.exists() else None

    @classmethod
    def tearDownClass(cls):
        if cls.progress_bytes is None:
            cls.progress.unlink(missing_ok=True)
        else:
            cls.progress.parent.mkdir(parents=True, exist_ok=True)
            cls.progress.write_bytes(cls.progress_bytes)

    def test_unknown_exercise_is_an_error_with_a_suggestion(self):
        result = run("run", "03_variables/01_recursive_vs_simple")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown exercise", result.stdout)
        self.assertIn("Did you mean:", result.stdout)

    def test_make_diagnostic_is_visible_for_a_broken_recipe(self):
        result = run("run", "00_getting_started/01_first_rule")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing separator", result.stdout)
        self.assertIn("working directory kept at build/makefiling/", result.stdout)
        self.assertIn("recipe 需要真正的 Tab", result.stdout)

    def test_topic_and_basic_counts_are_filtered(self):
        topic = run("list", "--topic", "00_getting_started")
        self.assertEqual(topic.returncode, 0)
        self.assertRegex(topic.stdout, r"/6 completed")

        basic = run("list", "--basic")
        self.assertEqual(basic.returncode, 0)
        self.assertRegex(basic.stdout, r"/20 completed")

    def test_hint_steps_explain_the_whole_contract(self):
        result = run("hint", "00_getting_started/01_first_rule", "--steps")
        self.assertEqual(result.returncode, 0)
        self.assertIn("expected exit code: 0", result.stdout)
        self.assertIn("stdout must match", result.stdout)

    def test_verify_and_selftest_can_run_in_parallel(self):
        environment = os.environ.copy()
        environment["NO_COLOR"] = "1"
        verify = subprocess.Popen(
            ["./makefiling", "verify", "--topic", "00_getting_started"],
            cwd=ROOT, text=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, env=environment,
        )
        selftest = subprocess.Popen(
            ["./makefiling", "selftest", "--topic", "00_getting_started"],
            cwd=ROOT, text=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, env=environment,
        )
        verify_output, _ = verify.communicate(timeout=30)
        selftest_output, _ = selftest.communicate(timeout=30)
        self.assertEqual(verify.returncode, 0, verify_output)
        self.assertEqual(selftest.returncode, 0, selftest_output)

    def test_selftest_uses_the_immutable_template(self):
        exercise = ROOT / "exercises/00_getting_started/01_first_rule/Makefile"
        solution = ROOT / "solutions/00_getting_started/01_first_rule/Makefile"
        original = exercise.read_bytes()
        try:
            exercise.write_bytes(solution.read_bytes())
            result = run("selftest", "--topic", "00_getting_started")
            self.assertEqual(result.returncode, 0)
            self.assertIn("all 6 exercises behave correctly", result.stdout)
        finally:
            exercise.write_bytes(original)


if __name__ == "__main__":
    unittest.main()
