# NeighShrink-SURE denoising

Filtrado de ruido para señales 1D mediante wavelets, selección de umbral SURE y cycle spinning. Extraído de [sense-lab](https://github.com/KimiK1983/sense-lab). Numba acelera el cálculo de los umbrales.

## Uso

```bash
python -m pip install -r requirements.txt
```

```python
import numpy as np
from neighshrink_sure import neighshrink_sure_denoise

signal = np.sin(np.linspace(0, 8 * np.pi, 512))
params = {
    "wavelet_name": "sym8",
    "level": 4,
    "shifts": 8,
    "attenuation_start_level": 2,
    "attenuation_factor": 0.9,
}
filtered = neighshrink_sure_denoise(signal, params)
```

`shifts=0` desactiva cycle spinning. La función devuelve un array de la misma longitud. `python neighshrink_sure.py` ejecuta la demostración gráfica incluida en el código.

Comprobación rápida: `python -m unittest -q`.

© 2025 Javier F. Santamaria. Todos los derechos reservados. Véase [LICENSE](LICENSE).
