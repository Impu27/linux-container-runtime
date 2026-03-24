import unittest
import os
import tempfile
import yaml
import sys

from containerctl.parser import load_config
from runtime.gpu_scheduler import assign_gpu
from runtime.affinity import set_cpu_affinity


class TestContainerRuntime(unittest.TestCase):

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def tearDown(self):
        sys.stdout.close()
        sys.stdout = self._stdout

    # Test YAML Config Parsing

    def test_load_config(self):
        test_config = {
            "cpu": 2,
            "memory": "512M",
            "gpu": True,
            "command": "echo hello"
        }

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            yaml.dump(test_config, f)
            file_path = f.name

        config = load_config(file_path)

        self.assertEqual(config["cpu"], 2)
        self.assertEqual(config["memory"], "512M")
        self.assertTrue(config["gpu"])
        self.assertEqual(config["command"], "echo hello")

        os.remove(file_path)



    # Test GPU Scheduler

    def test_gpu_assignment_success(self):
        config = {
            "gpu_mem": 2000,
            "container_id": "test_container"
        }

        gpu_id = assign_gpu(config)

        self.assertIn(gpu_id, [0, 1])  # Based on  mock GPUs


    def test_gpu_assignment_failure(self):
        config = {
            "gpu_mem": 999999  # Too large → should fail
        }

        gpu_id = assign_gpu(config)

        self.assertEqual(gpu_id, -1)



    # Test CPU Affinity
    def test_cpu_affinity(self):
        # Only run on Linux
        if not hasattr(os, "sched_getaffinity"):
            self.skipTest("CPU affinity not supported on this OS")

        set_cpu_affinity(1)

        affinity = os.sched_getaffinity(0)

        self.assertEqual(len(affinity), 1)



    # Test Command Execution

    def test_command_execution(self):
        result = os.system("echo test")

        self.assertEqual(result, 0)



    # Test Config Missing Fields

    def test_missing_config_fields(self):
        test_config = {}

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            yaml.dump(test_config, f)
            file_path = f.name

        config = load_config(file_path)

        self.assertIsNone(config.get("cpu"))
        self.assertIsNone(config.get("gpu"))

        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
