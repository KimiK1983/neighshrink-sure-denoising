import unittest

import numpy as np

from neighshrink_sure import neighshrink_sure_denoise


class DenoisingSmokeTest(unittest.TestCase):
    def test_synthetic_signal(self):
        rng = np.random.default_rng(42)
        t = np.linspace(0, 1, 512)
        clean = np.sin(2 * np.pi * 6 * t)
        noisy = clean + rng.normal(0, 0.25, t.size)
        params = {
            "wavelet_name": "sym8",
            "level": 4,
            "shifts": 0,
            "attenuation_start_level": 2,
            "attenuation_factor": 0.9,
        }
        filtered = neighshrink_sure_denoise(noisy, params)
        self.assertEqual(filtered.shape, noisy.shape)
        self.assertTrue(np.isfinite(filtered).all())
        self.assertLess(np.mean((filtered - clean) ** 2), np.mean((noisy - clean) ** 2))


if __name__ == "__main__":
    unittest.main()
